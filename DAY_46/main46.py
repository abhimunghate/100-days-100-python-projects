# This is Day 46 project : Sales Report Analyzer

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt

class SalesReportAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Report Analyzer")
        self.root.geometry("1200x800")
        self.data = None
        self.filtered_data = None
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Sales Report Analyzer", font=("Arial", 24, "bold"))
        title.pack(pady=10)
        
        file_frame = tk.LabelFrame(self.root, text="Data Input", padx=10, pady=10)
        file_frame.pack(fill="x", padx=15, pady=5)
        tk.Button(file_frame, text="Load CSV / Excel", command=self.load_file, width=18).pack(side="left", padx=5)
        tk.Button(file_frame, text="Export Clean Data", command=self.export_clean_data, width=18).pack(side="left", padx=5)
        tk.Button(file_frame, text="Export Summary", command=self.export_summary, width=18).pack(side="left", padx=5)
        
        filter_frame = tk.LabelFrame(self.root, text="Filters", padx=10, pady=10)
        filter_frame.pack(fill="x", padx=15, pady=5)
        tk.Label(filter_frame, text="Category:").pack(side="left", padx=5)

        self.category_combo = ttk.Combobox(filter_frame, state="readonly", width=20)
        self.category_combo.pack(side="left", padx=5)

        tk.Label(filter_frame, text="Start Date:").pack(side="left", padx=5)
        self.start_date = tk.Entry(filter_frame, width=15)
        self.start_date.pack(side="left", padx=5)

        tk.Label(filter_frame, text="End Date:").pack(side="left", padx=5)
        self.end_date = tk.Entry(filter_frame, width=15)
        self.end_date.pack(side="left", padx=5)

        tk.Button(filter_frame, text="Apply Filter", command=self.apply_filter, width=15).pack(side="left", padx=5)
        tk.Button(filter_frame, text="Clear Filter", command=self.clear_filter, width=15).pack(side="left", padx=5)
        
        analysis_frame = tk.LabelFrame( self.root, text="Sales Analysis", padx=10, pady=10)
        analysis_frame.pack(fill="x", padx=15, pady=5)

        buttons = [("Dataset Info", self.show_dataset_info), ("Monthly Sales", self.monthly_sales), ("Top 5 Products", self.top_products),
            ("Top Categories", self.top_categories), ("Best-Selling Product", self.best_selling_product), ("Category Chart", self.category_chart), 
            ("Product Revenue", self.product_revenue_chart), ("Quantity Sold", self.quantity_chart), ("Pie Chart", self.pie_chart), ("Stacked Bar", self.stacked_bar_chart)]

        for index, (text, command) in enumerate(buttons):
            row = index // 5
            column = index % 5
            tk.Button(analysis_frame, text=text, command=command, width=20).grid(row=row, column=column, padx=5, pady=5)
        
        result_frame = tk.LabelFrame(self.root, text="Results", padx=10, pady=10)
        result_frame.pack(fill="both", expand=True, padx=15, pady=10)
        self.result_text = tk.Text(result_frame, height=20, width=120)
        self.result_text.pack(fill="both", expand=True)
        
        self.status_label = tk.Label(self.root, text="No data loaded.", anchor="w")
        self.status_label.pack(fill="x", padx=15, pady=5)
        
    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Data Files", "*.csv *.xlsx *.xls"), ("CSV Files", "*.csv"), ("Excel Files", "*.xlsx *.xls")])
        if not filename:
            return

        try:
            if filename.lower().endswith(".csv"):
                data = pd.read_csv(filename)
            else:
                data = pd.read_excel(filename)
            if data.empty:
                raise ValueError("The selected file contains no data.")
            self.data = self.clean_data(data)

            if self.data is None:
                return
            self.filtered_data = self.data.copy()
            self.update_category_list()
            self.status_label.config(text=f"Loaded {len(self.data)} records successfully.")
            self.show_dataset_info()

            messagebox.showinfo("Success", "Sales data loaded successfully.")
        except Exception as error:
            messagebox.showerror("File Error", str(error))
        
    def clean_data(self, data):
        data = data.copy()
        required_columns = ["Product_Name", "Product_Category", "Quantity", "Price", "Sales_Amount", "Date"]

        missing_columns = [column for column in required_columns if column not in data.columns]
        if missing_columns:
            raise ValueError("Missing required columns : " + ", ".join(missing_columns))

        data["Product_Category"] = (data["Product_Category"].fillna("Unknown"))
        data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
        data["Price"] = pd.to_numeric(data["Price"], errors="coerce")
        data["Sales_Amount"] = pd.to_numeric(data["Sales_Amount"], errors="coerce")
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
        data = data.dropna(subset=["Quantity", "Price", "Sales_Amount", "Date"])

        data = data[(data["Quantity"] >= 0) & (data["Price"] >= 0) & (data["Sales_Amount"] >= 0)]
        data = data.drop_duplicates()

        data["Revenue"] = (data["Quantity"] * data["Price"])
        data["Year_Month"] = (data["Date"].dt.to_period("M"))
        
        if data.empty:
            raise ValueError("No valid records remain after cleaning.")
        return data
        
    def update_category_list(self):
        categories = ["All"] + sorted(self.data["Product_Category"].unique().tolist())
        self.category_combo["values"] = categories
        self.category_combo.current(0)
        
    def apply_filter(self):
        if self.data is None:
            messagebox.showwarning("No Data", "Please load a sales file first.")
            return
        filtered = self.data.copy()
        category = self.category_combo.get()
        
        if category and category != "All":
            filtered = filtered[filtered["Product_Category"] == category]
        start = self.start_date.get().strip()
        end = self.end_date.get().strip()

        try:
            if start:
                start_date = pd.to_datetime(start)
                filtered = filtered[filtered["Date"] >= start_date]
            if end:
                end_date = pd.to_datetime(end)
                filtered = filtered[filtered["Date"] <= end_date]
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter dates in YYYY-MM-DD format.")
            return

        self.filtered_data = filtered
        self.status_label.config(text=f"Filter applied. {len(filtered)} records found.")
        self.show_dataset_info()
        
    def clear_filter(self):
        if self.data is None:
            return
        self.filtered_data = self.data.copy()
        self.category_combo.current(0)
        self.start_date.delete(0, tk.END)
        self.end_date.delete(0, tk.END)
        self.status_label.config(text=f"Showing all {len(self.data)} records.")
        self.show_dataset_info()
        
    def get_active_data(self):
        if self.filtered_data is None:
            raise ValueError("Please load a sales file first.")
        
        if self.filtered_data.empty:
            raise ValueError("No records match the selected filters.")
        return self.filtered_data
        
    def display_result(self, text):
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, text)
    
    def show_dataset_info(self):
        try:
            data = self.get_active_data()
            total_records = len(data)
            total_sales = data["Sales_Amount"].sum()
            total_revenue = data["Revenue"].sum()
            average_sales = data["Sales_Amount"].mean()
            result = (
                "------ Dataset Information ------\n\n"
                f"Total Records   : {total_records}\n"
                f"Total Sales     : ${total_sales:,.2f}\n"
                f"Total Revenue   : ${total_revenue:,.2f}\n"
                f"Average Sales   : ${average_sales:,.2f}\n"
            )
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Analysis Error", str(error))    
        
    def monthly_sales(self):
        try:
            data = self.get_active_data()
            monthly = (data.groupby("Year_Month")["Sales_Amount"].sum())

            result = (
                "------ Monthly Sales ------\n\n"
                f"{monthly.to_string()}"
            )
            self.display_result(result)

            plt.figure(figsize=(10, 6))
            monthly.plot(kind="bar")
            plt.title("Monthly Sales")
            plt.xlabel("Month")
            plt.ylabel("Sales Amount")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as error:
            messagebox.showerror("Analysis Error", str(error))
        
    def top_products(self):
        try:
            data = self.get_active_data()
            top = (data.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head(5))

            result = (
                "------ Top 5 Products by Revenue ------\n\n"
                f"{top.to_string()}"
            )
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Analysis Error", str(error))        
        
    def top_categories(self):
        try:
            data = self.get_active_data()
            categories = (data.groupby("Product_Category")["Sales_Amount"].sum().sort_values(ascending=False))

            result = (
                "------ Sales by Category ------\n\n"
                f"{categories.to_string()}"
            )
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Analysis Error", str(error))
        
    def best_selling_product(self):
        try:
            data = self.get_active_data()
            products = (data.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False))
            best_product = products.index[0]
            quantity = products.iloc[0]

            result = (
                "------ Best-Selling Product ------\n\n"
                f"Product  : {best_product}\n"
                f"Quantity : {quantity}"
            )
            self.display_result(result)
        except Exception as error:
            messagebox.showerror("Analysis Error", str(error))
        
    def category_chart(self):
        try:
            data = self.get_active_data()
            category_sales = (data.groupby("Product_Category")["Sales_Amount"].sum().sort_values(ascending=False))
            
            plt.figure(figsize=(9, 6))
            category_sales.plot(kind="bar")
            plt.title("Category-wise Sales")
            plt.xlabel("Category")
            plt.ylabel("Sales")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as error:
            messagebox.showerror("Chart Error", str(error))
        
    def product_revenue_chart(self):
        try:
            data = self.get_active_data()
            products = (data.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head(10))

            plt.figure(figsize=(10, 6))
            products.plot(kind="bar")
            plt.title("Top Products by Revenue")
            plt.xlabel("Product")
            plt.ylabel("Revenue")
            plt.xticks(rotation=45,ha="right")
            plt.tight_layout()
            plt.show()
        except Exception as error:
            messagebox.showerror("Chart Error", str(error))
        
    def quantity_chart(self):
        try:
            data = self.get_active_data()
            quantity = (data.groupby("Product_Category")["Quantity"].sum().sort_values(ascending=False))

            plt.figure(figsize=(9, 6))
            quantity.plot(kind="bar")
            plt.title("Quantity Sold by Category")
            plt.xlabel("Category")
            plt.ylabel("Quantity Sold")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as error:
            messagebox.showerror("Chart Error", str(error))
        
    def pie_chart(self):
        try:
            data = self.get_active_data()
            category_sales = (data.groupby("Product_Category")["Sales_Amount"].sum())

            plt.figure(figsize=(8, 8))
            plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%", startangle=90)
            plt.title("Sales Distribution by Category")
            plt.tight_layout()
            plt.show()
        except Exception as error:
            messagebox.showerror("Chart Error", str(error))
        
    def stacked_bar_chart(self):
        try:
            data = self.get_active_data()
            stacked = pd.pivot_table(data, values="Sales_Amount", index="Year_Month", columns="Product_Category", aggfunc="sum", fill_value=0)
            ax = stacked.plot(kind="bar", stacked=True, figsize=(10, 6))
            ax.set_title("Monthly Sales by Category")
            ax.set_xlabel("Month")
            ax.set_ylabel("Sales Amount")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as error:
            messagebox.showerror("Chart Error", str(error))
        
    def export_clean_data(self):
        try:
            data = self.get_active_data()
            filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if not filename:
                return
            export_data = data.copy()
            export_data["Year_Month"] = (export_data["Year_Month"] .astype(str))
            export_data.to_csv(filename, index=False)
            messagebox.showinfo("Success", "Cleaned dataset exported successfully.")
        except Exception as error:
            messagebox.showerror("Export Error", str(error))

    def export_summary(self):
        try:
            data = self.get_active_data()
            total_records = len(data)
            total_sales = data["Sales_Amount"].sum()
            total_revenue = data["Revenue"].sum()
            average_sales = data["Sales_Amount"].mean()
            
            top_products = (data.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head(5))
            categories = (data.groupby("Product_Category")["Sales_Amount"].sum().sort_values(ascending=False))
            best_product = (data.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False).index[0])

            report = (
                "SALES REPORT\n"
                "============================\n\n"
                "DATASET INFORMATION\n"
                "----------------------------\n"
                f"Total Records : {total_records}\n"
                f"Total Sales   : ${total_sales:,.2f}\n"
                f"Total Revenue : ${total_revenue:,.2f}\n"
                f"Average Sales : ${average_sales:,.2f}\n\n"

                "TOP 5 PRODUCTS BY REVENUE\n"
                "----------------------------\n"
                f"{top_products.to_string()}\n\n"

                "SALES BY CATEGORY\n"
                "----------------------------\n"
                f"{categories.to_string()}\n\n"

                "BEST-SELLING PRODUCT\n"
                "----------------------------\n"
                f"{best_product}\n")

            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if not filename:
                return

            with open(filename, "w", encoding="utf-8") as file:
                file.write(report)
            messagebox.showinfo("Success", "Summary report exported successfully.")
        except Exception as error:
            messagebox.showerror("Export Error", str(error))

if __name__ == "__main__":
    root = tk.Tk()
    app = SalesReportAnalyzer(root)
    root.mainloop()
    
# Done