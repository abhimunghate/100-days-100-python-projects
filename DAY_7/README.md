# 🚀 Day 7 - Shopping List App

Welcome to **Day 7** of my **100 Days, 100 Python Projects** challenge!

This project is a menu-driven Shopping List application built using Python. It allows users to create, manage, and save a shopping list using a text file, ensuring that the list is available even after the program is closed.

---

## 📌 Project Overview

The application provides an interactive menu where users can:

- 📋 View the shopping list
- ➕ Add new items
- ❌ Remove existing items
- ✏️ Edit items
- 🗑️ Clear the entire shopping list
- 💾 Save the list before exiting

All shopping items are stored in a text file (`shopping_list.txt`) so the data persists between program executions.

---

## ✨ Features

- 📋 View all shopping list items
- ➕ Add new items
- ❌ Remove existing items
- ✏️ Edit items
- 🗑️ Clear the complete list
- 💾 Automatically saves the list when exiting
- 📂 Loads previously saved items when the program starts
- 🚫 Prevents duplicate entries
- 🖥️ Simple menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- File Handling (`open()`, `read()`, `write()`)

---

## 📂 Project Structure

```
DAY_7/
│── main7.py
│── shopping_list.txt
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Ensure `shopping_list.txt` exists in the project folder.
4. Open the terminal in the project folder.
5. Run the program:

```bash
python main7.py
```

---

## 💻 Sample Output

```
------ Shopping List Menu ------

1. View the shopping list.
2. Add an item.
3. Remove an item.
4. Clear list.
5. Edit an item.
6. Exit.

Enter your choice (1-6) : 2

Enter the item to add : Milk

Milk has been added to the shopping list.

Enter your choice (1-6) : 1

------ Shopping List ------

1. Milk

Enter your choice (1-6) : 6

Goodbye! Happy Shopping!
```

---

## 📚 Concepts Practiced

- Functions
- Variables
- Lists
- File Handling
- Reading from Files
- Writing to Files
- `with` Statement
- Loops (`while`)
- Conditional Statements (`if`, `elif`, `else`)
- `enumerate()`
- List Methods
  - `append()`
  - `remove()`
  - `clear()`
  - `index()`
- String Methods (`title()`)

---

## 🎯 Learning Outcome

This project helped me practice:

- Working with file handling in Python
- Building a menu-driven application
- Persisting data using text files
- Manipulating lists efficiently
- Preventing duplicate entries
- Creating reusable functions
- Improving program organization

---

## ⚠️ Note

- The application stores data in `shopping_list.txt`.
- If the file does not exist, create an empty `shopping_list.txt` before running the program.
- Changes are saved only when the user selects the **Exit** option.
- Duplicate items are not allowed in the shopping list.

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀