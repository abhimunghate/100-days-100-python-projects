# 🚀 Day 21 - Wikipedia Article Scraper

Welcome to **Day 21** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Wikipedia Article Scraper** built with Python. It allows users to search for any Wikipedia article, extract useful information such as the article title, summary, headings, and related links, and save the extracted data in **Text** or **JSON** format for future reference.

---

## 📌 Project Overview

The application enables users to:

- 🔍 Search Wikipedia articles by topic
- 📖 View the article title and summary
- 📑 Extract the first five section headings
- 🔗 Display related Wikipedia article links
- 💾 Save article information as a text file
- 📂 Export article data to a JSON file
- ✅ Prevent duplicate entries in the JSON database

The project uses **Requests** to fetch web pages and **BeautifulSoup** to parse HTML content from Wikipedia.

---

## ✨ Features

- 🔍 Search any Wikipedia article
- 📖 Display article title
- 📝 Extract article summary
- 📑 Retrieve the first five headings
- 🔗 Display related Wikipedia article links
- 💾 Save article details to a text file
- 📂 Export article information to JSON
- 💾 Option to save in both formats
- 🚫 Prevent duplicate JSON entries
- ⚠️ Handles invalid topics and network errors gracefully
- 🖥️ Simple menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- JSON
- OS Module
- File Handling
- Exception Handling

---

## 📂 Project Structure

```text
DAY_21/
│── main21.py
│── wikipedia_articles.txt
│── wikipedia_articles.json
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Install the required libraries

```bash
pip install requests beautifulsoup4
```
4. Open the terminal inside the project folder.
5. Run the application

```bash
python main21.py
```

If **wikipedia_articles.json** does not exist, it will be created automatically.

---

## 💻 Sample Output

```text
Enter a topic to search on Wikipedia (or 'q' to quit) :

Python Programming

------ Wikipedia Article Details ------

Title : Python (programming language)

Summary :
Python is a high-level, general-purpose programming language...

Headings :

1. History
2. Features and Philosophy
3. Syntax and Semantics
4. Libraries
5. Applications

Related Links :

- https://en.wikipedia.org/wiki/Programming_language
- https://en.wikipedia.org/wiki/Guido_van_Rossum
- https://en.wikipedia.org/wiki/Software_development
```

---

## 💾 Save Options

After viewing the article, users can choose one of the following:

```text
------ Save Options ------

1. Save as Text File
2. Export to JSON
3. Save Both
4. Don't Save
```

---

## 📄 Data Storage

### Text File (`wikipedia_articles.txt`)

Stores article details in a readable format.

Example:

```text
============================================================
Article: Python (programming language)
============================================================

Summary:
Python is a high-level, general-purpose programming language...

Headings:
1. History
2. Features and Philosophy
3. Syntax and Semantics

Related Links:
- https://en.wikipedia.org/wiki/Programming_language
```

---

### JSON File (`wikipedia_articles.json`)

Stores structured article data.

Example:

```json
[
    {
        "Title": "Python (programming language)",
        "Summary": "Python is a high-level programming language...",
        "Headings": [
            "History",
            "Features",
            "Syntax"
        ],
        "Related Links": [
            "https://en.wikipedia.org/wiki/Programming_language"
        ]
    }
]
```

---

## 📚 Concepts Practiced

- Web Scraping
- HTTP Requests
- HTML Parsing using BeautifulSoup
- JSON File Handling
- Text File Handling
- Reading & Writing Files
- Functions
- Lists & Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- User Input Validation

---

## 🎯 Learning Outcome

This project helped me practice:

- Fetching web pages using the Requests library
- Parsing HTML using BeautifulSoup
- Extracting useful information from web pages
- Working with structured JSON data
- Saving information into text and JSON files
- Handling duplicate records
- Managing exceptions and network errors
- Building interactive command-line applications

---

## ⚠️ Note

- An active internet connection is required.
- Wikipedia article names are **not case-sensitive**.
- Only the **first five headings** and **first five related links** are displayed.
- Duplicate articles are prevented in the JSON file.
- If an article does not exist, the program displays an appropriate error message.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 🖼️ Download article images
- 📄 Export articles to PDF
- 📊 Export to CSV format
- 🌍 Support multiple Wikipedia languages
- 🔎 Search suggestions for incorrect article names
- 📚 Save complete article content
- ⭐ Bookmark favorite articles
- 🗑️ Delete saved articles
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🌐 Build a web-based Wikipedia scraper

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀