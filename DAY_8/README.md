# 🚀 Day 8 - Contact Book

Welcome to **Day 8** of my **100 Days, 100 Python Projects** challenge!

This project is a **menu-driven Contact Book application** built using Python. It allows users to add, view, search, edit, and delete contacts directly from the command line.

---

## 📌 Project Overview

The application stores contact information using a **Python dictionary** and supports multiple phone numbers and email addresses for the same contact name.

Users can manage their contacts through a simple interactive menu.

---

## ✨ Features

* 📋 View all contacts
* ➕ Add new contacts
* 🔍 Search contacts by name
* ✏️ Edit existing contact details
* 🗑️ Delete specific contact entries
* 👥 Support multiple phone numbers and emails for the same person
* 🚫 Handles invalid menu selections gracefully
* 🖥️ Beginner-friendly command-line interface

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
DAY_8/
│── main8.py
└── README.md
```

---

## ▶️ How to Run

1. Make sure **Python 3** is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main8.py
```

---

## 💻 Sample Output

```text
------ Contact Book Menu ------

1. View Contacts.
2. Add Contact.
3. Search Contact.
4. Edit Contact.
5. Delete Contact.
6. Exit.

Enter your choice (1-6) : 2

Enter contact name : Abhijit
Enter contact number : 9876543210
Enter contact email : abhijit@example.com

Contact Abhijit has been added to your contact book successfully!
```

---

## 📚 Concepts Practiced

* Functions
* Dictionaries
* Lists
* Nested Data Structures
* Loops (`while`, `for`)
* Conditional Statements (`if`, `elif`, `else`)
* User Input Handling
* List Methods (`append()`, `pop()`)
* Dictionary Operations
* `enumerate()`
* String Formatting (f-strings)

---

## 🧠 Data Structure Used

The contact book stores data in the following format:

```python
contacts = {
    'Abhijit': [
        {'Phone': '9876543210', 'Email': 'abhijit@example.com'},
        {'Phone': '9123456780', 'Email': 'work@example.com'}
    ]
}
```

This structure allows a single contact name to have **multiple phone numbers and email addresses**.

---

## 🎯 Learning Outcome

This project helped me practice:

* Organizing code into functions
* Working with nested dictionaries and lists
* Managing dynamic data
* Implementing CRUD operations:

  * **Create** → Add Contact
  * **Read** → View/Search Contact
  * **Update** → Edit Contact
  * **Delete** → Delete Contact
* Building a complete menu-driven application

---

## ⚠️ Note

* Contact names are automatically converted to **Title Case** for consistency.
* The current version stores contacts in memory only.
* All contacts are lost when the program is closed.
* A future improvement would be to add **file handling** or a **database** for permanent storage.

---

## 🚀 Future Improvements

* 💾 Save contacts to a file (JSON/CSV)
* 📱 Add phone number validation
* 📧 Validate email format
* 🔢 Sort contacts alphabetically
* ⭐ Add favorite contacts
* 🔐 Add password protection

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen logical thinking, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀
