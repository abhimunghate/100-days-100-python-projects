# 🚀 Day 5 - Countdown Timer

Welcome to **Day 5** of my **100 Days, 100 Python Projects** challenge!

This project is a simple Python countdown timer that counts down from a user-specified number with a customizable delay between each count. It also displays a motivational halfway message and a custom message when the countdown finishes.

---

## 📌 Project Overview

The program asks the user to enter:

- ⏳ Starting number for the countdown
- ⌛ Delay between each countdown step (in seconds)
- 💬 A custom message to display when the countdown ends

During the countdown, the program pauses for the specified delay after each number, displays a halfway message, and finally prints the user's custom message along with a completion message.

---

## ✨ Features

- ⏱️ Countdown from any positive integer
- ⚙️ Custom delay between countdown steps
- 💬 User-defined completion message
- 👋 Displays a "Halfway there!" message
- 🚫 Handles zero and negative inputs
- 🖥️ Beginner-friendly command-line application

---

## 🛠️ Technologies Used

- Python 3
- `time` module

---

## 📂 Project Structure

```
DAY_5/
│── main5.py
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main5.py
```

---

## 💻 Sample Output

```
Enter the number to start the countdown from : 10
Enter the number of seconds to delay the timer (e.g. 0.5s, 1s, 1.5s,...) : 1
Enter the message to display when the countdown ends : Time's Up!

------ Countdown Begins ------

10
9
8
7
6
You are Halfway there! 👋
5
4
3
2
1

Time's Up!

Countdown Finished! 🎉
```

---

## 📚 Concepts Practiced

- Variables
- User Input (`input()`)
- Type Casting (`int()`, `float()`)
- `while` Loop
- Conditional Statements (`if`, `elif`, `else`)
- Arithmetic Operations
- Importing Modules
- `time.sleep()`
- Formatted Strings (f-strings)

---

## 🎯 Learning Outcome

This project helped me practice:

- Creating a countdown timer
- Working with loops and conditions
- Using Python's `time` module
- Accepting user-defined delays
- Displaying custom messages
- Handling invalid user input

---

## ⚠️ Note

- The countdown only accepts positive integers.
- Decimal values are supported for the delay (e.g., `0.5`, `1`, `1.5` seconds).
- If the starting number is `0` or negative, the program displays an appropriate message instead of starting the countdown.

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and maintain a consistent coding habit.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀