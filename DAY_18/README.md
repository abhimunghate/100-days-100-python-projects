# 🚀 Day 18 - Mini To-Do App

Welcome to **Day 18** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Mini To-Do App** built with Python. It helps users manage daily tasks by allowing them to add, view, update, delete, and filter tasks. The application stores data in JSON files, ensuring tasks are saved even after the program is closed.

---

## 📌 Project Overview

The application allows users to:

- ➕ Add new tasks
- 📋 View all tasks
- ✅ Mark tasks as Complete or Incomplete
- 🗑️ Delete tasks
- 🔍 Filter tasks by status
- 🏆 View completed task history
- 💾 Store tasks permanently using JSON files

Task information is automatically saved, so your to-do list is always available the next time you run the application.

---

## ✨ Features

- ➕ Add new tasks with due dates
- 📋 View all saved tasks
- ✅ Update task status (Complete/Incomplete)
- 🗑️ Delete tasks with confirmation
- 🔍 Filter tasks by completion status
- 🏆 View completed task history
- 💾 Persistent storage using JSON
- 🚫 Prevent duplicate task names
- ⚠️ Input validation
- 🖥️ Easy-to-use menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- JSON Module
- OS Module
- File Handling

---

## 📂 Project Structure

```text
DAY_18/
│── main18.py
│── my_tasks.json
│── completed_tasks.json
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the application:

```bash
python main18.py
```

The required JSON files will be created automatically if they do not already exist.

---

## 💻 Sample Output

```text
------ Mini To-Do App ------

1. Add a new task.
2. View all tasks.
3. Update task status.
4. Delete a task.
5. Filter tasks.
6. View completed tasks.
7. Exit.

Enter your choice (1-7): 1

Enter the task name : Complete Python Day 18
Enter due date (YYYY-MM-DD) : 2026-07-30

Task "Complete Python Day 18" added successfully!
```

---

## 📄 Example Task

```json
[
    {
        "Task": "Complete Python Day 18",
        "Due Date": "2026-07-30",
        "Status": "Incomplete"
    }
]
```

When completed:

```json
[
    {
        "Task": "Complete Python Day 18",
        "Due Date": "2026-07-30",
        "Status": "Complete"
    }
]
```

---

## 📚 Concepts Practiced

- Functions
- JSON File Handling
- Reading JSON Files
- Writing JSON Files
- Lists
- Dictionaries
- Loops (`while`, `for`)
- Conditional Statements (`if`, `elif`, `else`)
- Exception Handling (`try-except`)
- Input Validation
- String Methods (`strip()`, `lower()`, `title()`)
- File Existence Checking (`os.path.exists()`)

---

## 🎯 Learning Outcome

This project helped me practice:

- Working with JSON files as a lightweight database
- Building a complete CRUD (Create, Read, Update, Delete) application
- Managing structured data using dictionaries and lists
- Preventing duplicate records
- Validating user input
- Organizing programs into reusable functions
- Separating active and completed task records
- Building a real-world command-line productivity application

---

## ⚠️ Note

- Active tasks are stored in `my_tasks.json`.
- Completed tasks are stored in `completed_tasks.json`.
- The application automatically creates both files if they do not exist.
- Duplicate task names are not allowed.
- Due dates should be entered in the format:

```text
YYYY-MM-DD
```

- Updating a task to **Complete** automatically adds it to the completed task log.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 📅 Validate due date format automatically
- ⏰ Highlight overdue tasks
- 🔔 Add reminder notifications
- ⭐ Add task priorities (High, Medium, Low)
- 🏷️ Categorize tasks (Work, Study, Personal)
- 🔍 Search tasks by keyword
- 📊 Show task completion statistics
- 📤 Export tasks to CSV or PDF
- 🖥️ Build a GUI version using Tkinter or CustomTkinter
- 🌐 Develop a web version using Flask or Django

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀