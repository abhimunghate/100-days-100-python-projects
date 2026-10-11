# 📝 Day 92 - Online Quiz App

Welcome to **Day 92** of my **100 Days, 100 Python Projects** challenge!

This project is an **Online Quiz App** built using Python. It demonstrates how quiz questions can be managed, how participants can submit answers, and how scores can be calculated based on the correctness of their responses.

The application uses Python dataclasses, object-oriented programming, lists, dictionaries, and conditional logic to implement a simple quiz system. It simulates API-style requests and responses through formatted JSON output in the terminal.

The quiz contains three Python programming questions and evaluates the participant's answers to generate a final result with a score, percentage, correct answers, and explanations.

---

## 📌 Project Overview

An online quiz application allows participants to answer questions, submit their responses, and receive results based on their performance.

This project demonstrates the backend logic of a quiz application without requiring a web server or graphical user interface.

The application follows a simple workflow:

- 📚 Load questions from a question bank.
- 👤 Create a quiz session for a participant.
- ❓ Display the available questions and answer options.
- ✍️ Submit answers for individual questions.
- ✅ Validate submitted answers against the available options.
- 🧮 Compare submitted answers with the correct answers.
- 📊 Calculate the final score and percentage.
- 💡 Display explanations for each question.

The sample participant is **Arjun**, and the quiz includes three Python programming questions.

**Note:** This is a terminal-based backend simulation. It does not currently provide a live website, interactive GUI, database, user registration, or real HTTP endpoints.

---

## ✨ Features

- 📝 Online quiz backend simulation
- 📚 Centralized question bank
- ❓ Multiple-choice questions
- 👤 Participant-based quiz sessions
- ✍️ Answer submission
- ✅ Answer option validation
- 🎯 Automatic answer evaluation
- 🧮 Automatic score calculation
- 📊 Percentage-based results
- 💡 Question explanations
- 📋 Detailed result breakdown
- 🔍 Question lookup by ID
- ⚠️ Error handling for invalid questions and answers
- 🧾 JSON-formatted terminal output
- 🔄 API-style request and response labels
- 🧩 Modular project structure
- 🐍 Python standard-library implementation

---

## 📚 Question Bank

The `QuestionBank` class in `questions.py` manages the available quiz questions.

The application initializes three questions about Python programming fundamentals.

| Question ID | Topic | Correct Answer |
|---:|---|---|
| 1 | Python function keyword | `def` |
| 2 | Collection storing unique values | `set` |
| 3 | Output of `len([10, 20, 30])` | `3` |

Each question contains:

- A unique ID
- A question prompt
- A list of answer options
- The correct answer
- An explanation of the answer

This structure allows the quiz session to evaluate responses and provide useful feedback.

---

## 🧩 Question Dataclass

The `Question` dataclass defines the structure of each quiz question.

It is implemented in `questions.py`.

```python
from dataclasses import dataclass

@dataclass
class Question:
    id: int
    prompt: str
    options: list[str]
    correct_answer: str
    explanation: str
```

### Attributes

| Attribute | Description |
|---|---|
| `id` | Unique question identifier |
| `prompt` | Question text |
| `options` | List of available answers |
| `correct_answer` | Expected correct answer |
| `explanation` | Explanation shown in the results |

Using a dataclass makes question records easier to create and maintain.

For example, the first question is defined as:

```python
Question(
    1,
    "Which keyword defines a Python function?",
    ["class", "def", "func", "return"],
    "def",
    "Python uses def to begin a function definition."
)
```

The `QuestionBank` stores these question objects in a list.

---

## 📋 QuestionBank Class

The `QuestionBank` class is responsible for maintaining and providing access to quiz questions.

It contains the following method:

```python
def all(self):
    return list(self.questions)
```

The `all()` method returns a new list containing the question objects.

This allows the main program and quiz session to access the available questions.

The method copies the list, but the contained question objects are still shared references. It does not create independent copies of each question.

### Responsibilities

- Store the predefined questions.
- Maintain question IDs and answer options.
- Provide the question collection to the main application.
- Supply questions to the quiz session for evaluation.

The current implementation uses a predefined question list. Questions are not loaded from a database or external file.

---

## 👤 Quiz Session

The `QuizSession` class in `quiz.py` manages the participant's quiz activity.

```python
class QuizSession:
    def __init__(self, questions, participant):
        self.questions, self.participant, self.answers = (
            questions,
            participant,
            {}
        )
```

When a session is created, it stores:

- `questions` — the questions available for the quiz
- `participant` — the participant's name
- `answers` — a dictionary containing submitted answers

The main application creates a session for Arjun:

```python
session = QuizSession(bank.all(), "Arjun")
```

Each participant session maintains its own answer dictionary.

---

## ✍️ Answer Submission

The `submit()` method accepts a question ID and an answer.

```python
session.submit(question_id, answer)
```

The method performs three main operations.

### 1. Find the Question

It searches for a question matching the submitted ID.

```python
question = next(
    (q for q in self.questions if q.id == question_id),
    None
)
```

If no matching question exists, the method raises:

```python
LookupError("Question not found")
```

### 2. Validate the Answer

The submitted answer must match one of the question's available options.

```python
if answer not in question.options:
    raise ValueError(
        "Answer must match one of the options"
    )
```

For example, `def` is a valid answer to the first question because it appears in that question's options.

An answer that is not listed is rejected.

### 3. Store the Answer

After validation, the answer is stored using the question ID as the dictionary key.

```python
self.answers[question_id] = answer
```

The method returns:

```python
{
    "question_id": question_id,
    "accepted": True
}
```

This confirms that the answer was accepted for processing. It does not mean the answer is necessarily correct.

**Important:** Submitting another valid answer for the same question replaces the previously stored answer because the dictionary uses the question ID as its key.

---

## 🧠 Answer Evaluation

The `results()` method compares the participant's submitted answers with the correct answers in the question bank.

The comparison is:

```python
correct = answer == q.correct_answer
```

If the submitted answer matches the correct answer, the result is `True`; otherwise, it is `False`.

The method also includes the correct answer and explanation in the result details.

For each question, the result contains:

| Field | Description |
|---|---|
| `question_id` | ID of the question |
| `answer` | Participant's submitted answer, or `null` if unanswered |
| `correct` | Whether the answer is correct |
| `correct_answer` | Expected correct answer |
| `explanation` | Explanation of the answer |

This provides a detailed breakdown of the participant's performance.

---

## 🧮 Score Calculation

The application calculates the score by counting the number of correct answers.

```python
score = sum(
    1 for item in details if item["correct"]
)
```

Each correct answer contributes one point.

The current quiz contains three questions, so the maximum possible score is three.

### Example

If a participant answers all three questions correctly:

```text
Correct Answers: 3
Total Questions: 3
Score: 3/3
```

If two answers are correct:

```text
Correct Answers: 2
Total Questions: 3
Score: 2/3
```

The score is calculated automatically from the answer details rather than being entered manually.

---

## 📊 Percentage Calculation

The application converts the score into a percentage using:

```python
percentage = round(
    score / len(self.questions) * 100,
    1
)
```

The percentage is rounded to one decimal place.

For example:

| Score | Total Questions | Percentage |
|---:|---:|---:|
| 3 | 3 | 100.0% |
| 2 | 3 | 66.7% |
| 1 | 3 | 33.3% |
| 0 | 3 | 0.0% |

The current question bank contains three questions, so the denominator is three.

**Current limitation:** The code assumes that the quiz contains at least one question. If an empty question list is passed to `QuizSession`, the percentage calculation will attempt to divide by zero.

---

## 💡 Answer Explanations

Every question includes an explanation that appears in the final results.

For example, the first question's explanation is:

```text
Python uses def to begin a function definition.
```

The explanation helps the participant understand why an answer is correct.

The other sample explanations cover Python sets and the behavior of the `len()` function.

Providing explanations makes the quiz useful for learning, rather than simply reporting a score.

---

## 🧾 API-Style Request and Response Format

The application uses a helper function in `main92.py` to display each operation.

```python
def show(action, data, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(data, indent=2)}"
    )
```

This function displays the operation name, a simulated response status, and the result formatted as JSON.

The application demonstrates three operation types:

| Operation | Status Label | Purpose |
|---|---:|---|
| `GET /api/questions` | `200` | Displays the available questions |
| `POST /api/answers` | `201` | Displays an accepted answer submission |
| `GET /api/results` | `200` | Displays the final quiz results |

These are simulated API-style labels printed in the terminal. The project does not currently expose actual HTTP endpoints or send HTTP requests.

---

## 🔄 Complete Application Workflow

The application follows this workflow:

```text
Start Application
        |
        v
Create QuestionBank
        |
        v
Load Available Questions
        |
        v
Create QuizSession
        |
        v
Set Participant Name
        |
        v
Display Questions and Options
        |
        v
Submit Answers
        |
        v
Validate Question IDs
        |
        v
Validate Answer Options
        |
        v
Store Submitted Answers
        |
        v
Evaluate Correct Answers
        |
        v
Calculate Score and Percentage
        |
        v
Display Final Results
```

The workflow separates question management, answer submission, and result evaluation into dedicated components.

---

## 🏗️ Project Architecture

The project contains three Python modules.

```text
                 main92.py
                     |
          +----------+----------+
          |                     |
          v                     v
     QuestionBank          QuizSession
          |                     |
          v                     v
    Question Objects       Submitted Answers
          |                     |
          +----------+----------+
                     |
                     v
               Result Evaluation
                     |
                     v
             Score and Percentage
                     |
                     v
                JSON Output
```

### Module Responsibilities

- **`main92.py`** — initializes the question bank and quiz session, submits sample answers, and displays results.
- **`questions.py`** — defines the `Question` dataclass and `QuestionBank` class.
- **`quiz.py`** — defines `QuizSession`, validates submitted answers, stores responses, and calculates results.

This modular design keeps question data separate from quiz processing.

---

## 🖥️ Sample Quiz Questions

The application contains the following questions.

### Question 1

**Which keyword defines a Python function?**

Options:

- `class`
- `def`
- `func`
- `return`

Correct answer: `def`

### Question 2

**Which collection stores unique values?**

Options:

- `list`
- `tuple`
- `set`
- `string`

Correct answer: `set`

### Question 3

**What does `len([10, 20, 30])` return?**

Options:

- `2`
- `3`
- `30`
- `Error`

Correct answer: `3`

---

## 📊 Example Results

The main program submits the following answers:

```python
for qid, answer in [
    (1, "def"),
    (2, "set"),
    (3, "3")
]:
    show(
        "POST /api/answers",
        session.submit(qid, answer),
        201
    )
```

All three answers match the correct answers in the question bank.

Therefore, the final results should contain:

```text
Participant: Arjun
Score: 3
Total Questions: 3
Percentage: 100.0%
```

The detailed result contains one entry for each question, with the submitted answer, correctness status, correct answer, and explanation.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement the question bank, quiz sessions, answer validation, score calculation, and result generation.

### 🧩 Dataclasses

The `dataclasses` module defines structured question records.

```python
from dataclasses import dataclass
```

### 📦 Lists

Lists store question options, the predefined question bank, and detailed quiz results.

### 🗂️ Dictionaries

Dictionaries store participant answers and structure the returned result data.

### 🔄 Object-Oriented Programming

The project uses classes to separate question management from quiz-session processing.

### 🧾 JSON

The `json` module converts dictionaries and lists into readable JSON output.

### ⚠️ Exceptions

The project uses `LookupError` and `ValueError` to report missing questions and invalid answer options.

---

## 📦 Requirements

This project uses Python's standard library and does not require any external Python packages.

Check your Python version:

```bash
python --version
```

### `requirements.txt`

```text
# No external dependencies required.
```

---

## 📂 Project Structure

```text
DAY_92/
│
├── main92.py
├── questions.py
├── quiz.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Purpose |
|---|---|
| `main92.py` | Entry point and sample quiz workflow |
| `questions.py` | Question dataclass and question bank |
| `quiz.py` | Quiz session, answer validation, and result calculation |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Make sure Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal inside your `DAY_92` folder.

```bash
cd DAY_92
```

### Step 3 — Check the Files

Make sure the following Python files are present:

```text
main92.py
questions.py
quiz.py
```

### Step 4 — Run the Application

Execute:

```bash
python main92.py
```

### Step 5 — Review the Output

The terminal displays:

- The available questions
- Three answer-submission responses
- The participant's final score
- The percentage achieved
- The correct answers
- The explanation for each question

No database setup, API key, external dependency installation, or server configuration is required.

---

## ⚠️ Important Notes and Limitations

### 1. Predefined Questions

Questions are hardcoded in `questions.py`. The application does not currently load questions from a database or external file.

### 2. Terminal-Based Application

The current version simulates quiz operations in the terminal. It does not have an interactive GUI or web interface.

### 3. No Persistent Storage

Answers exist only in the quiz session's in-memory dictionary. They are not saved after the program exits.

### 4. No Authentication

The participant name is supplied directly when creating the session. There is no login, registration, or user-account system.

### 5. Answer Validation

The application checks whether the answer matches one of the available options. It does not normalize capitalization or whitespace.

For example, `def` is accepted, but `DEF` is rejected because the comparison is case-sensitive.

### 6. Repeated Submissions

Submitting another valid answer for an already answered question replaces the previous answer. The current implementation does not prevent repeated submissions.

### 7. Unanswered Questions

If a participant does not answer a question, its `answer` value appears as `None` in the Python result data and is serialized as `null` in JSON. It is counted as incorrect.

### 8. No Time Limit

The quiz does not currently implement a countdown timer or submission deadline.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Dataclasses
- Lists and dictionaries
- Object-oriented programming
- Question-bank design
- Quiz-session management
- Answer validation
- Dictionary-based answer storage
- Conditional logic
- List comprehensions and generator expressions
- Searching objects by ID
- Score calculation
- Percentage calculation
- Boolean comparisons
- Exception handling
- JSON serialization
- Modular programming
- API-style response formatting

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Define a structured question model using a dataclass
- Maintain a collection of predefined questions
- Create a quiz session for a participant
- Retrieve questions and their answer options
- Validate submitted question IDs
- Validate answers against available options
- Store answers using question IDs
- Compare answers with correct answers
- Generate detailed quiz results
- Calculate scores and percentages
- Include explanations in the result output
- Handle missing questions and invalid answers
- Format structured results as JSON
- Separate question management from quiz logic
- Build the backend foundation of an online quiz application

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🌐 Build a web interface using Flask or Django
- 🎨 Add an interactive GUI using Tkinter
- 🗄️ Store questions and results in SQLite or PostgreSQL
- 👤 Add participant registration and login
- 📚 Support multiple quizzes and subjects
- ➕ Add functionality to create, update, and delete questions
- 🎲 Randomize question order
- 🔀 Shuffle answer options
- ⏱️ Add a quiz timer
- 📅 Record quiz completion dates
- 🏆 Add leaderboards and rankings
- 📈 Track participant performance over time
- 📊 Generate quiz analytics
- 🔁 Allow participants to retake quizzes
- 🛑 Prevent duplicate answer submissions when required
- 🧮 Support negative marking
- 🎯 Set passing scores and grade categories
- 📤 Export results to CSV or PDF
- 🧪 Add automated unit tests
- 🔐 Implement authentication and authorization
- 🚀 Deploy the application as a live web service

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 92** focuses on **Quiz Application Development**, combining question management, answer validation, session handling, automatic scoring, and result generation using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍📝
