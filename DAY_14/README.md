# 🚀 Day 14 - Random Password Generator

Welcome to **Day 14** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line Random Password Generator built with Python. It allows users to generate one or more secure passwords with customizable options, ensuring that selected character types are included in every password. Users can also save generated passwords with timestamps for future reference.

---

## 📌 Project Overview

The application allows users to:

- 🔐 Generate secure random passwords
- 📏 Choose the password length
- 🔢 Generate multiple passwords at once
- 🔡 Include uppercase letters
- 🔠 Include lowercase letters
- 🔢 Include digits
- 🔣 Include special characters
- 💾 Save selected passwords to a file with timestamps

The program validates user input to ensure strong and usable passwords are generated.

---

## ✨ Features

- 🔐 Generate random passwords
- 📏 Custom password length
- 🔢 Generate multiple passwords in one run
- ✅ Guarantees inclusion of selected character types
- 🔡 Uppercase letter support
- 🔠 Lowercase letter support
- 🔢 Number support
- 🔣 Special character support
- 💾 Save passwords to a text file
- 🕒 Automatic timestamp for saved passwords
- ⚠️ Input validation and error handling

---

## 🛠️ Technologies Used

- Python 3
- `random` Module
- `string` Module
- `time` Module
- File Handling

---

## 📂 Project Structure

```text
DAY_14/
│── main14.py
│── saved_passwords.txt
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main14.py
```

---

## 💻 Sample Output

```text
Enter the desired password length : 12
How many passwords do you want to generate? : 2

Include uppercase letters? (Y/N): Y
Include lowercase letters? (Y/N): Y
Include digits? (Y/N): Y
Include special characters? (Y/N): Y

Generated Passwords:

----------------------------------------

Password 1 : K#4m!P9x@Q2a

Do you want to save this password? (Y/N): Y
Password saved successfully!

----------------------------------------

Password 2 : 7@Lp$8nQ!f2R

Do you want to save this password? (Y/N): N
Password not saved.
```

---

## 📚 Concepts Practiced

- Functions
- Variables
- Lists
- Strings
- User Input (`input()`)
- Type Casting (`int()`)
- Conditional Statements (`if`, `else`)
- Loops (`for`, `while`)
- Exception Handling (`try-except`)
- File Handling
- Random Number Generation
- String Manipulation
- List Operations (`append()`, `shuffle()`)
- Input Validation

---

## 🎯 Learning Outcome

This project helped me practice:

- Building a secure password generator
- Using Python's `random` and `string` modules
- Creating reusable functions
- Validating user input
- Working with file handling
- Saving generated data with timestamps
- Writing modular and maintainable code

---

## 🔒 Password Options

Users can choose whether to include:

| Character Type | Example |
|----------------|---------|
| Uppercase Letters | `A-Z` |
| Lowercase Letters | `a-z` |
| Digits | `0-9` |
| Special Characters | `! @ # $ % ^ & *` |

The generated password always contains at least one character from every selected category.

---

## ⚠️ Note

- At least one character type must be selected.
- The password length must be greater than zero.
- If multiple character types are selected, the password length must be at least equal to the number of selected categories.
- Saved passwords are stored in `saved_passwords.txt` with timestamps.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 📋 Copy passwords directly to the clipboard
- 👁️ Password strength indicator
- 🚫 Exclude ambiguous characters (e.g., `O`, `0`, `I`, `l`)
- 📂 Categorize saved passwords by website or application
- 🔍 Search previously saved passwords
- 🔐 Encrypt saved passwords
- 🖥️ Build a graphical interface using Tkinter or CustomTkinter

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀