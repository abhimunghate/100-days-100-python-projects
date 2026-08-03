# 📚 Day 23 - Library Management System

Welcome to **Day 23** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Library Management System** built with Python. It allows users to manage a collection of books by adding, viewing, searching, borrowing, and returning books. The application stores all book records permanently using a JSON file, ensuring that data remains available even after closing the program.

---

## 📌 Project Overview

The application enables users to:

- 📖 Add new books to the library
- 📋 View all available books
- 🔍 Search books by title or author
- 📚 Borrow books with a 14-day return period
- 🔄 Return borrowed books
- ⏰ Check overdue returns
- 💾 Store library records permanently using JSON

The library data is automatically saved in a JSON file for persistent storage.

---

## ✨ Features

- 📖 Add new books with title and author
- 📋 Display all books with availability status
- 🔍 Search books by title or author
- 📚 Borrow available books
- 📅 Automatically assign borrow and due dates
- 🔄 Return borrowed books
- ⏰ Detect overdue returns
- 🚫 Prevent duplicate books
- 💾 Persistent storage using JSON
- ✅ Input validation
- 🖥️ Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- `json` Module
- `os` Module
- `datetime` Module
- `timedelta` Module
- Object-Oriented Programming (Classes & Objects)

---

## 📂 Project Structure

```text
DAY_23/
│── main23.py
│── library.json
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the application:

```bash
python main23.py
```

If `library.json` does not exist, it will be created automatically.

---

## 💻 Sample Output

### Main Menu

```text
------ Library Management System ------

1. Add Book
2. View Books
3. Search Book
4. Borrow Book
5. Return Book
6. Exit
```

---

### Adding a Book

```text
Enter book title : Python Crash Course
Enter author name : Eric Matthes

Book 'Python Crash Course' by Eric Matthes added to the Library.
```

---

### Viewing Books

```text
------ Library Catalog ------

Total Books : 2

1.
Title  : Python Crash Course
Author : Eric Matthes
Status : Available

2.
Title  : Clean Code
Author : Robert C. Martin
Status : Borrowed

Borrowed On : 03-08-2026
Return By : 17-08-2026
```

---

### Borrowing a Book

```text
Enter book title to borrow : Clean Code

Book 'Clean Code' has been borrowed successfully.
Enjoy Reading!

Return before: 17-08-2026
```

---

### Returning a Book

```text
Book returned successfully.

Book 'Clean Code' has been returned.
```

---

### Searching Books

```text
Enter book title or author : Python

------ Search Results ------

Found 1 matching book(s).

Title  : Python Crash Course
Author : Eric Matthes
Status : Available
```

---

## 📄 Data Storage

All library records are stored in **`library.json`**.

Example:

```json
[
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "is_borrowed": false,
        "borrow_date": null,
        "due_date": null
    },
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "is_borrowed": true,
        "borrow_date": "03-08-2026",
        "due_date": "17-08-2026"
    }
]
```

---

## 📚 Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Methods
- JSON File Handling
- Reading & Writing JSON
- File Handling
- Date & Time Manipulation
- `datetime` and `timedelta`
- Lists
- Loops
- Conditional Statements
- User Input Validation
- Searching Algorithms
- Data Persistence

---

## 🎯 Learning Outcome

This project helped me practice:

- Designing applications using Object-Oriented Programming
- Creating reusable classes and methods
- Working with JSON for persistent storage
- Managing structured data efficiently
- Using the `datetime` module for borrow and due dates
- Implementing searching functionality
- Preventing duplicate records
- Building interactive menu-driven applications
- Improving input validation and program organization

---

## ⚠️ Note

- Books are automatically saved in `library.json`.
- Duplicate books (same title and author) are not allowed.
- Borrowed books receive a **14-day return period**.
- Returning overdue books displays the number of late days.
- The application stores data permanently between program executions.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 👤 Member registration system
- 🆔 Unique Book IDs
- 📊 Fine calculation for overdue books
- ✏️ Edit book information
- 🗑️ Delete books
- 📈 Borrowing history reports
- 📅 Custom borrowing duration
- 🔔 Due date reminders
- 📖 Book categories and genres
- ⭐ Book ratings and reviews
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🌐 Database integration using SQLite or MySQL

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀