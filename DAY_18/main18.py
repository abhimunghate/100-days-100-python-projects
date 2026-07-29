# This is Day 18 project : Mini To-Do App

import json
import os

TASK_FILE = 'my_tasks.json'
COMPLETED_FILE = 'completed_tasks.json'

if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)
        
def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
        
if not os.path.exists(COMPLETED_FILE):
    with open(COMPLETED_FILE, 'w') as file:
        json.dump([], file)
        
def load_completed_tasks():
    with open(COMPLETED_FILE, 'r') as file:
        return json.load(file)
    
def save_completed_tasks(tasks):
    with open(COMPLETED_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def add_task():
    task_name = input("\nEnter the task name : ").strip()
    due_date = input("Enter due date (YYYY-MM-DD) : ").strip()
    
    if not task_name:
        print("Task name cannot be empty.")
        return
    
    if not due_date:
        print("Due date cannot be empty.")
        return
    
    tasks = load_tasks()
    
    for task in tasks:
        if task['Task'].lower() == task_name.lower():
            print("Task already exists.")
            return
    
    tasks.append({"Task" : task_name, "Due Date" : due_date, "Status" : "Incomplete"})
    save_tasks(tasks)
    print(f'Task "{task_name}" added successfully!')
    
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n------ To-Do List ------\n")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['Task']} | "
                  f"Due : {task['Due Date']} | "
                  f"Status : {task['Status']}")    
    else:
        print("\nNo tasks found.")
        
def update_status():
    tasks = load_tasks()
    
    if not tasks:
       print("\nNo tasks found.")
       return

    view_tasks()
    
    try:
        task_index = int(input("\nEnter the task number to update : ")) - 1
        if 0 <= task_index < len(tasks):
            new_status = input("\nEnter the new status (Complete/Incomplete) : ").strip().title()
            
            if new_status not in ["Complete", "Incomplete"]:
                print("Invalid status.")
                return
            
            tasks[task_index] ['Status'] = new_status
            save_tasks(tasks)
            print("Task status updated successfully!")
            
            if new_status == "Complete":
                completed_tasks = load_completed_tasks()
                
                if tasks[task_index] not in completed_tasks:
                    completed_tasks.append(tasks[task_index])
                    save_completed_tasks(completed_tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        
def delete_task():
    tasks = load_tasks()
    
    if not tasks:
        print("\nNo tasks found.")
        return

    view_tasks()
    try:
        task_index = int(input("\nEnter the task number to delete : ")) - 1
        
        if 0 <= task_index < len(tasks):
            confirm = input("Delete this task? (Y/N) : ").strip().upper()
            if confirm != "Y":
                print("Deletion cancelled.")
                return
            
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f'\nTask "{deleted_task["Task"]}" deleted successfully!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        
def filter_tasks():
    tasks = load_tasks()
    
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print("\n1. Completed")
    print("2. Incomplete")
    
    choice = input("\nEnter your choice (1/2) : ").strip()
    
    if choice == "1":
        status = "Complete"
    elif choice == "2":
        status = "Incomplete"
    else:
        print("Invalid choice.")
        return
    
    found = False
    
    for i, task in enumerate(tasks, start=1):
        if task['Status'] == status:
            print(f"{i}. {task['Task']} | Due : {task['Due Date']}")
            found = True
            
    if not found:
        print(f"No {status.lower()} tasks found.")
        
def view_completed_tasks():
    tasks = load_completed_tasks()
    
    if not tasks:
        print("\nNo completed tasks found.")
        return
    
    print("\n------ Completed Task Log ------\n")
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['Task']} | Due : {task['Due Date']} | Status : {task['Status']}")
    
def display_menu():
    print("\n------ Mini To-Do App ------\n")
    print("1. Add a new task.")
    print("2. View all tasks.")
    print("3. Update task status.")
    print("4. Delete a task.")
    print("5. Filter tasks.")
    print("6. View completed tasks.")
    print("7. Exit.")
    
while True:
    display_menu()
    choice = input("\nEnter your choice (1-7) : ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_status()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        filter_tasks()
    elif choice == "6":
        view_completed_tasks()
    elif choice == "7":
        print("\nExiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
        
# Done