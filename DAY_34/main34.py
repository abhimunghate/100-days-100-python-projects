# This is Day 34 project : To-Do List GUI

import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("To-Do List App")
root.geometry("700x650")
root.configure(bg="#e3f2fd")

TASK_FILE = "tasks.json"

if os.path.exists(TASK_FILE):
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
else:
    tasks = []
    
def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def refresh_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_text = (f"[{task['priority']}] " f"[{task['category']}] " f"{task['task']}")
        task_listbox.insert(tk.END, task_text)

def add_task():
    task = task_entry.get().strip()
    priority = priority_var.get()
    category = category_var.get()

    if not task:
        messagebox.showerror("Error", "Task cannot be empty.")
        return
    new_task = {"task": task, "priority": priority, "category": category}
    tasks.append(new_task)
    save_tasks()
    refresh_list()
    task_entry.delete(0, tk.END)
        
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        save_tasks()
        refresh_list()
    else:
        messagebox.showerror("Error", "Select a task to delete.")
        
def clear_tasks():
    if not tasks:
        return
    confirmation = messagebox.askyesno("Clear Tasks", "Are you sure you want to delete all tasks?")
    if confirmation:
        tasks.clear()
        save_tasks()
        refresh_list()
    
title_label = tk.Label(root, text="To-Do List", font=("Arial", 24), bg="#e3f2fd")
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=35)
task_entry.pack(pady=10)

options_frame = tk.Frame(root, bg="#e3f2fd")
options_frame.pack(pady=5)

priority_label = tk.Label(options_frame, text="Priority:", font=("Arial", 12), bg="#e3f2fd")
priority_label.grid(row=0, column=0, padx=5)

priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(options_frame, priority_var, "High", "Medium", "Low")
priority_menu.config(font=("Arial", 11))
priority_menu.grid(row=0, column=1, padx=10)

category_label = tk.Label(options_frame, text="Category:", font=("Arial", 12), bg="#e3f2fd")
category_label.grid(row=0, column=2, padx=5)

category_var = tk.StringVar(value="Other")
category_menu = tk.OptionMenu(options_frame, category_var, "Work", "Personal", "Study", "Other")
category_menu.config(font=("Arial", 11))
category_menu.grid(row=0, column=3, padx=10)

button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#4caf50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 12), bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks, font=("Arial", 12), bg="#607d8b", fg="white")
clear_button.grid(row=0, column=2, padx=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=60, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
task_listbox.pack()

scrollbar.config(command=task_listbox.yview)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="#d32f2f", fg="white")
exit_button.pack(pady=10)

refresh_list()

root.mainloop()

# Done