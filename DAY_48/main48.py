# This is Day 48 project : Stock Price Tracker

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class StockPriceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Price Tracker")
        self.root.geometry("1100x700")
        self.tracking = False
        self.refresh_id = None
        self.stock_data = {}
        self.price_history = []
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Stock Price Tracker", font=("Arial", 24, "bold"))
        title.pack(pady=15)

        input_frame = tk.LabelFrame(self.root, text="Stock Settings", padx=10, pady=10)
        input_frame.pack(fill="x", padx=15, pady=5)

        tk.Label(input_frame, text="Stock Symbols : ").grid(row=0, column=0, padx=5, pady=5)
        self.symbol_entry = tk.Entry(input_frame, width=60)
        self.symbol_entry.grid(row=0, column=1, padx=5, pady=5)
        self.symbol_entry.insert(0, "AAPL, MSFT, GOOGL")

        tk.Label(input_frame, text="Refresh Interval (seconds) : ").grid(row=1, column=0, padx=5, pady=5)
        self.interval_entry = tk.Entry(input_frame, width=15)
        self.interval_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.interval_entry.insert(0, "60")

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Start Tracking", command=self.start_tracking, width=18).pack(side="left", padx=5)
        tk.Button(button_frame, text="Stop Tracking", command=self.stop_tracking, width=18).pack(side="left", padx=5)
        tk.Button(button_frame, text="Refresh Now", command=self.update_prices, width=18).pack(side="left", padx=5)
        tk.Button(button_frame, text="Show Chart", command=self.show_chart, width=18).pack(side="left", padx=5)
        tk.Button(button_frame, text="Save History", command=self.save_history, width=18).pack(side="left", padx=5)

        table_frame = tk.LabelFrame(self.root, text="Live Stock Prices", padx=10, pady=10)
        table_frame.pack(fill="both", expand=True, padx=15, pady=5)
        columns = ("Symbol", "Price", "Previous Close", "Change", "Change %", "Updated")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=150, anchor="center")
        self.tree.pack(fill="both", expand=True)

        self.status_label = tk.Label(self.root, text="Ready", anchor="w")
        self.status_label.pack(fill="x", padx=15, pady=5)

    def get_symbols(self):
        text = self.symbol_entry.get().strip()
        if not text:
            raise ValueError("Please enter at least one stock symbol.")
        symbols = [symbol.strip().upper() for symbol in text.split(",") if symbol.strip()]

        if not symbols:
            raise ValueError("No valid stock symbols entered.")
        return list(dict.fromkeys(symbols))

    def get_interval(self):
        try:
            interval = int(self.interval_entry.get())

            if interval < 10:
                raise ValueError("Refresh interval should be at least 10 seconds.")
            return interval
        except ValueError as error:
            if "at least" in str(error):
                raise
            raise ValueError("Enter a valid refresh interval.")

    def get_stock_data(self, symbol):
        try:
            ticker = yf.Ticker(symbol)
            history = ticker.history(period="2d", interval="1d", auto_adjust=False)

            if history.empty:
                raise ValueError(f"No market data found for {symbol}.")
            latest = history.iloc[-1]
            price = float(latest["Close"])

            if len(history) >= 2:
                previous_close = float(history.iloc[-2]["Close"])
            else:
                previous_close = price
                
            change = (price - previous_close)
            change_percent = ((change / previous_close) * 100 if previous_close != 0 else 0)
            return {"symbol": symbol, "price": price, "previous_close": previous_close, "change": change, "change_percent": change_percent}
        except Exception as error:
            print(f"{symbol}: {error}")
            return None

    def update_prices(self):
        try:
            symbols = self.get_symbols()
        except ValueError as error:
            messagebox.showerror("Input Error", str(error))
            return
        self.status_label.config(text="Fetching stock prices...")
        self.root.update_idletasks()

        for symbol in symbols:
            result = self.get_stock_data(symbol)
            if result is None:
                self.update_table_error(symbol)
                continue
            self.stock_data[symbol] = result
            self.update_table(result)

            self.price_history.append({"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Symbol": symbol, "Price": result["price"],
                    "Previous_Close": result["previous_close"], "Change": result["change"], "Change_Percent": result["change_percent"]})
        self.status_label.config(text=(f"Last updated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))

    def update_table(self, result):
        symbol = result["symbol"]
        values = (symbol,
            f"${result['price']:.2f}",
            f"${result['previous_close']:.2f}",
            f"{result['change']:+.2f}",
            f"{result['change_percent']:+.2f}%",
            datetime.now().strftime("%H:%M:%S"))
        existing_item = None

        for item in self.tree.get_children():
            item_values = self.tree.item(item)["values"]
            if item_values and item_values[0] == symbol:
                existing_item = item
                break
            
        if existing_item:
            self.tree.item(existing_item, values=values)
        else:
            self.tree.insert("", tk.END, values=values)

    def update_table_error(self, symbol):
        values = (symbol, "Unavailable", "-", "-", "-", datetime.now().strftime("%H:%M:%S"))

        for item in self.tree.get_children():
            item_values = self.tree.item(item)["values"]
            if item_values and item_values[0] == symbol:
                self.tree.item(item, values=values)
                return
        self.tree.insert("", tk.END, values=values)

    def start_tracking(self):
        try:
            interval = self.get_interval()
        except ValueError as error:
            messagebox.showerror("Input Error", str(error))
            return

        if self.tracking:
            return
        self.tracking = True
        self.status_label.config(text="Stock tracking started...")
        self.update_prices()
        self.schedule_update(interval)

    def schedule_update(self, interval):
        if not self.tracking:
            return
        self.refresh_id = self.root.after(interval * 1000, lambda: self.scheduled_refresh(interval))

    def scheduled_refresh(self, interval):
        if not self.tracking:
            return
        self.update_prices()
        self.schedule_update(interval)

    def stop_tracking(self):
        self.tracking = False
        if self.refresh_id:
            self.root.after_cancel(self.refresh_id)
            self.refresh_id = None
        self.status_label.config(text="Tracking stopped.")

    def show_chart(self):
        if not self.price_history:
            messagebox.showwarning("No Data", "No price history available yet.")
            return

        data = pd.DataFrame(self.price_history)
        data["Timestamp"] = pd.to_datetime(data["Timestamp"])
        plt.figure(figsize=(11, 6))
        
        for symbol in data["Symbol"].unique():
            symbol_data = data[data["Symbol"] == symbol]
            plt.plot(symbol_data["Timestamp"], symbol_data["Price"], marker="o", label=symbol)
        plt.title("Stock Price History")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def save_history(self):
        if not self.price_history:
            messagebox.showwarning("No Data", "No stock price history available.")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not filename:
            return

        try:
            data = pd.DataFrame(self.price_history)
            data.to_csv(filename, index=False)
            messagebox.showinfo("Success", "Stock price history saved successfully.")
        except Exception as error:
            messagebox.showerror("Save Error", str(error))
            
if __name__ == "__main__":
    root = tk.Tk()
    app = StockPriceTracker(root)
    root.mainloop()
    
# Done