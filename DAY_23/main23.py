# This is Day 23 project : Library Management System

import json
import os
from datetime import datetime, timedelta

BOOK_FILE = "library.json"

if not os.path.exists(BOOK_FILE):
    with open(BOOK_FILE, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)

class Book:
    def __init__(self, title, author, is_borrowed=False, borrow_date=None, due_date=None):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrow_date = borrow_date
        self.due_date = due_date
        
    def to_dict(self):
        return {"title" : self.title, "author" : self.author, "is_borrowed" : self.is_borrowed, "borrow_date" : self.borrow_date, "due_date" : self.due_date}
        
    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")
        
        if self.is_borrowed:
            print(f"Borrowed On : {self.borrow_date}")
            print(f"Return By : {self.due_date}")
        
class Library:
    def __init__(self):
        self.books = []
        self.load_books()
        
    def save_books(self):
        with open(BOOK_FILE, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4, ensure_ascii=False)
            
    def load_books(self):
        self.books.clear()
        try:
            with open(BOOK_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        for item in data:
            self.books.append(Book(item["title"], item["author"], item["is_borrowed"], item["borrow_date"], item["due_date"]))
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        for book in self.books:
            if (book.title.lower() == title.lower() and book.author.lower() == author.lower()):
                print("Book already exists.")
                return
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' by {author} added to the Library.")
        
    def view_books(self):
        if not self.books:
            print("No books available in the Library.")
        else:
            print("\n------ Library Catalog ------\n")
            print(f"\nTotal Books : {len(self.books)}\n")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}.")
                book.display_info()
                print()
                
    def borrow_book(self, title):
        if not self.books:
            print("No books available.")
            return
        
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f"Book '{book.title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    today = datetime.now()
                    deadline = today + timedelta(days=14)
                    
                    book.borrow_date = today.strftime("%d-%m-%Y")
                    book.due_date = deadline.strftime("%d-%m-%Y")
                    print(f"\nBook '{book.title}' has been borrowed successfully. Enjoy Reading!")
                    print(f"Return before: {book.due_date}")
                    self.save_books()
                return
        print(f"Book '{title}' not found.")
        
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print(f"Book '{book.title}' was not borrowed.")
                else:
                    today = datetime.now()
                    deadline = datetime.strptime(book.due_date, "%d-%m-%Y")
                    if today > deadline:
                        late_days = (today - deadline).days
                        print(f"\nBook returned successfully.")
                        print(f"You are {late_days} day(s) late.")
                    else:
                        remaining = (deadline - today).days
                        print(f"\nBook returned on time. {remaining} day(s) remaining before the deadline.")
                    book.is_borrowed = False
                    book.borrow_date = None
                    book.due_date = None
                    self.save_books()
                    print(f"Book '{book.title}' has been returned.")
                return
        print(f"Book '{title}' not found.")
        
    def search_book(self, keyword):
        keyword = keyword.strip().lower()
        if not keyword:
            print("Search keyword cannot be empty.")
            return
        found_books = []

        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                found_books.append(book)

        if not found_books:
            print("\nNo matching books found.")
            return

        print("\n------ Search Results ------\n")
        print(f"\nFound {len(found_books)} matching book(s).\n")
        for i, book in enumerate(found_books, start=1):
            print(f"{i}.")
            book.display_info()
            print()
        
library = Library()

while True:
    print("\n------ Library Management System ------\n")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6) : ").strip()
    
    if choice == "1":
        title = input("\nEnter book title : ").strip().title()
        author = input("Enter author name : ").strip().title()
        
        if not title:
            print("Book title cannot be empty.")
            continue
        if not author:
            print("Author name cannot be empty.")
            continue
        library.add_book(title, author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        keyword = input("\nEnter book title or author : ").strip()
        library.search_book(keyword)
    elif choice == "4":
        title = input("\nEnter book title to borrow : ").strip().title()
        library.borrow_book(title)
    elif choice == "5":
        title = input("\nEnter book title to return : ").strip().title()
        library.return_book(title)
    elif choice == "6":
        print("\nExiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")
        
# Done