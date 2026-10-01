# 🚀 Day 82 - Library Management System

Welcome to **Day 82** of my **100 Days, 100 Python Projects** challenge!

This project is a **CLI-based Library Management System** built using **Python**. The application simulates common library operations such as viewing available books, borrowing books, returning books, managing members, tracking loans, and updating book availability.

The project is designed using a simple **layered backend architecture** with separate modules for:

* API/request handling
* Business logic
* Data models
* Data storage/repository

The main purpose of this project is to gain practical experience with **backend development concepts, API-style routing, object-oriented programming, dataclasses, repository patterns, validation, exception handling, date handling, and library management workflows**.

---

## 📌 Project Overview

A Library Management System is responsible for managing books, members, borrowing transactions, and returns.

This project provides a lightweight backend-style simulation where users can:

* 📚 View available books
* 👤 Manage predefined library members
* 📖 Borrow books
* 🔄 Return borrowed books
* 📦 Track available book copies
* 🧾 Generate unique loan IDs
* 📅 Track borrowing and due dates
* ⏱️ Record return dates
* 🚨 Handle invalid requests and errors
* 📊 Return structured API-like responses

The application does not use a web framework or external database.

Instead, it uses an **in-memory repository** to store books, members, and loans while the program is running.

---

## ✨ Features

* 📚 Book listing
* 👤 Library member management
* 📖 Book borrowing
* 🔄 Book return functionality
* 📦 Available-copy tracking
* 🧾 Loan tracking
* 🆔 Unique loan IDs
* 🆔 Unique request IDs
* 📅 Borrowing date tracking
* 📅 Due date calculation
* 📅 Return date tracking
* ✅ Active/returned loan status
* 🚨 Custom error handling
* 📊 HTTP-style status codes
* 🖥️ CLI-based API simulation
* 📦 Dataclass-based models
* 🗃️ In-memory data repository
* 🧩 Layered backend architecture
* ⏱️ UTC request timestamps
* 🔍 Input validation
* 🔄 Automatic inventory update after borrowing/returning

---

# 🏗️ Backend Architecture

The project follows a simple layered architecture:

```text
┌───────────────────────────┐
│       CLI / main82.py     │
│  Sends simulated requests │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│       LibraryAPI          │
│ Request routing & response│
│       formatting          │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│      LibraryService       │
│       Business Logic      │
│ Borrow / Return / Validate│
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│    LibraryRepository      │
│      In-memory data       │
│ Books / Members / Loans   │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│          Models           │
│ Book / Member / Loan      │
└───────────────────────────┘
```

This separation keeps request handling, business logic, data storage, and data models independent.

---

# 🔄 Library Workflow

The application follows this workflow:

```text
Start Application
       │
       ▼
List Books
       │
       ▼
Select Member
       │
       ▼
Select Book
       │
       ▼
Validate Member
       │
       ▼
Validate Book
       │
       ▼
Check Availability
       │
       ▼
Create Loan
       │
       ▼
Decrease Available Copies
       │
       ▼
Return Book
       │
       ▼
Update Return Date
       │
       ▼
Increase Available Copies
       │
       ▼
List Books Again
```

---

# 📡 API Endpoints

The project simulates three main API operations.

---

## 📚 1. List Books

### Endpoint

```text
GET /api/books
```

This endpoint returns all books stored in the library repository.

Example response:

```json
{
  "status": 200,
  "request_id": "REQ-ABC12345",
  "timestamp": "2026-10-01T15:30:00+00:00",
  "data": {
    "books": [
      {
        "id": 101,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "available_copies": 2
      },
      {
        "id": 102,
        "title": "The Pragmatic Programmer",
        "author": "David Thomas",
        "available_copies": 1
      },
      {
        "id": 103,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "available_copies": 3
      }
    ]
  }
}
```

---

# 📖 2. Borrow a Book

### Endpoint

```text
POST /api/loans
```

Request body:

```json
{
  "member_id": 501,
  "book_id": 102
}
```

The system checks:

1. Whether the member exists
2. Whether the book exists
3. Whether at least one copy is available
4. Creates a new loan
5. Decreases the available book copies

---

## 🧾 Example Loan

A successful borrowing operation creates a unique loan ID.

Example:

```text
LOAN-7A93D4F1
```

The loan contains:

```text
Book ID
Member ID
Borrowed Date
Due Date
Return Date
Status
```

The default borrowing period is **14 days**.

---

# 🔄 3. Return a Book

### Endpoint

```text
POST /api/loans/{loan_id}/return
```

Example:

```text
POST /api/loans/LOAN-7A93D4F1/return
```

When a book is returned, the system:

1. Finds the loan
2. Checks whether the loan exists
3. Checks whether the book has already been returned
4. Records the return date
5. Increases the available book copies
6. Changes the loan status to `returned`

---

# 📚 Book Model

The `Book` model represents a library book.

```python
@dataclass
class Book:
    id: int
    title: str
    author: str
    available_copies: int
```

Each book contains:

```text
Book ID
Title
Author
Available Copies
```

---

## 📖 Sample Books

The repository starts with three books:

|  ID | Book                     | Author           | Available Copies |
| --: | ------------------------ | ---------------- | ---------------: |
| 101 | Clean Code               | Robert C. Martin |                2 |
| 102 | The Pragmatic Programmer | David Thomas     |                1 |
| 103 | Python Crash Course      | Eric Matthes     |                3 |

These values are stored in memory when the application starts.

---

# 👤 Member Model

The `Member` model represents a library member.

```python
@dataclass
class Member:
    id: int
    name: str
    email: str
```

Each member contains:

```text
Member ID
Name
Email
```

The repository includes two sample members:

|  ID | Name       | Email                                       |
| --: | ---------- | ------------------------------------------- |
| 501 | Ava Patel  | [ava@example.com](mailto:ava@example.com)   |
| 502 | Noah Smith | [noah@example.com](mailto:noah@example.com) |

---

# 🧾 Loan Model

The `Loan` model represents a book borrowing transaction.

```python
@dataclass
class Loan:
    id: str
    book_id: int
    member_id: int
    borrowed_on: date
    due_on: date
    returned_on: date | None = None
```

A loan tracks:

* Loan ID
* Book ID
* Member ID
* Borrowing date
* Due date
* Return date
* Loan status

---

# 📅 Due Date Calculation

When a book is borrowed, the application records the current date:

```python
today = date.today()
```

The due date is calculated using:

```python
today + timedelta(days=14)
```

Therefore, each new loan receives a due date **14 days after the borrowing date**.

Example:

```text
Borrowed On:  2026-10-01
Due On:       2026-10-15
```

---

# 🔄 Loan Status

The loan status is automatically determined by whether the book has been returned.

The `Loan.to_dict()` method uses:

```python
"status": "returned" if self.returned_on else "active"
```

Therefore, a loan can have two states:

```text
active
returned
```

### Active Loan

```json
{
  "status": "active",
  "returned_on": null
}
```

### Returned Loan

```json
{
  "status": "returned",
  "returned_on": "2026-10-01"
}
```

---

# 📦 Book Availability Management

The system automatically updates the number of available copies.

Suppose a book initially has:

```text
Available Copies = 1
```

After borrowing:

```text
Available Copies = 0
```

After returning:

```text
Available Copies = 1
```

This provides a simple simulation of library inventory management.

---

# 📄 main82.py

`main82.py` is the main entry point of the application.

It contains:

```text
LibraryAPI
send()
main()
```

---

## 🔀 LibraryAPI

The `LibraryAPI` class acts as the API layer.

```python
class LibraryAPI:
```

It connects the API layer with the service layer:

```python
self.service = LibraryService(LibraryRepository())
```

The architecture becomes:

```text
LibraryAPI
     ↓
LibraryService
     ↓
LibraryRepository
```

---

# 🛣️ Request Routing

The `handle()` method receives:

```python
method
path
body
```

For example:

```python
api.handle(
    "GET",
    "/api/books"
)
```

The API then routes the request to the appropriate service method.

---

# 🆔 Request ID

Every request receives a unique request ID.

```python
request_id = f"REQ-{uuid4().hex[:8].upper()}"
```

Example:

```text
REQ-5B82D1A4
```

This helps identify individual requests.

---

# ⏱️ Request Timestamp

Every API response includes a UTC timestamp:

```python
datetime.now(timezone.utc).isoformat()
```

Example:

```text
2026-10-01T15:30:21.452321+00:00
```

This demonstrates how backend systems can attach timestamps to responses.

---

# 📦 Structured API Response

The `_response()` method creates a consistent response structure:

```python
{
    "status": status,
    "request_id": request_id,
    "timestamp": timestamp,
    "data": data
}
```

This gives every request a predictable response format.

---

# 📄 repository.py

`repository.py` contains the data-storage layer.

The project uses an **in-memory repository instead of a database**.

```python
class LibraryRepository:
```

The repository stores:

```text
Books
Members
Loans
```

---

## 📚 Book Storage

Books are stored using a dictionary:

```python
self.books = {
    101: Book(...),
    102: Book(...),
    103: Book(...)
}
```

The book ID is used as the dictionary key.

---

## 👤 Member Storage

Members are also stored using a dictionary:

```python
self.members = {
    501: Member(...),
    502: Member(...)
}
```

---

## 🧾 Loan Storage

Loans are stored using:

```python
self.loans = {}
```

When a new loan is created:

```python
self.repository.save_loan(loan)
```

the loan is added to the in-memory repository.

---

# 🔍 Repository Operations

The repository provides methods for:

```text
list_books()
get_book()
get_member()
save_loan()
get_loan()
```

This keeps data-access operations separate from business logic.

---

# 📄 services.py

`services.py` contains the main business logic.

It defines:

```text
LibraryError
LibraryService
```

---

# ⚙️ LibraryService

The `LibraryService` class handles:

* Listing books
* Borrowing books
* Returning books
* Member validation
* Book validation
* Availability validation
* Loan creation
* Book availability updates

---

# 📖 Borrow Book Logic

The `borrow_book()` method performs several validation steps.

### Step 1 — Validate Member

```python
member = self.repository.get_member(member_id)

if not member:
    raise LibraryError(404, "Member not found")
```

If the member does not exist, the request fails.

---

### Step 2 — Validate Book

```python
book = self.repository.get_book(book_id)

if not book:
    raise LibraryError(404, "Book not found")
```

---

### Step 3 — Check Availability

```python
if book.available_copies < 1:
    raise LibraryError(409, "Book is currently unavailable")
```

This prevents users from borrowing books when no copies are available.

---

### Step 4 — Create Loan

A unique loan ID is generated:

```python
id=f"LOAN-{uuid4().hex[:8].upper()}"
```

The loan records the borrowing date and a due date 14 days later.

---

### Step 5 — Update Inventory

After creating the loan:

```python
book.available_copies -= 1
```

The available book count decreases by one.

---

# 🔄 Return Book Logic

The `return_book()` method handles book returns.

First, the loan is retrieved:

```python
loan = self.repository.get_loan(loan_id)
```

If the loan does not exist:

```text
404 - Loan not found
```

If the loan has already been returned:

```text
409 - Book has already been returned
```

Otherwise, the return date is recorded:

```python
loan.returned_on = date.today()
```

The available copy count is then increased:

```python
book.available_copies += 1
```

---

# 🚨 Error Handling

The project uses a custom exception:

```python
class LibraryError(Exception):
```

It stores:

```text
status
message
```

Example:

```python
LibraryError(404, "Book not found")
```

The API catches these errors and converts them into structured responses.

---

# 📊 HTTP-Style Status Codes

The project uses status codes similar to web APIs.

| Status | Meaning     | Example                             |
| -----: | ----------- | ----------------------------------- |
|    200 | Success     | Book listing / successful return    |
|    201 | Created     | Successful book borrowing           |
|    400 | Bad Request | Invalid request data                |
|    404 | Not Found   | Member, book or loan doesn't exist  |
|    409 | Conflict    | Book unavailable / already returned |

---

# ⚠️ Validation and Error Scenarios

The application handles several invalid situations.

## Member Not Found

If an invalid member ID is supplied:

```text
404
Member not found
```

---

## Book Not Found

If an invalid book ID is supplied:

```text
404
Book not found
```

---

## Book Unavailable

If:

```text
available_copies = 0
```

the system returns:

```text
409
Book is currently unavailable
```

---

## Loan Not Found

If an invalid loan ID is supplied during return:

```text
404
Loan not found
```

---

## Already Returned

Trying to return the same loan twice results in:

```text
409
Book has already been returned
```

---

## Invalid Request Data

If request values cannot be converted into the required integer values, the API catches:

```python
TypeError
ValueError
```

and returns:

```text
400
Invalid request data
```

---

# 🖥️ Example Application Flow

When the program starts, the following operations are automatically performed.

### Step 1 — Display Books

```text
GET /api/books
```

The initial book inventory is displayed.

---

### Step 2 — Borrow a Book

```text
POST /api/loans
```

with:

```json
{
  "member_id": 501,
  "book_id": 102
}
```

Member `501` borrows book `102`.

---

### Step 3 — Generate Loan

A loan is created:

```text
LOAN-XXXXXXXX
```

The loan contains:

```text
Borrowed Date
Due Date
Book ID
Member ID
Status: active
```

---

### Step 4 — Return the Book

The generated loan ID is used:

```text
POST /api/loans/LOAN-XXXXXXXX/return
```

The system records the return date and increases the available copy count.

---

### Step 5 — Display Books Again

```text
GET /api/books
```

The final book list demonstrates that the available copy count has been restored.

---

# 📊 Example Inventory Flow

The application initially has:

```text
The Pragmatic Programmer
Available Copies: 1
```

After member `501` borrows it:

```text
Available Copies: 0
```

After the book is returned:

```text
Available Copies: 1
```

This demonstrates basic inventory tracking.

---

# 📂 Project Structure

```text
DAY_82/

│
├── main82.py
├── models.py
├── repository.py
├── services.py
├── requirements.txt
└── README.md
 
```

### File Description

| File / Folder      | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| `main82.py`        | Main application, API routing and CLI workflow |
| `models.py`        | Defines Book, Member and Loan models           |
| `repository.py`    | Provides in-memory storage                     |
| `services.py`      | Contains library business logic                |
| `requirements.txt` | Python dependencies                            |
| `README.md`        | Project documentation                          |

---

# 📦 requirements.txt

This project uses only Python standard-library modules.

The main modules include:

```text
json
datetime
uuid
dataclasses
```

Therefore, no external packages are required.

The `requirements.txt` file can contain:

```text
# No external dependencies required
```

---

# ▶️ How to Run

## 1. Make sure Python is installed

Check the Python version:

```bash
python --version
```

---

## 2. Open the project folder

Open a terminal inside the `DAY_82` directory.

---

## 3. Run the application

```bash
python main82.py
```

The Library Management System CLI simulation will start automatically.

---

# 🖥️ Example Output

The terminal will display output similar to:

```text
Day 82 - Library Management System

REQUEST GET /api/books
RESPONSE 200
{
    ...
}

REQUEST POST /api/loans
{
    "member_id": 501,
    "book_id": 102
}
RESPONSE 201
{
    ...
}

REQUEST POST /api/loans/LOAN-XXXXXXXX/return
RESPONSE 200
{
    ...
}

REQUEST GET /api/books
RESPONSE 200
{
    ...
}
```

The exact request IDs, loan IDs, and timestamps will change each time the program runs.

---

# 🧩 Python Concepts Practiced

This project uses several important Python concepts.

## Object-Oriented Programming

Classes are used for:

```text
LibraryAPI
LibraryRepository
LibraryService
LibraryError
```

---

## Dataclasses

The application uses:

```python
@dataclass
```

for:

```text
Book
Member
Loan
```

This provides a clean way to represent structured data.

---

## Type Hints

The project uses type hints such as:

```python
date | None
```

to represent optional return dates.

---

## Properties and Methods

Data models provide methods such as:

```python
to_dict()
```

to convert model objects into dictionaries.

---

## UUID Generation

Unique request and loan IDs are generated using:

```python
uuid4()
```

Examples:

```text
REQ-A81F32BC
LOAN-7D4C92A1
```

---

## Date and Time Handling

The project uses:

```python
date.today()
timedelta(days=14)
datetime.now(timezone.utc)
```

for:

* Borrowing dates
* Due dates
* Return dates
* API timestamps

---

## Dictionary Storage

The repository uses Python dictionaries for:

```text
Books
Members
Loans
```

---

## Exception Handling

The application uses:

```python
try
except
```

to handle errors and return appropriate status codes.

---

# 🏗️ Backend Concepts Practiced

This project focuses on several backend development concepts:

* API routing
* Request handling
* Response formatting
* HTTP-style status codes
* Service-layer architecture
* Repository pattern
* Data models
* Business logic
* Input validation
* Exception handling
* Inventory management
* Borrowing workflow
* Return workflow
* Loan management
* Date calculations
* In-memory storage
* Separation of concerns
* Unique request identifiers
* Structured responses

---

# 🔍 Separation of Responsibilities

One of the main concepts practiced in this project is **separation of concerns**.

Instead of placing all application logic into one file, different responsibilities are separated.

```text
main82.py
    ↓
API / Request Handling

services.py
    ↓
Business Logic

repository.py
    ↓
Data Storage

models.py
    ↓
Data Structures
```

This architecture makes the project easier to maintain and provides a foundation for connecting the application to a real database or web framework later.

---

# 📚 Important Python Functions and Concepts

## `dataclass`

```python
@dataclass
```

Used for creating structured data models.

---

## `asdict()`

```python
asdict(self)
```

Converts dataclass objects into dictionaries.

---

## `uuid4()`

```python
uuid4()
```

Generates unique identifiers for requests and loans.

---

## `date.today()`

```python
date.today()
```

Gets the current local date used for borrowing and returning books.

---

## `timedelta()`

```python
timedelta(days=14)
```

Used to calculate the loan due date.

---

## `isoformat()`

```python
self.borrowed_on.isoformat()
```

Converts dates into standardized string representations.

---

## List Comprehension

The application uses:

```python
[book.to_dict() for book in self.repository.list_books()]
```

to convert book objects into dictionaries.

---

## Exception Handling

The API catches custom application errors:

```python
except LibraryError as error:
```

and converts them into structured API responses.

---

# 🗃️ Data Storage

The project currently uses **in-memory storage**.

The data flow is:

```text
Program Starts
      ↓
Books and Members Loaded
      ↓
Loans Stored in Memory
      ↓
Borrow / Return Operations
      ↓
Data Updated
      ↓
Program Ends
      ↓
Data Is Lost
```

No external database is required.

This keeps the project simple while allowing important backend concepts to be practiced.

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🗄️ Add SQLite or PostgreSQL database
* 🌐 Convert the CLI simulation into a real REST API
* ⚡ Use FastAPI or Flask
* 👤 Add member registration
* 🔐 Add authentication
* 🔑 Add JWT-based authorization
* 📚 Add book creation, editing and deletion
* 🔎 Add book search
* 🏷️ Add book categories
* ✍️ Add publisher information
* 📅 Add configurable loan periods
* ⏰ Add overdue detection
* 💰 Add late-return fines
* 📧 Add email notifications
* 🔔 Add due-date reminders
* 📖 Add borrowing history
* 👤 Add member borrowing history
* 📊 Add library statistics
* 🧾 Add transaction reports
* 🧪 Add automated unit tests
* 📋 Add API documentation
* 🗄️ Add database migrations
* 📝 Add application logging
* 🌐 Build a web-based frontend
* 📱 Build a responsive library dashboard
* 🐳 Dockerize the application
* ☁️ Deploy the backend to the cloud

---

# 🧪 Testing Improvements

A future version can include automated tests for important scenarios.

Possible test cases include:

```text
Test book listing
Test valid member lookup
Test invalid member
Test valid book lookup
Test invalid book
Test successful borrowing
Test unavailable book
Test loan creation
Test book availability reduction
Test successful return
Test invalid loan
Test duplicate return
Test availability restoration
Test due date calculation
```

A future project structure could be:

```text
DAY_82/

├── main82.py
├── models.py
├── repository.py
├── services.py
├── tests/
│   ├── test_models.py
│   ├── test_repository.py
│   └── test_services.py
└── README.md
```

---

# 🎯 Learning Outcome

This project helped me understand:

* How a Library Management System works
* How books and members can be represented using Python classes
* How dataclasses simplify data modeling
* How to build API-style request routing
* How to separate API, service and repository layers
* How to implement book borrowing
* How to implement book returns
* How to track available book copies
* How to create and manage loan records
* How to calculate due dates using `timedelta`
* How to track borrowing and return dates
* How to represent active and returned loans
* How to validate members and books
* How to handle unavailable books
* How to create custom exceptions
* How to use HTTP-style status codes
* How to generate unique IDs using UUID
* How to create structured API responses
* How to use in-memory storage
* How to separate business logic from data storage
* How backend workflows can be simulated through a CLI application

---

# 💡 Key Takeaway

The main concept learned from this project is that backend applications become easier to manage when different responsibilities are separated into layers.

```text
API Layer
    ↓
Business Logic Layer
    ↓
Repository / Data Layer
    ↓
Data Models
```

The current project uses an in-memory repository, but the architecture can later be extended with a real database and web framework.

For example:

```text
Current Project

CLI
 ↓
LibraryAPI
 ↓
LibraryService
 ↓
LibraryRepository
 ↓
In-Memory Data
```

Future version:

```text
Web Frontend
      ↓
FastAPI / Flask
      ↓
Library Service
      ↓
Repository
      ↓
PostgreSQL / SQLite
```

This makes the project a practical introduction to **backend architecture and library management system design**.

---

# 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to:

* Improve Python programming skills
* Strengthen problem-solving abilities
* Learn software development concepts
* Explore different Python technologies
* Practice writing structured and maintainable code
* Build practical projects
* Maintain consistency through daily coding

**Day 82** focuses on **Backend Development and Library Management System Design**, combining **Python classes, dataclasses, API-style routing, service-layer business logic, repository patterns, date handling, loan management, inventory tracking, and exception handling** into a practical library backend simulation.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍📚
