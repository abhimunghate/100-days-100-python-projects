# 🚀 Day 86 - Chat Application

Welcome to **Day 86** of my **100 Days, 100 Python Projects** challenge!

This project is a **simple Chat Application backend simulation** built using **Python**. It demonstrates how a basic messaging system can create conversations, manage participants, send messages, and retrieve conversation history.

The project focuses on practicing **Object-Oriented Programming, Dataclasses, UUID generation, service-based architecture, in-memory data storage, validation, permissions, timestamps, and message management**.

---

## 📌 Project Overview

A chat application allows users to communicate with each other by creating conversations and exchanging messages.

This project implements a simplified backend-style chat system where users can:

* 👥 Create conversations
* 🧑‍🤝‍🧑 Add multiple participants
* 💬 Send messages
* 👤 Validate message senders
* 📝 Store message text
* 🕐 Record message timestamps
* 🔢 Generate unique conversation IDs
* 🔢 Generate message IDs
* 📜 Maintain conversation history
* 🚫 Prevent unauthorized users from sending messages
* ⚠️ Prevent empty messages
* 📦 Store conversations and messages in memory
* 📄 Display structured JSON-style responses

The application runs through the command line and simulates the basic workflow of a messaging backend.

---

## ✨ Features

* 🖥️ CLI-based Chat Application
* 💬 Conversation creation
* 👥 Participant management
* 🧑‍🤝‍🧑 Multiple participants
* 📩 Send messages
* 👤 Sender validation
* 🔐 Participant-based permission checking
* 🚫 Empty message validation
* 🕐 UTC message timestamps
* 🔢 Automatic conversation ID generation
* 🔢 Automatic message ID generation
* 📜 Conversation history
* 🗂️ In-memory conversation storage
* 📦 Dataclass-based conversation model
* 📄 JSON-formatted terminal output
* 🧩 Separate conversation and message services

---

## 🛠️ Technologies Used

* **Python 3**
* **Dataclasses**
* **UUID**
* **Datetime**
* **JSON**
* **Object-Oriented Programming**
* **In-Memory Data Storage**

### 🐍 Python

Python is used to implement the complete chat application logic.

The project uses:

* Classes
* Objects
* Functions
* Lists
* Dictionaries
* Dataclasses
* Exceptions
* List comprehensions
* Formatted strings
* Generator expressions

### 📦 Dataclasses

The `Conversation` model uses Python's `dataclass` decorator.

```python
@dataclass
class Conversation:
    id: str
    participants: list[str]
    messages: list = field(default_factory=list)
```

Dataclasses make it easier to create structured conversation objects.

### 🔑 UUID

The `uuid4()` function is used to generate unique conversation IDs.

```python
uuid4().hex[:8].upper()
```

This produces IDs such as:

```text
CHAT-A1B2C3D4
```

### 🕐 Datetime

The `datetime` module is used to record when messages are sent.

```python
datetime.now(timezone.utc).isoformat()
```

This stores the message timestamp using UTC.

### 📄 JSON

The `json` module is used to display structured responses in a readable format.

```python
json.dumps(result, indent=2)
```

This gives the command-line output an API-like appearance.

---

## 📂 Project Structure

```text
DAY_86/
│
├── main86.py
├── conversations.py
├── messages.py
├── requirements.txt
└── README.md
```

### 📄 File Description

| File / Folder      | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| `main86.py`        | Main application workflow                                |
| `conversations.py` | Contains the conversation model and conversation service |
| `messages.py`      | Handles sending and validating messages                  |
| `requirements.txt` | Lists project dependencies                               |
| `README.md`        | Project documentation                                    |

---

## 📦 requirements.txt

This project uses only Python's standard library.

```text
# No external dependencies required
```

No external packages need to be installed.

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

Open a terminal inside the `DAY_86` folder.

---

### 3. Run the application

```bash
python main86.py
```

The application will create a conversation, send two messages, and display the conversation history.

---

# 🔄 Application Workflow

The application follows this workflow:

```text
                    Start
                      │
                      ▼
            Create Conversation
                      │
                      ▼
              Add Participants
                      │
                      ▼
               Send Message
                      │
                      ▼
              Validate Sender
                      │
                      ▼
             Validate Message
                      │
                      ▼
             Store Message
                      │
                      ▼
               Send Reply
                      │
                      ▼
            Get Conversation
                      │
                      ▼
                     End
```

The workflow is implemented in `main86.py`.

```python
conversations = ConversationService()
messages = MessageService(conversations)

chat = conversations.create(["Ava", "Noah"])

show(
    "CREATE CONVERSATION",
    chat.to_dict(),
    201
)

show(
    "SEND MESSAGE",
    messages.send(
        chat.id,
        "Ava",
        "Are we still meeting at 3 PM?"
    ),
    201
)

show(
    "SEND MESSAGE",
    messages.send(
        chat.id,
        "Noah",
        "Yes, see you then."
    ),
    201
)

show(
    "GET HISTORY",
    chat.to_dict()
)
```

---

# 👥 Creating a Conversation

A conversation is created using the `ConversationService`.

```python
chat = conversations.create(
    ["Ava", "Noah"]
)
```

The `create()` method receives a list of participants.

```python
def create(self, participants):
```

Each conversation contains:

* Conversation ID
* Participants
* Messages

Example:

```json
{
    "id": "CHAT-A1B2C3D4",
    "participants": [
        "Ava",
        "Noah"
    ],
    "messages": []
}
```

---

# 🧑‍🤝‍🧑 Participant Validation

The application requires at least two unique participants.

```python
if len(set(participants)) < 2:
    raise ValueError(
        "Two participants are required"
    )
```

The use of `set()` ensures duplicate participant names are not counted multiple times.

For example:

```text
["Ava", "Ava"]
```

is invalid because there is only one unique participant.

While:

```text
["Ava", "Noah"]
```

is valid.

---

# 🔑 Unique Conversation IDs

Every conversation receives a unique ID using `uuid4()`.

```python
f"CHAT-{uuid4().hex[:8].upper()}"
```

Example:

```text
CHAT-7F2A91BC
```

This provides a unique identifier for each conversation.

---

# 💬 Sending Messages

Messages are handled by the `MessageService`.

```python
messages = MessageService(conversations)
```

A message can be sent using:

```python
messages.send(
    chat.id,
    "Ava",
    "Are we still meeting at 3 PM?"
)
```

The method receives:

| Parameter         | Description                            |
| ----------------- | -------------------------------------- |
| `conversation_id` | ID of the target conversation          |
| `sender`          | Name of the person sending the message |
| `text`            | Message content                        |

---

# 🔐 Sender Validation

Only participants of a conversation are allowed to send messages.

The application checks:

```python
if sender not in chat.participants:
    raise PermissionError(
        "Sender is not a participant"
    )
```

For example, if the conversation contains:

```text
Ava
Noah
```

then:

```text
Ava  → ✅ Allowed
Noah → ✅ Allowed
Leo  → ❌ Not allowed
```

This demonstrates a basic permission rule.

---

# 🚫 Empty Message Validation

The application prevents users from sending empty messages.

```python
if not text.strip():
    raise ValueError(
        "Message cannot be empty"
    )
```

This also prevents messages containing only spaces.

For example:

```text
"Hello"      → ✅ Valid
"How are you?" → ✅ Valid
""           → ❌ Invalid
"    "       → ❌ Invalid
```

---

# 🔢 Automatic Message IDs

Every message receives an automatically generated ID.

```python
f"MSG-{len(chat.messages)+1:04}"
```

Example:

```text
MSG-0001
MSG-0002
MSG-0003
MSG-0004
```

The numbering is maintained separately within each conversation.

---

# 🕐 Message Timestamps

Each message records the time it was sent.

```python
datetime.now(
    timezone.utc
).isoformat()
```

The timestamp is stored in UTC.

Example:

```json
{
    "sent_at": "2026-10-05T06:45:21.123456+00:00"
}
```

Using UTC makes timestamps consistent regardless of the user's local timezone.

---

# 📜 Conversation History

All messages are stored inside the conversation.

The `Conversation` model contains:

```python
messages: list = field(
    default_factory=list
)
```

When a message is sent:

```python
chat.messages.append(message)
```

Therefore, the conversation keeps a history of all messages sent during the current application session.

Example:

```json
{
    "id": "CHAT-A1B2C3D4",
    "participants": [
        "Ava",
        "Noah"
    ],
    "messages": [
        {
            "id": "MSG-0001",
            "sender": "Ava",
            "text": "Are we still meeting at 3 PM?",
            "sent_at": "2026-10-05T06:45:21+00:00"
        },
        {
            "id": "MSG-0002",
            "sender": "Noah",
            "text": "Yes, see you then.",
            "sent_at": "2026-10-05T06:45:25+00:00"
        }
    ]
}
```

---

# 🔍 Retrieving a Conversation

The `get()` method is used to retrieve a conversation using its ID.

```python
def get(self, conversation_id):
    chat = self.conversations.get(conversation_id)

    if not chat:
        raise LookupError(
            "Conversation not found"
        )

    return chat
```

If the conversation does not exist, a `LookupError` is raised.

---

# 🗂️ In-Memory Conversation Storage

Conversations are stored using a Python dictionary.

```python
self.conversations = {}
```

When a new conversation is created:

```python
self.conversations[chat.id] = chat
```

Messages are stored inside each conversation object.

This provides a simple storage system without requiring a database.

> ⚠️ Since the project uses in-memory storage, conversations and messages are lost when the program terminates.

---

# 🔄 Converting Conversation Data to Dictionaries

The `Conversation` class provides a `to_dict()` method:

```python
def to_dict(self):
    return asdict(self)
```

The `asdict()` function converts the dataclass object into a dictionary.

This makes the conversation data easy to display as JSON.

---

# 🖥️ CLI Response Format

The `show()` function creates an API-style response format.

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
REQUEST CREATE CONVERSATION
RESPONSE 201

{
    "id": "CHAT-A1B2C3D4",
    "participants": [
        "Ava",
        "Noah"
    ],
    "messages": []
}
```

A sent message produces:

```text
REQUEST SEND MESSAGE
RESPONSE 201

{
    "id": "MSG-0001",
    "sender": "Ava",
    "text": "Are we still meeting at 3 PM?",
    "sent_at": "..."
}
```

---

# 🧩 Service-Based Architecture

The project separates conversation management and message management into different services.

```text
                 ┌──────────────────┐
                 │    main86.py     │
                 │   Application    │
                 │     Workflow     │
                 └────────┬─────────┘
                          │
              ┌───────────▼───────────┐
              │  ConversationService  │
              │                       │
              │ Create Conversation   │
              │ Get Conversation      │
              └───────────┬───────────┘
                          │
                          │
              ┌───────────▼───────────┐
              │    MessageService     │
              │                       │
              │ Send Message          │
              │ Validate Sender       │
              │ Validate Message      │
              │ Store Message         │
              └───────────────────────┘
```

This separation makes the application easier to maintain and extend.

---

# 🧩 Libraries and Functions Practiced

## Python `dataclasses`

| Function / Feature | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `@dataclass`       | Creates structured conversation objects      |
| `field()`          | Creates a default empty message list         |
| `asdict()`         | Converts dataclass objects into dictionaries |

---

## Python `uuid`

| Function  | Purpose                                    |
| --------- | ------------------------------------------ |
| `uuid4()` | Generates a unique conversation identifier |

Example:

```python
uuid4().hex[:8].upper()
```

---

## Python `datetime`

| Function / Feature | Purpose                            |
| ------------------ | ---------------------------------- |
| `datetime.now()`   | Gets the current date and time     |
| `timezone.utc`     | Uses UTC timezone                  |
| `isoformat()`      | Converts timestamp into ISO format |

---

## Python `json`

| Function       | Purpose                                       |
| -------------- | --------------------------------------------- |
| `json.dumps()` | Converts Python data into formatted JSON text |

---

## Python `set`

The `set()` function is used to identify unique participants.

```python
len(set(participants))
```

---

# 📚 Concepts Practiced

This project helped practice:

* 🐍 Python Programming
* 🧱 Object-Oriented Programming
* 📦 Dataclasses
* 👥 Participant Management
* 💬 Message Management
* 📜 Conversation History
* 🔑 UUID Generation
* 🔢 Automatic ID Generation
* 🕐 Date and Time Handling
* 🌍 UTC Timestamps
* 📋 Lists
* 🗂️ Dictionaries
* 🚫 Input Validation
* 🔐 Permission Validation
* ⚠️ Exception Handling
* 📄 JSON Formatting
* 🧩 Service-Based Architecture
* 🔗 Class Dependency
* 🗃️ In-Memory Storage
* 🏗️ Backend Application Design

---

# 🎯 Learning Outcome

This project helped me understand:

* How to design a basic chat application backend
* How to create conversations between participants
* How to manage messages within a conversation
* How to use dataclasses for structured data
* How to generate unique identifiers using UUIDs
* How to generate sequential message IDs
* How to validate conversation participants
* How to implement sender authorization
* How to prevent empty messages
* How to record UTC timestamps
* How to maintain conversation history
* How to separate logic using service classes
* How to store application data in memory
* How to convert objects into dictionaries
* How to format application responses as JSON
* How backend messaging logic can be simulated using the command line

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🌐 Build a REST API using Flask or FastAPI
* 🗄️ Add database support using SQLite, MySQL, or PostgreSQL
* 👤 Add user registration and login
* 🔐 Add authentication and authorization
* 💬 Add one-to-one and group chats
* 👥 Add user profiles
* 🟢 Add online/offline status
* ⌨️ Add typing indicators
* 📩 Add message delivery status
* 👁️ Add read receipts
* 🗑️ Add message deletion
* ✏️ Add message editing
* 📎 Add file and image sharing
* 🖼️ Add media messages
* 🔔 Add notifications
* 🔎 Add message search
* 📌 Add message reactions
* ⭐ Add message pinning
* 🗂️ Add chat archiving
* 🔄 Add real-time messaging using WebSockets
* 🌐 Build a web-based chat interface
* ⚛️ Build a React frontend
* 📱 Build a mobile application
* 🧪 Add automated tests
* 📚 Add API documentation
* 🐳 Dockerize the application
* ☁️ Deploy the application to the cloud

---

# 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, explore new technologies, and maintain consistency through daily coding.

**Day 86** focuses on building a **Chat Application**, with an emphasis on **conversation management, message handling, participant validation, permissions, timestamps, service-based architecture, and in-memory data management**.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍💬
