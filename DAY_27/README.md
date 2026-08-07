# 🚀 Day 27 - Inventory Management System

Welcome to **Day 27** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Inventory Management System** built with Python. It allows users to manage products, track stock quantities, sell products, monitor low-stock levels, check expiry dates for perishable items, calculate discounts, and export inventory data to a CSV file.

The application uses **JSON for persistent inventory storage** and **CSV for data export**.

---

## 📌 Project Overview

The Inventory Management System enables users to:

* 📦 Add and manage products
* 📋 View all products in the inventory
* 🛒 Sell products and automatically update stock
* ⚠️ Monitor low-stock products
* 🗓️ Track expiry dates for perishable products
* 💰 Calculate discounted prices
* 📊 View the total number of items
* 📄 Export inventory data to CSV
* 💾 Store inventory permanently using JSON

The inventory is automatically loaded when the application starts and saved whenever changes are made.

---

## ✨ Features

* 📦 Add new products to inventory
* 🔄 Increase quantity when an existing product is added
* 💰 Store product prices
* 🛒 Sell products and update stock automatically
* ⚠️ Low-stock alerts when quantity reaches 5 or below
* 🚨 Out-of-stock detection
* 🥛 Support for perishable products
* 📅 Automatic expiry-date calculation
* ⚠️ Expiry alerts for products expiring within 3 days
* ❌ Detect expired products
* 💵 Calculate product discounts
* 📊 Display total inventory quantity
* 📄 Export inventory to CSV
* 💾 Persistent storage using JSON
* 🛡️ Input validation and exception handling
* 🖥️ Menu-driven command-line interface

---

## 🛠️ Technologies Used

* Python 3
* `json` Module
* `csv` Module
* `datetime` Module
* `timedelta`
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling

---

## 📂 Project Structure

```text
DAY_27/
│── main27.py
│── inventory.json
│── inventory.csv
└── README.md
```

> `inventory.json` and `inventory.csv` are generated/updated by the application.

---

## ▶️ How to Run

1. Make sure **Python 3** is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the application:

```bash
python main27.py
```

If `inventory.json` does not exist, the application will handle the missing inventory file and start with an empty inventory.

---

## 💻 Main Menu

```text
------ Inventory Management System ------

1. Add Product
2. View Products
3. Sell Product
4. Calculate Discount
5. Total Items Report
6. Export Inventory to CSV
7. Check Inventory Alerts
8. Exit

Enter your choice (1-8) :
```

---

## 📦 Adding a Product

The application asks for:

* Product name
* Price
* Quantity
* Whether the product is perishable
* Number of days until expiry if applicable

Example:

```text
Enter product name : Milk
Enter price : 50
Enter quantity : 10
Is this a perishable item? (y/n) : y
How many days will it last? : 3

10 Milk(s) added to inventory.
Perishable : Yes
Expiry Date : 2026-08-10
```

If a product already exists, its quantity is increased instead of creating a duplicate product.

---

## 📋 Viewing Products

Example:

```text
------ Inventory ------

Total Product Types : 2

------ Product Details ------

Product Name : Milk
Price : $50.00
Quantity : 10

Perishable : Yes
Expiry Date : 2026-08-10
```

The application also checks each product for:

* Low stock
* Expiry warnings
* Expired products

---

## 🛒 Selling Products

Users can sell a specific quantity of a product.

Example:

```text
Enter product name to sell : Milk
Enter amount to sell : 6

6 Milk(s) sold.
```

The inventory quantity is automatically reduced.

If the remaining quantity is low:

```text
⚠ Low stock alert :
Milk has only 4 item(s) left.
```

If the quantity reaches zero:

```text
⚠ OUT OF STOCK:
Milk is completely out of stock.
```

---

## 💰 Discount Calculator

The application includes a discount calculator for calculating the final price after applying a percentage discount.

Example:

```text
Enter price : 1000
Enter discount percentage : 20

Discounted Price : $800.00
```

The discount percentage must be between **0 and 100**.

---

## 📊 Total Items Report

The application keeps track of the total quantity of all products.

Example:

```text
------ Total Items Report ------

Total Items : 35
```

The total is automatically updated when products are added or sold.

---

## ⚠️ Inventory Alerts

The application automatically checks for inventory problems.

### Low Stock

Products with **5 or fewer items** remaining generate a low-stock warning.

```text
⚠ Low stock: Keyboard
Has only 3 item(s).
```

### Expiring Soon

Perishable products expiring within 3 days generate an alert.

```text
⚠ Expiry alert:
Milk
Expires in 2 day(s).
```

### Expiring Today

```text
⚠ EXPIRING TODAY :
Milk.
```

### Expired Products

```text
⚠ EXPIRED : Milk
Expired on 2026-08-05.
```

---

## 📄 Export Inventory to CSV

The inventory can be exported to:

```text
inventory.csv
```

The CSV contains:

```text
Product Name,Price,Quantity,Perishable,Expiry Date
```

Example:

```csv
Milk,50.0,10,True,2026-08-10
Keyboard,1500.0,8,False,
```

---

## 💾 Data Storage

Inventory information is stored in:

```text
inventory.json
```

Example:

```json
[
    {
        "product_name": "Milk",
        "price": 50.0,
        "quantity": 10,
        "is_perishable": true,
        "expiry_date": "2026-08-10"
    },
    {
        "product_name": "Keyboard",
        "price": 1500.0,
        "quantity": 8,
        "is_perishable": false,
        "expiry_date": null
    }
]
```

The JSON file allows inventory data to remain available after restarting the application.

---

## 📚 Concepts Practiced

* Object-Oriented Programming
* Classes and Objects
* Class Variables
* Static Methods
* Class Methods
* Functions
* JSON File Handling
* CSV File Handling
* Reading and Writing Files
* `datetime` and `timedelta`
* Lists and Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* Input Validation
* Data Persistence
* Inventory Tracking
* Stock Management
* Date Calculations

---

## 🎯 Learning Outcome

This project helped me practice:

* Building an application using **Object-Oriented Programming**
* Managing product data using classes and objects
* Working with persistent JSON data
* Exporting structured data to CSV
* Performing date calculations using `datetime`
* Implementing stock management logic
* Creating low-stock and expiry alerts
* Using static and class methods
* Handling invalid input and corrupted files
* Building a more structured command-line application

---

## ⚠️ Notes

* The low-stock threshold is currently set to **5 items**.
* Product prices must be greater than 0.
* Product quantities must be greater than 0 when adding stock.
* Discount percentages must be between 0 and 100.
* Perishable products automatically receive an expiry date based on the number of days entered.
* Inventory data is stored in `inventory.json`.
* CSV exports are saved as `inventory.csv`.
* Expiry alerts are checked when the application starts and when the user selects **Check Inventory Alerts**.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

* ✏️ Edit existing products
* 🗑️ Delete products
* 🔍 Search products by name
* 📈 Generate inventory statistics
* 📊 Add graphical inventory reports
* 🧾 Generate sales receipts
* 💰 Track total sales and revenue
* 📦 Add supplier information
* 🏷️ Add product categories and IDs
* 🔐 Add user authentication
* 📅 Add automatic expiry notifications
* 🖥️ Create a GUI using Tkinter or CustomTkinter
* 🌐 Develop a web-based inventory dashboard
* 🗄️ Replace JSON storage with SQLite/MySQL

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, practice real-world application development, and maintain consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀
