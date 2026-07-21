# 🚀 Day 10 - Note-Taking App

Welcome to **Day 10** of my **100 Days, 100 Python Projects** challenge!

This project is a simple command-line Note-Taking Application built with Python. It allows users to create notes, view saved notes, and delete all notes. Each note is automatically stored with a timestamp, making it easy to keep track of when notes were created.

---

## 📌 Project Overview

The application provides a menu-driven interface where users can:

- 📝 Add new notes
- 👀 View all saved notes
- 🗑️ Delete all notes
- 🚪 Exit the application

All notes are stored in a text file (`notes.txt`) and remain available even after the program is closed.

---

## ✨ Features

- 📝 Create and save notes
- 🕒 Automatic timestamp for each note
- 👀 View all saved notes
- 🗑️ Delete all notes with confirmation
- 💾 Persistent storage using text files
- 📂 Automatically creates the notes file when needed
- 🖥️ Simple and beginner-friendly interface

---

## 🛠️ Technologies Used

- Python 3
- `time` Module
- File Handling

---

## 📂 Project Structure

```text
DAY_10/
│── main10.py
│── notes.txt
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main10.py
```

---

## 💻 Sample Output

```text
------ Note-Taking App Menu ------

1. Add a new note.
2. View all notes.
3. Delete all notes.
4. Exit.

Enter your choice (1-4) : 1

Enter your note : Complete Python Day 10 project

Note added successfully at 21/07/2026 22:15:30!

------ Note-Taking App Menu ------

Enter your choice (1-4) : 2

------ Your Notes ------

[21/07/2026 22:15:30] Complete Python Day 10 project
```

---

## 📚 Concepts Practiced

- Functions
- File Handling
- Reading Files
- Writing Files
- Appending Data to Files
- Exception Handling (`try-except`)
- Loops (`while`)
- Conditional Statements (`if-elif-else`)
- Menu-Driven Programs
- Python `time` Module
- String Formatting (f-strings)

---

## 🎯 Learning Outcome

This project helped me practice:

- Working with text files
- Saving and retrieving user data
- Using timestamps in applications
- Handling file-related exceptions
- Building a menu-driven application
- Organizing code using functions

---

## ⚠️ Note

- Notes are stored in `notes.txt`.
- If `notes.txt` does not exist, it will be created automatically when a note is added.
- Viewing notes before any notes are created will display an appropriate message.
- Deleting notes permanently removes all saved notes from the file.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- ✏️ Edit specific notes
- ❌ Delete individual notes
- 🔍 Search notes by keyword
- 📌 Pin important notes
- 📅 Filter notes by date
- 📤 Export notes to a separate file

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀