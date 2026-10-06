# 🚀 Day 87 - Online Polling System

Welcome to **Day 87** of my **100 Days, 100 Python Projects** challenge!

This project is a **simple Online Polling System** built using **Python**. It simulates the basic functionality of an online voting platform where users can view a poll, select an option, cast a vote, and receive updated voting results.

The project focuses on practicing **Object-Oriented Programming, Dataclasses, sets, dictionaries, validation, service-based architecture, vote tracking, and in-memory data management**.

---

## 📌 Project Overview

An online polling system allows users to participate in a question-based poll by selecting one of several available options.

This project implements a simplified polling backend where users can:

* 📊 View an available poll
* ❓ Display the poll question
* 🔘 Display available voting options
* 🗳️ Cast a vote
* 👤 Identify voters using unique voter IDs
* 🚫 Prevent users from voting more than once
* ⚠️ Validate voting options
* 📈 Update vote counts
* 🔢 Calculate total votes
* 📋 Display current poll results
* 📦 Store poll data in memory
* 📄 Display structured JSON-style responses

The application runs through the command line and simulates basic polling operations.

---

## ✨ Features

* 🖥️ CLI-based Online Polling System
* 📊 Poll management
* ❓ Poll question display
* 🔘 Multiple voting options
* 🗳️ Vote casting
* 👤 Unique voter identification
* 🚫 One-vote-per-voter validation
* ⚠️ Invalid option validation
* 📈 Automatic vote count updates
* 🔢 Total vote calculation
* 📋 Poll result display
* 🗂️ In-memory poll storage
* 📦 Dataclass-based poll model
* 🔤 Dictionary-based option and vote storage
* 🔒 Set-based voter tracking
* 📄 JSON-formatted terminal output
* 🧩 Separate poll and voting services

---

## 🛠️ Technologies Used

* **Python 3**
* **Dataclasses**
* **Sets**
* **Dictionaries**
* **JSON**
* **Object-Oriented Programming**
* **In-Memory Data Storage**

### 🐍 Python

Python is used to implement the complete polling system.

The project uses:

* Classes
* Objects
* Functions
* Dictionaries
* Sets
* Dataclasses
* Exceptions
* Formatted strings
* Built-in functions

### 📦 Dataclasses

The `Poll` model uses Python's `dataclass` decorator.

```python id="l4u3qu"
@dataclass
class Poll:
    id: int
    question: str
    options: dict[str, int]
    voters: set[str] = field(default_factory=set)
```

This provides a structured way to represent poll information.

### 🗂️ Dictionaries

Dictionaries are used to store:

* Poll options
* Vote counts
* Poll objects

For example:

```python id="mb6xqg"
{
    "API": 0,
    "Automation": 0,
    "Data": 0
}
```

Each option has a corresponding vote count.

### 🔒 Sets

A set is used to keep track of voters:

```python id="vqux9j"
voters: set[str] = field(
    default_factory=set
)
```

Sets are useful because each voter ID can only occur once.

### 📄 JSON

The `json` module is used to format the terminal output.

```python id="p4j4jz"
json.dumps(result, indent=2)
```

This makes the responses easier to read.

---

## 📂 Project Structure

```text id="x9p8s7"
DAY_87/
│
├── main87.py
├── polls.py
├── voting.py
├── requirements.txt
└── README.md
```

### 📄 File Description

| File / Folder      | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `main87.py`        | Main polling workflow                       |
| `polls.py`         | Contains the `Poll` model and `PollService` |
| `voting.py`        | Handles vote validation and vote recording  |
| `requirements.txt` | Lists project dependencies                  |
| `README.md`        | Project documentation                       |

---

## 📦 requirements.txt

This project uses only Python's standard library.

```text id="l3g3s2"
# No external dependencies required
```

No additional packages are required.

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash id="x8w3u1"
python --version
```

Python 3 is recommended.

---

### 2. Open the project folder

Open a terminal inside the `DAY_87` folder.

---

### 3. Run the application

```bash id="u1y7ve"
python main87.py
```

The application will display the poll, record a vote, and show the updated results.

---

# 🔄 Application Workflow

The application follows this workflow:

```text id="f1qv3g"
                    Start
                      │
                      ▼
                Load Poll
                      │
                      ▼
               Display Poll
                      │
                      ▼
                 Cast Vote
                      │
                      ▼
             Validate Voter
                      │
                      ▼
            Validate Option
                      │
                      ▼
              Record Vote
                      │
                      ▼
           Calculate Results
                      │
                      ▼
                End
```

The workflow is implemented in `main87.py`.

```python id="k9s0y2"
polls = PollService()
voting = VotingService(polls)

poll = polls.get(101)

show(
    "GET POLL",
    {
        "id": poll.id,
        "question": poll.question,
        "options": poll.options
    }
)

show(
    "CAST VOTE",
    voting.vote(
        101,
        "USR-501",
        "API"
    ),
    201
)

show(
    "GET RESULTS",
    {
        "results": poll.options
    }
)
```

---

# 📊 Poll Details

The `PollService` manages the available polls.

A sample poll is created when the service is initialized:

```python id="2f7l5d"
self.polls = {
    101: Poll(
        101,
        "What should we build next?",
        {
            "API": 0,
            "Automation": 0,
            "Data": 0
        }
    )
}
```

The current poll contains:

| Field    | Value                        |
| -------- | ---------------------------- |
| Poll ID  | `101`                        |
| Question | `What should we build next?` |
| Option 1 | `API`                        |
| Option 2 | `Automation`                 |
| Option 3 | `Data`                       |

Initially, all options have zero votes.

---

# ❓ Getting a Poll

The `get()` method retrieves a poll using its ID.

```python id="k73j3u"
def get(self, poll_id):
    poll = self.polls.get(poll_id)

    if not poll:
        raise LookupError(
            "Poll not found"
        )

    return poll
```

The application retrieves poll `101`:

```python id="n6crwu"
poll = polls.get(101)
```

The poll information is then displayed using the `show()` function.

---

# 🗳️ Casting a Vote

Votes are handled by the `VotingService`.

```python id="y4h4d0"
voting = VotingService(polls)
```

A vote can be cast using:

```python id="n0s0ef"
voting.vote(
    101,
    "USR-501",
    "API"
)
```

The method receives:

| Parameter  | Description                    |
| ---------- | ------------------------------ |
| `poll_id`  | ID of the poll                 |
| `voter_id` | Unique identifier of the voter |
| `option`   | Selected poll option           |

---

# 👤 Voter Identification

Each voter is identified using a voter ID.

For example:

```text id="g2y6xv"
USR-501
```

The voter ID is stored in the poll's `voters` set.

```python id="p6e9tq"
poll.voters.add(voter_id)
```

This allows the system to determine whether a voter has already participated.

---

# 🚫 Preventing Duplicate Votes

The system prevents the same voter from voting more than once.

Before recording a vote, the application checks:

```python id="t0m4ri"
if voter_id in poll.voters:
    raise ValueError(
        "Voter has already voted"
    )
```

For example:

```text id="6n5qyk"
USR-501 → ✅ First vote
USR-501 → ❌ Second vote
USR-502 → ✅ Vote allowed
```

This demonstrates a basic **one-vote-per-voter** rule.

---

# ⚠️ Option Validation

The voting service checks whether the selected option exists.

```python id="cz3w9r"
if option not in poll.options:
    raise ValueError(
        "Invalid option"
    )
```

For the current poll:

```text id="3f1rwu"
API          → ✅ Valid
Automation   → ✅ Valid
Data         → ✅ Valid
Python       → ❌ Invalid
```

This prevents votes from being recorded against nonexistent options.

---

# 📈 Updating Vote Counts

After validation, the selected option's vote count is increased.

```python id="8k9z7q"
poll.options[option] += 1
```

For example, the initial poll is:

```json id="f5v8rm"
{
    "API": 0,
    "Automation": 0,
    "Data": 0
}
```

After a voter selects `API`:

```json id="4ps0b4"
{
    "API": 1,
    "Automation": 0,
    "Data": 0
}
```

---

# 🔢 Calculating Total Votes

The system calculates the total number of votes using:

```python id="g7h0jv"
sum(poll.options.values())
```

For example:

```text id="z1n7qs"
API          → 1
Automation   → 2
Data         → 1
----------------
Total Votes  → 4
```

The total is included in the vote response.

---

# 📋 Poll Results

After a vote is recorded, the system returns the updated results.

```python id="f9v5u7"
return {
    "message": "Vote recorded",
    "results": poll.options,
    "total_votes": sum(
        poll.options.values()
    )
}
```

Example:

```json id="6ef3kd"
{
    "message": "Vote recorded",
    "results": {
        "API": 1,
        "Automation": 0,
        "Data": 0
    },
    "total_votes": 1
}
```

The final `GET RESULTS` operation displays the current option counts.

---

# 🔒 Voter Tracking with Sets

The project uses a Python set to track voters:

```python id="z4x6kr"
voters: set[str] = field(
    default_factory=set
)
```

Sets are useful for this purpose because they contain unique values.

For example:

```python id="xv8w0a"
{
    "USR-501",
    "USR-502",
    "USR-503"
}
```

A voter cannot be added twice.

This makes the set a simple solution for implementing duplicate-vote prevention.

---

# 🗂️ In-Memory Poll Storage

Polls are stored using a Python dictionary:

```python id="2u3v1r"
self.polls = {
    101: Poll(...)
}
```

The poll ID is used as the dictionary key.

This makes it easy to retrieve a poll:

```python id="x4d8g1"
self.polls.get(poll_id)
```

The current version does not use an external database.

> ⚠️ Since the application uses in-memory storage, poll data and votes are lost when the program terminates.

---

# 🖥️ CLI Response Format

The `show()` function creates an API-style response format.

```python id="r5j1k8"
def show(action, result, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(result, indent=2)}"
    )
```

Example:

```text id="w2z8x0"
REQUEST GET POLL
RESPONSE 200

{
    "id": 101,
    "question": "What should we build next?",
    "options": {
        "API": 0,
        "Automation": 0,
        "Data": 0
    }
}
```

After voting:

```text id="n3v6p2"
REQUEST CAST VOTE
RESPONSE 201

{
    "message": "Vote recorded",
    "results": {
        "API": 1,
        "Automation": 0,
        "Data": 0
    },
    "total_votes": 1
}
```

Although the project runs in the terminal, the response structure resembles a simple backend API response.

---

# 🧩 Service-Based Architecture

The project separates polling and voting responsibilities into different services.

```text id="9u6q2h"
                 ┌──────────────────┐
                 │    main87.py     │
                 │   Application    │
                 │     Workflow     │
                 └────────┬─────────┘
                          │
               ┌──────────▼──────────┐
               │    PollService      │
               │                     │
               │ Store Polls         │
               │ Get Poll            │
               └──────────┬──────────┘
                          │
                          │
               ┌──────────▼──────────┐
               │   VotingService     │
               │                     │
               │ Validate Voter      │
               │ Validate Option     │
               │ Record Vote         │
               │ Calculate Results   │
               └─────────────────────┘
```

This separation keeps the application logic organized and easier to extend.

---

# 🧩 Libraries and Functions Practiced

## Python `dataclasses`

| Function / Feature | Purpose                         |
| ------------------ | ------------------------------- |
| `@dataclass`       | Creates structured poll objects |
| `field()`          | Creates a default voter set     |

---

## Python `set`

| Feature  | Purpose                                  |
| -------- | ---------------------------------------- |
| `set()`  | Stores unique voter IDs                  |
| `in`     | Checks whether a voter has already voted |
| `.add()` | Adds a voter after a successful vote     |

Example:

```python id="n0v4ba"
poll.voters.add(voter_id)
```

---

## Python `dict`

Dictionaries are used to store:

* Polls
* Poll options
* Vote counts

Example:

```python id="s7x9mz"
{
    "API": 0,
    "Automation": 0,
    "Data": 0
}
```

---

## Python `sum()`

The `sum()` function calculates the total number of votes.

```python id="f1p5tq"
sum(poll.options.values())
```

---

## Python `json`

| Function       | Purpose                          |
| -------------- | -------------------------------- |
| `json.dumps()` | Formats results as readable JSON |

---

# 📚 Concepts Practiced

This project helped practice:

* 🐍 Python Programming
* 🧱 Object-Oriented Programming
* 📦 Dataclasses
* 🗳️ Voting Systems
* 📊 Poll Management
* 🔘 Option Management
* 👤 Voter Identification
* 🔒 One-Vote-Per-User Validation
* 🚫 Duplicate Detection
* ⚠️ Input Validation
* 📈 Vote Counting
* 🔢 Total Calculation
* 🗂️ Dictionaries
* 🔐 Sets
* 📄 JSON Formatting
* 🧩 Service-Based Architecture
* 🔗 Class Dependency
* 🗃️ In-Memory Storage
* 🏗️ Basic Backend Design
* ⚠️ Exception Handling

---

# 🎯 Learning Outcome

This project helped me understand:

* How to build a simple online polling system
* How to represent poll data using dataclasses
* How to store poll options and vote counts using dictionaries
* How sets can be used to track unique voters
* How to prevent duplicate voting
* How to validate voting options
* How to update vote counts dynamically
* How to calculate total votes
* How to separate poll management and voting logic
* How to use exceptions for invalid operations
* How to retrieve objects using dictionary keys
* How to format polling results as JSON
* How a backend-style voting workflow can be simulated using Python
* How business rules can be implemented inside service classes

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🌐 Build a REST API using Flask or FastAPI
* 🗄️ Add SQLite, MySQL, or PostgreSQL database support
* 👤 Add user registration and authentication
* 🔐 Add secure voter authentication
* ➕ Create polls dynamically
* ✏️ Edit polls
* 🗑️ Delete polls
* 🔘 Add and remove poll options
* ⏰ Add poll start and end times
* 🔒 Automatically close expired polls
* 📊 Add percentage-based results
* 📈 Add graphical result visualization
* 🏆 Display the winning option
* 📋 Add voting history
* 🔎 Add poll search
* 🏷️ Add poll categories
* 📱 Build a web interface
* ⚛️ Build a React frontend
* 🔄 Add real-time results
* 📊 Add an admin dashboard
* 🧪 Add unit tests
* 📚 Add API documentation
* 🐳 Dockerize the application
* ☁️ Deploy the polling system to the cloud

---

# 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, explore new technologies, and maintain consistency through daily coding.

**Day 87** focuses on building an **Online Polling System**, with an emphasis on **poll management, vote counting, voter validation, duplicate-vote prevention, sets, dictionaries, service-based architecture, and in-memory data management**.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🗳️
