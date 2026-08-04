# 👨‍💼 Day 24 - Employee Management System

Welcome to **Day 24** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Employee Management System** built with Python using **Object-Oriented Programming (OOP)** principles. It allows users to manage different types of employees, including Regular Employees, Managers, Developers, and Interns. Employee records are stored permanently using a JSON file, making the data available even after the application is closed.

---

## 📌 Project Overview

The application enables users to:

- 👤 Add different types of employees
- 📋 Display all employee records
- 🔍 Search employees by Employee ID
- 💰 Calculate bonuses based on employee type
- 💾 Store employee information permanently using JSON

The project demonstrates **Inheritance**, **Polymorphism**, **Method Overriding**, and **JSON file handling** in Python.

---

## ✨ Features

- 👤 Add Regular Employees
- 👨‍💼 Add Managers with department information
- 👨‍💻 Add Developers with programming language
- 🎓 Add Interns with internship duration
- 📋 Display complete employee details
- 🔍 Search employees using Employee ID
- 💰 Automatic bonus calculation based on employee role
- 💾 Persistent storage using JSON
- 🚫 Prevent duplicate Employee IDs
- ✅ Input validation for salary and duration
- 🖥️ Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- `json` Module
- `os` Module
- Object-Oriented Programming (OOP)
- Inheritance
- Polymorphism
- Method Overriding

---

## 📂 Project Structure

```text
DAY_24/
│── main24.py
│── employees.json
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the application:

```bash
python main24.py
```

If `employees.json` does not exist, it will be created automatically.

---

## 💻 Sample Output

### Main Menu

```text
------ Employee Management System ------

1. Add Employee
2. Display All Employees
3. Search Employee
4. Exit
```

---

### Adding a Manager

```text
------ Choose Employee Type ------

1. Regular Employee
2. Manager
3. Developer
4. Intern

Enter your choice : 2

Enter Employee Name : John Smith
Enter Employee ID : EMP101
Enter Employee Salary : 75000
Enter Department : Human Resources

Employee added successfully!
```

---

### Displaying Employees

```text
------ All Employees ------

Total Employees : 2

------ Employee Details ------

Name : John Smith
Employee ID : EMP101
Salary : $75000.00
Employee Type : Manager
Department : Human Resources
Bonus : $15000.00
```

---

### Searching an Employee

```text
Enter Employee ID : EMP101

------ Employee Details ------

Name : John Smith
Employee ID : EMP101
Salary : $75000.00
Employee Type : Manager
Department : Human Resources
Bonus : $15000.00
```

---

## 📄 Data Storage

All employee records are stored in **`employees.json`**.

Example:

```json
[
    {
        "type": "Manager",
        "name": "John Smith",
        "emp_id": "EMP101",
        "salary": 75000,
        "department": "Human Resources"
    },
    {
        "type": "Developer",
        "name": "Alice Johnson",
        "emp_id": "EMP102",
        "salary": 65000,
        "programming_language": "Python"
    },
    {
        "type": "Intern",
        "name": "David Lee",
        "emp_id": "EMP103",
        "salary": 15000,
        "duration": 6
    }
]
```

---

## 📚 Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Inheritance
- Method Overriding
- Polymorphism
- JSON File Handling
- Reading & Writing JSON
- File Handling
- Lists
- Loops
- Conditional Statements
- Functions
- User Input Validation

---

## 🎯 Learning Outcome

This project helped me practice:

- Designing applications using Object-Oriented Programming
- Implementing inheritance and polymorphism
- Overriding methods in child classes
- Managing employee data using JSON
- Building reusable classes and methods
- Performing role-based bonus calculations
- Validating user input effectively
- Creating interactive menu-driven applications

---

## ⚠️ Note

- Employee records are automatically stored in `employees.json`.
- Employee IDs must be unique.
- Interns receive a fixed monthly stipend.
- Bonus percentages vary depending on employee type:
  - 👤 Employee: **10%**
  - 👨‍💼 Manager: **20%**
  - 👨‍💻 Developer: **50%**
  - 🎓 Intern: **No bonus**
- Data is preserved between program executions.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- ✏️ Edit employee information
- 🗑️ Delete employee records
- 📊 Salary statistics and reports
- 📈 Employee performance ratings
- 💵 Tax and salary deductions
- 🏢 Multiple department management
- 📅 Attendance tracking
- 🔐 Login and authentication system
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🗄️ Database integration using SQLite or MySQL

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀