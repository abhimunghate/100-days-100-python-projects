# This is Day 8 project : Contact Book

contacts = {}

def show_menu():
    print("\n------ Contact Book Menu ------\n")
    print("1. View Contacts.")
    print("2. Add Contact.")
    print("3. Search Contact.")
    print("4. Edit Contact.")
    print("5. Delete Contact.")
    print("6. Exit.")
    
def view_contact():
    if not contacts:
        print("\nYour contact book is empty.")
    else:
        print("\n------ Contacts List ------\n")
        for name in contacts:
            print(f"Name : {name}")
            for details in contacts[name]:
                print(f"Phone : {details['Phone']}")
                print(f"Email : {details['Email']}\n")
            
def add_contact():
    name = input("\nEnter contact name : ").title()
    phone = input("Enter contact number :")
    email = input("Enter contact email : ")
    
    if name in contacts:
        print(f"\nContact {name} already exists in the contact book.")
        print("Adding another phone number and email.")
        contacts[name].append({"Phone" : phone, "Email" : email})
    else:
        contacts[name] = [{"Phone" : phone, "Email" : email}]
        print(f"\nContact {name} has been added to your contact book successfully!")
       
def search_contact():
    if not contacts:
        print("\nYour contact book is empty.")
    else:
        name = input("\nEnter the name of the contact you want to search : ").title()
        if name in contacts:
            print(f"\n------ Contact Details for {name} ------\n")
            print(f"Name : {name}")
            for details in contacts[name]:
                print(f"Phone : {details['Phone']}")
                print(f"Email : {details['Email']}\n")
        else:
            print(f"\nContact {name} not found in your contact book.")
            
def edit_contact():
    if not contacts:
        print("\nYour contact book is empty.")
    else:
        name = input("\nEnter the name of the contact you want to edit : ").title()

        if name in contacts:
            print(f"\n------ Editing Contact : {name} ------\n")
            
            for index, details in enumerate(contacts[name]):
                print(f"{index + 1}.")
                print(f"Phone : {details['Phone']}")
                print(f"Email : {details['Email']}\n")

            edit = int(input("Which contact do you want to edit (1/2/...) : ")) - 1

            if 0 <= edit < len(contacts[name]):
                phone = input("Enter new phone number : ")
                email = input("Enter new email : ")

                contacts[name][edit] = {"Phone": phone, "Email": email}

                print(f"\nContact {name} has been updated successfully!")
            else:
                print("\nInvalid contact selection.")
        else:
            print(f"\nContact {name} not found in your contact book.")
             
def delete_contact():
    if not contacts:
        print("\nYour contact book is empty.")
    else:
        name = input("\nEnter the name of the contact you want to delete : ").title()
        if name in contacts:
            for index, details in enumerate(contacts[name]):
                print(f"{index + 1}.")
                print(f"Phone : {details['Phone']}")
                print(f"Email : {details['Email']}\n")
                
            delete = int(input("Which contact do you want to delete? (1/2/...) ")) - 1
            
            if 0 <= delete < len(contacts[name]):
                contacts[name].pop(delete)
                print(f"\nContact {name} has been deleted successfully!")
                
            else:
                print("\nInvalid contact selection.")
            
            if not contacts[name]:
                del contacts[name]
                
        else:
            print(f"\nContact {name} not found in your contact book.")
            

while True:
    show_menu()
    
    choice = input("\nEnter your choice (1-6) : ")
    
    if choice == "1":
        view_contact()
        
    elif choice == "2":
        add_contact()
    
    elif choice == "3":
        search_contact()
        
    elif choice == "4":
        edit_contact()
        
    elif choice == "5":
        delete_contact()
                
    elif choice == "6":
        print("\nThank you for using the Contact Book. Goodbye!")
        break
    
    else:
        print("\nInvalid choice. Please select a valid option (1-6).")
        
# Done