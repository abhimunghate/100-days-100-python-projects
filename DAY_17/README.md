# 🚀 Day 17 - Student Report Generator

Welcome to **Day 17** of my **100 Days, 100 Python Projects** challenge!

This project is a Python-based **Student Report Generator** that reads student marks from a CSV file, calculates averages, assigns grades, determines pass/fail status, identifies top performers, and generates a detailed report in a new CSV file.

---

## 📌 Project Overview

The program reads student data from an input CSV file named `students.csv`.

For every student, it:

* 🧮 Calculates the average score
* 🎓 Assigns a grade
* ✅ Determines pass or fail status
* 🏆 Identifies the top performer(s)
* 📄 Generates a detailed student report
* 🔍 Allows users to search for a student by name

The processed data is saved in a new file named `student_report.csv`.

---

## ✨ Features

* 📂 Reads student records from a CSV file
* 🧮 Calculates the average score
* 🎓 Automatically assigns grades from `A` to `F`
* ✅ Determines pass or fail status
* 🏆 Identifies the student(s) with the highest average
* 🔍 Searches for students by name
* 📄 Generates a detailed CSV report
* 🚫 Validates marks between `0` and `100`
* ⚠️ Handles missing files and invalid data
* 🔎 Supports partial and case-insensitive name searches

---

## 🛠️ Technologies Used

* Python 3
* Python `csv` Module
* File Handling
* Exception Handling

---

## 📂 Project Structure

```text
DAY_17/
│── main17.py
│── students.csv
│── student_report.csv
└── README.md
```

---

## 📥 Input File Format

The `students.csv` file should contain the following columns:

```csv
Name,Math,Science,English
Abhijit,90,85,88
Rahul,75,80,70
Priya,95,92,98
Amit,55,50,60
```

> The column names must be written exactly as:

```text
Name, Math, Science, English
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Ensure that `students.csv` is present in the same folder as `main17.py`.
5. Run the program:

```bash
python main17.py
```

6. Enter a student name when prompted to search for a student.

---

## 💻 Sample Output

```text
Enter the student name to search: Priya

------ Student Details ------

Name: Priya
Math: 95
Science: 92
English: 98
Average: 95.00
Grade: A
Status: Pass
Top Performer: Yes
----------------------------------------

Student report generated successfully: 'student_report.csv'
```

---

## 📊 Grade Criteria

| Average Score | Grade |
| ------------- | ----- |
| 90–100        | A     |
| 80–89         | B     |
| 70–79         | C     |
| 60–69         | D     |
| Below 60      | F     |

---

## ✅ Pass/Fail Criteria

| Average Score | Status |
| ------------- | ------ |
| 60 or above   | Pass   |
| Below 60      | Fail   |

---

## 📄 Generated Report

The generated `student_report.csv` file contains:

```csv
Name,Math,Science,English,Average,Status,Grade,Top Performer
Abhijit,90,85,88,87.67,Pass,B,No
Rahul,75,80,70,75.0,Pass,C,No
Priya,95,92,98,95.0,Pass,A,Yes
Amit,55,50,60,55.0,Fail,F,No
```

---

## 📚 Concepts Practiced

* Functions
* CSV File Handling
* `csv.DictReader`
* `csv.DictWriter`
* Dictionaries
* Lists
* Loops (`for`)
* Conditional Statements
* List Comprehensions
* Generator Expressions
* Built-in Functions:

  * `max()`
  * `all()`
  * `round()`
* Exception Handling:

  * `FileNotFoundError`
  * `KeyError`
  * `ValueError`
  * Generic Exceptions
* String Methods:

  * `strip()`
  * `lower()`

---

## 🎯 Learning Outcome

This project helped me practice:

* Reading structured data from CSV files
* Processing multiple student records
* Calculating averages and grades
* Validating numerical data
* Writing processed data to a new CSV file
* Searching data using partial text matching
* Handling file and data-related errors
* Building a practical data-processing application

---

## ⚠️ Note

* The input file must be named `students.csv`.
* The required columns are:

  * `Name`
  * `Math`
  * `Science`
  * `English`
* All marks must be between `0` and `100`.
* The program identifies all students who share the highest average as top performers.
* The generated report is saved as `student_report.csv`.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

* ➕ Add more subjects
* 📊 Display class statistics
* 📈 Generate charts for student performance
* 🏅 Create student rankings
* 🔍 Add an interactive search menu
* ✏️ Edit student records
* ❌ Delete student records
* 📤 Export reports to Excel or PDF
* 🖥️ Build a graphical user interface using Tkinter

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀
