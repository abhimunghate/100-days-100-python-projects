# This is Day 68 project : Task Scheduler

import json
import tkinter as tk

from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path

TASKS_FILE = Path("tasks.json")

PRIORITIES = ["High", "Medium", "Low"]

def load_tasks(file_path=TASKS_FILE):
    """Load tasks from the JSON file."""
    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            loaded_tasks = json.load(file)
        for task in loaded_tasks:
            task.setdefault("priority", "Medium")
            task.setdefault("completed", False)
        return loaded_tasks
    except json.JSONDecodeError:
        messagebox.showerror("JSON Error", "The tasks.json file contains invalid JSON.")
        return []
    except OSError as error:
        messagebox.showerror("File Error", f"Could not load tasks:\n{error}")
        return []

def save_tasks(tasks, file_path=TASKS_FILE):
    """Save tasks to the JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        messagebox.showerror("File Error", f"Could not save tasks:\n{error}")

def update_task_list(task_data=None):
    """Display tasks in the Listbox. If task_data is not provided, all tasks are displayed."""
    if task_data is None:
        task_data = tasks
    task_listbox.delete(0, tk.END)

    for index, task in enumerate(task_data):
        status = "Completed" if task["completed"] else "Pending"
        task_text = (f"{index + 1}. {task['title']} | Due: {task['due_date']} | Priority: {task['priority']} | {status}")
        task_listbox.insert(tk.END, task_text)

def search_tasks(*args):
    """Search tasks by title, due date, priority or status."""
    search_text = search_var.get().strip().lower()
    if not search_text:
        update_task_list()
        return

    filtered_tasks = []

    for task in tasks:
        status = "completed" if task["completed"] else "pending"
        searchable_text = (f"{task['title']} {task['due_date']} {task['priority']} {status}").lower()
        if search_text in searchable_text:
            filtered_tasks.append(task)

    update_task_list(filtered_tasks)
    status_label.config(text=f"{len(filtered_tasks)} task(s) found.")

def add_task():
    title = title_entry.get().strip()
    due_date = date_entry.get().strip()
    priority = priority_var.get()

    if not title or not due_date:
        messagebox.showwarning("Missing Information", "Please enter a task title and due date.")
        return

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showwarning("Invalid Date", "Please use the YYYY-MM-DD date format.")
        return

    new_task = {"title": title, "due_date": due_date, "priority": priority, "completed": False}
    tasks.append(new_task)
    save_tasks(tasks)
    update_task_list()

    title_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    priority_var.set("Medium")
    status_label.config(text="Task added successfully.")

def mark_task_completed():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("No Task Selected", "Please select a task first.")
        return

    index = selected_index[0]
    displayed_task = get_displayed_tasks()
    if index >= len(displayed_task):
        return

    selected_task = displayed_task[index]
    selected_task["completed"] = True
    save_tasks(tasks)
    search_tasks()
    status_label.config(text="Task marked as completed.")

def delete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("No Task Selected", "Please select a task first.")
        return

    index = selected_index[0]
    displayed_task = get_displayed_tasks()
    if index >= len(displayed_task):
        return

    selected_task = displayed_task[index]
    tasks.remove(selected_task)
    save_tasks(tasks)
    search_tasks()
    status_label.config(text="Task deleted successfully.")

def get_displayed_tasks():
    """Return the same task collection currently displayed. This is necessary because the Listbox may be showing filtered search results instead of all tasks."""
    search_text = search_var.get().strip().lower()
    if not search_text:
        return tasks

    filtered_tasks = []

    for task in tasks:
        status = "completed" if task["completed"] else "pending"
        searchable_text = (f"{task['title']} {task['due_date']} {task['priority']} {status}").lower()
        if search_text in searchable_text:
            filtered_tasks.append(task)
    return filtered_tasks

def clear_search():
    search_var.set("")
    update_task_list()
    status_label.config(text="Showing all tasks.")

root = tk.Tk()
root.title("Task Scheduler")
root.geometry("850x650")
root.minsize(750, 550)

heading_label = tk.Label(root, text="Task Scheduler", font=("Arial", 20, "bold"))
heading_label.pack(pady=15)

input_frame = tk.LabelFrame(root, text="Add New Task", font=("Arial", 11, "bold"))
input_frame.pack(fill="x", padx=20, pady=10)

tk.Label(input_frame, text="Task Title:", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="w")

title_entry = tk.Entry(input_frame, width=35, font=("Arial", 11))
title_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Due Date:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="w")

date_entry = tk.Entry(input_frame, width=35, font=("Arial", 11))
date_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Priority:", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=10, sticky="w")

priority_var = tk.StringVar(value="Medium")

priority_dropdown = ttk.Combobox(input_frame, textvariable=priority_var, values=PRIORITIES, state="readonly", width=32)
priority_dropdown.grid(row=2, column=1, padx=10, pady=10)

add_button = tk.Button(input_frame, text="Add Task", command=add_task, width=18, font=("Arial", 10, "bold"))
add_button.grid(row=3, column=0, columnspan=2, pady=10)

search_frame = tk.LabelFrame(root, text="Search Tasks", font=("Arial", 11, "bold"))
search_frame.pack(fill="x", padx=20, pady=10)

tk.Label(search_frame, text="Search:", font=("Arial", 11)).pack(side="left", padx=10, pady=10)

search_var = tk.StringVar()

search_entry = tk.Entry(search_frame, textvariable=search_var, width=45, font=("Arial", 11))
search_entry.pack(side="left", padx=5, pady=10)

search_var.trace_add("write", search_tasks)

clear_search_button = tk.Button(search_frame, text="Clear Search", command=clear_search)
clear_search_button.pack(side="left", padx=5)

list_frame = tk.LabelFrame(root, text="Task List", font=("Arial", 11, "bold"))
list_frame.pack(fill="both", expand=True, padx=20, pady=10)

task_listbox = tk.Listbox(list_frame, width=100, height=12, font=("Arial", 10), selectmode=tk.SINGLE)
task_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=task_listbox.yview)
scrollbar.pack(side="right", fill="y")

task_listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

complete_button = tk.Button(button_frame, text="Mark as Completed", command=mark_task_completed, width=20, font=("Arial", 10, "bold"))
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=15, font=("Arial", 10, "bold"))
delete_button.grid(row=0, column=1, padx=5)

status_label = tk.Label(root, text="Ready", anchor="w", font=("Arial", 10))
status_label.pack(fill="x", padx=20, pady=8)

tasks = load_tasks()
update_task_list()

root.mainloop()

# Done