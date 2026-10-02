# 🚀 Day 83 - Simple CMS (Content Management System)

Welcome to **Day 83** of my **100 Days, 100 Python Projects** challenge!

This project is a **Simple Content Management System (CMS)** built using **Python**. The application provides a lightweight simulation of a content management backend where users can create pages, assign unique slugs, publish pages, and retrieve published content.

The project uses a simple layered structure with separate modules for:

* Content management
* Data storage
* Data modeling
* CLI interaction

The main purpose of this project is to gain practical experience with **backend development, content management concepts, CRUD-style operations, data validation, dataclasses, in-memory storage, status management, and separation of responsibilities**.

---

## 📌 Project Overview

A Content Management System allows users to create, manage, and publish digital content such as:

* Web pages
* Articles
* Blog posts
* Documentation
* Informational pages

This project implements a simplified CMS focused on page management.

The current application allows users to:

* 📝 Create content pages
* 🏷️ Assign titles to pages
* 🔗 Assign unique URL-friendly slugs
* 📄 Store page content
* 📝 Create pages as drafts
* 🚀 Publish pages
* 📋 List published pages
* 🔍 Search pages by slug
* 🆔 Automatically generate page IDs
* ⚠️ Validate required fields
* 🚨 Prevent duplicate slugs
* ❌ Handle missing pages
* 💾 Store content in memory
* 🖥️ Simulate CMS operations through the CLI

---

# ✨ Features

* 📝 Create CMS pages
* 🏷️ Page title support
* 🔗 Unique slug support
* 📄 Page body/content support
* 📝 Draft page status
* 🚀 Publish page functionality
* 📋 List published pages
* 🔍 Search pages by slug
* 🆔 Automatic page ID generation
* ⚠️ Title validation
* ⚠️ Slug validation
* 🚫 Duplicate slug prevention
* 🚨 Error handling using Python exceptions
* 💾 In-memory content storage
* 📦 Dataclass-based page model
* 🖥️ CLI-based CMS simulation
* 📊 JSON-formatted output
* 🧩 Separation of content management and storage

---

# 🏗️ Project Architecture

The project is divided into three main components:

```text
┌────────────────────────────┐
│        main83.py           │
│     CLI / Application      │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│      ContentManager        │
│     Business Logic         │
│ Create / Publish / List    │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│       ContentStorage       │
│      In-Memory Storage     │
│        Page Records        │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│           Page             │
│       Data Model           │
└────────────────────────────┘
```

The application follows a simple separation of responsibilities:

```text
main83.py
    ↓
ContentManager
    ↓
ContentStorage
    ↓
Page
```

---

# 🔄 CMS Workflow

The current application follows this workflow:

```text
Start Application
       │
       ▼
Create Content Page
       │
       ▼
Validate Title
       │
       ▼
Validate Slug
       │
       ▼
Check Duplicate Slug
       │
       ▼
Create Page
       │
       ▼
Page Status = Draft
       │
       ▼
Publish Page
       │
       ▼
Page Status = Published
       │
       ▼
List Published Pages
```

---

# 📝 Content Management

The main purpose of the application is to manage pages.

Each page contains:

```text
ID
Title
Slug
Body
Status
```

Example:

```text
ID:       1
Title:    About Us
Slug:     about-us
Body:     We build useful software.
Status:   draft
```

After publishing:

```text
Status: published
```

---

# 📄 Page Model

The `Page` dataclass is defined in `content.py`.

```python
@dataclass
class Page:
    id: int
    title: str
    slug: str
    body: str
    status: str = "draft"
```

The model contains five fields:

| Field    | Purpose                                            |
| -------- | -------------------------------------------------- |
| `id`     | Unique page identifier                             |
| `title`  | Page title                                         |
| `slug`   | Unique page identifier used as a URL-friendly name |
| `body`   | Main page content                                  |
| `status` | Current publishing status                          |

---

# 📝 Default Draft Status

Every newly created page starts with:

```text
draft
```

This is defined directly in the dataclass:

```python
status: str = "draft"
```

For example:

```json
{
  "id": 1,
  "title": "About Us",
  "slug": "about-us",
  "body": "We build useful software.",
  "status": "draft"
}
```

This simulates a common CMS workflow where content can be created first and published later.

---

# 🚀 Publishing Pages

The `publish()` method changes the page status from:

```text
draft
```

to:

```text
published
```

The method first checks whether the page exists:

```python
page = self.storage.get(page_id)

if not page:
    raise LookupError("Page not found")
```

If the page exists:

```python
page.status = "published"
```

The updated page is then returned.

---

# 📋 Published Pages

The `published()` method returns only pages whose status is:

```text
published
```

The filtering logic is:

```python
return [
    p for p in self.storage.all()
    if p.status == "published"
]
```

This means draft pages are not included in the published content list.

---

# 🔗 Slug Management

A slug is a URL-friendly identifier for a page.

For example:

```text
About Us
```

can use:

```text
about-us
```

The project requires every page to have a slug.

---

## 🚫 Duplicate Slug Prevention

Before creating a page, the CMS checks whether the slug already exists:

```python
if self.storage.find_by_slug(slug):
    raise ValueError("Slug already exists")
```

This prevents multiple pages from using the same slug.

For example:

```text
Page 1 → about-us
Page 2 → about-us
```

The second page would be rejected.

This is important because slugs are commonly used as unique identifiers for content pages.

---

# ⚠️ Input Validation

The `create()` method validates the required fields.

```python
if not title or not slug:
    raise ValueError("Title and slug are required")
```

Therefore, both:

```text
Title
Slug
```

must be provided.

An empty title or empty slug will result in an error.

---

# 🆔 Automatic Page IDs

Page IDs are generated automatically by the storage layer.

The `next_id()` method uses:

```python
return len(self.pages) + 1
```

For example:

```text
First page  → ID 1
Second page → ID 2
Third page  → ID 3
```

This keeps page creation simple without requiring the user to manually provide an ID.

---

# 💾 In-Memory Storage

The project uses an in-memory storage system instead of an external database.

The `ContentStorage` class initializes:

```python
self.pages = {}
```

Pages are stored inside this dictionary.

The page ID is used as the dictionary key.

For example:

```text
{
    1: Page(...),
    2: Page(...),
    3: Page(...)
}
```

---

# 📄 storage.py

The `storage.py` file contains the `ContentStorage` class.

```python
class ContentStorage:
```

Its main responsibility is to store and retrieve page objects.

---

## 🔢 `next_id()`

```python
def next_id(self):
    return len(self.pages) + 1
```

Generates the next page ID.

---

## 💾 `save()`

```python
def save(self, page):
    self.pages[page.id] = page
```

Stores a page in the repository.

---

## 🔍 `get()`

```python
def get(self, page_id):
    return self.pages.get(page_id)
```

Retrieves a page using its ID.

If the page does not exist, it returns:

```text
None
```

---

## 📋 `all()`

```python
def all(self):
    return list(self.pages.values())
```

Returns all stored pages.

---

## 🔎 `find_by_slug()`

```python
def find_by_slug(self, slug):
    return next(
        (p for p in self.pages.values() if p.slug == slug),
        None
    )
```

Searches for a page with a matching slug.

This method is used to prevent duplicate slugs.

---

# ⚙️ ContentManager

The `ContentManager` class contains the main CMS business logic.

It is responsible for:

* Creating pages
* Validating pages
* Publishing pages
* Listing published pages

The class receives a storage object:

```python
class ContentManager:
    def __init__(self, storage):
        self.storage = storage
```

This keeps content-management logic separate from data storage.

---

# 📝 Create Page

The `create()` method handles page creation.

```python
def create(self, title, slug, body):
```

The method performs the following steps:

```text
Receive page information
        ↓
Validate title
        ↓
Validate slug
        ↓
Check duplicate slug
        ↓
Generate page ID
        ↓
Create Page object
        ↓
Save page
        ↓
Return page
```

---

# 🚀 Publish Page

The `publish()` method handles publishing.

```python
def publish(self, page_id):
```

It first retrieves the page.

If the page does not exist:

```text
LookupError
Page not found
```

If the page exists, its status becomes:

```text
published
```

---

# 📋 List Published Content

The `published()` method returns only published pages.

This allows the CMS to separate:

```text
Draft Content
```

from:

```text
Published Content
```

For example:

```text
All Pages
├── About Us       → published
├── Services       → draft
└── Contact Us     → draft
```

The published list would contain only:

```text
About Us
```

---

# 🖥️ main83.py

`main83.py` is the application entry point.

It performs a simple CMS workflow.

The application starts with:

```python
cms = ContentManager(ContentStorage())
```

This creates:

```text
ContentManager
      ↓
ContentStorage
```

---

# 📊 CLI Output

The `show()` function is responsible for displaying operations and their results.

```python
def show(action, result, status=200):
```

It prints:

```text
REQUEST
RESPONSE
JSON DATA
```

For example:

```text
REQUEST CREATE PAGE
RESPONSE 201
{
  "id": 1,
  "title": "About Us",
  "slug": "about-us",
  "body": "We build useful software.",
  "status": "draft"
}
```

---

# 🔄 Application Workflow

The `main()` function performs three main operations.

## Step 1 — Create Page

```python
page = cms.create(
    "About Us",
    "about-us",
    "We build useful software."
)
```

The page is initially created as:

```text
status = draft
```

---

## Step 2 — Publish Page

```python
cms.publish(page.id)
```

The page status changes to:

```text
published
```

---

## Step 3 — List Published Pages

```python
cms.published()
```

The application displays all currently published pages.

---

# 📦 JSON Conversion

The `Page` model provides:

```python
def to_dict(self):
    return asdict(self)
```

Python's `asdict()` function converts the dataclass into a dictionary.

For example:

```python
Page(
    1,
    "About Us",
    "about-us",
    "We build useful software."
)
```

becomes:

```json
{
  "id": 1,
  "title": "About Us",
  "slug": "about-us",
  "body": "We build useful software.",
  "status": "draft"
}
```

This makes the content easy to display as JSON.

---

# 🚨 Error Handling

The current CMS uses Python's built-in exceptions for validation and lookup errors.

## Missing Title or Slug

If either field is empty:

```python
raise ValueError("Title and slug are required")
```

---

## Duplicate Slug

If the slug already exists:

```python
raise ValueError("Slug already exists")
```

---

## Page Not Found

If an invalid page ID is used during publishing:

```python
raise LookupError("Page not found")
```

These errors help protect the content-management workflow from invalid operations.

---

# 📊 CMS Status Flow

Each page follows a simple status lifecycle:

```text
        CREATE
          │
          ▼
       ┌───────┐
       │ DRAFT │
       └───┬───┘
           │
           │ publish()
           ▼
    ┌─────────────┐
    │  PUBLISHED  │
    └─────────────┘
```

The current implementation supports two statuses:

```text
draft
published
```

---

# 🧩 Python Concepts Practiced

This project uses several important Python concepts.

## Object-Oriented Programming

Classes are used for:

```text
ContentManager
ContentStorage
```

---

## Dataclasses

The `Page` model uses:

```python
@dataclass
class Page:
```

This provides a clean structure for representing content.

---

## Dictionary Storage

Pages are stored using:

```python
self.pages = {}
```

The page ID acts as the dictionary key.

---

## List Comprehension

The published page filtering uses:

```python
[
    p for p in self.storage.all()
    if p.status == "published"
]
```

This is used to select only published pages.

---

## Generator Expression

Slug searching uses:

```python
next(
    (p for p in self.pages.values() if p.slug == slug),
    None
)
```

This searches through stored pages efficiently until a matching slug is found.

---

## Exception Handling

The application uses:

```python
ValueError
LookupError
```

to represent invalid input and missing content.

---

## Dataclass Conversion

The project uses:

```python
asdict()
```

to convert page objects into dictionaries.

---

# 🏗️ Separation of Responsibilities

A major concept practiced in this project is **separation of concerns**.

The project separates responsibilities into:

```text
main83.py
    ↓
Application / CLI

content.py
    ↓
CMS Business Logic + Page Model

storage.py
    ↓
Data Storage
```

This makes the application easier to understand and extend.

---

# 📂 Project Structure

```text
DAY_83/

│
├── main83.py
├── content.py
├── storage.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder      | Purpose                           |
| ------------------ | --------------------------------- |
| `main83.py`        | Main application and CLI workflow |
| `content.py`       | Page model and CMS business logic |
| `storage.py`       | In-memory page storage            |
| `requirements.txt` | Python dependencies               |
| `README.md`        | Project documentation             |

---

# 📦 requirements.txt

This project uses only Python's standard library.

The main standard-library module used is:

```text
json
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

Check your Python version:

```bash
python --version
```

---

## 2. Open the project folder

Open a terminal inside the `DAY_83` directory.

---

## 3. Run the application

```bash
python main83.py
```

The Simple CMS CLI simulation will start automatically.

---

# 🖥️ Example Output

The terminal will display output similar to:

```text
Day 83 - Simple CMS (Content Management System)

REQUEST CREATE PAGE
RESPONSE 201
{
  "id": 1,
  "title": "About Us",
  "slug": "about-us",
  "body": "We build useful software.",
  "status": "draft"
}

REQUEST PUBLISH PAGE
RESPONSE 200
{
  "id": 1,
  "title": "About Us",
  "slug": "about-us",
  "body": "We build useful software.",
  "status": "published"
}

REQUEST LIST PUBLISHED
RESPONSE 200
{
  "pages": [
    {
      "id": 1,
      "title": "About Us",
      "slug": "about-us",
      "body": "We build useful software.",
      "status": "published"
    }
  ]
}
```

---

# 📝 Example Content Lifecycle

The application creates:

```text
Title:
About Us

Slug:
about-us

Body:
We build useful software.
```

Initially:

```text
Status: draft
```

After publishing:

```text
Status: published
```

The page then appears in the published-page list.

---

# 🔍 Validation Examples

## Empty Title

```python
cms.create(
    "",
    "about-us",
    "Content"
)
```

Result:

```text
ValueError:
Title and slug are required
```

---

## Empty Slug

```python
cms.create(
    "About Us",
    "",
    "Content"
)
```

Result:

```text
ValueError:
Title and slug are required
```

---

## Duplicate Slug

Creating two pages using:

```text
about-us
```

will result in:

```text
ValueError:
Slug already exists
```

---

## Invalid Page ID

Trying to publish a page that does not exist:

```python
cms.publish(999)
```

results in:

```text
LookupError:
Page not found
```

---

# 🗃️ Data Storage

The project currently uses **in-memory storage**.

The data flow is:

```text
Program Starts
      ↓
ContentStorage Created
      ↓
Pages Stored in Dictionary
      ↓
Create / Publish Operations
      ↓
Published Pages Retrieved
      ↓
Program Ends
      ↓
Data Is Lost
```

No external database is required.

This makes the project lightweight and suitable for practicing CMS concepts.

---

# 🎯 CMS Concepts Practiced

This project introduces several concepts commonly found in content management systems:

* Content creation
* Page management
* Draft status
* Publishing workflow
* Published content filtering
* Slug management
* Unique content identifiers
* Content validation
* Content storage
* Status-based filtering
* Content retrieval
* Business logic separation
* In-memory persistence

---

# 🧪 Testing Improvements

A future version can include automated tests for:

```text
Test page creation
Test empty title validation
Test empty slug validation
Test duplicate slug validation
Test page retrieval
Test publishing a page
Test invalid page publishing
Test published page filtering
Test multiple pages
Test draft pages remaining unpublished
```

A possible future testing structure:

```text
DAY_83/

├── main83.py
├── content.py
├── storage.py
├── tests/
│   ├── test_content.py
│   └── test_storage.py
└── README.md
```

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🌐 Convert the CMS into a real REST API
* ⚡ Use FastAPI or Flask
* 🗄️ Add SQLite/PostgreSQL database
* 👤 Add user accounts
* 🔐 Add authentication
* 🔑 Add role-based access control
* ✏️ Add page editing
* 🗑️ Add page deletion
* 📋 Add page listing
* 🔎 Add content search
* 🏷️ Add categories
* 🔖 Add tags
* 🖼️ Add image uploads
* 📁 Add media management
* 📝 Add rich-text content
* 📅 Add scheduled publishing
* 🔄 Add unpublish functionality
* 🕐 Add publication timestamps
* 👤 Track page authors
* 📊 Add content statistics
* 🗂️ Add content versioning
* ↩️ Add revision history
* 💾 Add database persistence
* 🧪 Add automated testing
* 📚 Add API documentation
* 🌐 Build a web-based admin dashboard
* 🎨 Build a frontend content editor
* 🐳 Dockerize the application
* ☁️ Deploy the CMS to the cloud

---

# 🧱 Possible Future Architecture

The current architecture is:

```text
CLI
 ↓
ContentManager
 ↓
ContentStorage
 ↓
In-Memory Dictionary
```

A future web-based version could use:

```text
Web Frontend
      ↓
FastAPI / Flask
      ↓
Content Service
      ↓
Repository
      ↓
SQLite / PostgreSQL
```

Additional components could then be added:

```text
Authentication
      ↓
Authorization
      ↓
Content Management
      ↓
Database
      ↓
Media Storage
```

---

# 🎯 Learning Outcome

This project helped me understand:

* How a basic CMS works
* How content pages can be modeled using Python
* How to create pages programmatically
* How to assign unique page IDs
* How slugs can be used to identify content
* How to prevent duplicate slugs
* How to validate required content fields
* How draft and published states work
* How to publish content
* How to filter published content
* How to separate business logic from storage
* How to use dataclasses
* How to convert dataclasses into dictionaries
* How to use dictionaries for in-memory storage
* How to use list comprehensions for filtering
* How to use generator expressions for searching
* How to handle validation errors
* How to handle missing pages
* How to structure a small backend application
* How to simulate CMS operations through a CLI
* How a simple CMS can later be extended into a full web application

---

# 💡 Key Takeaway

The main concept learned from this project is that even a small content management system can be organized into separate layers.

```text
Application Layer
        ↓
Business Logic
        ↓
Storage Layer
        ↓
Data Model
```

In this project:

```text
main83.py
    ↓
ContentManager
    ↓
ContentStorage
    ↓
Page
```

This separation makes the project easier to understand, maintain, test, and extend.

The current implementation uses in-memory storage, but it provides a foundation for adding a real database, REST API, authentication, content editing, and a web-based administration panel in future versions.

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

**Day 83** focuses on **Content Management and Backend Architecture**, combining **Python dataclasses, in-memory storage, content validation, slug management, publishing workflows, status-based filtering, and separation of business logic from data storage** to create a practical Simple CMS.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍📝
