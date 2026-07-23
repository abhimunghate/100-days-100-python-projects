# 🚀 Day 12 - Temperature Converter

Welcome to **Day 12** of my **100 Days, 100 Python Projects** challenge!

This project is a feature-rich command-line Temperature Converter built with Python. It supports conversions between Celsius, Fahrenheit, and Kelvin, along with automatic unit detection, batch conversions, customizable decimal precision, and input validation.

---

## 📌 Project Overview

The application allows users to:

- 🌡️ Convert Celsius to Fahrenheit and Kelvin
- 🌡️ Convert Fahrenheit to Celsius and Kelvin
- 🌡️ Convert Kelvin to Celsius and Fahrenheit
- 🔄 Automatically convert any temperature to all units
- 📊 Convert multiple temperatures at once (Batch Mode)
- 🎯 Control the number of decimal places displayed

The program also validates user input and prevents invalid Kelvin temperatures.

---

## ✨ Features

- 🌡️ Celsius ↔ Fahrenheit ↔ Kelvin conversions
- 🔄 Automatic conversion to all temperature units
- 📊 Batch conversion of multiple values
- 🎯 User-defined decimal precision
- ✅ Input validation and error handling
- 🚫 Prevents negative Kelvin values
- 🖥️ Menu-driven interface
- 📚 Modular design using separate conversion functions

---

## 🛠️ Technologies Used

- Python 3

---

## 📂 Project Structure

```text
DAY_12/
│── main12.py
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main12.py
```

---

## 💻 Sample Output

```text
------ Temperature Converter Menu ------

1. Celsius to Fahrenheit & Kelvin
2. Fahrenheit to Celsius & Kelvin
3. Kelvin to Celsius & Fahrenheit
4. Automatic conversion to all units
5. Batch conversion (multiple temperatures)
6. Exit

Enter your choice (1/2/3/4/5/6) : 4
Enter the number of decimal places : 2

Enter temperature value : 25
Enter unit (C/F/K) : C

------ Converted Temperatures ------

Celsius    : 25.00 °C
Fahrenheit : 77.00 °F
Kelvin     : 298.15 K
```

---

## 📚 Concepts Practiced

- Functions
- Variables
- User Input (`input()`)
- Type Casting (`float()`, `int()`)
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Exception Handling (`try-except`)
- String Methods (`upper()`, `strip()`)
- String Formatting
- Batch Data Processing
- Modular Programming

---

## 🎯 Learning Outcome

This project helped me practice:

- Building reusable conversion functions
- Handling user input and validation
- Working with floating-point formatting
- Processing multiple inputs efficiently
- Designing menu-driven applications
- Implementing real-world error handling

---

## 🌡️ Supported Conversions

| From | To |
|--------|--------|
| Celsius | Fahrenheit, Kelvin |
| Fahrenheit | Celsius, Kelvin |
| Kelvin | Celsius, Fahrenheit |
| Any Unit | Automatic Conversion to All Units |

---

## ⚠️ Note

- Kelvin temperatures cannot be negative.
- Batch mode accepts comma-separated temperature values.
- Invalid inputs are handled gracefully without crashing the program.
- Users can choose the number of decimal places displayed in the output.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 📁 Save conversion history to a file
- 📊 Export results to CSV
- 🕒 Maintain conversion logs with timestamps
- 🎨 GUI version using Tkinter
- 🌍 Support additional temperature scales
  - Rankine
  - Réaumur
  - Delisle
- 📈 Graph temperature conversions

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀