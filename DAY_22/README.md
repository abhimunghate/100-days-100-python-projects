# 🚀 Day 22 - Bank Account Simulator

Welcome to **Day 22** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Bank Account Simulator** built with Python using **Object-Oriented Programming (OOP)** concepts. It allows users to create multiple bank accounts, perform transactions such as deposits, withdrawals, transfers, apply interest, and view transaction history, all through an interactive menu-driven interface.

---

## 📌 Project Overview

The application enables users to:

- 🏦 Create multiple bank accounts
- 💰 Deposit money
- 💸 Withdraw money
- 🔄 Transfer money between accounts
- 📈 Apply interest to account balances
- 📋 View account details
- 🧾 Track complete transaction history
- 👥 Manage multiple users during a single program execution

The project demonstrates the use of **classes, objects, dictionaries, and methods** to simulate basic banking operations.

---

## ✨ Features

- 🏦 Create new bank accounts
- 💰 Deposit money
- 💸 Withdraw money
- 🔄 Transfer money between accounts
- 📈 Add interest to account balance
- 📋 View account details
- 🧾 Transaction history for every account
- 👥 Supports multiple bank accounts
- 🚫 Prevent duplicate account creation
- ⚠️ Input validation and error handling
- 🖥️ Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Classes & Objects
- Dictionaries
- Lists
- Functions
- Exception Handling

---

## 📂 Project Structure

```text
DAY_22/
│── main22.py
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal inside the project folder.
4. Run the application

```bash
python main22.py
```

---

## 💻 Sample Output

```text
------ Bank Account Simulator ------

1. Create Account
2. Access Account
3. Exit

Enter your choice : 1

Enter account holder's name : Abhijit
Enter initial Deposit Amount : 5000

Account created successfully!
```

---

### Deposit Money

```text
Enter deposit amount : 1500

Deposited $1500.00
Current balance : $6500.00
```

---

### Withdraw Money

```text
Enter withdrawal amount : 1000

Withdrew $1000.00
New balance : $5500.00
```

---

### Transfer Money

```text
Enter receiver name : Rahul
Enter amount : 500

Transferred $500.00 to Rahul.
Current Balance : $5000.00
```

---

### Account Details

```text
------ Account Details ------

Account Holder : Abhijit
Account Balance : $5000.00
```

---

### Transaction History

```text
------ Transaction History ------

Account created | Initial Balance : $5000.00
Deposited $1500.00 | Balance : $6500.00
Withdrew $1000.00 | Balance : $5500.00
Transferred $500.00 to Rahul | Balance : $5000.00
```

---

## 📚 Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes & Objects
- Constructors (`__init__`)
- Instance Variables
- Class Methods
- Dictionaries
- Lists
- Loops
- Conditional Statements
- Functions
- Exception Handling
- Input Validation

---

## 🎯 Learning Outcome

This project helped me practice:

- Designing applications using Object-Oriented Programming
- Creating and managing multiple objects
- Working with dictionaries to store objects
- Implementing real-world banking operations
- Recording transaction history
- Validating user input
- Building menu-driven command-line applications
- Improving code organization using methods and classes

---

## ⚠️ Note

- All account data is stored **only in memory**.
- Accounts are **not saved permanently** after the program exits.
- Duplicate account names are not allowed.
- Interest is applied only when the account balance is greater than zero.
- Transfers can only be made to existing accounts.
- Negative deposits and withdrawals are not allowed.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 💾 Save account data permanently using JSON or a database
- 🔐 Password-protected accounts
- 🏦 Unique account numbers
- 📊 Monthly bank statements
- 💳 Loan management system
- 💵 Transaction receipts
- 📅 Transaction timestamps
- 📈 Different account types (Savings/Current)
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🌐 Web-based banking application using Flask or Django

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀