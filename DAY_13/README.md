# 🚀 Day 13 - Student Grade Manager

Welcome to **Day 13** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line Student Grade Manager built with Python. It accepts multiple student scores, assigns grades, sorts results, identifies passing and failing students, calculates the class average, and displays the highest and lowest scores.

---

## 📌 Project Overview

The application allows users to:

- 📝 Enter multiple student scores
- 🎓 Automatically assign letter grades
- 📊 Sort scores in ascending or descending order
- ✅ Display passing and failing students
- 📈 Calculate the class average
- 🏆 Find the highest and lowest scoring students
- ✔️ Validate all user inputs

---

## ✨ Features

- 📝 Accepts multiple student scores
- 🎓 Automatic grade assignment (A–F)
- 📊 Ascending and descending sorting
- ✅ Displays passing students
- ❌ Displays failing students
- 📈 Calculates average score
- 🏆 Finds highest and lowest scores
- 🚫 Validates score range (0–100)
- ⚠️ Handles invalid and empty inputs gracefully

---

## 🛠️ Technologies Used

- Python 3

---

## 📂 Project Structure

```text
DAY_13/
│── main13.py
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main13.py
```

---

## 💻 Sample Output

```text
Enter student scores separated by commas : 95,82,67,45,78

Sort the scores in ascending or descending order (A/D) : D

------ Student Grades ------

Student 1 : Score = 95, Grade = A
Student 2 : Score = 82, Grade = B
Student 5 : Score = 78, Grade = C
Student 3 : Score = 67, Grade = D
Student 4 : Score = 45, Grade = F

------ Passing and Failing Students ------

Passing Students :

Student 1: 95 (A)
Student 2: 82 (B)
Student 5: 78 (C)
Student 3: 67 (D)

Failing Students :

Student 4: 45 (F)

------ Average Score of Students ------

Average : 73.40

------ Highest and Lowest Mark ------

Highest Score
Student 1 : Score = 95, Grade = A

Lowest Score
Student 4 : Score = 45, Grade = F
```

---

## 🎓 Grade Criteria

| Score Range | Grade |
|-------------|-------|
| 90 – 100 | A |
| 80 – 89 | B |
| 70 – 79 | C |
| 60 – 69 | D |
| Below 60 | F |

---

## 📚 Concepts Practiced

- Lists
- Tuples
- List Comprehensions
- Functions
- Variables
- User Input (`input()`)
- Type Casting (`int()`)
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`for`)
- Sorting with `sort()` and `lambda`
- Built-in Functions
  - `sum()`
  - `max()`
  - `min()`
  - `len()`
  - `enumerate()`
- Exception Handling (`try-except`)

---

## 🎯 Learning Outcome

This project helped me practice:

- Processing multiple user inputs
- Assigning grades automatically
- Sorting complex data using `lambda`
- Working with tuples and lists together
- Calculating statistical values
- Validating user input
- Writing modular and readable Python code

---

## ⚠️ Note

- Scores must be between **0 and 100**.
- Only numeric values are accepted.
- Users can sort the results in ascending or descending order.
- The program exits gracefully when invalid input is provided.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 💾 Save student records to a file
- 📂 Load existing student records
- ✏️ Edit individual student scores
- ❌ Delete student records
- 📊 Display grade distribution using charts
- 📄 Export results to CSV or Excel
- 🏅 Show class ranking
- 🔍 Search students by ID or name

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀