# This is Day 35 project : Expense Tracker App

import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from reportlab.pdfgen import canvas
import csv
import os

EXPENSE_FILE = "expenses.csv"

root = tk.Tk()
root.title("Expense Tracker App")
root.geometry("700x700")
root.configure(bg="#f0f4c3")

expenses = []

def export_pdf():
    file_path = "expenses.pdf"
    pdf = canvas.Canvas(file_path)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "Expense Report")
    y = 770
    pdf.setFont("Helvetica", 10)

    for expense in expenses:
        text = f"{expense[3]} | {expense[0]} | ${float(expense[1]):.2f} | {expense[2]}"
        pdf.drawString(50, y, text)
        y -= 20
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 800
    pdf.save()
    messagebox.showinfo("PDF Exported", "Expenses successfully exported to expenses.pdf")

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                expenses.append(row)
                expense_listbox.insert(tk.END, f"{row[0]} | ${float(row[1]):.2f} | {row[2]} | {row[3]}")
                
def save_expenses():
    with open(EXPENSE_FILE, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for expense in expenses:
            writer.writerow(expense)
            
def add_expense():
    category = category_var.get()
    amount = amount_entry.get()
    description = description_entry.get().strip()
    date = date_entry.get()
    
    if category == "Select Category":
        messagebox.showerror("Invalid Input", "Please select a category.")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        return

    if amount <= 0:
        messagebox.showerror("Invalid Input", "Amount must be greater than 0.")
        return
    
    if not description:
        messagebox.showerror("Invalid Input", "Please enter a description.")
        return
    
    expenses.append([category, amount, description, date])
    expense_listbox.insert(tk.END, f"{category} | ${amount:.2f} | {description} | {date}")
    calculate_total()
    clear_inputs()
    save_expenses()
    
def delete_expense():
    selected = expense_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select an expense to delete.")
        return
    
    index = selected[0]
    del expenses[index]
    expense_listbox.delete(index)
    calculate_total()
    save_expenses()
    
def search_expense():
    search = search_entry.get().lower()
    expense_listbox.delete(0, tk.END)
    
    for expense in expenses:
        if any(search in str(value).lower() for value in expense):
            expense_listbox.insert(tk.END, f"{expense[0]} | ${float(expense[1]):.2f} | {expense[2]} | {expense[3]}")
            
def show_all_expenses():
    expense_listbox.delete(0, tk.END)
    for expense in expenses:
        expense_listbox.insert(tk.END, f"{expense[0]} | ${float(expense[1]):.2f} | {expense[2]} | {expense[3]}")
    
def clear_inputs():
    category_var.set("Select Category")
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    
def calculate_total():
    total = sum(float(expense[1]) for expense in expenses)
    total_label.config(text=f"Total Expenses : ${total:.2f}")
    
def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expenses.clear()
        expense_listbox.delete(0, tk.END)
        calculate_total()
        save_expenses()
        
title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 24), bg="#f0f4c3")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f4c3")
input_frame.pack(pady=10)

category_label = tk.Label(input_frame, text="Category : ", font=("Arial", 12), bg="#f0f4c3")
category_label.grid(row=0, column=0, padx=5, pady=5)
category_var = tk.StringVar(value="Select Category")
category_dropdown = ttk.Combobox(input_frame, textvariable=category_var, values=["Food", "Transport", "Rent", "Utilities", "Other"])
category_dropdown.grid(row=0, column=1, padx=5, pady=5)

amount_label = tk.Label(input_frame, text="Amount ($) : ", font=("Arial", 12), bg="#f0f4c3")
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=5, pady=5)

description_label = tk.Label(input_frame, text="Description : ", font=("Arial", 12), bg="#f0f4c3")
description_label.grid(row=2, column=0, padx=5, pady=5)
description_entry = tk.Entry(input_frame, font=("Arial", 12))
description_entry.grid(row=2, column=1, padx=5, pady=5)

date_label = tk.Label(input_frame, text="Date : ", font=("Arial", 12), bg="#f0f4c3")
date_label.grid(row=3, column=0, padx=5, pady=5)
date_entry = DateEntry(input_frame, font=("Arial", 12), date_pattern="dd-mm-yyyy")
date_entry.grid(row=3, column=1, padx=5, pady=5)

search_frame = tk.Frame(root, bg="#f0f4c3")
search_frame.pack(pady=5)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=25)
search_entry.grid(row=0, column=0, padx=5)
search_button = tk.Button(search_frame, text="Search", command=search_expense, bg="#ff9800", fg="white")
search_button.grid(row=0, column=1, padx=5)

show_all_button = tk.Button(search_frame, text="Show All", command=show_all_expenses, bg="#607d8b", fg="white")
show_all_button.grid(row=0, column=2, padx=5)

btn_frame = tk.Frame(root, bg="#f0f4c3")
btn_frame.pack(pady=10)

add_button = tk.Button(btn_frame, text="Add Expense", command=add_expense, bg="#4caf50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(btn_frame, text="Delete Expense", command=delete_expense, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(btn_frame, text="Clear All", command=clear_all, bg="#607d8b", fg="white")
clear_button.grid(row=0, column=2, padx=5)

pdf_button = tk.Button(btn_frame, text="Export PDF", command=export_pdf, bg="#9c27b0", fg="white")
pdf_button.grid(row=0, column=3, padx=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expense_listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
expense_listbox.pack()

scrollbar.config(command=expense_listbox.yview)

total_label = tk.Label(root, text="Total Expenses : $0.00", font=("Arial", 14), bg="#f0f4c3")
total_label.pack(pady=10)

load_expenses()
calculate_total()

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#d32f2f", fg="white")
exit_button.pack(pady=10)

root.mainloop()

# Done