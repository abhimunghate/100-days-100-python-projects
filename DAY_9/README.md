# 🚀 Day 9 - Ingredient Checker

Welcome to **Day 9** of my **100 Days, 100 Python Projects** challenge!

This project is an **Ingredient Checker and Recipe Suggestion System** built using Python. It checks the ingredients available with the user, identifies missing and extra ingredients, suggests possible substitutes, and recommends recipes that can be prepared with the available ingredients.

---

## 📌 Project Overview

The program asks the user to enter the ingredients they currently have. It then:

* Compares them with the required recipe ingredients
* Detects missing ingredients
* Identifies extra ingredients
* Checks for available substitutes
* Suggests recipes that can be made completely
* Suggests recipes that are only one ingredient away

---

## ✨ Features

* 🥣 Check available ingredients
* ❌ Identify missing ingredients
* ➕ Identify extra ingredients
* 🔄 Suggest ingredient substitutes
* 🍽️ Recommend recipes you can make immediately
* ⚠️ Recommend recipes that are almost possible
* 🖥️ Beginner-friendly command-line application

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
DAY_9/
│── main9.py
└── README.md
```

---

## ▶️ How to Run

1. Make sure **Python 3** is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the program:

```bash
python main9.py
```

---

## 💻 Sample Output

```text
Enter the ingredients you have (separated by commas) : flour, sugar, almond milk, eggs, coconut oil

------ Ingredient Check Results ------

Using 'almond milk' as a substitute for 'milk'.
Using 'coconut oil' as a substitute for 'butter'.
You have all the ingredients needed for the main recipe!
You also have extra ingredients : almond milk, coconut oil

------ Recipe Suggestions ------

Recipes you can make:
- Pancakes
- Cookies
- Cake

Recipes you are very close to making:
- French Toast (missing: bread)
```

---

## 📚 Concepts Practiced

* Sets
* Dictionaries
* Set Operations
* Loops (`for`)
* Conditional Statements (`if`, `else`)
* String Manipulation
* List Operations
* Data Processing
* User Input Handling

---

## 🧠 Core Logic

### Ingredient Comparison

```python
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients
```

### Substitute Checking

```python
common = substitutes[ingredient].intersection(user_ingredients)
```

### Recipe Validation

```python
required.issubset(effective_ingredients)
```

These set operations make the program efficient and easy to understand.

---

## 🎯 Learning Outcome

This project helped me practice:

* Working with **sets** for fast comparisons
* Using **dictionaries** to store structured data
* Implementing **real-world logic** (substitutions and recipe matching)
* Filtering and processing user input
* Building a practical recommendation system

---

## ⚠️ Note

* Ingredient names are automatically converted to **lowercase** for consistent matching.
* The program currently uses a predefined set of recipes and substitutes.
* Only recipes missing **one ingredient** are shown in the “almost possible” section.

---

## 🚀 Future Improvements

* 💾 Save recipes in a JSON file
* ➕ Allow users to add their own recipes
* 🧮 Show ingredient quantities
* 🛒 Generate a shopping list for missing items
* 🧠 Add AI-based recipe recommendations
* 🌐 Create a web version using Flask or Django

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen logical thinking, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀
