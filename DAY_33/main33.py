# This is Day 33 project : Simple Login System

import tkinter as tk
from tkinter import messagebox
import re
import time
import json
import os

root = tk.Tk()
root.title("Simple Login System")
root.geometry("500x500")
root.configure(bg="#f0f4c3")

USER_FILE = "users.json"

if os.path.exists(USER_FILE):
    with open(USER_FILE, "r") as file:
        USER_CREDENTIALS = json.load(file)
else:
    USER_CREDENTIALS = {
        "admin": "admin123",
        "user": "user123"
    }

    with open(USER_FILE, "w") as file:
        json.dump(USER_CREDENTIALS, file, indent=4)

MAX_ATTEMPTS = 3
LOCKOUT_TIME = 30

login_attempts = 0
locked_until = 0

title_label = tk.Label(root, text="Login System", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

username_label = tk.Label(root, text="Username : ", font=("Arial", 12), bg="#f0f4c3")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password : ", font=("Arial", 12), bg="#f0f4c3")
password_label.pack()
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

status_label = tk.Label(root, text="", font=("Arial", 10), bg="#f0f4c3")
status_label.pack(pady=5)

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"

    has_uppercase = re.search(r"[A-Z]", password)
    has_lowercase = re.search(r"[a-z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[^A-Za-z0-9]", password)

    strength = sum([bool(has_uppercase), bool(has_lowercase), bool(has_digit), bool(has_special)])
    if strength == 4:
        return "Strong"
    elif strength >= 2:
        return "Medium"
    else:
        return "Weak"

def register():
    username = username_entry.get().strip()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Registration Failed", "Please enter a username and password.")
        return

    if username in USER_CREDENTIALS:
        messagebox.showerror("Registration Failed", "Username already exists.")
        return

    strength = check_password_strength(password)
    if strength != "Strong":
        messagebox.showwarning("Weak Password", "Password must be at least 8 characters and contain :\n" "- Uppercase letter\n" "- Lowercase letter\n" "- Number\n" "- Special character")
        return

    USER_CREDENTIALS[username] = password
    with open(USER_FILE, "w") as file:
        json.dump(USER_CREDENTIALS, file, indent=4)
    messagebox.showinfo("Registration Successful", f"User '{username}' registered successfully!")
    clear()
    
def login():
    global login_attempts, locked_until
    current_time = time.time()

    if current_time < locked_until:
        remaining = int(locked_until - current_time) + 1
        messagebox.showwarning("Account Locked", f"Too many failed attempts.\n" f"Try again in {remaining} seconds.")
        return

    username = username_entry.get().strip()
    password = password_entry.get()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        login_attempts = 0
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        status_label.config(text="Login successful!", fg="green")
    else:
        login_attempts += 1
        remaining_attempts = MAX_ATTEMPTS - login_attempts
        
        if login_attempts >= MAX_ATTEMPTS:
            locked_until = time.time() + LOCKOUT_TIME
            login_attempts = 0

            messagebox.showerror("Account Locked", f"Too many failed login attempts.\n" f"Login locked for {LOCKOUT_TIME} seconds.")
            status_label.config(text="Login temporarily locked.", fg="red")
        else:
            messagebox.showerror("Login Failed", f"Invalid username or password.\n" f"Attempts remaining: {remaining_attempts}")
            status_label.config(text=f"Attempts remaining: {remaining_attempts}", fg="red")
        
def clear():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    status_label.config(text="")
    
login_button = tk.Button(root, text="Login", command=login, font=("Arial", 12), bg="#4CAF50", fg="white")
login_button.pack(pady=10)

register_button = tk.Button(root, text="Register", command=register, font=("Arial", 12), bg="#2196F3", fg="white")
register_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 12), bg="#f44336", fg="white")
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="#607d8b", fg="white")
exit_button.pack(pady=10)

root.mainloop()

# Done