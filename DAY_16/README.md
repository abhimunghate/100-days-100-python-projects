# 🚀 Day 16 - Daily Journal Logger

Welcome to **Day 16** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Daily Journal Logger** built with Python. It allows users to write, view, search, edit, delete, and export journal entries. Each journal entry is automatically saved with a timestamp, making it easy to maintain a personal journal directly from the terminal.

---

## 📌 Project Overview

The application provides a menu-driven interface where users can:

- 📝 Add new journal entries
- 📖 View all saved entries
- 🔍 Search entries by keyword
- ✏️ Edit existing entries
- 🗑️ Delete specific entries
- 📤 Export the journal to a new text file
- 🚪 Exit the application

All journal entries are stored in a text file (`daily_journal.txt`), ensuring that data persists between program executions.

---

## ✨ Features

- 📝 Add journal entries with timestamps
- 📖 View all journal entries
- 🔍 Search entries using keywords
- ✏️ Edit existing entries
- 🗑️ Delete individual entries
- 📤 Export journal to another text file
- 🕒 Automatic timestamp for every entry
- 💾 Persistent storage using text files
- ⚠️ Input validation and error handling
- 🖥️ Simple menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- `time` Module
- File Handling

---

## 📂 Project Structure

```text
DAY_16/
│── main16.py
│── daily_journal.txt
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main16.py
```

---

## 💻 Sample Output

```text
------ Daily Journal Logger ------

1. Add a new entry.
2. View all entries.
3. Search entries by keyword.
4. Edit entries.
5. Delete entries.
6. Export journal to a new file.
7. Exit

Enter your choice (1 - 7) : 1

Write your journal entry : Today I completed my Day 16 Python project.

Entry added successfully!

Enter your choice (1 - 7) : 2

------ Your Journal Entries ------

[12/07/2026 22:15:45] Today I completed my Day 16 Python project.
```

---

## 📚 Concepts Practiced

- Functions
- Variables
- File Handling
- Reading Files
- Writing Files
- Exception Handling (`try-except`)
- Loops (`while`, `for`)
- Conditional Statements (`if`, `elif`, `else`)
- Lists
- String Methods (`strip()`, `lower()`, `upper()`)
- Enumeration (`enumerate()`)
- Time Module (`time.strftime()`)

---

## 🎯 Learning Outcome

This project helped me practice:

- Building a CRUD (Create, Read, Update, Delete) application
- Working with persistent data storage
- Searching data using keywords
- Editing and deleting file-based records
- Exporting data to another file
- Organizing code into reusable functions
- Handling user input and exceptions gracefully

---

## ⚠️ Note

- Journal entries are stored in `daily_journal.txt`.
- Each entry is automatically timestamped.
- Empty journal entries are not allowed.
- Exported journals are saved as separate `.txt` files.
- If the journal file does not exist, the program handles the situation gracefully.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 📅 Filter entries by date
- 😊 Add mood tracking with each entry
- 🏷️ Tag journal entries (e.g., Work, Personal, Study)
- 🔒 Password-protect the journal
- 🔐 Encrypt journal data for privacy
- 📄 Export to PDF
- 🔍 Advanced search with multiple keywords
- 🖥️ Build a GUI version using Tkinter or CustomTkinter

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀