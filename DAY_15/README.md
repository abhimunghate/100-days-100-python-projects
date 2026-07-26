# 🚀 Day 15 - Recipe Viewer App

Welcome to **Day 15** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line Recipe Viewer application built with Python. It allows users to browse recipes by name or ingredient, add new recipes, and view all available recipes. All recipes are stored in a text file, so they remain available even after the program is closed.

---

## 📌 Project Overview

The application allows users to:

- 🍽️ View a recipe by its name
- 🥕 Search recipes by ingredient
- ➕ Add new recipes
- 📋 List all available recipes
- 💾 Store recipes permanently in a text file

Recipes are loaded from `recipes.txt` when the application starts and updated whenever a new recipe is added.

---

## ✨ Features

- 🍽️ Search recipes by name
- 🥕 Find recipes containing a specific ingredient
- ➕ Add new recipes
- 📋 Display all available recipes
- 💾 Persistent storage using a text file
- ✅ Prevents duplicate recipe names
- ⚠️ Validates empty inputs
- 🖥️ Simple menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- File Handling

---

## 📂 Project Structure

```text
DAY_15/
│── main15.py
│── recipes.txt
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Ensure `recipes.txt` is present in the project folder.
4. Open the terminal in the project folder.
5. Run the program:

```bash
python main15.py
```

---

## 📝 Recipe File Format

Each recipe in `recipes.txt` should follow this format:

```text
Pancakes
Ingredients : Flour, Milk, Eggs, Butter
Instructions : Mix all ingredients and cook on a hot pan.

Cookies
Ingredients : Flour, Sugar, Butter
Instructions : Mix ingredients, shape cookies, and bake.
```

Each recipe should be separated by a blank line.

---

## 💻 Sample Output

```text
------ Recipe Viewer Menu ------

1. View Recipe by Name.
2. View Recipe by Ingredients.
3. Add New Recipe.
4. List All Recipes.
5. Exit.

Enter your choice (1/2/3/4/5) : 2

Enter the name of the ingredient : butter

------ Recipes containing butter ------

Recipe : Pancakes
Ingredients : Flour, Milk, Eggs, Butter
Instructions : Mix all ingredients and cook on a hot pan.

----------------------------------------

Recipe : Cookies
Ingredients : Flour, Sugar, Butter
Instructions : Mix ingredients, shape cookies, and bake.
```

---

## 📚 Concepts Practiced

- Functions
- Dictionaries
- Nested Dictionaries
- Variables
- User Input (`input()`)
- Loops (`for`, `while`)
- Conditional Statements (`if`, `else`)
- File Handling
- Reading Files
- Writing Files
- Exception Handling (`try-except`)
- String Methods (`strip()`, `lower()`, `title()`)
- Data Parsing

---

## 🎯 Learning Outcome

This project helped me practice:

- Reading structured data from text files
- Storing information using dictionaries
- Searching through collections efficiently
- Writing new data to files
- Building menu-driven applications
- Validating user input
- Organizing code into reusable functions

---

## ⚠️ Note

- Recipes are stored in `recipes.txt`.
- If the file is missing, the application starts with an empty recipe collection.
- Recipe names must be unique.
- Ingredient searches are case-insensitive.
- Each recipe must follow the required file format to be loaded correctly.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- ✏️ Edit existing recipes
- ❌ Delete recipes
- ⭐ Mark favorite recipes
- ⏱️ Add preparation and cooking time
- 🥗 Categorize recipes (Breakfast, Lunch, Dinner, Dessert)
- 🔍 Search recipes by multiple ingredients
- 📷 Store image links for recipes
- 🖥️ Build a GUI version using Tkinter or CustomTkinter

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀