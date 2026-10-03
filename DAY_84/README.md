# 🚀 Day 84 - Blog Platform

Welcome to **Day 84** of my **100 Days, 100 Python Projects** challenge!

This project is a **simple Blog Platform backend simulation** built using **Python**. It demonstrates how a basic blogging system can manage posts, publishing, and comments using a clean service-based structure.

The project focuses on practicing **Object-Oriented Programming, Dataclasses, in-memory data management, service classes, validation, and basic backend logic**.

---

## 📌 Project Overview

A blog platform allows users to create posts, publish them, and receive comments from other users.

This project implements a simplified version of a blog platform where users can:

* ✍️ Create blog posts
* 👤 Store post author information
* 📝 Store post titles and content
* 📢 Publish blog posts
* 💬 Add comments to published posts
* 📋 List publicly published posts
* 🔢 Automatically generate post and comment IDs
* 🚫 Prevent comments on unpublished posts
* 🗂️ Store posts in memory
* 📦 Convert dataclass objects into dictionaries for JSON output

The application runs through the command line and simulates backend-style operations using Python classes.

---

## ✨ Features

* 🖥️ CLI-based Blog Platform
* ✍️ Create blog posts
* 👤 Store author information
* 📝 Store post title and body
* 📢 Publish posts
* 💬 Add comments
* 📋 List published posts
* 🔢 Automatic post ID generation
* 🔢 Automatic comment ID generation
* 🚫 Prevent comments on unpublished posts
* 🗂️ In-memory post storage
* 📦 Dataclass-based models
* 🔄 Dictionary/JSON-style output
* ⚠️ Basic validation using exceptions
* 🧩 Separate services for posts and comments
* 🔗 Comment service works with the post service

---

## 🛠️ Technologies Used

* **Python 3**
* **Dataclasses**
* **JSON**
* **Object-Oriented Programming**
* **In-Memory Data Storage**

### 🐍 Python

Python is used to implement the complete blog platform logic.

The project uses Python features such as:

* Classes
* Objects
* Functions
* Dictionaries
* Lists
* Exceptions
* Dataclasses
* List comprehensions
* Default values
* Type-oriented data structures

### 📦 Dataclasses

The `dataclass` decorator is used to define the `Post` model.

```python
@dataclass
class Post:
    id: int
    author: str
    title: str
    body: str
    published: bool = False
    comments: list = field(default_factory=list)
```

Dataclasses make it easier to create structured objects without manually writing an initializer.

### 🗂️ In-Memory Storage

The project stores posts inside a Python dictionary:

```python
self.posts = {}
```

Each post is stored using its ID as the dictionary key.

This keeps the project simple and avoids the need for an external database.

### 📄 JSON

The `json` module is used to display structured responses in a readable format.

```python
json.dumps(result, indent=2)
```

This makes the terminal output look similar to a backend API response.

---

## 📂 Project Structure

```text
DAY_84/
│
├── main84.py
├── posts.py
├── comments.py
├── requirements.txt
└── README.md

```

### 📄 File Description

| File / Folder      | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `main84.py`        | Main program and workflow demonstration     |
| `posts.py`         | Contains the `Post` model and `PostService` |
| `comments.py`      | Contains the `CommentService`               |
| `requirements.txt` | Lists project dependencies                  |
| `README.md`        | Project documentation                       |

---

## 📦 requirements.txt

This project uses only Python's standard library.

```text
# No external dependencies required
```

No `pip install` command is required for this project.

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

Open a terminal inside the `DAY_84` project folder.

---

### 3. Run the application

```bash
python main84.py
```

The program will execute the blog workflow and display the results in the terminal.

---

## 🔄 Application Workflow

The application follows a simple blog workflow:

```text
Start
  │
  ▼
Create Post
  │
  ▼
Publish Post
  │
  ▼
Add Comment
  │
  ▼
List Published Posts
  │
  ▼
End
```

The workflow is implemented in `main84.py`.

```python
post = posts.create(
    "Maya",
    "Learning Python",
    "Build one project each day."
)

show("CREATE POST", post.to_dict(), 201)

show(
    "PUBLISH POST",
    posts.publish(post.id).to_dict()
)

show(
    "ADD COMMENT",
    comments.add(post.id, "Leo", "Great advice!"),
    201
)

show(
    "LIST POSTS",
    {"posts": [p.to_dict() for p in posts.public_posts()]}
)
```

---

# ✍️ Creating a Blog Post

A new post can be created using the `create()` method.

```python
post = posts.create(
    "Maya",
    "Learning Python",
    "Build one project each day."
)
```

The method receives:

| Parameter | Description              |
| --------- | ------------------------ |
| `author`  | Name of the post author  |
| `title`   | Title of the blog post   |
| `body`    | Main content of the post |

A newly created post is initially unpublished.

```python
published: bool = False
```

Example:

```json
{
    "id": 1,
    "author": "Maya",
    "title": "Learning Python",
    "body": "Build one project each day.",
    "published": false,
    "comments": []
}
```

---

# 📢 Publishing a Post

Posts can be published using the `publish()` method.

```python
posts.publish(post.id)
```

The method first retrieves the post:

```python
self.get(post_id)
```

Then changes its publishing status:

```python
self.get(post_id).published = True
```

After publishing, the post becomes publicly visible.

Example:

```json
{
    "id": 1,
    "author": "Maya",
    "title": "Learning Python",
    "body": "Build one project each day.",
    "published": true,
    "comments": []
}
```

---

# 💬 Adding Comments

Comments are handled by the `CommentService` class.

```python
comments = CommentService(posts)
```

A comment can be added using:

```python
comments.add(
    post.id,
    "Leo",
    "Great advice!"
)
```

The comment contains:

* Comment ID
* Commenter's name
* Comment text

Example:

```json
{
    "id": 1,
    "name": "Leo",
    "text": "Great advice!"
}
```

---

# 🚫 Comment Validation

Comments are only accepted after a post has been published.

The following validation is implemented:

```python
if not post.published:
    raise ValueError(
        "Post must be published before comments are accepted"
    )
```

Therefore:

```text
Draft Post
    │
    └── ❌ Comment not allowed

Published Post
    │
    └── ✅ Comment allowed
```

This demonstrates how business rules can be implemented inside a service class.

---

# 📋 Listing Published Posts

The `public_posts()` method returns only posts that have been published.

```python
def public_posts(self):
    return [
        p for p in self.posts.values()
        if p.published
    ]
```

This prevents unpublished posts from appearing in the public post list.

The result is displayed using:

```python
show(
    "LIST POSTS",
    {
        "posts": [
            p.to_dict()
            for p in posts.public_posts()
        ]
    }
)
```

---

# 🧩 Post Model

The `Post` class is implemented using a Python dataclass.

```python
@dataclass
class Post:
    id: int
    author: str
    title: str
    body: str
    published: bool = False
    comments: list = field(default_factory=list)
```

Each post contains:

| Attribute   | Description        |
| ----------- | ------------------ |
| `id`        | Unique post ID     |
| `author`    | Post author's name |
| `title`     | Blog post title    |
| `body`      | Blog post content  |
| `published` | Publishing status  |
| `comments`  | List of comments   |

---

# 🔢 Automatic ID Generation

Post IDs are generated automatically.

```python
post = Post(
    len(self.posts) + 1,
    author,
    title,
    body
)
```

For example:

```text
First Post  → ID 1
Second Post → ID 2
Third Post  → ID 3
```

Comments also receive automatically generated IDs:

```python
"id": len(post.comments) + 1
```

---

# 🗂️ In-Memory Post Storage

The `PostService` stores posts using a Python dictionary.

```python
self.posts = {}
```

When a post is created:

```python
self.posts[post.id] = post
```

This provides a simple storage mechanism without requiring:

* MySQL
* PostgreSQL
* MongoDB
* SQLite
* Any external database

The data exists only while the application is running.

---

# 🔍 Finding a Post

The `get()` method retrieves a post using its ID.

```python
def get(self, post_id):
    post = self.posts.get(post_id)

    if not post:
        raise LookupError("Post not found")

    return post
```

If the requested post does not exist, a `LookupError` is raised.

This demonstrates basic exception-based error handling.

---

# 🔄 Converting Objects to Dictionaries

The `Post` class provides a `to_dict()` method:

```python
def to_dict(self):
    return asdict(self)
```

The `asdict()` function converts the dataclass object into a dictionary.

For example:

```python
post.to_dict()
```

produces:

```python
{
    "id": 1,
    "author": "Maya",
    "title": "Learning Python",
    "body": "Build one project each day.",
    "published": True,
    "comments": [
        {
            "id": 1,
            "name": "Leo",
            "text": "Great advice!"
        }
    ]
}
```

This makes the data easy to display or later return from an API.

---

# 🖥️ CLI Response Format

The `show()` function creates a simple API-style response format.

```python
def show(action, result, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(result, indent=2)}"
    )
```

Example output:

```text
REQUEST CREATE POST
RESPONSE 201

{
    "id": 1,
    "author": "Maya",
    "title": "Learning Python",
    "body": "Build one project each day.",
    "published": false,
    "comments": []
}
```

This provides an API-like structure even though the project currently runs as a command-line application.

---

# 🧱 Service-Based Architecture

The project separates responsibilities into different classes.

```text
             ┌─────────────────┐
             │    main84.py    │
             │  Application    │
             │     Workflow    │
             └────────┬────────┘
                      │
             ┌────────▼────────┐
             │  PostService    │
             │                 │
             │ Create Post     │
             │ Get Post        │
             │ Publish Post    │
             │ List Posts      │
             └────────┬────────┘
                      │
                      │
             ┌────────▼────────┐
             │ CommentService  │
             │                 │
             │ Add Comments    │
             │ Validate Post   │
             └─────────────────┘
```

This structure keeps the project organized and separates different responsibilities.

---

# 🧩 Libraries and Functions Practiced

## Python `dataclasses`

| Function / Feature | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `@dataclass`       | Creates structured data classes              |
| `field()`          | Provides a default value factory             |
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

Lists are used to store comments:

```python
comments: list = field(default_factory=list)
```

They are also used to return published posts.

---

## Python Dictionaries

Dictionaries are used as the project's in-memory storage:

```python
self.posts = {}
```

Posts are stored using their IDs as keys.

---

# 📚 Concepts Practiced

This project helped practice:

* 🐍 Python Programming
* 🧱 Object-Oriented Programming
* 📦 Dataclasses
* 🗂️ Dictionaries
* 📋 Lists
* 🔢 Automatic ID Generation
* ✍️ CRUD-style concepts
* 📢 Publishing workflows
* 💬 Comment management
* ⚠️ Exception Handling
* 🔍 Object Retrieval
* 🔄 Data Transformation
* 📄 JSON Formatting
* 🧩 Service Classes
* 🔗 Class Dependency
* 🗃️ In-Memory Data Storage
* 🏗️ Basic Backend Architecture
* 🔒 Business Rule Validation

---

# 🎯 Learning Outcome

This project helped me understand:

* How to create a simple blog backend structure
* How to use Python dataclasses
* How to store objects inside dictionaries
* How to separate application logic into service classes
* How to create and manage blog posts
* How to implement publishing functionality
* How to manage comments for posts
* How to apply business rules before performing an operation
* How to use exceptions for invalid operations
* How to convert dataclass objects into dictionaries
* How to format Python data as JSON
* How a simple backend workflow can be simulated through the command line
* How different services can interact with each other

---

# 🔮 Future Improvements

The current project is intentionally simple and can be expanded into a complete blog platform.

Possible improvements include:

* 🌐 Build a REST API using Flask or FastAPI
* 🗄️ Add SQLite, MySQL, or PostgreSQL database support
* 👤 Add user registration and login
* 🔐 Add authentication and authorization
* ✏️ Add post editing
* 🗑️ Add post deletion
* 💬 Add comment deletion and editing
* ❤️ Add likes and reactions
* 🔎 Add post search
* 🏷️ Add categories and tags
* 🖼️ Add image uploads
* 📄 Add pagination
* 📅 Add timestamps
* 👥 Add author profiles
* 📊 Add blog statistics
* 🔍 Add post filtering
* 📝 Add Markdown or rich-text support
* 🌐 Build a frontend using HTML/CSS/JavaScript or React
* 🧪 Add unit tests
* 📚 Add API documentation
* 🐳 Dockerize the application
* ☁️ Deploy the application to the cloud

---

# 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my programming skills, strengthen my problem-solving abilities, explore new technologies, and maintain consistency through daily coding.

**Day 84** focuses on building a **Blog Platform**, with an emphasis on **service-based design, dataclasses, in-memory storage, publishing workflows, comment handling, and basic backend architecture**.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍📝
