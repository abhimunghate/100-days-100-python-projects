# 🚀 Day 28 - Mini ATM Machine

Welcome to **Day 28** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Mini ATM / Banking System** built with Python. It simulates a basic banking environment where users can create accounts, log in using a PIN, perform banking operations, view transaction history, and manage different types of accounts.

The system also includes an **Admin Dashboard** for managing users, viewing accounts and transactions, and freezing or unfreezing accounts.

---

## 📌 Project Overview

The Mini ATM Machine provides a simple banking simulation with support for:

* 👤 User registration and PIN authentication
* 🏦 Multiple bank account types
* 💰 Deposits and withdrawals
* 💳 Credit card purchases and payments
* 💵 Savings account interest
* 📜 Transaction history
* 🔒 Account freeze/unfreeze functionality
* 👨‍💼 Admin dashboard
* 💾 Persistent data storage using JSON
* 🔢 Automatic account number generation

All banking data is stored in `atm_data.json`, allowing the data to remain available even after restarting the program.

---

## ✨ Features

### 👤 User Management

* Create a new user
* Unique User ID validation
* Four-digit PIN authentication
* Secure PIN validation
* User login and logout
* View all accounts associated with a user

### 🏦 Account Management

The system supports three account types:

* 💳 Checking Account
* 💰 Savings Account
* 💳 Credit Card Account

Each account receives a unique account number such as:

```text
ACC1001
ACC1002
ACC1003
```

---

### 💰 Checking & Savings Accounts

Users can:

* Check account balance
* Deposit money
* Withdraw money
* View transaction history

Savings accounts additionally support:

* 📈 Adding interest to the account balance

The default savings interest rate is **4%**.

---

### 💳 Credit Card

Credit Card accounts support:

* Check available credit
* View credit limit
* View used credit
* Make purchases
* Make credit card payments
* View transaction history

The default credit limit is:

```text
₹50,000
```

Users can also specify a custom credit limit while creating the account.

---

### 📜 Transaction History

Every transaction is recorded with:

* Transaction type
* Amount
* Description
* Date and time

Example:

```text
2026-08-08 23:30:12 | DEPOSIT         | ₹5000.00 | Cash deposit
2026-08-08 23:35:18 | WITHDRAWAL      | ₹1000.00 | Cash withdrawal
```

Supported transaction types include:

* `DEPOSIT`
* `WITHDRAWAL`
* `INTEREST`
* `PURCHASE`
* `PAYMENT`

---

### 🔒 Account Freeze System

Administrators can freeze or unfreeze accounts.

A frozen account cannot perform banking operations such as:

* Deposits
* Withdrawals
* Credit card purchases
* Credit card payments

The account status is displayed as:

```text
ACTIVE
```

or

```text
FROZEN
```

---

### 👨‍💼 Admin Dashboard

The system includes a separate administrator interface.

Admin features include:

* 👥 View all users
* 🏦 View all accounts
* 📜 View all transactions
* 🔒 Freeze an account
* 🔓 Unfreeze an account
* 🚪 Admin logout

Default admin credentials configured in the program:

```text
Username : admin
Password : admin123
```

> ⚠️ These credentials are for demonstration purposes only and should not be used in a real banking application.

---

## 🛠️ Technologies Used

* Python 3
* `datetime` Module
* `json` Module
* `os` Module
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling

---

## 📂 Project Structure

```text
DAY_28/
│── main28.py
│── atm_data.json
└── README.md
```

> `atm_data.json` is created automatically when the program saves banking data for the first time.

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal inside the project folder.
4. Run the application:

```bash
python main28.py
```

The main menu will appear:

```text
====== MINI BANKING SYSTEM ======

1. Create User
2. User Login
3. Admin Login
4. Exit
```

---

## 💻 Sample Usage

### Creating a User

```text
====== MINI BANKING SYSTEM ======

1. Create User
2. User Login
3. Admin Login
4. Exit

Choose option : 1

Enter user ID : user101
Enter name : Abhijit
Set 4-digit PIN : 1234

User created successfully.
```

---

### User Login

```text
Enter User ID : user101
Enter PIN : 1234

Welcome, Abhijit!
```

The user dashboard:

```text
------ User Dashboard ------

1. View Accounts
2. Create Account
3. Account Operations
4. Logout
```

---

### Creating an Account

```text
------ Create Account ------

1. Checking Account
2. Savings Account
3. Credit Card

Choose account type : 2

Savings created successfully.
Account Number : ACC1001
```

---

### Deposit

```text
Enter amount : 5000

₹5000.00 deposited successfully.
New Balance : ₹5000.00
```

---

### Withdrawal

```text
Enter amount : 1000

₹1000.00 withdrawn successfully.
New Balance : ₹4000.00
```

---

### Savings Interest

```text
₹160.00 interest added.
```

For example, with a balance of ₹4000 and a 4% interest rate:

```text
Interest = ₹4000 × 4 / 100
         = ₹160
```

---

### Transaction History

```text
------ Transaction History ------

2026-08-08 23:30:12 | DEPOSIT         | ₹5000.00 | Cash deposit
2026-08-08 23:32:20 | WITHDRAWAL      | ₹1000.00 | Cash withdrawal
2026-08-08 23:35:45 | INTEREST        | ₹160.00  | 4% savings interest
```

---

## 💳 Credit Card Example

A user can create a credit card with a custom limit:

```text
Enter credit limit : 75000
```

The account can then be used for purchases:

```text
Purchase amount : 5000

Purchase of ₹5000.00 successful.

Credit Limit     : ₹75000.00
Credit Used      : ₹5000.00
Available Credit : ₹70000.00
```

The user can later make a payment:

```text
Payment amount : 2000

₹2000.00 credit card payment successful.
```

---

## 👨‍💼 Admin Dashboard Example

```text
====== ADMIN DASHBOARD ======

1. View All Users
2. View All Accounts
3. View All Transactions
4. Freeze Account
5. Unfreeze Account
6. Logout
```

### View Users

```text
------ All Users ------

ID: user101 | Name: Abhijit | Accounts: 2
```

### View Accounts

```text
User: Abhijit | Account: ACC1001 | Type: Savings | Status: ACTIVE
Balance: ₹5000.00
```

### Freeze Account

```text
Enter account number : ACC1001

Account frozen successfully.
```

---

## 📄 Data Storage

All application data is stored in:

```text
atm_data.json
```

The file stores:

* User information
* PINs
* Account information
* Account balances
* Account status
* Credit card limits
* Credit card usage
* Transaction history

A simplified structure looks like:

```json
{
    "users": {
        "user101": {
            "user_id": "user101",
            "name": "Abhijit",
            "pin": "1234",
            "accounts": [
                "ACC1001"
            ]
        }
    },
    "accounts": {
        "ACC1001": {
            "account_number": "ACC1001",
            "account_type": "Savings",
            "balance": 5000,
            "is_frozen": false,
            "transactions": []
        }
    }
}
```

---

## 📚 Concepts Practiced

* Object-Oriented Programming
* Classes and Objects
* Constructors
* Inheritance
* Method Overriding
* Encapsulation
* Polymorphism
* Dictionaries
* Lists
* JSON File Handling
* Reading and Writing JSON
* Persistent Data Storage
* File Existence Checking
* Exception Handling
* User Authentication
* PIN Validation
* Transaction Management
* Account Management
* Conditional Statements
* Loops
* Input Validation
* Date and Time Handling
* Static Data Structures
* Menu-Driven Applications

---

## 🎯 OOP Concepts Used

This project focuses heavily on **Object-Oriented Programming**.

### Inheritance

```text
BankAccount
├── SavingsAccount
├── CheckingAccount
└── CreditCardAccount
```

### Composition

A `User` can have multiple bank accounts, while each account can contain multiple `Transaction` objects.

### Encapsulation

The user's PIN is stored using a private attribute:

```python
self.__pin
```

### Polymorphism

Different account classes implement their own behavior, such as:

```python
check_balance()
```

and:

```python
to_dict()
```

---

## 🎓 Learning Outcome

This project helped me practice:

* Designing a larger Python application using OOP
* Understanding inheritance and polymorphism
* Managing relationships between multiple objects
* Building a user authentication system
* Working with persistent JSON data
* Creating different account types with specialized behavior
* Implementing transaction tracking
* Handling account states such as frozen and active
* Creating separate user and admin workflows
* Validating financial operations
* Building a more structured command-line application

---

## ⚠️ Security Note

This project is intended for **learning and simulation purposes only**.

It is **not a real banking application**.

The current implementation stores PINs directly in the JSON file and uses hardcoded administrator credentials. A production banking system should use:

* Password/PIN hashing
* Secure authentication
* Encryption
* Access control
* Secure session management
* Database-backed storage
* Audit logging
* Rate limiting
* Multi-factor authentication
* Secure secret management

---

## 🔮 Future Improvements

Possible enhancements for future versions:

* 🔐 Hash user PINs using a secure hashing algorithm
* 🔑 Change PIN functionality
* 🚫 Account lockout after multiple failed login attempts
* 💸 Money transfer between accounts
* 📱 OTP / Two-Factor Authentication
* 🗄️ Replace JSON storage with SQLite or MySQL
* 📊 Generate account statements
* 📅 Transaction filtering by date
* 🔎 Search transactions
* 💰 Daily withdrawal limits
* 🏦 Multiple users per account
* 📧 Transaction notifications
* 🧾 Generate downloadable transaction receipts
* 🖥️ GUI version using Tkinter or CustomTkinter
* 🌐 Web-based banking dashboard
* 🔒 Proper role-based access control for administrators

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, practice Object-Oriented Programming, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀
