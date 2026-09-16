# This is Day 67 project : Stock Market Dashboard

import pandas as pd
import yfinance as yf
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

CSV_FILE = Path("stock_data.csv")
DEFAULT_STOCKS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA",]

def load_csv_data(file_path=CSV_FILE):
    """Load stock data from the local CSV file."""
    if not file_path.exists():
        return pd.DataFrame(columns=["date", "stock", "price"])

    try:
        data = pd.read_csv(file_path)
        required_columns = {"date", "stock", "price"}
        if not required_columns.issubset(data.columns):
            raise ValueError("CSV must contain date, stock and price columns.")

        data["date"] = pd.to_datetime(data["date"])
        data["price"] = pd.to_numeric(data["price"])
        return data.sort_values("date")
    except Exception as error:
        messagebox.showerror("CSV Loading Error", f"Could not load CSV data:\n{error}")
        return pd.DataFrame(columns=["date", "stock", "price"])

def fetch_yahoo_data(stock_symbols, period="1mo"):
    """Fetch historical stock data from Yahoo Finance.

    Parameters:
        stock_symbols: list of stock ticker symbols
        period: Yahoo Finance period such as 1mo, 3mo, 6mo, 1y

    Returns:
        DataFrame containing date, stock and price columns.
    """
    all_stock_data = []

    for symbol in stock_symbols:
        try:
            ticker = yf.Ticker(symbol)
            history = ticker.history(period=period, auto_adjust=False)

            if history.empty:
                continue
            history = history.reset_index()
            date_column = "Date"

            if date_column not in history.columns:
                continue
            selected_data = history[[date_column, "Close"]].copy()
            selected_data.rename(columns={"Date": "date", "Close": "price"}, inplace=True)
            selected_data["stock"] = symbol
            selected_data["date"] = pd.to_datetime(selected_data["date"]).dt.tz_localize(None)
            selected_data["price"] = pd.to_numeric(selected_data["price"])
            selected_data = selected_data[["date", "stock", "price"]]
            all_stock_data.append(selected_data)
        except Exception as error:
            print(f"Could not fetch {symbol}: {error}")

    if not all_stock_data:
        return pd.DataFrame(columns=["date", "stock", "price"])
    return pd.concat(all_stock_data, ignore_index=True).sort_values("date")

class StockMarketDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Market Dashboard")
        self.root.geometry("1150x750")
        self.root.minsize(950, 650)

        self.current_data = pd.DataFrame()
        self.current_figure = None
        self.current_canvas = None

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Stock Market Dashboard", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", padx=15, pady=5)
        tk.Label(control_frame, text="Select Stocks:", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.stock_listbox = tk.Listbox(control_frame, selectmode=tk.MULTIPLE, height=5, exportselection=False)

        for stock in DEFAULT_STOCKS:
            self.stock_listbox.insert(tk.END, stock)
        self.stock_listbox.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

        tk.Label(control_frame, text="Data Source:", font=("Arial", 11, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.data_source_var = tk.StringVar(value="Yahoo Finance")
        self.data_source_dropdown = ttk.Combobox(control_frame, textvariable=self.data_source_var, values=["Yahoo Finance", "Local CSV"], state="readonly", width=18)
        self.data_source_dropdown.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(control_frame, text="Period:", font=("Arial", 11, "bold")).grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.period_var = tk.StringVar(value="1mo")
        self.period_dropdown = ttk.Combobox(control_frame, textvariable=self.period_var, values=["1mo", "3mo", "6mo", "1y", "2y", "5y"], state="readonly", width=18)
        self.period_dropdown.grid(row=1, column=3, padx=5, pady=5)

        button_frame = tk.Frame(control_frame)
        button_frame.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

        self.plot_button = tk.Button(button_frame, text="Plot Selected Stocks", command=self.plot_selected_stocks, font=("Arial", 10, "bold"))
        self.plot_button.pack(side="left", padx=5)

        self.export_button = tk.Button(button_frame, text="Export Plot", command=self.export_plot, font=("Arial", 10, "bold"))
        self.export_button.pack(side="left", padx=5)

        self.clear_button = tk.Button(button_frame, text="Clear", command=self.clear_dashboard, font=("Arial", 10, "bold"))
        self.clear_button.pack(side="left", padx=5)

        self.status_label = tk.Label(self.root, text="Select one or more stocks and click Plot Selected Stocks.", anchor="w", font=("Arial", 10))
        self.status_label.pack(fill="x", padx=15, pady=5)

        self.chart_frame = tk.LabelFrame(self.root, text="Stock Price Comparison", font=("Arial", 11, "bold"))
        self.chart_frame.pack(fill="both", expand=True, padx=15, pady=5)

        statistics_frame = tk.LabelFrame(self.root, text="Stock Statistics", font=("Arial", 11, "bold"))
        statistics_frame.pack(fill="both", padx=15, pady=5)

        columns = ("stock", "average", "minimum", "maximum", "latest", "change")
        self.statistics_table = ttk.Treeview(statistics_frame, columns=columns, show="headings", height=5)
        headings = {"stock": "Stock", "average": "Average Price", "minimum": "Minimum Price", "maximum": "Maximum Price", "latest": "Latest Price", "change": "Change %"}

        for column in columns:
            self.statistics_table.heading(column, text=headings[column])
            self.statistics_table.column(column, width=130, anchor="center")
        self.statistics_table.pack(fill="x", padx=5, pady=5)

    def get_selected_stocks(self):
        selected_indices = self.stock_listbox.curselection()
        selected_stocks = [self.stock_listbox.get(index) for index in selected_indices]
        return selected_stocks

    def plot_selected_stocks(self):
        selected_stocks = self.get_selected_stocks()
        if not selected_stocks:
            messagebox.showwarning("No Stocks Selected", "Please select at least one stock.")
            return

        data_source = self.data_source_var.get()
        period = self.period_var.get()
        if data_source == "Yahoo Finance":
            self.status_label.config(text="Fetching data from Yahoo Finance...")
            self.root.update_idletasks()
            data = fetch_yahoo_data(selected_stocks, period)
        else:
            data = load_csv_data()
            data = data[data["stock"].isin(selected_stocks)]

        if data.empty:
            messagebox.showerror("No Data", "No stock data was found.")
            self.status_label.config(text="No data available.")
            return

        self.current_data = data
        self.draw_plot(data)
        self.update_statistics(data)
        self.status_label.config(
            text=(f"Showing {len(selected_stocks)} stock(s) using {data_source} data."))

    def draw_plot(self, data):
        if self.current_canvas is not None:
            self.current_canvas.get_tk_widget().destroy()

        self.current_figure = Figure(figsize=(10, 5), dpi=100)
        axis = self.current_figure.add_subplot(111)

        for stock in data["stock"].unique():
            stock_data = data[data["stock"] == stock].sort_values("date")
            axis.plot(stock_data["date"], stock_data["price"], marker="o", linewidth=2, label=stock)
        axis.set_title("Stock Price Comparison", fontsize=14, fontweight="bold")

        axis.set_xlabel("Date")
        axis.set_ylabel("Price")
        axis.grid(True, linestyle="--", alpha=0.5)
        axis.legend()
        axis.tick_params(axis="x", rotation=30)

        self.current_figure.tight_layout()
        self.current_canvas = FigureCanvasTkAgg(self.current_figure, master=self.chart_frame)
        self.current_canvas.draw()
        self.current_canvas.get_tk_widget().pack(fill="both", expand=True)

    def update_statistics(self, data):
        for row in self.statistics_table.get_children():
            self.statistics_table.delete(row)

        for stock in data["stock"].unique():
            stock_data = data[data["stock"] == stock]["price"]

            average_price = stock_data.mean()
            minimum_price = stock_data.min()
            maximum_price = stock_data.max()
            latest_price = stock_data.iloc[-1]

            first_price = stock_data.iloc[0]
            if first_price != 0:
                change_percentage = ((latest_price - first_price) / first_price) * 100
            else:
                change_percentage = 0

            self.statistics_table.insert("", tk.END, values=(stock, f"{average_price:.2f}", f"{minimum_price:.2f}", f"{maximum_price:.2f}", f"{latest_price:.2f}", f"{change_percentage:.2f}%"))

    def export_plot(self):
        if self.current_figure is None:
            messagebox.showwarning("No Plot", "Please create a plot before exporting.")
            return

        file_path = filedialog.asksaveasfilename(title="Save Stock Plot", defaultextension=".png", filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("PDF File", "*.pdf"), ("All Files", "*.*")])
        if not file_path:
            return

        try:
            self.current_figure.savefig(file_path, dpi=300, bbox_inches="tight")
            messagebox.showinfo("Export Successful", f"Plot exported successfully:\n{file_path}")
        except Exception as error:
            messagebox.showerror("Export Error", f"Could not export plot:\n{error}")

    def clear_dashboard(self):
        if self.current_canvas is not None:
            self.current_canvas.get_tk_widget().destroy()

        self.current_canvas = None
        self.current_figure = None
        self.current_data = pd.DataFrame()

        for row in self.statistics_table.get_children():
            self.statistics_table.delete(row)

        self.status_label.config(text="Dashboard cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockMarketDashboard(root)
    root.mainloop()
    
# Done