# This is Day 60 project : Personal Diary App

import tkinter as tk
from tkinter import messagebox
import getpass
import hashlib
import json
from pathlib import Path

from encryption import generate_key
from diary_manager import initialize_storage
from gui import DiaryApp

AUTH_FILE = Path("password.hash")

def hash_password(password):
    """Create a SHA-256 hash of the password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def setup_password():
    """Create the diary password on first launch."""
    print("\nNo diary password has been configured.")

    while True:
        password = getpass.getpass("Create a password: ")
        confirm = getpass.getpass("Confirm password: ")
        if not password:
            print("Password cannot be empty.")
            continue

        if password != confirm:
            print("Passwords do not match.")
            continue

        with open(AUTH_FILE, "w", encoding="utf-8") as file:
            file.write(hash_password(password))
            
        print("Password created successfully.")
        return True

def authenticate():
    """Authenticate the diary user."""
    if not AUTH_FILE.exists():
        return setup_password()

    password = getpass.getpass("Enter your diary password: ")
    stored_hash = AUTH_FILE.read_text(encoding="utf-8").strip()

    if hash_password(password) == stored_hash:
        print("Access Granted!")
        return True

    print("Access Denied!")
    return False

def main():
    print("=" * 50)
    print("        🔐 PERSONAL DIARY")
    print("=" * 50)

    generate_key()
    initialize_storage()

    if not authenticate():
        return

    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
# Done