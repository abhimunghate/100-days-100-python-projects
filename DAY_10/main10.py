# This is Day 10 project : Note-Taking App

import time

FILENAME = "notes.txt"

def show_menu():
    print("\n------ Note-Taking App Menu ------\n")
    print("1. Add a new note.")
    print("2. View all notes.")
    print("3. Delete all notes.")
    print("4. Exit.")
    
def add_note():
    note = input("\nEnter your note : ")
    timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
    with open(FILENAME, 'a') as file:
        file.write(f"[{timestamp}] {note}\n")
    print(f"Note added successfully at {timestamp}!")
    
def view_notes():
    try:
        with open(FILENAME, 'r') as file:
            content = file.read()
            if content:
                print("\n------ Your Notes ------\n")
                print(content)
            else:
                print("\nNo notes found.")
    
    except FileNotFoundError:
        print("\nNo notes found.")
        
def delete_notes():
    confirm = input("\nAre you sure you want to delete all notes? (Yes/n) : ")
    if confirm.lower() == "yes":
        with open(FILENAME, "w") as file:
            pass
        print("All notes have been deleted.")
    
    else:
        print("Deletion cancelled.")
        
while True:
    show_menu()
    choice = input("\nEnter your choice (1-4) : ")
    
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("\nExiting Note-Taking App. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")
        
# Done