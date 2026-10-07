# 🚀 Day 88 - Social Media Backend

Welcome to **Day 88** of my **100 Days, 100 Python Projects** challenge!

This project is a **simple Social Media Backend** built using **Python**. It simulates the basic functionality of a social media platform where users can follow other users, create posts, and view a personalized feed containing posts from themselves and the users they follow.

The project focuses on practicing **Object-Oriented Programming, Dataclasses, sets, lists, dictionaries, validation, service-based architecture, user relationships, post management, feed generation, timestamps, and in-memory data management**.

---

## 📌 Project Overview

A social media backend is responsible for managing users, relationships between users, posts, and personalized feeds.

This project implements a simplified social media backend where users can:

* 👤 Store users
* 👥 Follow other users
* 🚫 Prevent users from following themselves
* 📝 Create posts
* ✍️ Validate post content
* 🕒 Store post creation timestamps
* 📰 Generate personalized feeds
* 👀 Display posts from followed users
* 👤 Display the user's own posts
* 🔄 Display newest posts first
* 📦 Store user and post data in memory
* 📄 Display structured JSON-style responses
* 🧩 Separate user, post, and feed responsibilities into services

The application runs through the command line and simulates basic social media backend operations.

---

## ✨ Features

* 🖥️ CLI-based Social Media Backend
* 👤 User management
* 👥 Follow user functionality
* 🚫 Self-follow validation
* 📝 Post creation
* ✍️ Empty post validation
* 🕒 UTC timestamp generation
* 📰 Personalized feed generation
* 👀 Own-post visibility
* 👥 Followed-user post visibility
* 🔄 Newest-first feed ordering
* 🗂️ In-memory user storage
* 🗂️ In-memory post storage
* 📦 Dataclass-based user and post models
* 🔒 Set-based follower relationship storage
* 📋 List-based post storage
* 📄 JSON-formatted terminal output
* 🧩 Separate user, post, and feed services
* ⚠️ Exception-based validation

---

## 🛠️ Technologies Used

* **Python 3**
* **Dataclasses**
* **Sets**
* **Lists**
* **Dictionaries**
* **JSON**
* **Datetime**
* **Object-Oriented Programming**
* **In-Memory Data Storage**

### 🐍 Python

Python is used to implement the complete social media backend.

The project uses:

* Classes
* Objects
* Functions
* Dictionaries
* Sets
* Lists
* Dataclasses
* Exceptions
* Formatted strings
* List comprehensions
* Set operations

---

## 📦 Dataclasses

The project uses Python's `dataclass` decorator to represent users and posts.

The `User` model is defined as:

```python
@dataclass
class User:
    id: int
    name: str
    following: set[int] = field(default_factory=set)
```

The `Post` model is defined as:

```python
@dataclass
class Post:
    id: int
    user_id: int
    text: str
    created_at: str
```

Dataclasses provide a clean and structured way to represent application data.

---

## 👥 Sets

A set is used to store the users that a particular user follows.

```python
following: set[int] = field(default_factory=set)
```

For example:

```text
Ava
 │
 └── follows → Noah
```

The user ID of the followed user is stored inside the `following` set.

Sets are useful because they automatically maintain unique values.

---

## 🗂️ Dictionaries

Dictionaries are used to store users.

```python
self.users = {
    1: User(1, "Ava"),
    2: User(2, "Noah")
}
```

The user ID acts as the dictionary key.

This allows users to be retrieved efficiently:

```python
self.users.get(user_id)
```

---

## 📂 Project Structure

```text
DAY_88/
│
├── main88.py
├── users.py
├── posts.py
├── feed.py
├── requirements.txt
└── README.md
```

### 📄 File Description

| File / Folder      | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `main88.py`        | Main application workflow                   |
| `users.py`         | Contains the `User` model and `UserService` |
| `posts.py`         | Contains the `Post` model and `PostService` |
| `feed.py`          | Handles personalized feed generation        |
| `requirements.txt` | Lists project dependencies                  |
| `README.md`        | Project documentation                       |

---

## 📦 requirements.txt

This project uses only Python's standard library.

```text
# No external dependencies required
```

No additional packages are required to run the project.

---

# ▶️ How to Run

## 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

Python 3 is recommended.

---

## 2. Open the project folder

Open a terminal inside the `DAY_88` folder.

---

## 3. Run the application

```bash
python main88.py
```

The application will:

1. Initialize users
2. Make Ava follow Noah
3. Create a post for Noah
4. Generate Ava's personalized feed
5. Display the results in the terminal

---

# 🔄 Application Workflow

The application follows this workflow:

```text
                    Start
                      │
                      ▼
              Initialize Services
                      │
                      ▼
               Load Users
                      │
                      ▼
              Follow User
                      │
                      ▼
              Create Post
                      │
                      ▼
              Request Feed
                      │
                      ▼
          Determine Visible Users
                      │
                      ▼
         Filter Relevant Posts
                      │
                      ▼
          Sort Newest Posts First
                      │
                      ▼
                 Show Feed
                      │
                      ▼
                    End
```

The workflow is implemented in `main88.py`.

```python
users = UserService()
posts = PostService(users)
feed = FeedService(users, posts)

show("FOLLOW USER", users.follow(1, 2))

show(
    "CREATE POST",
    posts.create(
        2,
        "Shipping my Python project today!"
    ).to_dict(),
    201
)

show(
    "GET FEED",
    {
        "posts": [
            p.to_dict()
            for p in feed.get(1)
        ]
    }
)
```

---

# 👤 User Management

Users are managed by the `UserService` class.

Two sample users are created when the service starts:

```python
self.users = {
    1: User(1, "Ava"),
    2: User(2, "Noah")
}
```

The current users are:

| User ID | Name |
| ------- | ---- |
| `1`     | Ava  |
| `2`     | Noah |

Each user also has a `following` set.

Initially:

```text
Ava
Following → {}

Noah
Following → {}
```

---

# 🔎 Getting a User

The `get()` method retrieves a user using their ID.

```python
def get(self, user_id):
    user = self.users.get(user_id)

    if not user:
        raise LookupError("User not found")

    return user
```

For example:

```python
users.get(1)
```

returns the user:

```text
User ID: 1
Name: Ava
```

If the requested user does not exist, a `LookupError` is raised.

---

# 👥 Following a User

Users can follow other users using the `follow()` method.

```python
users.follow(1, 2)
```

This means:

```text
User 1 → follows → User 2
```

In the current application:

```text
Ava → follows → Noah
```

The method returns:

```json
{
    "message": "Ava now follows Noah"
}
```

---

# 🚫 Preventing Self-Following

The system prevents a user from following themselves.

The validation is implemented as:

```python
if user_id == target_id:
    raise ValueError(
        "Users cannot follow themselves"
    )
```

For example:

```text
Ava → Noah      ✅ Allowed
Ava → Ava       ❌ Not allowed
Noah → Ava      ✅ Allowed
Noah → Noah     ❌ Not allowed
```

This implements a basic social-media relationship rule.

---

# 📝 Creating Posts

Posts are handled by the `PostService`.

A post can be created using:

```python
posts.create(
    2,
    "Shipping my Python project today!"
)
```

The method receives:

| Parameter | Description                      |
| --------- | -------------------------------- |
| `user_id` | ID of the user creating the post |
| `text`    | Content of the post              |

The system first verifies that the user exists.

```python
self.users.get(user_id)
```

A new post is then created:

```python
post = Post(
    len(self.posts) + 1,
    user_id,
    text,
    datetime.now(timezone.utc).isoformat()
)
```

---

# ✍️ Post Validation

The system does not allow empty posts.

The validation is:

```python
if not text.strip():
    raise ValueError(
        "Post cannot be empty"
    )
```

For example:

```text
"Hello World!"          → ✅ Valid
"Shipping my project"  → ✅ Valid
""                      → ❌ Invalid
"   "                   → ❌ Invalid
```

This prevents meaningless empty posts from being stored.

---

# 🕒 Post Timestamps

Every post receives a UTC timestamp when it is created.

```python
datetime.now(
    timezone.utc
).isoformat()
```

A timestamp may look like:

```text
2026-10-07T15:30:45.123456+00:00
```

The timestamp is stored inside the `created_at` field of the post.

Example:

```json
{
    "id": 1,
    "user_id": 2,
    "text": "Shipping my Python project today!",
    "created_at": "2026-10-07T15:30:45.123456+00:00"
}
```

Using UTC makes timestamps consistent across different locations.

---

# 📰 Personalized Feed

The `FeedService` is responsible for generating a user's feed.

A feed is generated using:

```python
feed.get(1)
```

This requests the feed for user `1`, which is Ava.

The service first retrieves the user:

```python
user = self.users.get(user_id)
```

It then determines which users' posts should be visible.

```python
visible = user.following | {user_id}
```

This is an important part of the project.

---

# 👀 Feed Visibility

The user's feed contains:

1. The user's own posts
2. Posts from users they follow

For example:

```text
Ava follows Noah

Visible Users:
├── Ava
└── Noah
```

The expression:

```python
user.following | {user_id}
```

uses a **set union operation**.

If Ava follows Noah:

```python
user.following
```

contains:

```text
{2}
```

Adding Ava's own ID:

```python
{1}
```

produces:

```text
{1, 2}
```

Therefore, posts created by either user can appear in Ava's feed.

---

# 🔄 Newest Posts First

The feed displays the newest posts first.

This is achieved using:

```python
reversed(self.posts.posts)
```

The posts are stored in creation order:

```text
Post 1
Post 2
Post 3
```

The feed processes them in reverse:

```text
Post 3
Post 2
Post 1
```

This simulates the common social-media behavior where recent posts appear at the top of the feed.

---

# 🔍 Filtering Feed Posts

The feed filters posts using:

```python
[
    p
    for p in reversed(self.posts.posts)
    if p.user_id in visible
]
```

Only posts whose `user_id` exists in the `visible` set are included.

For example:

```text
Visible Users = {1, 2}

Post 1 → User 1 → ✅ Included
Post 2 → User 2 → ✅ Included
Post 3 → User 3 → ❌ Not included
```

This creates a basic personalized feed.

---

# 📊 Example Feed

Suppose:

```text
Ava follows Noah
```

Noah creates:

```text
Shipping my Python project today!
```

Ava requests her feed.

The response contains Noah's post:

```json
{
    "posts": [
        {
            "id": 1,
            "user_id": 2,
            "text": "Shipping my Python project today!",
            "created_at": "2026-10-07T15:30:45.123456+00:00"
        }
    ]
}
```

Because Ava follows Noah, the post is visible in her feed.

---

# 📄 JSON-Formatted Responses

The `show()` function formats the application's output.

```python
def show(action, result, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(result, indent=2)}"
    )
```

This creates an API-style terminal response.

For example:

```text
REQUEST FOLLOW USER
RESPONSE 200
{
  "message": "Ava now follows Noah"
}
```

The post creation response uses status `201`:

```text
REQUEST CREATE POST
RESPONSE 201
{
  "id": 1,
  "user_id": 2,
  "text": "Shipping my Python project today!",
  "created_at": "..."
}
```

Although the application runs in the terminal, the response structure resembles a simple backend API.

---

# 🧩 Service-Based Architecture

The project separates responsibilities into three services.

```text
                    ┌─────────────────────┐
                    │      main88.py      │
                    │  Application Flow   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
      │ UserService  │ │ PostService  │ │ FeedService  │
      │              │ │              │ │              │
      │ Get Users    │ │ Create Post  │ │ Generate     │
      │ Follow Users │ │ Validate     │ │ Personalized │
      │ Validate     │ │ Timestamps   │ │ Feed         │
      └──────────────┘ └──────────────┘ └──────────────┘
              │                │                │
              └────────────────┴────────────────┘
                               │
                               ▼
                       In-Memory Data
```

### `UserService`

Responsible for:

* User storage
* User retrieval
* Follow relationships
* Self-follow validation

### `PostService`

Responsible for:

* Post creation
* Post validation
* Post IDs
* Post timestamps
* Post storage

### `FeedService`

Responsible for:

* Retrieving users
* Determining visible users
* Filtering posts
* Ordering posts
* Generating personalized feeds

This separation keeps the project organized and easier to extend.

---

# 🗂️ In-Memory Data Storage

The current project stores all data in memory.

Users are stored in a dictionary:

```python
self.users = {
    1: User(1, "Ava"),
    2: User(2, "Noah")
}
```

Posts are stored in a list:

```python
self.posts = []
```

New posts are appended:

```python
self.posts.append(post)
```

The project does not currently use:

* MySQL
* PostgreSQL
* SQLite
* MongoDB
* Redis
* Any external database

> ⚠️ Since the project uses in-memory storage, all users, relationships, and posts are lost when the program terminates.

---

# 🔢 Post ID Generation

Each post receives a sequential ID.

```python
Post(
    len(self.posts) + 1,
    user_id,
    text,
    ...
)
```

For example:

```text
First Post  → ID 1
Second Post → ID 2
Third Post  → ID 3
```

This provides a simple unique identifier during the application's execution.

---

# 🔗 User Relationship Management

The project uses a set to represent the relationship between users.

For example:

```text
Ava (1)
 │
 └── follows
       │
       ▼
     Noah (2)
```

Internally:

```python
User(
    id=1,
    name="Ava",
    following={2}
)
```

The value `2` represents Noah's user ID.

This approach avoids storing complete user objects inside another user and keeps the relationship lightweight.

---

# 🧮 Set Union for Feed Generation

One of the important Python concepts practiced in this project is **set union**.

The feed uses:

```python
visible = user.following | {user_id}
```

Suppose:

```python
user.following = {2, 3}
```

and:

```python
user_id = 1
```

Then:

```python
{2, 3} | {1}
```

produces:

```text
{1, 2, 3}
```

Therefore, the user can see:

```text
Their own posts
+
Posts from users 2 and 3
```

---

# 🧩 Libraries and Functions Practiced

## Python `dataclasses`

| Feature      | Purpose                                       |
| ------------ | --------------------------------------------- |
| `@dataclass` | Creates structured user/post models           |
| `field()`    | Creates default sets                          |
| `asdict()`   | Converts a dataclass object into a dictionary |

Example:

```python
@dataclass
class Post:
    id: int
    user_id: int
    text: str
    created_at: str
```

---

## Python `set`

| Feature  | Purpose                         |
| -------- | ------------------------------- |
| `set()`  | Stores unique followed-user IDs |
| `in`     | Checks membership               |
| `.add()` | Adds a followed user            |
| `\|`     | Performs set union              |

Example:

```python
user.following.add(target_id)
```

and:

```python
visible = user.following | {user_id}
```

---

## Python `list`

Lists are used to store posts.

```python
self.posts = []
```

New posts are added using:

```python
self.posts.append(post)
```

The list can then be traversed to generate the feed.

---

## Python `dict`

Dictionaries are used to store users.

```python
self.users = {
    1: User(1, "Ava"),
    2: User(2, "Noah")
}
```

They allow users to be retrieved using their IDs.

---

## Python `json`

The `json` module is used to format terminal responses.

```python
json.dumps(
    result,
    indent=2
)
```

This makes output easier to read.

---

## Python `datetime`

The `datetime` module is used to create UTC timestamps.

```python
datetime.now(
    timezone.utc
).isoformat()
```

---

## Python `reversed()`

The `reversed()` function is used to process posts from newest to oldest.

```python
reversed(self.posts.posts)
```

This allows the feed to display recent posts first.

---

# 📚 Concepts Practiced

This project helped practice:

* 🐍 Python Programming
* 🧱 Object-Oriented Programming
* 📦 Dataclasses
* 👤 User Management
* 👥 User Relationships
* ➕ Follow Functionality
* 🚫 Self-Follow Validation
* 📝 Post Creation
* ✍️ Input Validation
* 📰 Feed Generation
* 👀 Content Visibility
* 🔄 Reverse Ordering
* 🗂️ Dictionaries
* 🔐 Sets
* 📋 Lists
* 📄 JSON Formatting
* 🕒 UTC Timestamps
* 🧩 Service-Based Architecture
* 🔗 Class Dependencies
* 🗃️ In-Memory Storage
* 🏗️ Basic Backend Design
* ⚠️ Exception Handling
* 🔢 Sequential ID Generation
* 🧮 Set Union Operations
* 🔍 List Comprehensions

---

# 🎯 Learning Outcome

This project helped me understand:

* How to build a basic social media backend using Python
* How to represent users and posts using dataclasses
* How to store users using dictionaries
* How to store posts using lists
* How sets can represent user relationships
* How to implement a follow-user feature
* How to prevent users from following themselves
* How to validate post content
* How to generate UTC timestamps
* How to create personalized feeds
* How to include a user's own posts in their feed
* How to display posts from followed users
* How to filter posts using set membership
* How to display newest posts first
* How to separate responsibilities using service classes
* How to use exceptions for invalid operations
* How to format backend-style responses as JSON
* How to simulate backend functionality without a database
* How to use set union for visibility calculations
* How to organize a small backend project using multiple Python modules

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🌐 Build a REST API using Flask or FastAPI
* 🗄️ Add SQLite, MySQL, or PostgreSQL database support
* 👤 Add user registration
* 🔐 Add user authentication and authorization
* 🔑 Add password hashing
* 👥 Add followers and following lists
* 🔍 Add user search
* 📝 Add post editing
* 🗑️ Add post deletion
* ❤️ Add likes and unlike functionality
* 💬 Add comments
* 🔁 Add repost/share functionality
* 🏷️ Add hashtags
* 🔎 Add post search
* 🖼️ Add image and video posts
* 📎 Add media uploads
* 📊 Add engagement statistics
* 🔔 Add notifications
* 📰 Improve feed ranking
* 🤝 Add suggested users
* 👥 Add private accounts
* 🔒 Add follow-request functionality
* 🚫 Add blocking and muting
* 📱 Build a web interface
* ⚛️ Build a React frontend
* 🔄 Add real-time feed updates
* 📊 Add an admin dashboard
* 🧪 Add unit tests
* 📚 Add API documentation
* 🐳 Dockerize the application
* ☁️ Deploy the backend to the cloud

---

# 🖥️ Example Application Output

The application produces output similar to:

```text
Day 88 - Social Media Backend

REQUEST FOLLOW USER
RESPONSE 200
{
  "message": "Ava now follows Noah"
}

REQUEST CREATE POST
RESPONSE 201
{
  "id": 1,
  "user_id": 2,
  "text": "Shipping my Python project today!",
  "created_at": "2026-10-07T..."
}

REQUEST GET FEED
RESPONSE 200
{
  "posts": [
    {
      "id": 1,
      "user_id": 2,
      "text": "Shipping my Python project today!",
      "created_at": "2026-10-07T..."
    }
  ]
}
```

The exact `created_at` value will change every time the application runs.

---

# 🏗️ Backend Design

The project follows a simple layered service design:

```text
                    Social Media Backend
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        User Service   Post Service   Feed Service
             │              │              │
             ▼              ▼              ▼
          Users           Posts       Feed Logic
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                    In-Memory Storage
```

### User Service

Manages:

```text
Users
Follow relationships
User validation
```

### Post Service

Manages:

```text
Posts
Post validation
Post IDs
Timestamps
```

### Feed Service

Manages:

```text
Visible users
Post filtering
Feed ordering
Personalized feed
```

This structure provides a basic foundation for a future web-based social media backend.

---

# 🔐 Validation and Error Handling

The application uses Python exceptions to handle invalid operations.

### Invalid User

```python
if not user:
    raise LookupError(
        "User not found"
    )
```

### Self-Follow

```python
if user_id == target_id:
    raise ValueError(
        "Users cannot follow themselves"
    )
```

### Empty Post

```python
if not text.strip():
    raise ValueError(
        "Post cannot be empty"
    )
```

These validations prevent invalid data from entering the system.

---

# 🧠 Key Python Concepts

Some of the most important concepts practiced in this project are:

### 1. Dataclasses

Used to create structured `User` and `Post` objects.

### 2. Sets

Used to store unique following relationships.

### 3. Dictionaries

Used for efficient user lookup.

### 4. Lists

Used to maintain posts.

### 5. Set Union

Used to combine followed users with the current user:

```python
user.following | {user_id}
```

### 6. List Comprehension

Used to filter posts:

```python
[
    p
    for p in reversed(self.posts.posts)
    if p.user_id in visible
]
```

### 7. Exception Handling

Used to reject invalid operations.

### 8. UTC Timestamps

Used to record when posts are created.

---

# 📈 Example Social Media Flow

The current application demonstrates the following scenario:

```text
Ava
User ID → 1

Noah
User ID → 2

        │
        ▼

Ava follows Noah

        │
        ▼

Noah creates a post

"Shipping my Python project today!"

        │
        ▼

Ava requests her feed

        │
        ▼

Feed checks:

Ava's posts       → Visible
Noah's posts      → Visible
Other users       → Not visible

        │
        ▼

Personalized Feed
```

This demonstrates the basic idea behind a social media feed.

---

# 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, explore new technologies, and maintain consistency through daily coding.

**Day 88** focuses on building a **Social Media Backend**, with an emphasis on **user relationships, follow functionality, post creation, personalized feeds, sets, dictionaries, lists, dataclasses, validation, service-based architecture, timestamps, and in-memory data management**.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍👥
