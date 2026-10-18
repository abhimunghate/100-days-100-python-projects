# 🤖 Day 99 - AI-Powered Customer Service Chatbot

Welcome to **Day 99** of my **100 Days, 100 Python Projects** challenge!

This project is an **AI-Powered Customer Service Chatbot** built using Python. It demonstrates how a chatbot can identify customer requests, match messages with relevant knowledge-base articles, generate automated responses, and create support tickets when a request cannot be resolved.

The application uses Python classes, dictionaries, sets, regular expressions, keyword matching, and JSON serialization to implement a simple customer support system. It simulates chatbot interactions through formatted JSON output in the terminal.

The chatbot handles common customer service requests related to order tracking, returns, refunds, account access, and billing. When no knowledge-base article matches a customer's message, the system automatically creates a support ticket for further assistance.

**Note:** This is a rule-based chatbot simulation. Despite the project title, it does not currently use a trained machine learning model, a large language model (LLM), or an external AI API. It identifies customer intent using keyword matching.

---

## 📌 Project Overview

A customer service chatbot helps businesses respond to common customer questions automatically. It can provide information from a knowledge base and escalate unresolved requests to a support team.

This project demonstrates the backend logic of a customer support chatbot without requiring a web server or graphical user interface.

The application follows a simple workflow:

- 💬 Receive a customer message.
- 🔤 Convert the message to lowercase.
- 🔎 Extract words using regular expressions.
- 🧠 Compare message words with knowledge-base keywords.
- 🎯 Identify the best-matching customer intent.
- 📊 Calculate a simple keyword-based confidence score.
- 💡 Return the relevant knowledge-base answer.
- 🎫 Create a support ticket when no keywords match.
- 🕒 Record the ticket creation timestamp in UTC.
- 🧾 Display chatbot responses as formatted JSON.

The sample program tests three customer messages covering order tracking, a refund request, and a damaged device.

---

## ✨ Features

- 🤖 Automated customer support responses
- 💬 Customer message processing
- 📚 Centralized knowledge base
- 🎯 Rule-based intent detection
- 🔤 Text preprocessing with regular expressions
- 🔍 Keyword matching using sets
- 📊 Keyword-based confidence scoring
- 📦 Order tracking information
- 🔄 Return and refund assistance
- 🔐 Password reset guidance
- 💳 Billing and invoice assistance
- 🎫 Automatic support ticket creation for unmatched messages
- 🆔 Sequential ticket ID generation
- 🕒 UTC timestamp recording
- 📋 Open-ticket status tracking
- 🧾 JSON-formatted terminal output
- 🧩 Modular project structure
- 🐍 Python standard-library implementation

---

## 📚 Knowledge Base

The `knowledge_base.py` module contains predefined customer support articles.

The knowledge base is stored in a dictionary named `ARTICLES`. Each article contains an intent, a set of keywords, and a predefined response.

### Supported Customer Intents

| Intent | Example Keywords | Purpose |
|---|---|---|
| `order_status` | `order`, `status`, `tracking`, `shipment` | Provides order tracking instructions |
| `returns` | `return`, `refund`, `exchange` | Explains the return process |
| `password` | `password`, `login`, `account`, `reset` | Provides password reset guidance |
| `billing` | `charge`, `billing`, `payment`, `invoice` | Explains how to review charges and invoices |

### Example Knowledge-Base Entry

```python
"order_status": {
    "keywords": {
        "order",
        "status",
        "tracking",
        "shipment"
    },
    "answer": (
        "You can track your order from Orders > Track Package. "
        "Tracking updates may take up to 24 hours."
    )
}
```

When a customer's message contains one or more matching keywords, the chatbot can identify the corresponding article and return its answer.

### Predefined Responses

The knowledge base includes the following responses:

- **Order tracking:** Directs customers to `Orders > Track Package`.
- **Returns and refunds:** Explains the 30-day return policy and directs customers to `Orders > Return Item`.
- **Password reset:** Directs customers to the password recovery option on the sign-in page.
- **Billing:** Directs customers to `Account > Billing` for charges and invoices.

These are example support policies defined in the code, not verified policies of an actual business.

---

## 🧠 SupportChatbot Class

The `chatbot.py` module defines the `SupportChatbot` class, which processes customer messages and generates responses.

### Initialization

```python
class SupportChatbot:
    def __init__(self, articles, tickets):
        self.articles = articles
        self.tickets = tickets
```

The chatbot receives two dependencies:

- `articles` — the knowledge base containing supported intents and responses.
- `tickets` — a `TicketService` instance used to create tickets when requests cannot be resolved.

This design allows the chatbot to use a separate knowledge base and ticket-management service instead of combining all functionality in one class.

---

## 🔤 Message Preprocessing

Before matching a customer message with the knowledge base, the chatbot converts it to lowercase and extracts alphabetic words.

```python
words = set(
    re.findall(r"[a-z]+", message.lower())
)
```

### How It Works

1. `message.lower()` converts the message to lowercase.
2. `re.findall(r"[a-z]+", ...)` extracts sequences of English alphabetic characters.
3. `set()` stores the extracted words as a set, removing duplicates.

For example:

**Customer message:**

```text
Where can I track my order status?
```

**Extracted words:**

```python
{
    "where",
    "can",
    "i",
    "track",
    "my",
    "order",
    "status"
}
```

Using a set makes it convenient to calculate the overlap between the customer's words and the keywords defined in each knowledge-base article.

**Current limitation:** The regular expression handles only English letters from `a` to `z`. It does not perform advanced language understanding, stemming, synonym expansion, or multilingual processing.

---

## 🎯 Intent Detection and Keyword Matching

The chatbot compares the extracted message words with the keywords associated with each knowledge-base article.

```python
ranked = []

for intent, article in self.articles.items():
    ranked.append(
        (
            len(words & article["keywords"]),
            intent,
            article
        )
    )
```

The expression:

```python
words & article["keywords"]
```

uses set intersection to identify words present in both the customer's message and the article's keyword set.

The length of the intersection determines the keyword match score.

### Example

For the message:

```text
Where can I track my order status?
```

The `order_status` article contains the keywords `order` and `status` that match the extracted message words.

The message also contains `track`, but the article uses `tracking` rather than `track`. Since the current implementation performs exact keyword matching, these words do not match.

The chatbot calculates the score for every article and selects the entry with the highest score.

```python
score, intent, article = max(
    ranked,
    key=lambda item: item[0]
)
```

The selected article supplies the intent name and response text.

### Important Matching Behavior

- Matching is based on exact words after converting the message to lowercase.
- Duplicate words do not increase the score because the extracted words are stored in a set.
- The chatbot does not understand the meaning of a sentence beyond its keyword matches.
- If multiple articles have the same highest score, Python's `max()` returns the first matching maximum encountered in the iteration order.
- If all articles receive a score of zero, the chatbot creates a support ticket.

This makes the application simple and predictable, although it is less flexible than a trained natural language processing model.

---

## 📊 Confidence Score Calculation

The chatbot calculates a simple confidence value using:

```python
confidence = round(
    score / max(len(words), 1),
    2
)
```

Where:

- `score` is the number of distinct message words that match the selected article's keywords.
- `len(words)` is the number of distinct words extracted from the message.
- `max(len(words), 1)` prevents division by zero when the message contains no extracted alphabetic words.
- `round(..., 2)` rounds the result to two decimal places.

### Example

Suppose a message contains seven distinct words and two words match the selected article.

\[
\text{Confidence} = \frac{2}{7} \approx 0.29
\]

The returned confidence value would be `0.29`.

**Important:** This value is a keyword-overlap ratio, not a statistically calibrated AI confidence score. It should not be interpreted as a verified probability that the chatbot has correctly understood the customer.

---

## 💬 Generating Chatbot Responses

The `reply()` method is responsible for processing a customer message and returning the chatbot's response.

When a matching article is found, the chatbot returns a dictionary containing:

| Field | Description |
|---|---|
| `intent` | The selected knowledge-base intent |
| `confidence` | The calculated keyword-overlap ratio |
| `reply` | The predefined answer from the selected article |
| `escalated` | `False` when the chatbot returns a knowledge-base answer |

### Example Response Structure

```json
{
  "intent": "order_status",
  "confidence": 0.29,
  "reply": "You can track your order from Orders > Track Package. Tracking updates may take up to 24 hours.",
  "escalated": false
}
```

The confidence shown is illustrative for a message with seven distinct extracted words and two matching keywords. The exact result depends on the input message.

The chatbot returns the selected article's answer without generating new text dynamically.

---

## 🎫 Automatic Support Ticket Creation

When no knowledge-base article matches the customer's message, the chatbot escalates the request by creating a support ticket.

```python
if score == 0:
    ticket = self.tickets.create(
        message,
        "No matching knowledge article"
    )

    return {
        "intent": "unknown",
        "confidence": 0,
        "reply": (
            "I could not resolve that request, "
            "so I created a support ticket."
        ),
        "escalated": True,
        "ticket": ticket
    }
```

### When Does Escalation Occur?

Escalation occurs when the highest keyword match score is zero.

For example, a message such as:

```text
The mobile application keeps freezing.
```

does not match the keywords in the predefined knowledge base. The chatbot therefore creates a support ticket.

### Escalation Response Fields

| Field | Description |
|---|---|
| `intent` | Set to `unknown` |
| `confidence` | Set to `0` |
| `reply` | Explains that a support ticket was created |
| `escalated` | Set to `True` |
| `ticket` | Contains the newly created ticket record |

This provides a fallback mechanism for requests that cannot be answered using the available articles.

**Note:** The three messages in the current `main99.py` example all have matching keywords, so the sample run does not demonstrate the ticket-escalation branch. That branch can be tested by supplying a message with no matching knowledge-base keywords.

---

## 🗂️ TicketService Class

The `tickets.py` module defines the `TicketService` class, which manages support tickets created by the chatbot.

### Ticket Service Implementation

```python
from datetime import datetime, timezone

class TicketService:
    def __init__(self):
        self.tickets = []

    def create(self, message, reason):
        ticket = {
            "ticket_id": (
                f"TKT-{len(self.tickets)+1:04}"
            ),
            "message": message,
            "reason": reason,
            "status": "open",
            "created_at": (
                datetime.now(timezone.utc).isoformat()
            )
        }

        self.tickets.append(ticket)
        return ticket
```

### Ticket Fields

| Field | Description |
|---|---|
| `ticket_id` | Sequential ticket identifier |
| `message` | Original customer message |
| `reason` | Explanation for ticket creation |
| `status` | Initial ticket status, set to `open` |
| `created_at` | Ticket creation timestamp in UTC |

### Ticket ID Generation

Ticket identifiers are generated using:

```python
f"TKT-{len(self.tickets)+1:04}"
```

For example:

- First ticket: `TKT-0001`
- Second ticket: `TKT-0002`
- Third ticket: `TKT-0003`

The identifier is based on the current number of tickets in memory.

### Timestamp Handling

The application uses:

```python
datetime.now(timezone.utc).isoformat()
```

This records the ticket creation time as an ISO-formatted UTC timestamp with timezone information.

The exact timestamp changes whenever a ticket is created.

### Ticket Lifecycle

The current implementation assigns every new ticket the status `open`.

It does not yet implement ticket assignment, priority levels, replies from support agents, status updates, or ticket closure.

---

## 🧪 Sample Customer Interactions

The main program sends three customer messages to the chatbot.

### 1. Order Tracking Request

**Customer message:**

```text
Where can I track my order status?
```

The chatbot matches the `order` and `status` keywords in the `order_status` article.

Expected intent:

```text
order_status
```

Expected response:

```text
You can track your order from Orders > Track Package. Tracking updates may take up to 24 hours.
```

### 2. Return and Refund Request

**Customer message:**

```text
I need to return an item for a refund.
```

The chatbot matches the `return` and `refund` keywords in the `returns` article.

Expected intent:

```text
returns
```

Expected response:

```text
Returns are accepted within 30 days. Start a return from Orders > Return Item.
```

### 3. Damaged Device Report

**Customer message:**

```text
My device arrived with a cracked screen.
```

The message contains no keywords that match the current knowledge base.

Expected intent:

```text
unknown
```

Expected behavior:

- Create a support ticket.
- Assign a sequential ticket ID.
- Record the original message.
- Set the reason to `No matching knowledge article`.
- Set the ticket status to `open`.
- Record the creation timestamp in UTC.
- Return a response indicating that the request was escalated.

The exact ticket timestamp and other time-dependent values vary with each run.

---

## 🧾 Terminal Output Format

The application uses the `show()` function in `main99.py` to display chatbot interactions.

```python
def show(message, data):
    print(
        f"\nCUSTOMER {message}\n"
        f"BOT RESPONSE\n"
        f"{json.dumps(data, indent=2)}"
    )
```

The function displays the original customer message and the chatbot response as formatted JSON.

Unlike an HTTP API, this helper does not return an HTTP status code. It simply prints the customer message and response data.

The three sample interactions appear in this order:

1. Order tracking
2. Return and refund
3. Damaged device

The first two messages match existing articles, while the third triggers support ticket creation.

---

## 🔄 Complete Application Workflow

```text
Start Application
        |
        v
Initialize TicketService
        |
        v
Load Knowledge Base
        |
        v
Initialize SupportChatbot
        |
        v
Receive Customer Message
        |
        v
Convert Message to Lowercase
        |
        v
Extract Unique Words
        |
        v
Compare Words with Article Keywords
        |
        v
Calculate Match Scores
        |
        v
Select Highest-Scoring Article
        |
        v
     Score > 0?
       /    \
     Yes     No
      |       |
      v       v
 Return      Create Support
 Article     Ticket
 Answer       |
      |       v
      |    Return Escalation
      |    Response and Ticket
      |       |
      +---+---+
          |
          v
    Display JSON Output
```

The application separates message processing, knowledge-base data, and ticket creation into independent modules.

---

## 🏗️ Project Architecture

The project contains four Python modules.

```text
                 main99.py
                     |
          +----------+----------+
          |                     |
          v                     v
      chatbot.py          knowledge_base.py
          |
          v
    Intent Detection
          |
          v
    Keyword Matching
          |
     +----+----+
     |         |
     v         v
Knowledge   No Matching
  Match      Article
     |         |
     v         v
  Return    tickets.py
  Answer        |
     |          v
     |      Create Ticket
     |          |
     +-----+----+
           |
           v
      JSON Output
```

### Module Responsibilities

- **`main99.py`** — entry point; initializes the services, submits sample customer messages, and displays responses.
- **`knowledge_base.py`** — defines supported intents, matching keywords, and predefined customer support answers.
- **`chatbot.py`** — preprocesses messages, identifies intents, calculates match scores, and handles escalation.
- **`tickets.py`** — creates and stores support tickets with identifiers, reasons, statuses, and timestamps.

This modular design makes it easier to add new support topics or extend ticket-management functionality.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement message processing, intent detection, response selection, and ticket management.

### 🔤 Regular Expressions

The `re` module extracts alphabetic words from customer messages.

```python
import re
```

### 🗂️ Dictionaries

Dictionaries store knowledge-base articles, chatbot responses, and ticket information.

### 🔍 Sets

Sets store article keywords and unique words extracted from customer messages. Set intersection makes keyword matching straightforward.

### 🕒 Date and Time

The `datetime` module generates UTC timestamps for support tickets.

```python
from datetime import datetime, timezone
```

### 🧮 Built-in Functions

The project uses:

- `len()` to count matching keywords and existing tickets.
- `max()` to select the highest-scoring article.
- `round()` to round the confidence ratio.
- `set()` to remove duplicate message words.
- `re.findall()` to extract words from messages.

### 🧾 JSON Serialization

The `json` module converts response dictionaries into readable terminal output.

### 🏗️ Object-Oriented Programming

The project uses `SupportChatbot` and `TicketService` classes to separate chatbot processing from ticket creation.

### 📦 Standard Library

All implemented functionality uses Python's standard library. No third-party packages are required.

---

## 📦 Requirements

This project uses Python's standard library and does not require any external Python packages.

### Check Python Installation

```bash
python --version
```

Python 3.7 or later supports the syntax used in this project, including f-strings and the date/time functionality.

### `requirements.txt`

```text
# No external dependencies required.
```

---

## 📂 Project Structure

```text
DAY_99/
│
├── main99.py
├── chatbot.py
├── knowledge_base.py
├── tickets.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Purpose |
|---|---|
| `main99.py` | Main entry point and sample chatbot interactions |
| `chatbot.py` | Message processing, keyword matching, and response generation |
| `knowledge_base.py` | Predefined support articles, keywords, and answers |
| `tickets.py` | Support ticket creation and timestamp generation |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Ensure Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal inside your `DAY_99` folder.

```bash
cd DAY_99
```

### Step 3 — Check the Project Files

Make sure the following Python files are present:

```text
main99.py
chatbot.py
knowledge_base.py
tickets.py
```

### Step 4 — Run the Application

Execute:

```bash
python main99.py
```

### Step 5 — Review the Output

The terminal displays:

- The application title.
- The three customer messages.
- The detected intent for each message.
- The keyword-based confidence value.
- The chatbot's response.
- Whether the request was escalated.
- Ticket details when a request cannot be matched.

No database setup, API key, external dependency installation, or server configuration is required.

---

## ⚠️ Important Notes and Limitations

### 1. Rule-Based Intent Detection

The chatbot relies on exact keyword matching rather than machine learning or a large language model. It cannot reliably understand intent when customers use unfamiliar wording.

### 2. Limited Knowledge Base

Only four predefined intents are supported: order status, returns, password assistance, and billing.

### 3. Exact Keyword Matching

The chatbot does not automatically recognize synonyms or related word forms.

For example, the keyword `tracking` does not match `track`, and `password` does not automatically match `passcode`.

### 4. Simple Confidence Calculation

The confidence value measures keyword overlap relative to the number of unique words. It is not a calibrated probability of correctness.

### 5. Ticket Escalation Depends on Matching

A ticket is created only when no article receives a positive keyword match. A weak or irrelevant match can therefore produce an automated answer instead of escalation.

### 6. No Persistent Storage

Knowledge-base data is defined in Python, and support tickets are stored in a list. Tickets disappear when the program exits.

### 7. No Live Customer Support Integration

The chatbot does not connect to a real order-management system, payment gateway, email service, or customer support platform. Its responses are predefined examples.

### 8. No Authentication or Personalization

The current version does not identify customers, retrieve personal order details, or access customer account information.

### 9. No Ticket Management Workflow

Tickets are created with an `open` status, but there is no functionality for assigning agents, responding to tickets, changing priority, or closing requests.

### 10. No Actual AI Model

Although the project is titled an AI-powered chatbot, the implementation currently uses a rule-based approach. A future version could integrate NLP, intent classification, or a language model for more flexible responses.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Python classes and object-oriented programming
- Dictionaries and nested data structures
- Sets and set intersection
- Regular expressions
- Text preprocessing
- Keyword-based intent classification
- Scoring and ranking
- Conditional logic
- `max()` with a custom key
- Confidence-ratio calculations
- Exception-free fallback handling
- Sequential ID generation
- UTC timestamps
- ISO date/time formatting
- JSON serialization
- Modular application architecture
- Separation of concerns
- Automated support ticket creation
- Customer support workflow design

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Design a knowledge base for customer support.
- Organize intents, keywords, and predefined responses.
- Preprocess customer messages using regular expressions.
- Extract unique words from text.
- Match customer messages against predefined keywords.
- Rank knowledge-base articles based on match scores.
- Calculate a simple keyword-overlap confidence value.
- Return structured chatbot responses.
- Handle requests that cannot be matched.
- Create support tickets automatically.
- Generate sequential ticket identifiers.
- Record ticket timestamps in UTC.
- Format chatbot responses as JSON.
- Separate chatbot logic, knowledge-base data, and ticket management.
- Build the foundation of a customer service automation system.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🧠 Integrate a trained NLP intent-classification model.
- 💬 Use an LLM to generate more natural responses.
- 🔤 Add stemming, lemmatization, and synonym handling.
- 🌐 Build a web interface using Flask or Django.
- 🎨 Create a desktop chatbot interface using Tkinter.
- 🗄️ Store tickets and conversations in SQLite or PostgreSQL.
- 🔐 Add customer authentication and secure account access.
- 📦 Integrate a real order-tracking system.
- 💳 Connect to a billing and payment support service.
- 🎫 Add ticket priorities, assignment, replies, and closure.
- 📧 Send ticket confirmation emails.
- 📚 Allow knowledge-base articles to be added and updated dynamically.
- 🌍 Support multiple languages.
- 🧪 Add automated unit tests for intent matching and ticket creation.
- 📊 Build an analytics dashboard for customer queries.
- 🛡️ Add safeguards to avoid exposing sensitive customer information.
- 🚀 Deploy the chatbot as a live web application.

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 99** focuses on **Customer Support Chatbot Development**, combining keyword-based intent detection, knowledge-base responses, confidence scoring, and automatic support ticket creation using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🤖