# 🔐 Day 26 - Secure User Profile App

Welcome to **Day 26** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Secure User Profile App** built with Python using **Object-Oriented Programming (OOP)** principles. It allows users to create secure profiles, update email addresses, reset passwords, and manage user information. The application validates email addresses, enforces strong password rules, and stores user data permanently using a JSON file.

---

## 📌 Project Overview

The application enables users to:

- 👤 Create secure user profiles
- 📋 View all registered user profiles
- 📧 Update email addresses
- 🔑 Reset passwords securely
- 🛡️ Enforce strong password requirements
- 💾 Store user information permanently using JSON

The project demonstrates **Encapsulation**, **Data Validation**, **JSON file handling**, and secure password management concepts in Python.

---

## ✨ Features

- 👤 Create new user profiles
- 📧 Validate email format before saving
- 🔒 Strong password validation
- 🔑 Password reset with current password verification
- 👀 Display user profiles while hiding passwords
- 🚫 Prevent duplicate usernames
- 💾 Persistent storage using JSON
- 🛡️ Encapsulation using protected and private attributes
- ✅ Input validation for usernames, emails, and passwords
- 🖥️ Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- `json` Module
- `os` Module
- Object-Oriented Programming (OOP)
- Encapsulation
- File Handling

---

## 📂 Project Structure

```text
DAY_26/
│── main26.py
│── users.json
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the application:

```bash
python main26.py
```

If `users.json` does not exist, it will be created automatically.

---

## 🔐 Password Requirements

Passwords must satisfy the following conditions:

- Minimum **8 characters**
- At least **one uppercase letter**
- At least **one lowercase letter**
- At least **one digit**
- At least **one special character**

Example of a valid password:

```text
Python@123
```

---

## 💻 Sample Output

### Main Menu

```text
------ Secure User Profile App ------

1. Create User
2. View All Profiles
3. Update Email
4. Reset Password
5. Exit
```

---

### Creating a User

```text
Enter username : Abhijit
Enter email : abhijit@example.com
Enter password : Python@123

User created successfully
```

---

### Viewing Profiles

```text
Total Users : 1

------ User Profile ------

Username : Abhijit
Email : abhijit@example.com
Password : ********
```

---

### Updating Email

```text
Enter username to update email : Abhijit
Enter new email : abhijit123@gmail.com

Email updated successfully
```

---

### Resetting Password

```text
Enter username : Abhijit

Enter current password : Python@123
Enter new password : Secure@456

Password updated successfully.
```

---

## 📄 Data Storage

All user profiles are stored in **`users.json`**.

Example:

```json
[
    {
        "username": "Abhijit",
        "email": "abhijit@example.com",
        "password": "Python@123"
    },
    {
        "username": "John",
        "email": "john@gmail.com",
        "password": "John@2026"
    }
]
```

---

## 📚 Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Encapsulation
- Protected Attributes
- Private Attributes
- Getter and Setter Methods
- Method Validation
- JSON File Handling
- Reading & Writing JSON
- File Handling
- User Input Validation
- Exception Handling
- Lists
- Loops
- Conditional Statements

---

## 🎯 Learning Outcome

This project helped me practice:

- Implementing encapsulation using protected and private attributes
- Creating getter and setter methods
- Validating user input effectively
- Designing secure password policies
- Managing persistent user data using JSON
- Preventing duplicate usernames
- Building menu-driven applications
- Writing clean and reusable Object-Oriented code

---

## ⚠️ Note

- User data is automatically stored in `users.json`.
- Usernames must be unique.
- Passwords are validated before being accepted.
- Passwords are hidden when displaying user profiles.
- Current password verification is required before resetting a password.
- Invalid user records in the JSON file are skipped automatically while loading.

> **Educational Note:**  
> This project stores passwords as plain text for learning purposes. In real-world applications, passwords should **never** be stored in plain text. Instead, they should be securely hashed using libraries such as **bcrypt**, **argon2**, or **hashlib**.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 🔐 Hash passwords using `bcrypt`
- 👤 User login and authentication system
- 🔑 Forgot password functionality
- 📱 OTP verification via email
- 📧 Email confirmation during registration
- 🖼️ Profile picture support
- 👥 User roles (Admin/User)
- 🗑️ Delete user accounts
- ✏️ Edit usernames
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🗄️ Database integration using SQLite or MySQL

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀