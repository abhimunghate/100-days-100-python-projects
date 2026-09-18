# This is Day 69 project : Currency Converter

import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from decimal import Decimal, InvalidOperation

RATES_FILE = "exchange_rates.json"
HISTORY_FILE = "conversion_history.json"

DEFAULT_RATES = {"USD": 1.0, "EUR": 0.85, "GBP": 0.75, "INR": 74.0, "JPY": 110.0, "CAD": 1.25, "AUD": 1.35, "CHF": 0.92, "CNY": 6.45, "SGD": 1.35}

def load_json(file_path, default_value):
    """Load data from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_value
    except (json.JSONDecodeError, OSError):
        return default_value

def save_json(file_path, data):
    """Save data to a JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as error:
        messagebox.showerror("File Error", f"Could not save data.\n\n{error}")
        return False

def load_exchange_rates():
    """Load exchange rates from JSON file."""
    rates = load_json(RATES_FILE, DEFAULT_RATES.copy())
    if not isinstance(rates, dict) or not rates:
        rates = DEFAULT_RATES.copy()
    return rates

def load_history():
    """Load conversion history from JSON file."""
    history = load_json(HISTORY_FILE, [])
    if not isinstance(history, list):
        return []
    return history

def save_history(history):
    """Save conversion history."""
    save_json(HISTORY_FILE, history)

def convert_using_rates(amount, from_currency, to_currency, rates):
    """Convert currency using USD-based exchange rates.

    Example:
    USD = 1.0
    EUR = 0.85
    INR = 74.0

    EUR -> INR:

    74 / 0.85 = 87.05
    """
    if from_currency not in rates:
        raise ValueError(f"Exchange rate for {from_currency} is not available.")

    if to_currency not in rates:
        raise ValueError(f"Exchange rate for {to_currency} is not available.")

    from_rate = Decimal(str(rates[from_currency]))
    to_rate = Decimal(str(rates[to_currency]))
    if from_rate <= 0 or to_rate <= 0:
        raise ValueError("Exchange rates must be greater than zero.")

    exchange_rate = to_rate / from_rate
    converted_amount = amount * exchange_rate
    return converted_amount, exchange_rate

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter - Day 69")
        self.root.geometry("900x750")
        self.root.minsize(800, 650)

        self.rates = load_exchange_rates()
        self.history = load_history()
        self.currency_codes = sorted(self.rates.keys())

        self.create_variables()
        self.create_widgets()
        self.load_currencies()
        self.display_history()

        self.status_var.set("Ready - using local exchange rates")

    def create_variables(self):
        self.amount_var = tk.StringVar(value="1")
        self.from_currency_var = tk.StringVar(value="USD")
        self.to_currency_var = tk.StringVar(value="INR")

        self.result_var = tk.StringVar(value="Enter an amount and click Convert")
        self.rate_var = tk.StringVar(value="Exchange Rate: --")
        self.source_var = tk.StringVar(value="Source: Local JSON rates")
        self.status_var = tk.StringVar(value="Ready")
        self.custom_from_var = tk.StringVar(value="USD")
        self.custom_to_var = tk.StringVar(value="INR")
        self.custom_rate_var = tk.StringVar()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        title_label = ttk.Label(main_frame, text="Currency Converter", font=("Segoe UI", 24, "bold"))
        title_label.pack(pady=(0, 5))

        subtitle_label = ttk.Label(main_frame, text="Day 69 - 100 Days, 100 Python Projects", font=("Segoe UI", 11))
        subtitle_label.pack(pady=(0, 20))

        conversion_frame = ttk.LabelFrame(main_frame, text="Currency Conversion", padding=20)
        conversion_frame.pack(fill="x", pady=(0, 15))

        ttk.Label(conversion_frame, text="Amount:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.amount_entry = ttk.Entry(conversion_frame, textvariable=self.amount_var, width=25)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(conversion_frame, text="From:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.from_combo = ttk.Combobox(conversion_frame, textvariable=self.from_currency_var, state="readonly", width=22)
        self.from_combo.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(conversion_frame, text="To:").grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.to_combo = ttk.Combobox(conversion_frame, textvariable=self.to_currency_var, state="readonly", width=22)
        self.to_combo.grid(row=2, column=1, padx=10, pady=10)

        convert_button = ttk.Button(conversion_frame, text="Convert", command=self.convert)
        convert_button.grid(row=3, column=0, columnspan=2, pady=15)

        ttk.Label(conversion_frame, textvariable=self.result_var, font=("Segoe UI", 16, "bold")).grid(row=4, column=0, columnspan=2, pady=(10, 5))
        ttk.Label(conversion_frame, textvariable=self.rate_var).grid(row=5, column=0, columnspan=2, pady=3)
        ttk.Label(conversion_frame, textvariable=self.source_var).grid(row=6, column=0, columnspan=2, pady=3)

        custom_frame = ttk.LabelFrame(main_frame, text="Add / Update Custom Exchange Rate", padding=20)
        custom_frame.pack(fill="x", pady=(0, 15))

        ttk.Label(custom_frame, text="From:").grid(row=0, column=0, padx=10, pady=8)

        self.custom_from_combo = ttk.Combobox(custom_frame, textvariable=self.custom_from_var, state="readonly", width=15)
        self.custom_from_combo.grid(row=0, column=1, padx=10, pady=8)

        ttk.Label(custom_frame, text="To:").grid(row=0, column=2, padx=10, pady=8)

        self.custom_to_combo = ttk.Combobox(custom_frame, textvariable=self.custom_to_var, state="readonly", width=15)
        self.custom_to_combo.grid(row=0, column=3, padx=10, pady=8)

        ttk.Label(custom_frame, text="Rate:").grid(row=1, column=0, padx=10, pady=8)

        self.custom_rate_entry = ttk.Entry(custom_frame, textvariable=self.custom_rate_var, width=18)
        self.custom_rate_entry.grid(row=1, column=1, padx=10, pady=8)

        ttk.Label(custom_frame, text="Example: 1 USD = 83 INR").grid(row=1, column=2, columnspan=2, padx=10, pady=8)

        add_rate_button = ttk.Button(custom_frame, text="Save Custom Rate", command=self.add_custom_rate)
        add_rate_button.grid(row=2, column=0, columnspan=4, pady=12)

        history_frame = ttk.LabelFrame(main_frame, text="Conversion History", padding=10)
        history_frame.pack(fill="both", expand=True)

        columns = ("datetime", "conversion", "result", "rate", "source")

        self.history_tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=10)

        self.history_tree.heading("datetime", text="Date & Time")
        self.history_tree.heading("conversion", text="Conversion")
        self.history_tree.heading("result", text="Result")
        self.history_tree.heading("rate", text="Rate")
        self.history_tree.heading("source", text="Source")

        self.history_tree.column("datetime", width=150)
        self.history_tree.column("conversion", width=180)
        self.history_tree.column("result", width=150)
        self.history_tree.column("rate", width=120)
        self.history_tree.column("source", width=120)

        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_tree.yview)
        self.history_tree.configure(yscrollcommand=scrollbar.set)

        self.history_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        history_buttons = ttk.Frame(main_frame)
        history_buttons.pack(fill="x", pady=10)

        refresh_button = ttk.Button(history_buttons, text="Refresh History", command=self.display_history)
        refresh_button.pack(side="left", padx=5)

        clear_button = ttk.Button(history_buttons, text="Clear History", command=self.clear_history)
        clear_button.pack(side="left", padx=5)

        status_label = ttk.Label(main_frame, textvariable=self.status_var, relief="sunken", anchor="w", padding=5)
        status_label.pack(fill="x", pady=(5, 0))

    def load_currencies(self):
        self.rates = load_exchange_rates()
        self.currency_codes = sorted(self.rates.keys())

        self.from_combo["values"] = self.currency_codes
        self.to_combo["values"] = self.currency_codes

        self.custom_from_combo["values"] = self.currency_codes
        self.custom_to_combo["values"] = self.currency_codes

        if "USD" in self.currency_codes:
            self.from_currency_var.set("USD")

        if "INR" in self.currency_codes:
            self.to_currency_var.set("INR")

        if "USD" in self.currency_codes:
            self.custom_from_var.set("USD")

        if "INR" in self.currency_codes:
            self.custom_to_var.set("INR")

    def convert(self):
        try:
            amount = Decimal(self.amount_var.get().strip())
        except InvalidOperation:
            messagebox.showerror("Invalid Amount", "Please enter a valid numeric amount.")
            return

        if amount <= 0:
            messagebox.showerror("Invalid Amount", "Amount must be greater than zero.")
            return

        from_currency = (self.from_currency_var.get())
        to_currency = (self.to_currency_var.get())
        if not from_currency or not to_currency:
            messagebox.showerror("Currency Error", "Please select both currencies.")
            return

        try:
            converted_amount, exchange_rate = (convert_using_rates(amount, from_currency, to_currency, self.rates))
            result_text = (f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}")

            self.result_var.set(result_text)
            self.rate_var.set(f"Exchange Rate: 1 {from_currency} = {exchange_rate:.6f} {to_currency}")
            self.source_var.set("Source: Local JSON exchange rates")

            history_item = {"datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "conversion": (f"{amount:,.2f} {from_currency} → {to_currency}"),
                "result": (f"{converted_amount:,.2f} {to_currency}"),
                "rate": (f"1 {from_currency} = {exchange_rate:.6f} {to_currency}"),
                "source": "Local JSON"
            }

            self.history.insert(0, history_item)
            self.history = self.history[:100]
            save_history(self.history)
            self.display_history()
            self.status_var.set("Conversion completed successfully.")
        except (ValueError, ArithmeticError) as error:
            messagebox.showerror("Conversion Error", str(error))

    def add_custom_rate(self):
        from_currency = (self.custom_from_var.get())
        to_currency = (self.custom_to_var.get())
        if not from_currency or not to_currency:
            messagebox.showerror("Currency Error", "Please select both currencies.")
            return

        if from_currency == to_currency:
            messagebox.showerror("Currency Error", "From and To currencies must be different.")
            return

        try:
            new_rate = Decimal(self.custom_rate_var.get().strip())
        except InvalidOperation:
            messagebox.showerror("Invalid Rate", "Please enter a valid numeric exchange rate.")
            return

        if new_rate <= 0:
            messagebox.showerror("Invalid Rate", "Exchange rate must be greater than zero.")
            return

        try:
            if from_currency not in self.rates:
                messagebox.showerror("Currency Error", f"{from_currency} does not have a base rate.")
                return

            from_base_rate = Decimal(str(self.rates[from_currency]))
            new_to_base_rate = (from_base_rate * new_rate)

            self.rates[to_currency] = float(new_to_base_rate)
            self.rates["USD"] = 1.0
            save_json(RATES_FILE, self.rates)
            self.load_currencies()
            self.custom_rate_var.set("")

            self.status_var.set(f"Custom rate saved: 1 {from_currency} = {new_rate} {to_currency}")
            messagebox.showinfo("Rate Saved", f"Custom exchange rate saved successfully.\n\n 1 {from_currency} = {new_rate} {to_currency}")
        except (ValueError, ArithmeticError) as error:
            messagebox.showerror("Rate Error", str(error))

    def display_history(self):
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        self.history = load_history()
        for item in self.history:
            self.history_tree.insert("", "end", values=(item.get("datetime", ""), item.get("conversion", ""), item.get("result", ""), item.get("rate", ""), item.get("source", "")))

    def clear_history(self):
        if not self.history:
            messagebox.showinfo("History", "Conversion history is already empty.")
            return

        confirmation = messagebox.askyesno("Clear History", "Are you sure you want to delete all conversion history?")
        if not confirmation:
            return

        self.history = []
        save_history(self.history)
        self.display_history()
        self.status_var.set("Conversion history cleared.")

def main():
    root = tk.Tk()
    style = ttk.Style()

    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
# Done