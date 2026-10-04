# 🚀 Day 85 - Job Board App

Welcome to **Day 85** of my **100 Days, 100 Python Projects** challenge!

This project is a **simple Job Board Application** built using **Python**. It simulates the basic functionality of a job portal where users can view available job listings and submit applications with their personal information and resume link.

The project focuses on practicing **Object-Oriented Programming, Dataclasses, service-based architecture, in-memory data storage, validation, and application management**.

---

## 📌 Project Overview

A job board platform connects job seekers with companies that are looking for candidates.

This project implements a simplified backend-style Job Board App where users can:

* 💼 View available job listings
* 🏢 View company information
* 👨‍💻 View job titles
* 📍 View job locations
* 📝 Submit job applications
* 📧 Provide applicant email information
* 📄 Submit a resume URL
* 🔢 Generate unique application IDs
* 🚫 Prevent duplicate applications for the same job and email
* 📦 Store applications in memory
* 📄 Display structured JSON-style responses

The application runs through the command line and simulates basic job-board backend operations.

---

## ✨ Features

* 🖥️ CLI-based Job Board App
* 💼 Job listing management
* 🏢 Company information
* 👨‍💻 Job title information
* 📍 Job location information
* 📋 List available jobs
* 🔍 Find jobs using job ID
* 📝 Submit job applications
* 👤 Store applicant name
* 📧 Store applicant email
* 📄 Store resume URL
* 🔢 Automatic application ID generation
* 📊 Application status tracking
* 🚫 Duplicate application prevention
* ⚠️ Error handling for invalid job IDs
* 🗂️ In-memory application storage
* 📦 Dataclass-based job model
* 📄 JSON-formatted terminal output
* 🧩 Separate job and application services

---

## 🛠️ Technologies Used

* **Python 3**
* **Dataclasses**
* **JSON**
* **Object-Oriented Programming**
* **In-Memory Data Storage**

### 🐍 Python

Python is used to build the complete application logic.

The project uses:

* Classes
* Objects
* Functions
* Lists
* Dictionaries
* Dataclasses
* List comprehensions
* Conditional expressions
* Exception handling
* Formatted strings

### 📦 Dataclasses

The `Job` model uses Python's `dataclass` decorator.

```python
@dataclass
class Job:
    id: int
    company: str
    title: str
    location: str
```

Dataclasses provide a simple way to create structured objects for job information.

### 📄 JSON

The `json` module is used to display application responses in a structured and readable format.

```python
json.dumps(result, indent=2)
```

This gives the terminal output an API-like appearance.

---

## 📂 Project Structure

```text
DAY_85/
│
├── main85.py
├── jobs.py
├── applications.py
├── requirements.txt
└── README.md
```

### 📄 File Description

| File / Folder      | Purpose                                   |
| ------------------ | ----------------------------------------- |
| `main85.py`        | Main application workflow                 |
| `jobs.py`          | Contains the `Job` model and `JobCatalog` |
| `applications.py`  | Handles job application submission        |
| `requirements.txt` | Lists project dependencies                |
| `README.md`        | Project documentation                     |

---

## 📦 requirements.txt

This project uses only Python's standard library.

```text
# No external dependencies required
```

No additional packages need to be installed.

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

Python 3 is recommended.

---

### 2. Open the project folder

Open a terminal inside the `DAY_85` folder.

---

### 3. Run the application

```bash
python main85.py
```

The Job Board App will execute and display available jobs followed by a sample job application.

---

# 🔄 Application Workflow

The application follows a simple workflow:

```text
              Start
                │
                ▼
        Initialize JobCatalog
                │
                ▼
     Initialize ApplicationService
                │
                ▼
          List Available Jobs
                │
                ▼
       Submit Job Application
                │
                ▼
       Generate Application ID
                │
                ▼
        Store Application
                │
                ▼
               End
```

The complete workflow is implemented in `main85.py`.

```python
jobs = JobCatalog()
applications = ApplicationService(jobs)

show(
    "LIST JOBS",
    {"jobs": [j.to_dict() for j in jobs.list()]}
)

show(
    "SUBMIT APPLICATION",
    applications.submit(
        101,
        "Jordan Lee",
        "jordan@example.com",
        "https://files.example.com/jordan.pdf"
    ),
    201
)
```

---

# 💼 Job Listing

The `JobCatalog` class manages available job listings.

A sample job is created when the catalog is initialized:

```python
self.jobs = {
    101: Job(
        101,
        "Nova Labs",
        "Python Developer",
        "Remote"
    )
}
```

The current project contains one sample job:

| Field    | Value              |
| -------- | ------------------ |
| Job ID   | `101`              |
| Company  | `Nova Labs`        |
| Position | `Python Developer` |
| Location | `Remote`           |

---

# 📋 Listing Jobs

The `list()` method returns all available jobs.

```python
def list(self):
    return list(self.jobs.values())
```

The jobs are displayed using:

```python
show(
    "LIST JOBS",
    {
        "jobs": [
            j.to_dict()
            for j in jobs.list()
        ]
    }
)
```

Example output:

```json
{
    "jobs": [
        {
            "id": 101,
            "company": "Nova Labs",
            "title": "Python Developer",
            "location": "Remote"
        }
    ]
}
```

---

# 🔍 Finding a Job

The `get()` method searches for a job using its ID.

```python
def get(self, job_id):
    job = self.jobs.get(job_id)

    if not job:
        raise LookupError("Job not found")

    return job
```

For example:

```python
jobs.get(101)
```

returns the Python Developer position.

If the job does not exist, a `LookupError` is raised.

---

# 📝 Submitting a Job Application

Users can submit an application using the `ApplicationService`.

```python
applications.submit(
    101,
    "Jordan Lee",
    "jordan@example.com",
    "https://files.example.com/jordan.pdf"
)
```

The method accepts:

| Parameter    | Description                            |
| ------------ | -------------------------------------- |
| `job_id`     | ID of the job being applied for        |
| `name`       | Applicant's name                       |
| `email`      | Applicant's email                      |
| `resume_url` | URL pointing to the applicant's resume |

---

# 📄 Application Data

Each submitted application contains:

* Application ID
* Job ID
* Applicant name
* Applicant email
* Resume URL
* Application status

Example:

```json
{
    "id": "APP-0001",
    "job_id": 101,
    "name": "Jordan Lee",
    "email": "jordan@example.com",
    "resume_url": "https://files.example.com/jordan.pdf",
    "status": "received"
}
```

---

# 🔢 Automatic Application IDs

Application IDs are automatically generated.

The project uses:

```python
f"APP-{len(self.applications)+1:04}"
```

This generates IDs such as:

```text
APP-0001
APP-0002
APP-0003
APP-0004
```

The four-digit formatting makes the application IDs consistent and easy to read.

---

# 📊 Application Status

Every newly submitted application starts with the status:

```python
"status": "received"
```

Example:

```json
{
    "id": "APP-0001",
    "status": "received"
}
```

The current version only creates applications with the `received` status.

Future versions could introduce additional statuses such as:

```text
received
under_review
shortlisted
interview
rejected
accepted
```

---

# 🚫 Duplicate Application Prevention

The project prevents the same email address from applying to the same job more than once.

The following condition is used:

```python
if any(
    a["job_id"] == job_id
    and a["email"] == email
    for a in self.applications
):
    raise ValueError("Application already submitted")
```

For example, if:

```text
Job ID: 101
Email: jordan@example.com
```

has already submitted an application, another application using the same job ID and email will be rejected.

This demonstrates basic business-rule validation.

---

# ⚠️ Job Validation

Before submitting an application, the application service checks whether the job exists.

```python
self.jobs.get(job_id)
```

The `JobCatalog.get()` method raises:

```python
LookupError("Job not found")
```

if an invalid job ID is provided.

This prevents applications from being submitted for jobs that do not exist.

---

# 🗂️ In-Memory Application Storage

Applications are stored inside a Python list.

```python
self.jobs, self.applications = jobs, []
```

When an application is submitted:

```python
self.applications.append(application)
```

This is simple and useful for learning backend logic.

However, the data is temporary and will be lost when the application exits.

---

# 🧩 Service-Based Architecture

The project separates job management and application management into different classes.

```text
                 ┌──────────────────┐
                 │    main85.py     │
                 │  Application     │
                 │    Workflow      │
                 └────────┬─────────┘
                          │
                ┌─────────▼─────────┐
                │    JobCatalog     │
                │                   │
                │ List Jobs         │
                │ Get Job           │
                └─────────┬─────────┘
                          │
                          │
                ┌─────────▼─────────┐
                │ ApplicationService│
                │                   │
                │ Submit Application│
                │ Validate Job      │
                │ Prevent Duplicate │
                └───────────────────┘
```

This makes the application easier to understand and extend.

---

# 📦 Job Model

The `Job` class is defined using a dataclass.

```python
@dataclass
class Job:
    id: int
    company: str
    title: str
    location: str
```

Each job contains four properties:

| Property   | Description                   |
| ---------- | ----------------------------- |
| `id`       | Unique job identifier         |
| `company`  | Company offering the position |
| `title`    | Job title                     |
| `location` | Job location                  |

---

# 🔄 Converting Jobs to Dictionaries

The `Job` class provides a `to_dict()` method.

```python
def to_dict(self):
    return asdict(self)
```

The `asdict()` function converts the dataclass object into a dictionary.

For example:

```python
Job(
    101,
    "Nova Labs",
    "Python Developer",
    "Remote"
).to_dict()
```

produces:

```python
{
    "id": 101,
    "company": "Nova Labs",
    "title": "Python Developer",
    "location": "Remote"
}
```

This makes the job information easy to display and serialize.

---

# 🖥️ CLI Response Format

The `show()` function provides a simple API-style response format.

```python
def show(action, result, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(result, indent=2)}"
    )
```

Example:

```text
REQUEST LIST JOBS
RESPONSE 200
{
    "jobs": [
        {
            "id": 101,
            "company": "Nova Labs",
            "title": "Python Developer",
            "location": "Remote"
        }
    ]
}
```

For the application:

```text
REQUEST SUBMIT APPLICATION
RESPONSE 201
{
    "id": "APP-0001",
    "job_id": 101,
    "name": "Jordan Lee",
    "email": "jordan@example.com",
    "resume_url": "https://files.example.com/jordan.pdf",
    "status": "received"
}
```

Although this is a CLI application, the response structure is similar to what could later be returned by a web API.

---

# 🧩 Libraries and Functions Practiced

## Python `dataclasses`

| Function / Feature | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `@dataclass`       | Creates structured job objects               |
| `asdict()`         | Converts dataclass objects into dictionaries |

---

## Python `json`

| Function       | Purpose                                       |
| -------------- | --------------------------------------------- |
| `json.dumps()` | Converts Python data into formatted JSON text |

Example:

```python
json.dumps(result, indent=2)
```

---

## Python Lists

Lists are used to store:

* Job objects returned by `list()`
* Submitted applications

Example:

```python
self.applications = []
```

---

## Python Dictionaries

Dictionaries are used to store jobs:

```python
self.jobs = {
    101: Job(...)
}
```

Application information is also represented using dictionaries.

---

## Python `any()`

The `any()` function is used to detect duplicate applications.

```python
any(
    a["job_id"] == job_id
    and a["email"] == email
    for a in self.applications
)
```

It returns `True` if a matching application already exists.

---

## Python Formatted Strings

Formatted strings are used to generate application IDs:

```python
f"APP-{len(self.applications)+1:04}"
```

They are also used for terminal response formatting.

---

# 📚 Concepts Practiced

This project helped practice:

* 🐍 Python Programming
* 🧱 Object-Oriented Programming
* 📦 Dataclasses
* 📋 Lists
* 🗂️ Dictionaries
* 🔢 Automatic ID Generation
* 💼 Job Management
* 📝 Application Management
* 🚫 Duplicate Detection
* ⚠️ Exception Handling
* 🔍 Object Retrieval
* 🔄 Data Transformation
* 📄 JSON Formatting
* 🧩 Service Classes
* 🔗 Class Dependency
* 🗃️ In-Memory Storage
* 🏗️ Basic Backend Architecture
* 🔒 Business Rule Validation
* 🧮 List Comprehensions
* 🔎 Generator Expressions

---

# 🎯 Learning Outcome

This project helped me understand:

* How to build a simple job board backend
* How to represent jobs using dataclasses
* How to manage jobs using a catalog class
* How to submit and store job applications
* How to generate unique application IDs
* How to validate whether a job exists
* How to prevent duplicate applications
* How to use lists and dictionaries for temporary data storage
* How to separate application logic into service classes
* How to use exceptions for invalid operations
* How to convert Python objects into dictionaries
* How to format structured data as JSON
* How backend-style workflows can be simulated through the command line
* How business rules can be implemented in application services

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🌐 Build a REST API using Flask or FastAPI
* 🗄️ Add SQLite, MySQL, or PostgreSQL database support
* 👤 Add user registration and login
* 🔐 Add authentication and authorization
* 🏢 Add company registration
* ➕ Add job creation
* ✏️ Add job editing
* 🗑️ Add job deletion
* 🔎 Add job search
* 🏷️ Add job categories
* 💰 Add salary information
* 🧑‍💻 Add experience requirements
* 🎓 Add education requirements
* 🌍 Add multiple job locations
* 📊 Add application management dashboard
* 🔄 Add application status updates
* 📧 Add email notifications
* 📄 Add resume file upload
* 🔍 Add filtering and sorting
* 📑 Add pagination
* 👤 Add applicant profiles
* 🏢 Add company profiles
* 🧪 Add unit tests
* 📚 Add API documentation
* 🖥️ Build a web frontend
* ⚛️ Build a React-based interface
* 🐳 Dockerize the application
* ☁️ Deploy the application to the cloud

---

# 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, explore new technologies, and maintain consistency through daily coding.

**Day 85** focuses on building a **Job Board App**, with an emphasis on **job management, application submission, duplicate prevention, service-based architecture, dataclasses, and basic backend logic**.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍💼
