# This is Day 51 project : Expense Tracker

import os
import csv
from datetime import datetime
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from flask import (Flask, render_template, request, redirect, url_for, send_file, flash)
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle)

app = Flask(__name__)
app.secret_key = "expense-tracker-secret-key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILE = os.path.join(BASE_DIR, "expenses.csv")
CHART_DIR = os.path.join(BASE_DIR, "static", "charts")

os.makedirs(CHART_DIR, exist_ok=True)

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def load_expenses():
    initialize_csv()
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    return df

def save_expenses(df):
    df.to_csv(CSV_FILE, index=False)

@app.route("/")
def index():
    df = load_expenses()
    total_expenses = df["Amount"].sum()
    total_transactions = len(df)
    if not df.empty:
        category_summary = (df.groupby("Category")["Amount"].sum().sort_values(ascending=False))
        highest_category = (category_summary.index[0] if not category_summary.empty else "N/A")
    else:
        category_summary = pd.Series(dtype=float)
        highest_category = "N/A"
    return render_template("index.html", expenses=df.to_dict("records"), total_expenses=total_expenses, total_transactions=total_transactions, highest_category=highest_category)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        date = request.form["date"]
        category = request.form["category"]
        amount = request.form["amount"]
        description = request.form["description"]

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            flash("Invalid date format. Use YYYY-MM-DD.", "danger")
            return redirect(url_for("add_expense"))

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            flash("Please enter a valid positive amount.", "danger")
            return redirect(url_for("add_expense"))

        df = load_expenses()
        new_expense = pd.DataFrame([{"Date": date, "Category": category, "Amount": amount, "Description": description}])
        df = pd.concat([df, new_expense], ignore_index=True)
        save_expenses(df)
        flash("Expense added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("add_expense.html")

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_expense(index):
    df = load_expenses()
    if index < 0 or index >= len(df):
        flash("Expense not found.", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        date = request.form["date"]
        category = request.form["category"]
        amount = request.form["amount"]
        description = request.form["description"]

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            flash("Invalid date format.", "danger")
            return redirect(url_for("edit_expense", index=index))

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            flash("Please enter a valid positive amount.", "danger")
            return redirect(url_for("edit_expense", index=index))

        df.loc[index, "Date"] = date
        df.loc[index, "Category"] = category
        df.loc[index, "Amount"] = amount
        df.loc[index, "Description"] = description
        save_expenses(df)
        flash("Expense updated successfully!", "success")
        return redirect(url_for("index"))
    expense = df.iloc[index].to_dict()
    return render_template("edit_expense.html", expense=expense, index=index)

@app.route("/delete/<int:index>", methods=["POST"])
def delete_expense(index):
    df = load_expenses()
    if index < 0 or index >= len(df):
        flash("Expense not found.", "danger")
        return redirect(url_for("index"))
    df = df.drop(df.index[index]).reset_index(drop=True)
    save_expenses(df)
    flash( "Expense deleted successfully!", "success")
    return redirect(url_for("index"))

def generate_charts(df):
    category_chart = "charts/category_expenses.png"
    monthly_chart = "charts/monthly_expenses.png"

    if df.empty:
        return category_chart, monthly_chart
    category_summary = (df.groupby("Category")["Amount"].sum())
    plt.figure(figsize=(7, 7))
    category_summary.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "category_expenses.png"))
    plt.close()

    temp_df = df.copy()
    temp_df["Date"] = pd.to_datetime(temp_df["Date"])
    temp_df["Month"] = (temp_df["Date"].dt.to_period("M"))
    monthly_summary = (temp_df.groupby("Month")["Amount"].sum())
    plt.figure(figsize=(10, 6))
    monthly_summary.plot(kind="bar")
    plt.title("Monthly Expense Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_DIR, "monthly_expenses.png"))
    plt.close()
    return category_chart, monthly_chart

@app.route("/summary")
def summary():
    df = load_expenses()
    if df.empty:
        category_summary = {}
        monthly_summary = {}
    else:
        category_summary = (df.groupby("Category")["Amount"].sum().sort_values(ascending=False).to_dict())
        temp_df = df.copy()
        temp_df["Date"] = pd.to_datetime(temp_df["Date"])
        temp_df["Month"] = (temp_df["Date"].dt.to_period("M"))
        monthly_summary = (temp_df.groupby("Month")["Amount"].sum().to_dict())
        monthly_summary = {str(key): value for key, value in monthly_summary.items()}
    generate_charts(df)
    return render_template("summary.html", category_summary=category_summary, monthly_summary=monthly_summary)

@app.route("/export/excel")
def export_excel():
    df = load_expenses()
    output_file = os.path.join(BASE_DIR, "expense_summary.xlsx")
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Expenses", index=False)
        
        if not df.empty:
            category_summary = (df.groupby("Category")["Amount"].sum().reset_index())
        else:
            category_summary = pd.DataFrame(columns=["Category", "Amount"])
        category_summary.to_excel(writer, sheet_name="Category Summary", index=False)

        if not df.empty:
            temp_df = df.copy()
            temp_df["Date"] = pd.to_datetime(temp_df["Date"])
            temp_df["Month"] = (temp_df["Date"].dt.to_period("M"))
            monthly_summary = (temp_df.groupby("Month")["Amount"].sum().reset_index())
            monthly_summary["Month"] = (monthly_summary["Month"].astype(str))
        else:
            monthly_summary = pd.DataFrame(columns=["Month", "Amount"])
        monthly_summary.to_excel(writer, sheet_name="Monthly Summary", index=False)
    return send_file(output_file, as_attachment=True)

@app.route("/export/pdf")
def export_pdf():
    df = load_expenses()
    output_file = os.path.join(BASE_DIR, "expense_summary.pdf")
    document = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("Expense Tracker Report", styles["Title"]))
    elements.append(Spacer(1, 20))

    total = df["Amount"].sum()
    elements.append(Paragraph(f"Total Expenses: ₹{total:.2f}", styles["Heading2"]))
    elements.append(Spacer(1, 15))
    elements.append(Paragraph("Category Summary", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if not df.empty:
        category_summary = (df.groupby("Category")["Amount"].sum().reset_index())
        category_data = [["Category", "Amount"]]

        for _, row in category_summary.iterrows():
            category_data.append([str(row["Category"]), f"₹{row['Amount']:.2f}"])
    else:
        category_data = [["Category", "Amount"], ["No expenses", "₹0.00"]]
    category_table = Table(category_data)
    category_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.grey), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black), ("ALIGN", (1, 1), (-1, -1), "RIGHT")]))
    elements.append(category_table)
    elements.append(Spacer(1, 25))
    elements.append(Paragraph("Monthly Summary", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    if not df.empty:
        temp_df = df.copy()
        temp_df["Date"] = pd.to_datetime(temp_df["Date"])
        temp_df["Month"] = (temp_df["Date"].dt.to_period("M"))
        monthly_summary = (temp_df.groupby("Month")["Amount"].sum().reset_index())
        monthly_data = [["Month", "Amount"]]

        for _, row in monthly_summary.iterrows():
            monthly_data.append([str(row["Month"]), f"₹{row['Amount']:.2f}"])
    else:
        monthly_data = [["Month", "Amount"], ["No data", "₹0.00"]]
    monthly_table = Table(monthly_data)
    monthly_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.grey), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black), ("ALIGN", (1, 1), (-1, -1), "RIGHT")]))
    elements.append(monthly_table)
    document.build(elements)
    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    initialize_csv()
    app.run(debug=True)
    
# Done