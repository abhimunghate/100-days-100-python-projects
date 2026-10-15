# 🗳️ Day 96 - Online Voting System

Welcome to **Day 96** of my **100 Days, 100 Python Projects** challenge!

This project is an **Online Voting System** built using Python. It demonstrates how an election system can manage candidates, validate voter eligibility, accept votes, prevent duplicate voting, calculate election results, and maintain an audit log of voting activity.

The application uses object-oriented programming, Python classes, dictionaries, sets, SHA-256 hashing, dataclasses, and timestamps to implement a simple voting management system. It simulates API-style requests and responses through formatted JSON output in the terminal.

The system includes a **Community Board Election** with two candidates: Ava Patel and Noah Smith. It processes votes from two eligible voter tokens, generates hashed voter receipts, displays election results, and shows an audit log of recorded voting events.

---

## 📌 Project Overview

An online voting system allows eligible voters to cast their votes electronically. Such systems need to validate voter eligibility, prevent duplicate submissions, count votes accurately, and maintain records of voting activity.

This project implements the basic backend logic of an online voting system without requiring a web server, graphical interface, or database.

The application follows a simple workflow:

- 🗳️ Initialize an election with registered candidates.
- 👥 Maintain a list of eligible voter tokens.
- 🔐 Validate voter eligibility before accepting a vote.
- 🚫 Prevent the same token from voting more than once.
- ✅ Validate whether the selected candidate exists.
- 📊 Update the vote count for the selected candidate.
- 🧾 Generate an audit event for each accepted vote.
- 🔒 Hash voter tokens using SHA-256 before recording them in the audit log.
- 🕒 Record the time of each accepted vote in UTC.
- 📈 Calculate election results and total votes.
- 📋 Display audit records in JSON format.

**Note:** This is a terminal-based backend simulation. It does not currently provide a live website, real HTTP endpoints, a database, voter authentication, or a production-ready election security system.

---

## ✨ Features

- 🗳️ Online voting backend simulation
- 🏛️ Election initialization and management
- 👥 Multiple candidates
- 🔑 Eligible voter token validation
- 🚫 Duplicate voting prevention
- ✅ Candidate validation
- 📊 Automatic vote counting
- 🧾 Voting audit log
- 🔐 SHA-256 hashing of voter tokens
- 🕒 UTC timestamp recording
- 🧮 Total vote calculation
- 📈 Election result reporting
- 📋 JSON-formatted terminal output
- ⚠️ Exception handling for invalid operations
- 🧩 Modular Python project structure
- 🐍 Python standard-library implementation

---

## 🏛️ Election Data Model

The `Election` dataclass in `elections.py` defines the structure of an election.

```python
from dataclasses import dataclass, field

@dataclass
class Election:
    id: int
    title: str
    candidates: dict[str, int]
    eligible_tokens: set[str]
    used_tokens: set[str] = field(default_factory=set)
```

### Attributes

| Attribute | Description |
|---|---|
| `id` | Unique identifier assigned to the election |
| `title` | Name of the election |
| `candidates` | Dictionary containing candidate names and vote counts |
| `eligible_tokens` | Set containing tokens authorized to vote |
| `used_tokens` | Set containing tokens that have already voted |

### Example Election

The application initializes an election using the following data:

```python
Election(
    101,
    "Community Board Election",
    {
        "Ava Patel": 0,
        "Noah Smith": 0
    },
    {
        "TOKEN-A1",
        "TOKEN-B2",
        "TOKEN-C3"
    }
)
```

The initial election contains:

- Election ID: `101`
- Election title: `Community Board Election`
- Candidate 1: Ava Patel
- Candidate 2: Noah Smith
- Eligible voter tokens: 3
- Initially submitted votes: 0

Both candidates begin with zero votes. The `used_tokens` set is initially empty because no votes have been submitted.

The candidate dictionary stores each candidate's name as a key and the number of votes received as its value.

---

## 🗂️ ElectionService Class

The `ElectionService` class in `elections.py` manages the available elections.

```python
class ElectionService:
    def __init__(self):
        self.elections = {
            101: Election(
                101,
                "Community Board Election",
                {"Ava Patel": 0, "Noah Smith": 0},
                {"TOKEN-A1", "TOKEN-B2", "TOKEN-C3"}
            )
        }

    def get(self, election_id):
        election = self.elections.get(election_id)

        if not election:
            raise LookupError("Election not found")

        return election
```

### Responsibilities

- Initialize the election data.
- Store election objects in a dictionary.
- Retrieve an election using its ID.
- Raise an exception when the requested election does not exist.

### The `get()` Method

The method accepts an election ID and searches the `elections` dictionary.

```python
election = self.elections.get(election_id)
```

If the election exists, the method returns its object. Otherwise, it raises a `LookupError`.

For example:

```python
election = elections.get(101)
print(election.title)
```

Expected output:

```text
Community Board Election
```

**Important:** The current implementation initializes only one election. The data structure can hold multiple elections, but no methods for creating, updating, or deleting elections have been implemented.

---

## 🔐 VotingService Class

The `VotingService` class in `voting.py` contains the main voting logic.

```python
class VotingService:
    def __init__(self, elections, audit):
        self.elections, self.audit = elections, audit
```

The constructor receives two dependencies:

- `elections` — the election service used to retrieve election information.
- `audit` — the audit logger used to record accepted votes.

This design keeps election management, voting operations, and audit logging in separate modules.

### The `cast()` Method

The `cast()` method accepts a vote for a particular election.

```python
def cast(self, election_id, token, candidate):
    election = self.elections.get(election_id)

    if token not in election.eligible_tokens:
        raise PermissionError("Invalid voter token")

    if token in election.used_tokens:
        raise ValueError("Vote already submitted")

    if candidate not in election.candidates:
        raise ValueError("Candidate not found")

    election.candidates[candidate] += 1
    election.used_tokens.add(token)

    event = self.audit.record(
        election_id,
        token,
        candidate
    )

    return {
        "message": "Vote accepted",
        "receipt": event["voter_hash"]
    }
```

### How It Works

1. Retrieve the election using its ID.
2. Check whether the voter token is eligible.
3. Check whether the token has already been used.
4. Verify that the selected candidate exists.
5. Increment the selected candidate's vote count.
6. Add the token to the set of used tokens.
7. Record the accepted vote in the audit log.
8. Return a success message and a hashed voter receipt.

The order of validation matters. The vote count is updated only after the token and candidate checks pass.

### Example Vote Submission

```python
voting.cast(
    101,
    "TOKEN-A1",
    "Ava Patel"
)
```

The token `TOKEN-A1` is eligible and has not previously voted. Ava Patel is a registered candidate, so the vote is accepted.

Example response:

```json
{
  "message": "Vote accepted",
  "receipt": "example_hash"
}
```

The receipt shown above is illustrative. The actual receipt is generated from the SHA-256 hash of the submitted token and uses the first 12 hexadecimal characters.

**Important:** The receipt is not a randomly generated or independently unique transaction ID. It is a shortened hash of the voter token.

---

## 🚫 Duplicate Voting Prevention

One of the important features of the project is preventing a voter token from submitting multiple votes in the same election.

The system checks:

```python
if token in election.used_tokens:
    raise ValueError("Vote already submitted")
```

After a vote is accepted, the token is added to the `used_tokens` set:

```python
election.used_tokens.add(token)
```

### Example Scenario

Suppose `TOKEN-A1` submits a vote for Ava Patel.

The token is initially eligible and unused, so the vote is accepted. The token is then added to `used_tokens`.

If the same token attempts to vote again, the system raises:

```text
ValueError: Vote already submitted
```

### Why a Set Is Used

A Python set stores unique values and supports efficient membership checks.

The system uses two sets for different purposes:

| Set | Purpose |
|---|---|
| `eligible_tokens` | Stores tokens permitted to vote |
| `used_tokens` | Stores tokens that have already voted |

This approach prevents duplicate voting by the same token within the in-memory election state.

**Limitation:** This is a basic application-level check. A production voting system would also need durable storage, concurrency controls, stronger voter authentication, and safeguards against simultaneous duplicate submissions.

---

## 🧾 AuditLog Class

The `AuditLog` class in `audit.py` records information about accepted votes.

```python
from datetime import datetime, timezone
from hashlib import sha256

class AuditLog:
    def __init__(self):
        self.events = []

    def record(self, election_id, token, candidate):
        event = {
            "election_id": election_id,
            "voter_hash": sha256(token.encode()).hexdigest()[:12],
            "candidate": candidate,
            "recorded_at": datetime.now(timezone.utc).isoformat()
        }

        self.events.append(event)
        return event
```

### Responsibilities

- Create an audit event for each accepted vote.
- Hash the voter token.
- Record the election ID.
- Store the selected candidate.
- Record the event timestamp in UTC.
- Append the event to the audit log.
- Return the created event to the voting service.

### Audit Event Structure

Each event contains four fields:

| Field | Description |
|---|---|
| `election_id` | ID of the election in which the vote was cast |
| `voter_hash` | First 12 hexadecimal characters of the token's SHA-256 hash |
| `candidate` | Candidate selected by the voter |
| `recorded_at` | UTC timestamp when the event was recorded |

Example structure:

```json
{
  "election_id": 101,
  "voter_hash": "example_hash",
  "candidate": "Ava Patel",
  "recorded_at": "2026-10-15T12:00:00+00:00"
}
```

The hash and timestamp above are illustrative. Actual hash values depend on the voter token, and timestamps depend on when the program runs.

### Important Audit Behavior

The `record()` method is called only after the vote has passed validation and the candidate's count has been incremented.

Consequently, the current audit log records accepted votes, not failed voting attempts.

The log is maintained in the `events` list and exists only while the application is running.

---

## 🔒 SHA-256 Hashing

The project uses Python's built-in `hashlib` module to hash voter tokens.

```python
sha256(token.encode()).hexdigest()[:12]
```

### How It Works

1. `token.encode()` converts the token string into bytes.
2. `sha256()` calculates the SHA-256 hash.
3. `hexdigest()` converts the hash into a hexadecimal string.
4. `[:12]` extracts the first 12 characters.

The shortened hash is stored in the audit log and returned as the voting receipt.

### Why Hashing Is Used

- Avoids directly storing the original token in the audit event.
- Allows the system to produce a compact receipt value.
- Demonstrates a basic cryptographic hashing technique.
- Helps introduce privacy-related considerations in application design.

**Security note:** SHA-256 is a hash function, not encryption. Because the token values in this demonstration are simple and predictable, a shortened hash does not guarantee voter anonymity. A production system should use carefully designed authentication and privacy mechanisms, and should not treat this receipt as proof of a secure or anonymous election.

The audit log also records the candidate selected, so it is not a fully anonymous voting record.

---

## 📈 Election Results

The `results()` method in `voting.py` returns the election title, candidate vote counts, and total number of votes.

```python
def results(self, election_id):
    election = self.elections.get(election_id)

    return {
        "title": election.title,
        "votes": election.candidates,
        "total_votes": sum(election.candidates.values())
    }
```

### How It Works

1. Retrieve the requested election.
2. Read the current candidate vote counts.
3. Calculate the total using `sum()`.
4. Return the results in a dictionary.

### Example Results

After Ava Patel and Noah Smith each receive one vote, the results are:

```json
{
  "title": "Community Board Election",
  "votes": {
    "Ava Patel": 1,
    "Noah Smith": 1
  },
  "total_votes": 2
}
```

The total vote count is calculated dynamically from the candidate vote counts.

**Note:** The current method does not independently verify that the election exists before accessing its attributes. An invalid election ID can therefore cause an attribute-related error rather than the `LookupError` raised by `ElectionService.get()`.

---

## 🧾 API-Style Request and Response Format

The `show()` helper function in `main96.py` prints each operation in a structured format.

```python
def show(action, data, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(data, indent=2)}"
    )
```

The function displays:

- The simulated request label.
- The response status label.
- The returned data formatted as JSON.

### Operations Demonstrated

| Operation | Status Label | Purpose |
|---|---:|---|
| `POST /api/votes` | `201` | Displays the first accepted vote |
| `POST /api/votes` | `201` | Displays the second accepted vote |
| `GET /api/elections/101/results` | `200` | Displays election results |
| `GET /api/audit` | `200` | Displays recorded audit events |

These labels resemble REST API operations, but they are printed by a Python function. The application does not create a real HTTP server or expose actual API endpoints.

The `201` status labels are manually supplied by the demonstration code; they are not HTTP responses returned by a server.

---

## 🔄 Complete Application Workflow

The application follows this workflow:

```text
Start Application
        |
        v
Initialize ElectionService
        |
        v
Initialize AuditLog
        |
        v
Initialize VotingService
        |
        v
Submit Vote for Ava Patel
        |
        v
Validate Election and Voter Token
        |
        v
Check Duplicate Voting
        |
        v
Validate Candidate
        |
        v
Increment Vote Count
        |
        v
Mark Token as Used
        |
        v
Record Audit Event
        |
        v
Return Voting Receipt
        |
        v
Submit Vote for Noah Smith
        |
        v
Repeat Validation and Recording
        |
        v
Display Election Results
        |
        v
Display Audit Log
        |
        v
End Application
```

This workflow demonstrates how election management, vote validation, vote counting, and audit logging work together.

---

## 🏗️ Project Architecture

The project contains four main Python modules.

```text
                 main96.py
                     |
          +----------+----------+
          |          |          |
          v          v          v
    elections.py  voting.py   audit.py
          |          |          |
          v          v          v
   ElectionService  VotingService  AuditLog
          |          |          |
          v          v          v
   Election Data  Vote Counting  Audit Events
   and Tokens     and Validation  and Hashing
```

### Module Responsibilities

- **`main96.py`** — initializes the services, submits sample votes, displays results, and prints the audit log.
- **`elections.py`** — defines the `Election` dataclass and manages election retrieval.
- **`voting.py`** — validates votes, prevents duplicate submissions, updates vote counts, and returns receipts.
- **`audit.py`** — hashes voter tokens and records accepted voting events with UTC timestamps.

This modular structure separates the responsibilities of election data management, voting operations, and audit logging, making the application easier to understand and extend.

---

## 🖥️ Example Voting Operations

The following operations are executed by `main96.py`.

### 1. Initialize the Services

```python
elections = ElectionService()
audit = AuditLog()
voting = VotingService(elections, audit)
```

The application initializes the election data, creates an empty audit log, and connects both services to the voting service.

### 2. Cast the First Vote

```python
show(
    "POST /api/votes",
    voting.cast(101, "TOKEN-A1", "Ava Patel"),
    201
)
```

The system validates `TOKEN-A1` and accepts the vote for Ava Patel.

### 3. Cast the Second Vote

```python
show(
    "POST /api/votes",
    voting.cast(101, "TOKEN-B2", "Noah Smith"),
    201
)
```

The system validates `TOKEN-B2` and accepts the vote for Noah Smith.

### 4. Display Election Results

```python
show(
    "GET /api/elections/101/results",
    voting.results(101)
)
```

The system displays the updated vote counts and the total number of accepted votes.

### 5. Display the Audit Log

```python
show(
    "GET /api/audit",
    {"events": audit.events}
)
```

The application displays both accepted voting events, including their election IDs, shortened voter-token hashes, selected candidates, and timestamps.

---

## 📊 Expected Results

After the application runs successfully, the election should contain the following vote counts:

| Candidate | Votes |
|---|---:|
| Ava Patel | 1 |
| Noah Smith | 1 |
| **Total votes** | **2** |

The results response should contain:

- Election title: `Community Board Election`
- Ava Patel's vote count: `1`
- Noah Smith's vote count: `1`
- Total votes: `2`

The audit log should contain two events:

- One event for the vote cast by `TOKEN-A1` for Ava Patel.
- One event for the vote cast by `TOKEN-B2` for Noah Smith.

The voter hashes and timestamps will vary according to the actual token values and execution time. The JSON field order for sets and other collections should not be relied upon where ordering is unspecified.

The application does not cast a vote using `TOKEN-C3`, so that token remains eligible and unused when the demonstration finishes.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement election management, vote validation, vote counting, hashing, and audit logging.

### 🏗️ Object-Oriented Programming

The project uses classes to organize related functionality:

- `Election` — represents election information.
- `ElectionService` — manages election retrieval.
- `VotingService` — processes votes and calculates results.
- `AuditLog` — records accepted voting events.

### 🧱 Dataclasses

The `@dataclass` decorator defines the election data structure.

```python
from dataclasses import dataclass, field
```

It automatically generates useful methods for the `Election` class and makes its data fields explicit.

The `field(default_factory=set)` expression creates a separate empty `used_tokens` set for each election instance.

### 🗂️ Dictionaries

Dictionaries store:

- Election records indexed by election ID.
- Candidate names and vote counts.
- Audit event fields.
- Voting response data.

### 🔢 Sets

Sets maintain eligible and used voter tokens, supporting membership checks and preventing duplicate token entries.

### 🔐 SHA-256 Hashing

The `hashlib` module generates shortened hexadecimal hashes of voter tokens for audit records and receipts.

### 🕒 Date and Time

The `datetime` module records the timestamp of each accepted vote.

```python
datetime.now(timezone.utc).isoformat()
```

The timestamp includes UTC timezone information.

### 🧾 JSON

The built-in `json` module converts Python dictionaries and lists into readable JSON output in the terminal.

### ⚠️ Exception Handling

The project uses exceptions to reject invalid operations:

- `LookupError` — election not found.
- `PermissionError` — voter token is not eligible.
- `ValueError` — token has already voted or candidate does not exist.

The current demonstration does not catch these exceptions, so an invalid operation will terminate the program unless handled by the caller.

---

## 📦 Requirements

This project uses Python's standard library and does not require external Python packages.

Check your Python installation:

```bash
python --version
```

### `requirements.txt`

```text
# No external dependencies required.
```

No database, API key, or third-party package installation is needed.

---

## 📂 Project Structure

```text
DAY_96/
│
├── main96.py
├── elections.py
├── voting.py
├── audit.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Purpose |
|---|---|
| `main96.py` | Entry point and sample voting workflow |
| `elections.py` | Election dataclass and election service |
| `voting.py` | Vote validation, vote counting, and result calculation |
| `audit.py` | Token hashing and audit event recording |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

No database or external data files are required. Election information and audit events are maintained in memory while the program runs.

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Ensure that Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal in the `DAY_96` folder.

```bash
cd DAY_96
```

### Step 3 — Check the Files

Make sure the following Python files are present:

```text
main96.py
elections.py
voting.py
audit.py
```

### Step 4 — Run the Application

Execute the following command:

```bash
python main96.py
```

### Step 5 — Review the Terminal Output

The terminal displays:

- The project title.
- The response for the first accepted vote.
- The response for the second accepted vote.
- The election results.
- The audit log containing both voting events.

### Step 6 — Verify the Results

Confirm that Ava Patel and Noah Smith each have one vote and that the total vote count is two.

The program does not create an output file. Its election results and audit records are printed directly in the terminal.

---

## ⚠️ Important Notes and Limitations

### 1. No Graphical Interface

The current application is terminal-based. It does not provide a voting website, mobile application, or graphical interface.

### 2. No Actual HTTP API

The request labels are simulated output. There is no web server, network communication, or actual REST API implementation.

### 3. No Database

Election data, used voter tokens, vote counts, and audit events are stored in memory. They are lost when the program terminates.

### 4. Basic Voter Authentication

Voter eligibility is determined by checking whether a supplied token exists in a predefined set. The application does not verify the real-world identity of the voter or authenticate users through a secure login system.

### 5. Duplicate Prevention Is In-Memory

The `used_tokens` set prevents repeated votes during the current execution. The protection does not persist between application runs.

### 6. No Concurrency Protection

The application does not implement transaction management or locking. A production system would need safeguards against simultaneous requests attempting to use the same token.

### 7. Limited Election Management

Only one election is initialized, and its candidates and eligible tokens are hardcoded. There are no dedicated methods for creating elections or managing candidates dynamically.

### 8. Hashing Does Not Guarantee Anonymity

The application stores a shortened SHA-256 hash of the token rather than the original token in each audit event. However, short or predictable tokens may be vulnerable to guessing, and the audit log directly associates each hashed token with a selected candidate.

### 9. No Cryptographic Vote Receipt Verification

The receipt is the first 12 hexadecimal characters of the token hash. It is not a signed receipt, and the application does not provide a separate verification mechanism.

### 10. Audit Log Is Not Tamper-Evident

The audit log is a normal Python list. The application does not use digital signatures, chained hashes, append-only storage, or external audit verification to detect tampering.

### 11. No Audit of Failed Attempts

Only accepted votes are recorded. Invalid tokens, duplicate attempts, and unknown candidates are not added to the audit log.

### 12. Limited Error Handling

The code raises exceptions for invalid operations but does not catch them in the main application. Invalid input can stop program execution.

### 13. No Election Closing or Result Finalization

The system does not implement election start and end times, a voting deadline, or a finalized-results state.

### 14. Not Suitable for Real Elections

This project is an educational demonstration of backend voting logic. Real elections require rigorous security design, privacy protections, independent auditing, reliability testing, legal compliance, and appropriate election infrastructure.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Python classes and object-oriented programming
- Dataclasses and default factories
- Dictionaries and sets
- Constructor methods and instance attributes
- Dependency injection through constructors
- Election data modeling
- Voter token validation
- Duplicate submission prevention
- Conditional validation
- Vote counting and aggregation
- SHA-256 hashing
- String encoding and hexadecimal representation
- UTC timestamps
- JSON serialization
- Audit logging
- Exception handling
- Modular programming
- Simulated REST-style request and response formatting
- Basic application security concepts
- Separation of responsibilities across modules

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Define election data using a dataclass.
- Initialize and retrieve election records.
- Store candidates and their vote counts in a dictionary.
- Use sets to track eligible and previously used voter tokens.
- Validate voter eligibility before accepting a vote.
- Prevent the same token from voting more than once.
- Validate candidate names.
- Increment vote counts after successful validation.
- Generate SHA-256 hashes from token strings.
- Record accepted voting events in an audit log.
- Generate timestamps in UTC.
- Return structured voting receipts.
- Calculate total votes using Python's `sum()` function.
- Display election results in JSON format.
- Separate election, voting, and audit responsibilities into different modules.
- Recognize the limitations of an in-memory voting system.
- Understand why privacy, authentication, persistence, and concurrency controls matter in voting applications.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🌐 Build a web interface using Flask, Django, or FastAPI.
- 🎨 Create a responsive voting interface using HTML, CSS, and JavaScript.
- 🔐 Implement secure voter authentication.
- 🪪 Add a voter registration and eligibility management system.
- 🗳️ Support creating and managing multiple elections.
- 👥 Allow administrators to add and manage candidates.
- 🗄️ Store election data in PostgreSQL or SQLite.
- 💾 Persist used voter tokens to prevent repeat voting across sessions.
- 🔒 Add transaction handling and concurrency protection.
- 🕒 Implement election opening and closing times.
- 📊 Build a dashboard for election results.
- 🧾 Improve audit logging and tamper detection.
- 🔏 Introduce a carefully designed receipt verification mechanism.
- 🛡️ Strengthen token generation, storage, and authentication.
- 🧪 Add automated unit and integration tests.
- ⚠️ Add robust error handling and input validation.
- 📈 Add election reports and downloadable result summaries.
- 🔍 Add monitoring and security event reporting.
- 🚀 Deploy the application in a controlled test environment.
- 🔐 Conduct independent security reviews before considering any real-world voting use.

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 96** focuses on **Online Voting System Development**, combining voter validation, duplicate voting prevention, candidate vote counting, SHA-256 hashing, and audit logging using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🗳️