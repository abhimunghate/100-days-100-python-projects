# This is Day 16 project : Daily Journal Logger

import time

JOURNAL_FILE = 'daily_journal.txt'

def add_entry():
    timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
    entry = input("Write your journal entry : ")
    
    if not entry:
        print("Journal entry cannot be empty.")
        return
    
    with open(JOURNAL_FILE, 'a') as file:
        file.write(f"[{timestamp}] {entry}\n")
    print("Entry added successfully!")
    
def view_entries():
    try:
        with open(JOURNAL_FILE, 'r') as file:
            content = file.read()
            if content:
                print("\n------ Your Journal Entries ------\n")
                print(content.rstrip())
            else:
                print("No entries found. Start writing today.")
    
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")
        
def search_entries():
    keyword = input("Enter a keyword to search for : ").strip().lower()
    
    if not keyword:
        print("Keyword cannot be empty.")
        return    
    
    try:
        with open(JOURNAL_FILE, 'r') as file:
            content = file.readlines()
            found = False
            print("\n------ Search Results ------\n")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            
            if not found:
                print("No matching entries found.")
    
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")
        
def get_entries():
    try:
        with open(JOURNAL_FILE, "r") as file:
            entries = file.readlines()

        if not entries:
            print("No journal entries found.")
            return None

        for i, entry in enumerate(entries, start=1):
            print(f"{i}. {entry.strip()}")

        return entries

    except FileNotFoundError:
        print("No journal file found.")
        return None
        
def edit_entries():
    entries = get_entries()

    if entries is None:
        return

    try:
        choice = int(input("\nEntry number to edit : ")) - 1

        if choice not in range(len(entries)):
            print("Invalid entry number.")
            return

        new_entry = input("New journal entry : ").strip()
        
        if not new_entry:
            print("Journal entry cannot be empty.")
            return

        entries[choice] = f"[{time.strftime('%d/%m/%Y %H:%M:%S')}] {new_entry}\n"

        with open(JOURNAL_FILE, "w") as file:
            file.writelines(entries)

        print("Entry updated successfully!")

    except ValueError:
        print("Please enter a valid number.")

def delete_entries():
    entries = get_entries()

    if entries is None:
        return

    try:
        choice = int(input("\nEntry number to delete : ")) - 1

        if choice not in range(len(entries)):
            print("Invalid entry number.")
            return

        confirm = input("Are you sure you want to delete this entry? (Y/N): ").strip().upper()

        if confirm != "Y":
            print("Deletion cancelled.")
            return
        
        entries.pop(choice)

        with open(JOURNAL_FILE, "w") as file:
            file.writelines(entries)

        print("Entry deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")

def export_entries():
    export_file = input("Enter the export file name (without extension): ").strip()

    if not export_file:
        print("File name cannot be empty.")
        return

    export_file += ".txt"
    
    if export_file == JOURNAL_FILE:
        print("Export file cannot be the same as the journal file.")
        return

    try:
        with open(JOURNAL_FILE, "r") as source:
            content = source.read()
            
            if not content:
                print("Journal is empty. Nothing to export.")
                return

        with open(export_file, "w") as destination:
            destination.write(content)

        print(f"\nJournal exported successfully to '{export_file}'.")

    except FileNotFoundError:
        print("No journal file found. Add an entry first.")
        
def show_menu():
    print("\n------ Daily Journal Logger ------\n")
    print("1. Add a new entry.")
    print("2. View all entries.")
    print("3. Search entries by keyword.")
    print("4. Edit entries.")
    print("5. Delete entries.")
    print("6. Export journal to a new file.")
    print("7. Exit")
    
while True:
    show_menu()
    choice = input("\nEnter your choice (1 - 7) : ").strip()
    
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        edit_entries()
    elif choice == "5":
        delete_entries()
    elif choice == "6":
        export_entries()
    elif choice == "7":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
        
# Done