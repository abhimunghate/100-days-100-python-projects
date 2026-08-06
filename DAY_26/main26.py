# This is Day 26 project : Secure User Profile App

import json
import os

USER_FILE = "users.json"
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{};:,./<>?"

def save_users():
    with open(USER_FILE, "w", encoding="utf-8") as file:
        json.dump([user.to_dict() for user in users], file, indent=4)
        
def load_users():
    users.clear()
    if not os.path.exists(USER_FILE):
        return
    try:
        with open(USER_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    for item in data:
        try:
            users.append(UserProfile(item["username"], item["email"], item["password"]))
        except ValueError:
            print("Skipping invalid user record.")

class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = ""
        if not self.set_password(password):
            raise ValueError("Invalid password")
        if not self.set_email(email):
            raise ValueError("Invalid email")
        
    def to_dict(self):
        return {"username": self.username, "email": self._email, "password": self.__password}
        
    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self._email = new_email
            return True
        return False
            
    def set_password(self, new_password):
        if len(new_password) < 8:
            print("Password must be at least 8 characters.")
            return False
        if not any(ch.isupper() for ch in new_password):
            print("Password must contain at least one uppercase letter.")
            return False
        if not any(ch.islower() for ch in new_password):
            print("Password must contain at least one lowercase letter.")
            return False
        if not any(ch.isdigit() for ch in new_password):
            print("Password must contain at least one digit.")
            return False
        if not any(ch in SPECIAL_CHARS for ch in new_password):
            print("Password must contain at least one special character.")
            return False
        
        self.__password = new_password
        return True
        
    def reset_password(self):
        current_password = input("Enter current password : ").strip()
        if current_password != self.__password:
            print("Incorrect current password.")
            return False
        new_password = input("Enter new password : ").strip()
        if new_password == self.__password:
            print("New password cannot be the same as old password.")
            return False
        if self.set_password(new_password):
            print("Password updated successfully.")
            return True
        return False
            
    def display_profile(self):
        print("\n------ User Profile ------\n")
        print(f"Username : {self.username}")
        print(f"Email : {self.get_email()}")
        print("Password : ********")
        
users = []
load_users()

def create_user():
    username = input("\nEnter username : ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    for user in users:
        if user.username.lower() == username.lower():
            print("Username already exists.")
            return
    email = input("Enter email : ").strip()
    if "@" not in email or "." not in email:
        print("Invalid email format.")
        return
    password = input("Enter password : ").strip()
    try:
        user = UserProfile(username, email, password)
    except ValueError:
        return
    users.append(user)
    save_users()
    print("\nUser created successfully")
    
def view_profiles():
    if not users:
        print("No users found")
        return

    print(f"\nTotal Users : {len(users)}")
    for user in users:
        user.display_profile()
            
def update_email():
    if not users:
        print("No users found")
        return
    username = input("\nEnter username to update email : ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    for user in users:
        if user.username.lower() == username.lower():
            new_email = input("Enter new email : ").strip()
            if user.set_email(new_email):
                save_users()
                print("\nEmail updated successfully")
            return
    print("User not found")
        
def reset_user_password():
    if not users:
        print("No users found.")
        return
    username = input("\nEnter username : ").strip()
    for user in users:
        if user.username.lower() == username.lower():
            if user.reset_password():
                save_users()
            return
    print("User not found.")
        
while True:
    print("\n------ Secure User Profile App ------\n")
    print("1. Create User")
    print("2. View All Profiles")
    print("3. Update Email")
    print("4. Reset Password")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5) : ")
    
    if choice == "1":
        create_user()
    elif choice == "2":
        view_profiles()
    elif choice == "3":
        update_email()
    elif choice == "4":
        reset_user_password()
    elif choice == "5":
        print("\nExiting the program")
        break
    else:
        print("Invalid choice. Please try again")
        
# Done