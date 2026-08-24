# 🚀 Day 44 - Data Cleaner

Welcome to **Day 44** of my **100 Days, 100 Python Projects** challenge!

This project is a **Data Cleaner command-line tool** built using **Python and Pandas**. It is designed to demonstrate the fundamentals of **Data Science and Data Manipulation using the Pandas library**.

The application allows users to load CSV or Excel datasets, inspect the data, handle missing values, remove duplicate records, rename columns, and save the cleaned dataset.

---

## 📌 Project Overview

Data cleaning is one of the most important steps in the Data Science workflow. Real-world datasets often contain:

* ❌ Missing values
* 🔁 Duplicate records
* 🏷️ Unclear column names
* 📊 Inconsistent or incomplete data

This project provides a simple interactive tool for performing some of these common data-cleaning tasks.

The user can:

* 📂 Load CSV and Excel files
* 🔍 View the first few rows of the dataset
* 📊 View dataset dimensions
* ⚠️ Check for missing values
* 🧹 Remove rows containing missing values
* 🔢 Fill missing numerical values using the median
* 📝 Fill missing text values with `"Unknown"`
* 🔁 Remove duplicate rows
* ✏️ Rename columns interactively
* 💾 Save cleaned data as CSV or Excel

The main purpose of this project is to gain practical experience with **Pandas and basic Data Science data preprocessing techniques**.

---

## ✨ Features

* 📂 Supports CSV files
* 📊 Supports Excel files
* 🔍 Displays initial dataset information
* 📈 Displays number of rows and columns
* ⚠️ Detects missing values
* 🗑️ Option to remove rows containing missing values
* 🔢 Fills numerical missing values using the median
* 📝 Fills text missing values with `"Unknown"`
* 🔁 Detects and removes duplicate rows
* ✏️ Interactive column renaming
* 🚨 Input validation
* 💾 Saves cleaned data
* 📄 Supports CSV output
* 📊 Supports Excel output
* 🛡️ Error handling for file operations

---

## 🖥️ How the Tool Works

The application follows a simple data-cleaning workflow:

```text
Input Dataset
      ↓
Load Data
      ↓
Inspect Data
      ↓
Check Missing Values
      ↓
Handle Missing Values
      ↓
Remove Duplicates
      ↓
Rename Columns
      ↓
Cleaned Dataset
      ↓
Save Dataset
```

---

## 🛠️ Technologies Used

* **Python 3**
* **Pandas**
* **OpenPyXL**

### Python

Python is used to build the data-cleaning logic and command-line interface.

### Pandas

Pandas is the primary Data Science library used in this project.

It is used for:

* Reading datasets
* Inspecting data
* Detecting missing values
* Filling missing values
* Removing duplicates
* Renaming columns
* Saving cleaned datasets

### OpenPyXL

OpenPyXL is used by Pandas to read and write Excel `.xlsx` files.

---

## 📂 Project Structure

```text
DAY_44/

│── main44.py
│── requirements.txt
└── README.md
```

---

## 📦 requirements.txt

The project requires Pandas and OpenPyXL.

```text
pandas
openpyxl
```

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

### 2. Open the project folder

Open a terminal inside the `DAY_44` folder.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main44.py
```

The Data Cleaner Tool will start in the terminal.

---

## 📂 Supported Input Files

The application supports:

### CSV

```text
dataset.csv
```

### Excel

```text
dataset.xlsx
dataset.xls
```

When prompted, enter the path to your dataset:

```text
Enter the path to your file:
```

For example:

```text
data/students.csv
```

or:

```text
data/students.xlsx
```

---

## 🔍 Data Inspection

After loading the dataset, the application displays:

* Number of rows
* Number of columns
* First few rows of the dataset
* Missing value summary

The first few records are displayed using:

```python
df.head()
```

The dataset dimensions are obtained using:

```python
df.shape
```

The missing values are summarized using:

```python
df.isnull().sum()
```

---

## ⚠️ Handling Missing Values

Missing values are one of the most common problems in real-world datasets.

The application first checks whether missing values exist.

```python
missing_count = df.isnull().sum().sum()
```

If missing values are found, the user can choose between two options.

### Option 1: Drop Rows

The application removes rows containing missing values using:

```python
df.dropna()
```

For example:

```text
Before:
5 rows

After:
3 rows
```

The application also reports how many rows were removed.

---

### Option 2: Fill Missing Values

The application automatically separates numerical and text columns.

```python
numeric_columns = df.select_dtypes(include="number").columns
text_columns = df.select_dtypes(include="object").columns
```

#### 🔢 Numerical Columns

Missing numerical values are replaced using the **median**:

```python
df[column] = df[column].fillna(df[column].median())
```

Using the median can be useful because it is less affected by extreme values than the mean.

#### 📝 Text Columns

Missing text values are replaced with:

```text
Unknown
```

using:

```python
df[column] = df[column].fillna("Unknown")
```

---

## 🔁 Removing Duplicate Rows

Duplicate records can negatively affect data analysis.

The application first calculates the number of duplicate rows:

```python
duplicate_count = df.duplicated().sum()
```

Duplicate rows are then removed using:

```python
df.drop_duplicates()
```

The application reports the number of duplicate records removed.

---

## ✏️ Renaming Columns

The application allows users to rename dataset columns interactively.

First, the current columns are displayed:

```text
1. Name
2. Age
3. Marks
4. Department
```

The user can select a column number and provide a new name.

For example:

```text
Old:
Student Name

New:
Name
```

The application uses:

```python
df.rename(columns={old_name: new_name}, inplace=True)
```

The program also prevents:

* Empty column names
* Invalid column numbers
* Duplicate column names

---

## 💾 Saving Cleaned Data

After the cleaning process is completed, the user is asked where to save the cleaned dataset.

The application supports:

### CSV

```text
cleaned_data.csv
```

using:

```python
df.to_csv(output_path, index=False)
```

### Excel

```text
cleaned_data.xlsx
```

using:

```python
df.to_excel(output_path, index=False)
```

The original dataset is not directly overwritten unless the user specifically chooses the same output path.

---

## 📊 Data Cleaning Process

The complete cleaning process is handled by:

```python
def clean_data(df):
```

It performs the following operations:

1. Handle missing values
2. Remove duplicate rows
3. Rename columns
4. Display the final dataset shape

The application displays the initial and final dataset dimensions so the user can see the effect of the cleaning process.

---

## 🧩 Pandas Functions Practiced

| Pandas Function / Method | Purpose                      |
| ------------------------ | ---------------------------- |
| `pd.read_csv()`          | Reads CSV files              |
| `pd.read_excel()`        | Reads Excel files            |
| `df.head()`              | Displays the first rows      |
| `df.shape`               | Gets rows and columns        |
| `df.isnull()`            | Detects missing values       |
| `df.sum()`               | Calculates totals            |
| `df.dropna()`            | Removes missing-value rows   |
| `df.fillna()`            | Fills missing values         |
| `df.select_dtypes()`     | Selects columns by data type |
| `df.median()`            | Calculates median            |
| `df.duplicated()`        | Detects duplicate rows       |
| `df.drop_duplicates()`   | Removes duplicates           |
| `df.rename()`            | Renames columns              |
| `df.to_csv()`            | Saves CSV files              |
| `df.to_excel()`          | Saves Excel files            |

---

## 🧠 Example Cleaning Workflow

Suppose the input dataset contains:

```text
Name       Age    Marks
Abhijit    21     85
Rahul      22     NaN
Priya      NaN    90
Abhijit    21     85
```

The tool can:

1. Detect missing values.
2. Fill numerical missing values using the median or remove incomplete rows.
3. Remove the duplicate `Abhijit` record.
4. Rename columns if required.
5. Save the cleaned dataset.

The result is a cleaner dataset that can be used for further Data Science or Machine Learning tasks.

---

## ⚠️ Error Handling

The application includes error handling for common file-related problems.

Examples include:

* File does not exist
* Unsupported file extension
* Invalid input
* Invalid column number
* Empty column name
* Duplicate column name
* Problems while reading files
* Problems while saving files

For example, unsupported formats produce:

```text
Unsupported file format.
Please use a CSV or Excel file.
```

---

## 📚 Concepts Practiced

* Python Programming
* Data Science Basics
* Pandas
* DataFrames
* Data Cleaning
* Data Preprocessing
* CSV Files
* Excel Files
* Missing Value Handling
* Median Imputation
* Duplicate Detection
* Duplicate Removal
* Column Renaming
* Data Types
* File Handling
* Exception Handling
* User Input
* Functions
* Modular Programming

---

## 🎯 Learning Outcome

This project helped me understand:

* How Pandas DataFrames work
* How to load CSV datasets using Pandas
* How to work with Excel datasets
* How to inspect a dataset
* How to determine dataset dimensions
* How to identify missing values
* How to handle missing values
* Why median imputation can be useful for numerical data
* How to remove duplicate records
* How to rename DataFrame columns
* How to select columns based on their data type
* How to save cleaned datasets
* How data cleaning fits into the Data Science workflow
* How Pandas simplifies common data preprocessing tasks

---

## 🔮 Future Improvements

Possible enhancements for future versions:

* 📊 Add automatic data profiling
* 📈 Display dataset statistics
* 🔍 Add outlier detection
* 📉 Add visualization of missing values
* 🧹 Add more data-cleaning strategies
* 🔢 Allow users to choose mean, median, or mode for missing values
* 📅 Add date and time data cleaning
* 🔤 Standardize text formatting
* 🏷️ Automatically detect inconsistent column names
* 📊 Add data type conversion
* 🔎 Add duplicate comparison options
* 🖥️ Create a Tkinter or web-based GUI
* 📋 Add a cleaning report
* 📄 Export a summary report
* 🤖 Add automated data-quality checks

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, learn new technologies, and maintain consistency through daily coding.

**Day 44** focuses on **Data Science fundamentals using Pandas**, with practical experience in loading, inspecting, cleaning, transforming, and exporting real-world datasets.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍📊
