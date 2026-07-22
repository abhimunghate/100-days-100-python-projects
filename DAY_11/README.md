# 🚀 Day 11 - Safe Calculator

Welcome to **Day 11** of my **100 Days, 100 Python Projects** challenge!

This project is a **Safe Calculator** built using Python. Unlike a basic calculator, this version includes **exception handling** and **error logging**, making it more reliable and user-friendly.

---

## 📌 Project Overview

The application provides a menu-driven calculator that performs common arithmetic operations while safely handling invalid inputs and runtime errors.

Errors are automatically recorded in a log file with timestamps for debugging and tracking purposes.

---

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🧮 Modulus
* 🔢 Exponentiation
* ⚠️ Handles invalid numeric input
* 🚫 Prevents division by zero
* 📝 Logs errors to a file with timestamps
* 🔄 Continuous menu-driven interface
* 🖥️ Beginner-friendly command-line application

---

## 🛠️ Technologies Used

* Python 3
* `time` module
* File Handling
* Exception Handling

---

## 📂 Project Structure

```text
DAY_11/
│── main11.py
│── error_log.txt
└── README.md
```

---

## ▶️ How to Run

1. Make sure **Python 3** is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main11.py
```

---

## 💻 Sample Output

```text
------ Safe Calculator Menu ------

1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
6. Exponentiation
7. Exit

Enter your choice (1-7) : 4

Enter first number : 10
Enter second number : 0

Error : Cannot divide by zero

----------------------------------------
```

---

## 📝 Error Log Example

When an error occurs, it is stored in `error_log.txt`.

```text
[22/07/2026 22:15:30] ZeroDivisionError : Cannot divide by zero
[22/07/2026 22:16:02] ValueError : could not convert string to float: 'abc'
```

This makes the calculator safer and helps in debugging issues later.

---

## 📚 Concepts Practiced

* Functions
* File Handling
* Exception Handling
* `try-except-finally`
* Custom Error Raising (`raise`)
* Loops (`while`)
* Conditional Statements (`if-elif-else`)
* Menu-Driven Programs
* Logging Errors
* Timestamps using `time.strftime()`

---

## 🎯 Learning Outcome

This project helped me practice:

* Writing reusable functions
* Handling runtime errors gracefully
* Using `try`, `except`, and `finally`
* Raising custom exceptions
* Logging errors to a file
* Building a robust command-line application

---

## ⚠️ Error Handling Implemented

### ValueError

Handles invalid numeric input.

```python
except ValueError as e:
```

### ZeroDivisionError

Prevents division and modulus by zero.

```python
except ZeroDivisionError as e:
```

### Generic Exception

Catches unexpected errors.

```python
except Exception as e:
```

---

## 🔮 Future Improvements

Possible enhancements for future versions:

* ➗ Add Floor Division (`//`)
* 🧠 Add scientific calculator functions (`sqrt`, `sin`, `cos`, `log`)
* 📜 View error logs from the application
* 💾 Save calculation history
* 🎨 Create a GUI version using Tkinter
* 🌐 Build a web calculator using Flask

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen logical thinking, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀
