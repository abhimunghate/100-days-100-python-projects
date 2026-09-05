# This is Day 56 project : Personal Budget Planner

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import csv
import os
from datetime import datetime
from collections import defaultdict

import matplotlib.pyplot as plt

DATA_FILE = "budget_data.json"

def load_data():
    """Load all user data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}

def save_data(data):
    """Save all user data to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as error:
        messagebox.showerror("Save Error", f"Could not save data:\n{error}")
        return False

class BudgetPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Planner")
        self.root.geometry("1150x720")
        self.root.minsize(950, 650)
        self.root.configure(bg="#f4f6f8")

        self.data = load_data()
        self.current_user = None

        self.setup_style()
        self.show_user_screen()

    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"), background="#f4f6f8", foreground="#1f2937")
        style.configure("Subtitle.TLabel", font=("Segoe UI", 11), background="#f4f6f8", foreground="#6b7280")
        style.configure("Card.TFrame", background="white")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=32)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("TButton", font=("Segoe UI", 10), padding=8)
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), padding=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_user_screen(self):
        self.clear_window()

        container = tk.Frame(self.root, bg="#f4f6f8")
        container.pack(fill="both", expand=True)

        tk.Label(container, text="💰 Personal Budget Planner", font=("Segoe UI", 28, "bold"), bg="#f4f6f8", fg="#1f2937").pack(pady=(100, 10))
        tk.Label(container, text="Manage your income, expenses and savings goals", font=("Segoe UI", 12), bg="#f4f6f8", fg="#6b7280").pack(pady=(0, 35))
        card = tk.Frame(container, bg="white", padx=40, pady=35, highlightbackground="#e5e7eb", highlightthickness=1)
        card.pack()
        tk.Label(card, text="Select User", font=("Segoe UI", 15, "bold"), bg="white", fg="#1f2937").pack(pady=(0, 12))

        self.user_var = tk.StringVar()
        users = list(self.data.keys())
        self.user_combo = ttk.Combobox(card, textvariable=self.user_var, values=users, state="readonly", width=30, font=("Segoe UI", 11))
        self.user_combo.pack(pady=8)

        if users:
            self.user_combo.current(0)
        ttk.Button(card, text="Login", command=self.login_user).pack(fill="x", pady=(15, 8))
        ttk.Button(card, text="➕ Create New User", command=self.create_user).pack(fill="x", pady=8)

        if users:
            ttk.Button(card, text="🗑 Delete User", command=self.delete_user).pack(fill="x", pady=8)

    def create_user(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Create User")
        dialog.geometry("400x230")
        dialog.resizable(False, False)
        dialog.configure(bg="white")

        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="Create New User", font=("Segoe UI", 17, "bold"), bg="white").pack(pady=(25, 15))
        tk.Label(dialog, text="Enter username:", font=("Segoe UI", 10), bg="white").pack()
        username_entry = ttk.Entry(dialog, width=32)
        username_entry.pack(pady=8)
        username_entry.focus()

        def create():
            username = username_entry.get().strip()
            if not username:
                messagebox.showwarning("Invalid Username", "Please enter a username.", parent=dialog)
                return

            if username in self.data:
                messagebox.showerror("User Exists", "This username already exists.", parent=dialog)
                return

            self.data[username] = {"income": 0.0, "savings_goal": 0.0, "expenses": []}
            save_data(self.data)
            dialog.destroy()
            self.show_user_screen()
            messagebox.showinfo("User Created", f"User '{username}' has been created.")
        ttk.Button(dialog, text="Create User", command=create).pack(pady=15)

    def login_user(self):
        username = self.user_var.get().strip()

        if not username:
            messagebox.showwarning("Select User", "Please select or create a user.")
            return
        self.current_user = username
        self.show_dashboard()

    def delete_user(self):
        username = self.user_var.get().strip()

        if not username:
            messagebox.showwarning("Select User", "Please select a user to delete.")
            return

        confirmation = messagebox.askyesno("Delete User", f"Are you sure you want to delete '{username}'?\n\n All financial data for this user will be permanently deleted.")
        if confirmation:
            del self.data[username]
            save_data(self.data)
            self.show_user_screen()

    def show_dashboard(self):
        self.clear_window()
        user_data = self.data[self.current_user]

        header = tk.Frame(self.root, bg="#1f2937", height=65)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="💰 Personal Budget Planner", font=("Segoe UI", 18, "bold"), bg="#1f2937", fg="white").pack(side="left", padx=20)
        tk.Label(header, text=f"👤 {self.current_user}", font=("Segoe UI", 10, "bold"), bg="#1f2937", fg="white").pack(side="right", padx=20)

        main = tk.Frame(self.root, bg="#f4f6f8")
        main.pack(fill="both", expand=True, padx=15, pady=12)

        stats_frame = tk.Frame(main, bg="#f4f6f8")
        stats_frame.pack(fill="x", pady=(0, 10))

        self.income_label = self.create_stat_card(stats_frame, "💵 Income", "$0.00")
        self.expense_label = self.create_stat_card(stats_frame, "💸 Expenses", "$0.00")
        self.remaining_label = self.create_stat_card(stats_frame, "💰 Remaining", "$0.00")
        self.goal_label = self.create_stat_card(stats_frame, "🎯 Savings Goal", "$0.00")

        content = tk.Frame(main, bg="#f4f6f8")
        content.pack(fill="x", pady=(0, 10))

        left_panel = tk.Frame(content, bg="white", padx=18, pady=15)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 7))
        tk.Label(left_panel, text="💳 Budget Settings", font=("Segoe UI", 13, "bold"), bg="white", fg="#1f2937").pack(anchor="w")

        tk.Label(left_panel, text="Monthly Income", font=("Segoe UI", 9), bg="white").pack(anchor="w", pady=(8, 2))
        self.income_entry = ttk.Entry(left_panel)
        self.income_entry.pack(fill="x", pady=(0, 6))

        self.income_entry.insert(0, str(user_data.get("income", 0)))
        ttk.Button(left_panel, text="Update Income", command=self.update_income).pack(fill="x", pady=(0, 8))

        tk.Label(left_panel, text="Monthly Savings Goal", font=("Segoe UI", 9), bg="white").pack(anchor="w", pady=(2, 2))
        self.goal_entry = ttk.Entry(left_panel)
        self.goal_entry.pack(fill="x", pady=(0, 6))

        self.goal_entry.insert(0, str(user_data.get("savings_goal", 0)))
        ttk.Button(left_panel, text="Update Savings Goal", command=self.update_goal).pack(fill="x", pady=(0, 10))

        tk.Label(left_panel, text="➕ Add Expense", font=("Segoe UI", 13, "bold"), bg="white", fg="#1f2937").pack(anchor="w", pady=(3, 8))
        tk.Label(left_panel, text="Category", font=("Segoe UI", 9), bg="white").pack(anchor="w")
        self.category_entry = ttk.Entry(left_panel)
        self.category_entry.pack(fill="x", pady=(2, 6))

        tk.Label(left_panel, text="Amount", font=("Segoe UI", 9), bg="white").pack(anchor="w")
        self.amount_entry = ttk.Entry(left_panel)
        self.amount_entry.pack(fill="x", pady=(2, 6))

        ttk.Button(left_panel, text="Add Expense", command=self.add_expense).pack(fill="x", pady=3)

        right_panel = tk.Frame(content, bg="white", padx=18, pady=15)
        right_panel.pack(side="right", fill="both", expand=True, padx=(7, 0))
        tk.Label(right_panel, text="📊 Expense Summary", font=("Segoe UI", 13, "bold"), bg="white", fg="#1f2937").pack(anchor="w")
        self.progress_label = tk.Label(right_panel, text="Savings Progress", font=("Segoe UI", 9, "bold"), bg="white")
        self.progress_label.pack(anchor="w", pady=(12, 4))
        self.progress = ttk.Progressbar(right_panel, orient="horizontal", mode="determinate", maximum=100)
        self.progress.pack(fill="x", pady=(0, 8))
        self.status_label = tk.Label(right_panel, text="", font=("Segoe UI", 9), bg="white", justify="left", wraplength=400)
        self.status_label.pack(anchor="w", pady=5)
        ttk.Button(right_panel, text="📊 Visualize Expenses", command=self.plot_expenses).pack( fill="x", pady=4)
        ttk.Button(right_panel, text="📤 Export Financial Data to CSV", command=self.export_csv).pack( fill="x", pady=4)
        
        action_frame = tk.Frame(right_panel, bg="white")
        action_frame.pack(fill="x", pady=(12, 0))
        ttk.Button(action_frame, text="🗑 Delete Selected", command=self.delete_expense).pack(side="left", expand=True, fill="x", padx=(0, 4))
        ttk.Button(action_frame, text="🔄 Refresh", command=self.refresh_dashboard).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(action_frame, text="👤 Switch User", command=self.switch_user).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(action_frame, text="❌ Exit", command=self.root.destroy).pack(side="left", expand=True, fill="x", padx=(4, 0))

        history_frame = tk.Frame(main, bg="white", padx=12, pady=10)
        history_frame.pack(fill="both", expand=True, pady=(0, 8))
        tk.Label(history_frame, text="📋 Expense History", font=("Segoe UI", 13, "bold"), bg="white", fg="#1f2937").pack(anchor="w", pady=(0, 6))

        table_container = tk.Frame(history_frame, bg="white")
        table_container.pack(fill="both", expand=True)
        columns = ("date", "category", "amount")
        self.expense_tree = ttk.Treeview(table_container, columns=columns, show="headings", selectmode="browse")
        self.expense_tree.heading("date", text="Date")
        self.expense_tree.heading("category", text="Category")
        self.expense_tree.heading("amount", text="Amount")
        self.expense_tree.column("date", width=180, anchor="center")
        self.expense_tree.column("category", width=250, anchor="w")
        self.expense_tree.column("amount", width=150, anchor="e")

        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=self.expense_tree.yview)
        self.expense_tree.configure(yscrollcommand=scrollbar.set)
        self.expense_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.refresh_dashboard()

    def create_stat_card(self, parent, title, value):
        card = tk.Frame(parent, bg="white", padx=20, pady=15, highlightbackground="#e5e7eb", highlightthickness=1)
        card.pack(side="left", fill="x", expand=True, padx=5)
        tk.Label(card, text=title, font=("Segoe UI", 10), bg="white", fg="#6b7280").pack(anchor="w")
        label = tk.Label(card, text=value, font=("Segoe UI", 18, "bold"), bg="white", fg="#1f2937")
        label.pack(anchor="w", pady=(5, 0))

        return label

    def update_income(self):
        try:
            income = float(self.income_entry.get())
            if income < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Income", "Please enter a valid positive income amount.")
            return

        self.data[self.current_user]["income"] = income
        save_data(self.data)
        self.refresh_dashboard()
        messagebox.showinfo("Income Updated", f"Monthly income updated to ${income:.2f}")

    def update_goal(self):
        try:
            goal = float(self.goal_entry.get())
            if goal < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Goal", "Please enter a valid positive savings goal.")
            return

        self.data[self.current_user]["savings_goal"] = goal
        save_data(self.data)
        self.refresh_dashboard()
        messagebox.showinfo("Goal Updated", f"Savings goal updated to ${goal:.2f}")

    def add_expense(self):
        category = self.category_entry.get().strip().capitalize()
        amount_text = self.amount_entry.get().strip()

        if not category:
            messagebox.showwarning("Missing Category", "Please enter an expense category.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid amount greater than zero.")
            return

        expense = {"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "category": category, "amount": amount}

        self.data[self.current_user]["expenses"].append(expense)
        save_data(self.data)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.refresh_dashboard()
        messagebox.showinfo("Expense Added", f"${amount:.2f} added under {category}.")

    def delete_expense(self):
        selected = self.expense_tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an expense to delete.")
            return

        item = selected[0]
        values = self.expense_tree.item(item, "values")
        date = values[0]
        category = values[1]
        amount = float(values[2].replace("$", ""))

        confirmation = messagebox.askyesno("Delete Expense",
            f"Delete this expense?\n\n"
            f"Date: {date}\n"
            f"Category: {category}\n"
            f"Amount: ${amount:.2f}"
        )

        if not confirmation:
            return
        expenses = self.data[self.current_user]["expenses"]
        for index, expense in enumerate(expenses):
            if (expense["date"] == date and expense["category"] == category and abs(expense["amount"] - amount) < 0.001):
                expenses.pop(index)
                break
        save_data(self.data)
        self.refresh_dashboard()

    def refresh_dashboard(self):
        user_data = self.data[self.current_user]

        income = user_data.get("income", 0.0)
        goal = user_data.get("savings_goal", 0.0)
        expenses = user_data.get("expenses", [])

        total_expenses = sum(expense["amount"] for expense in expenses)
        remaining = income - total_expenses

        self.income_label.config(text=f"${income:,.2f}")
        self.expense_label.config(text=f"${total_expenses:,.2f}")
        self.remaining_label.config(text=f"${remaining:,.2f}")
        self.goal_label.config(text=f"${goal:,.2f}")
        
        if goal > 0:
            percentage = (remaining / goal) * 100
            progress_value = max(0, min(percentage, 100))
            self.progress["value"] = progress_value
            self.progress_label.config(text=f"Savings Progress: {percentage:.1f}%")

            if remaining >= goal:
                self.status_label.config(
                    text=(
                        f"🎉 Savings goal achieved!\n"
                        f"You have ${remaining - goal:,.2f} "
                        f"above your goal."
                    ),
                    fg="#15803d"
                )

            else:
                self.status_label.config(
                    text=(
                        f"⚠️ Savings goal not reached.\n"
                        f"You need ${goal - remaining:,.2f} "
                        f"more to reach your goal."
                    ),
                    fg="#b45309"
                )
        else:
            self.progress["value"] = 0

            self.progress_label.config(text="Savings Progress: No goal set")
            self.status_label.config(text="Set a savings goal to track your progress.", fg="#6b7280")
            
        for item in self.expense_tree.get_children():
            self.expense_tree.delete(item)

        for expense in expenses:
            self.expense_tree.insert("", tk.END, values=(expense["date"], expense["category"], f"${expense['amount']:,.2f}"))

    def plot_expenses(self):
        expenses = self.data[self.current_user]["expenses"]
        if not expenses:
            messagebox.showinfo("No Data", "Add some expenses before creating a chart.")
            return

        category_totals = defaultdict(float)

        for expense in expenses:
            category_totals[expense["category"]] += expense["amount"]
        labels = list(category_totals.keys())
        sizes = list(category_totals.values())

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.title(f"Expense Distribution - {self.current_user}")
        plt.tight_layout()
        plt.show()

    def export_csv(self):
        expenses = self.data[self.current_user]["expenses"]
        if not expenses:
            messagebox.showinfo("No Data", "There are no expenses to export.")
            return

        filename = filedialog.asksaveasfilename(title="Export Financial Data", defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            initialfile=f"{self.current_user}_financial_data.csv")

        if not filename:
            return

        try:
            income = self.data[self.current_user].get("income", 0.0)
            savings_goal = self.data[self.current_user].get("savings_goal", 0.0)
            total_expenses = sum(expense["amount"] for expense in expenses)
            remaining = income - total_expenses

            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow(["PERSONAL BUDGET REPORT"])
                writer.writerow(["User", self.current_user])
                writer.writerow(["Income", f"{income:.2f}"])
                writer.writerow(["Savings Goal", f"{savings_goal:.2f}"])
                writer.writerow(["Total Expenses", f"{total_expenses:.2f}"])
                writer.writerow(["Remaining Budget", f"{remaining:.2f}"])
                writer.writerow([])

                writer.writerow(["Date", "Category", "Amount"])
                for expense in expenses:
                    writer.writerow([expense["date"], expense["category"], f"{expense['amount']:.2f}"])
            messagebox.showinfo("Export Successful", f"Financial data exported successfully.\n\n" f"File:\n{filename}")
        except OSError as error:
            messagebox.showerror("Export Error", f"Could not export the CSV file:\n{error}")

    def switch_user(self):
        self.current_user = None
        self.show_user_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetPlanner(root)
    root.mainloop()
    
# Done