# This is Day 7 project : Shopping List App

FILENAME = "shopping_list.txt"

def load_list():
    with open(FILENAME, 'r') as file:
        return [line.strip() for line in file.readlines()]
            
shopping_list = load_list()

def save_list():
    with open(FILENAME, 'w') as file:
        for item in shopping_list:
            file.write(item + "\n")

def show_menu():
    print("\n------ Shopping List Menu ------")
    print("\n1. View the shopping list.")
    print("2. Add an item.")
    print("3. Remove an item.")
    print("4. Clear list.")
    print("5. Edit an item.")
    print("6. Exit.")

while True:
    show_menu()
    choice = input("\nEnter your choice (1-6) : ")

    if choice == "1":
        print("\n------ Shopping list ------\n")
        
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
    
    elif choice == "2":
        add_item = input("\nEnter the item to add : ").title()
        if add_item not in shopping_list:
            shopping_list.append(add_item)
            print(f"\n{add_item} has been added to the shopping list.")
        else:
            print(f"\n{add_item} is already present in the list.")
        
    elif choice == "3":
        if not shopping_list:
            print("\nYour shopping list is empty.")
        else:
            remove_item = input("\nEnter the item to remove : ").title()
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"\n{remove_item} has been removed from the shopping list.")
            else:
                print(f"\n{remove_item} is not in the shopping list.")
    
    elif choice == "4":
        shopping_list.clear()
        print("\nThe shopping list has been cleared.")
        
    elif choice == "5":
        if not shopping_list:
            print("\nYour shopping list is empty.")
        else:
            edit_input = input("\nEnter the item to edit : ").title()
            edit_replace = input("What do you want to replace it with : ").title()
            if edit_input in shopping_list:
                index = shopping_list.index(edit_input)
                if edit_replace in shopping_list:
                    print(f"\n{edit_replace} is already present in the shopping list. Please add another item.")
                else:
                    shopping_list[index] = edit_replace
                    print(f"\n{edit_input} has been changed to {edit_replace}.")
            else:
                print(f"\n{edit_input} is not in the shopping list.")
        
    elif choice == "6":
        save_list()
        print("\nGoodbye! Happy Shopping!")
        break
    
    else:
        print("Invalid choice. Please try again.")

# Done