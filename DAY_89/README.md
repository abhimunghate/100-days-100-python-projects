# 🚀 Day 89 - Event Booking App

Welcome to **Day 89** of my **100 Days, 100 Python Projects** challenge!

This project is a **simple Event Booking App** built using **Python**. It simulates the basic functionality of an event reservation system where users can view an event, book available seats, cancel a booking, and check the remaining seat availability.

The project focuses on practicing **Object-Oriented Programming, Dataclasses, lists, dictionaries, properties, validation, service-based architecture, booking management, seat availability calculation, cancellation handling, and in-memory data management**.

---

## 📌 Project Overview

An event booking system allows customers to reserve seats for events and manage their bookings.

This project implements a simplified event booking backend where users can:

* 🎫 View an available event
* 📋 Display event information
* 🏢 Display the event venue
* 💺 Check available seats
* 📝 Create a booking
* 👤 Store customer information
* 🔢 Reserve multiple seats
* 🚫 Prevent invalid seat quantities
* ⚠️ Prevent bookings when insufficient seats are available
* ❌ Cancel an existing booking
* 🔄 Automatically restore cancelled seats
* 📊 Calculate current seat availability
* 🗂️ Store event and booking data in memory
* 📄 Display structured JSON-style responses
* 🧩 Separate event and booking responsibilities into services

The application runs through the command line and simulates basic event-booking operations.

---

## ✨ Features

* 🖥️ CLI-based Event Booking App
* 🎫 Event management
* 📋 Event information retrieval
* 🏢 Venue information
* 💺 Seat capacity management
* 📝 Booking creation
* 👤 Customer information
* 🔢 Multiple-seat booking
* 🚫 Minimum seat validation
* ⚠️ Seat availability validation
* ❌ Booking cancellation
* 🔄 Automatic seat restoration after cancellation
* 📊 Dynamic availability calculation
* 🆔 Unique booking IDs
* 📦 Dataclass-based event model
* 📋 List-based booking storage
* 📄 Dictionary-based booking records
* 🗂️ In-memory event storage
* 📄 JSON-formatted terminal output
* 🧩 Separate event and booking services
* ⚠️ Exception-based validation

---

## 🛠️ Technologies Used

* **Python 3**
* **Dataclasses**
* **Lists**
* **Dictionaries**
* **Properties**
* **JSON**
* **Object-Oriented Programming**
* **In-Memory Data Storage**

### 🐍 Python

Python is used to implement the complete event booking system.

The project uses:

* Classes
* Objects
* Functions
* Dictionaries
* Lists
* Dataclasses
* Properties
* Exceptions
* List comprehensions
* Generator expressions
* Formatted strings

---

## 📦 Dataclasses

The project uses Python's `dataclass` decorator to represent an event.

```python
@dataclass
class Event:
    id: int
    name: str
    venue: str
    capacity: int
    bookings: list = field(default_factory=list)
```

The dataclass provides a structured way to store event information.

Each event contains:

| Field      | Description             |
| ---------- | ----------------------- |
| `id`       | Unique event ID         |
| `name`     | Event name              |
| `venue`    | Event location          |
| `capacity` | Maximum number of seats |
| `bookings` | List of event bookings  |

---

# 📂 Project Structure

```text
DAY_89/
│
├── main89.py
├── bookings.py
├── events.py
├── requirements.txt
└── README.md
```

### 📄 File Description

| File / Folder      | Purpose                                                        |
| ------------------ | -------------------------------------------------------------- |
| `main89.py`        | Main application workflow                                      |
| `bookings.py`      | Contains `BookingService` for creating and cancelling bookings |
| `events.py`        | Contains the `Event` model and `EventCatalog`                  |
| `requirements.txt` | Lists project dependencies                                     |
| `README.md`        | Project documentation                                          |

---

# 📦 requirements.txt

This project uses only Python's standard library.

```text
# No external dependencies required
```

No additional packages are required to run the application.

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

Open a terminal inside the `DAY_89` folder.

---

## 3. Run the application

```bash
python main89.py
```

The application will:

1. Load the available event.
2. Display event information.
3. Create a booking for 3 seats.
4. Cancel the booking.
5. Display the updated seat availability.

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
                Load Event
                      │
                      ▼
              Get Event Details
                      │
                      ▼
              Create Booking
                      │
                      ▼
           Validate Seat Quantity
                      │
                      ▼
         Check Available Seats
                      │
                      ▼
             Confirm Booking
                      │
                      ▼
            Cancel Booking
                      │
                      ▼
          Update Booking Status
                      │
                      ▼
          Calculate Availability
                      │
                      ▼
                    End
```

The workflow is implemented in `main89.py`.

```python
events = EventCatalog()
bookings = BookingService(events)

event = events.get(101)

show(
    "GET EVENT",
    {
        "id": event.id,
        "name": event.name,
        "available_seats": event.available_seats
    }
)

booking = bookings.create(
    101,
    "Mia Chen",
    3
)

show(
    "CREATE BOOKING",
    booking,
    201
)

show(
    "CANCEL BOOKING",
    bookings.cancel(
        101,
        booking["id"]
    )
)

show(
    "GET AVAILABILITY",
    {
        "available_seats":
        event.available_seats
    }
)
```

---

# 🎫 Event Details

The `EventCatalog` manages the available events.

A sample event is created when the service is initialized:

```python
self.events = {
    101: Event(
        101,
        "Python Developer Conference",
        "Austin Convention Center",
        50
    )
}
```

The current event contains:

| Field      | Value                         |
| ---------- | ----------------------------- |
| Event ID   | `101`                         |
| Event Name | `Python Developer Conference` |
| Venue      | `Austin Convention Center`    |
| Capacity   | `50 seats`                    |

Initially, the event has no confirmed bookings.

Therefore:

```text
Total Capacity → 50
Confirmed Seats → 0
Available Seats → 50
```

---

# 🔎 Getting an Event

The `EventCatalog` provides a `get()` method for retrieving an event.

```python
def get(self, event_id):
    event = self.events.get(event_id)

    if not event:
        raise LookupError("Event not found")

    return event
```

The application retrieves event `101`:

```python
event = events.get(101)
```

If the event does not exist, the application raises:

```text
LookupError: Event not found
```

This provides basic event validation.

---

# 📋 Displaying Event Information

The event information is displayed using the `show()` function.

```python
show(
    "GET EVENT",
    {
        "id": event.id,
        "name": event.name,
        "available_seats": event.available_seats
    }
)
```

The response contains:

* Event ID
* Event name
* Current available seats

Example:

```text
REQUEST GET EVENT
RESPONSE 200

{
  "id": 101,
  "name": "Python Developer Conference",
  "available_seats": 50
}
```

---

# 📝 Creating a Booking

Bookings are managed by the `BookingService`.

A booking is created using:

```python
booking = bookings.create(
    101,
    "Mia Chen",
    3
)
```

The method receives:

| Parameter  | Description                |
| ---------- | -------------------------- |
| `event_id` | ID of the event            |
| `customer` | Customer name              |
| `seats`    | Number of seats to reserve |

For the current example:

```text
Event ID → 101
Customer → Mia Chen
Seats → 3
```

---

# 💺 Seat Validation

The booking service first checks whether at least one seat has been requested.

```python
if seats < 1:
    raise ValueError(
        "At least one seat is required"
    )
```

Examples:

```text
3 seats   → ✅ Valid
1 seat    → ✅ Valid
0 seats   → ❌ Invalid
-2 seats  → ❌ Invalid
```

This prevents meaningless or invalid bookings.

---

# ⚠️ Checking Seat Availability

Before confirming a booking, the system checks whether enough seats are available.

```python
if seats > event.available_seats:
    raise ValueError(
        "Not enough seats available"
    )
```

For example:

```text
Available Seats → 50
Requested Seats → 3

3 <= 50
```

Therefore, the booking is allowed.

If a customer requests:

```text
Available Seats → 2
Requested Seats → 5
```

the booking is rejected.

```text
ValueError: Not enough seats available
```

This prevents the event from exceeding its capacity.

---

# 🆔 Booking ID Generation

Every booking receives a unique sequential booking ID.

The ID is generated using:

```python
f"BOOK-{len(event.bookings)+1:04}"
```

The first booking becomes:

```text
BOOK-0001
```

The next booking becomes:

```text
BOOK-0002
```

Then:

```text
BOOK-0003
```

This provides a simple identifier for bookings within the event.

---

# 📦 Booking Structure

A booking is stored as a dictionary:

```python
booking = {
    "id": f"BOOK-{len(event.bookings)+1:04}",
    "customer": customer,
    "seats": seats,
    "status": "confirmed"
}
```

A sample booking looks like:

```json
{
    "id": "BOOK-0001",
    "customer": "Mia Chen",
    "seats": 3,
    "status": "confirmed"
}
```

The booking contains:

| Field      | Description               |
| ---------- | ------------------------- |
| `id`       | Unique booking identifier |
| `customer` | Customer name             |
| `seats`    | Number of booked seats    |
| `status`   | Current booking status    |

---

# ✅ Confirming a Booking

After validation, the booking is added to the event's booking list:

```python
event.bookings.append(booking)
```

The booking status is initially:

```text
confirmed
```

The booking response is then displayed with status code `201`.

```text
REQUEST CREATE BOOKING
RESPONSE 201
```

---

# 📊 Seat Availability Calculation

One of the most important parts of the project is the `available_seats` property.

```python
@property
def available_seats(self):
    return self.capacity - sum(
        b["seats"]
        for b in self.bookings
        if b["status"] == "confirmed"
    )
```

The available seats are calculated dynamically.

The formula is:

```text
Available Seats =
Total Capacity - Confirmed Booked Seats
```

For the current event:

```text
Capacity = 50
Booked Seats = 3

Available Seats = 50 - 3
                 = 47
```

---

# 🧮 Calculating Confirmed Seats

The system uses a generator expression:

```python
sum(
    b["seats"]
    for b in self.bookings
    if b["status"] == "confirmed"
)
```

This adds the number of seats from only confirmed bookings.

For example:

```text
Booking 1 → 3 seats → confirmed
Booking 2 → 5 seats → confirmed
Booking 3 → 2 seats → cancelled
```

The calculation becomes:

```text
3 + 5
= 8 confirmed seats
```

The cancelled booking does not contribute to the occupied-seat count.

Therefore:

```text
Capacity = 50
Confirmed Seats = 8

Available Seats = 42
```

---

# ❌ Cancelling a Booking

A booking can be cancelled using:

```python
bookings.cancel(
    101,
    booking["id"]
)
```

The cancellation method first retrieves the event:

```python
event = self.events.get(event_id)
```

It then searches for the booking:

```python
booking = next(
    (
        b
        for b in event.bookings
        if b["id"] == booking_id
    ),
    None
)
```

If the booking does not exist:

```python
raise LookupError(
    "Booking not found"
)
```

---

# 🔄 Booking Status

When a booking is cancelled, its status changes from:

```text
confirmed
```

to:

```text
cancelled
```

The code is:

```python
booking["status"] = "cancelled"
```

The booking itself remains stored in the event's booking list, but it is no longer considered a confirmed booking.

---

# ♻️ Restoring Available Seats

Cancelled bookings are automatically excluded from the availability calculation.

For example:

```text
Before Cancellation

Capacity        → 50
Booked Seats    → 3
Available Seats → 47
```

After cancelling the 3-seat booking:

```text
Capacity        → 50
Confirmed Seats → 0
Available Seats → 50
```

This happens automatically because `available_seats` only counts bookings where:

```python
b["status"] == "confirmed"
```

Therefore, cancellation effectively releases the reserved seats.

---

# 📊 Booking Lifecycle

The booking follows this lifecycle:

```text
                 Create Booking
                       │
                       ▼
                  confirmed
                       │
                       │
                       ▼
                 Cancel Booking
                       │
                       ▼
                  cancelled
```

A confirmed booking contributes to occupied seats.

A cancelled booking does not contribute to occupied seats.

---

# 🔄 Complete Booking Example

The current application demonstrates:

```text
Event Capacity
      │
      ▼
    50 seats
      │
      ▼
Customer: Mia Chen
Requests: 3 seats
      │
      ▼
Availability Check
      │
      ▼
   3 ≤ 50
      │
      ▼
Booking Confirmed
      │
      ▼
Available Seats = 47
      │
      ▼
Booking Cancelled
      │
      ▼
Available Seats = 50
```

This demonstrates the complete basic booking lifecycle.

---

# 🖥️ CLI Response Format

The `show()` function creates an API-style response format:

```python
def show(action, result, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(result, indent=2)}"
    )
```

Although the project does not expose a real HTTP API, the output resembles backend API responses.

Example:

```text
REQUEST GET EVENT
RESPONSE 200
{
  "id": 101,
  "name": "Python Developer Conference",
  "available_seats": 50
}
```

Booking creation:

```text
REQUEST CREATE BOOKING
RESPONSE 201
{
  "id": "BOOK-0001",
  "customer": "Mia Chen",
  "seats": 3,
  "status": "confirmed"
}
```

Cancellation:

```text
REQUEST CANCEL BOOKING
RESPONSE 200
{
  "id": "BOOK-0001",
  "customer": "Mia Chen",
  "seats": 3,
  "status": "cancelled"
}
```

Final availability:

```text
REQUEST GET AVAILABILITY
RESPONSE 200
{
  "available_seats": 50
}
```

---

# 🧩 Service-Based Architecture

The project separates event management and booking operations into different services.

```text
                    ┌─────────────────────┐
                    │      main89.py      │
                    │  Application Flow   │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │  EventCatalog   │        │ BookingService  │
        │                 │        │                 │
        │ Store Events    │◄───────│ Create Booking  │
        │ Get Event       │        │ Cancel Booking  │
        │ Event Details   │        │ Validate Seats  │
        └─────────────────┘        └─────────────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                       In-Memory Data
```

### `EventCatalog`

Responsible for:

* Event storage
* Event retrieval
* Event validation

### `BookingService`

Responsible for:

* Creating bookings
* Validating seat quantities
* Checking availability
* Generating booking IDs
* Cancelling bookings
* Updating booking status

### `Event`

Responsible for:

* Event information
* Capacity
* Booking collection
* Dynamic seat availability

This separation makes the application easier to understand and extend.

---

# 🗂️ In-Memory Data Storage

The current application uses in-memory data structures.

Events are stored in a dictionary:

```python
self.events = {
    101: Event(
        101,
        "Python Developer Conference",
        "Austin Convention Center",
        50
    )
}
```

Bookings are stored inside each event:

```python
bookings: list = field(
    default_factory=list
)
```

No external database is used.

The project does not currently use:

* MySQL
* PostgreSQL
* SQLite
* MongoDB
* Redis

> ⚠️ Since the application uses in-memory storage, all events and bookings are lost when the program terminates.

---

# 🔍 Finding a Booking

The application searches for a booking using Python's `next()` function and a generator expression.

```python
booking = next(
    (
        b
        for b in event.bookings
        if b["id"] == booking_id
    ),
    None
)
```

The search:

1. Goes through the event's bookings.
2. Checks each booking ID.
3. Returns the matching booking.
4. Returns `None` if no booking is found.

This provides a compact way to search a list of dictionaries.

---

# ⚠️ Error Handling

The project uses Python exceptions for invalid operations.

### Event Not Found

```python
if not event:
    raise LookupError(
        "Event not found"
    )
```

### Invalid Seat Quantity

```python
if seats < 1:
    raise ValueError(
        "At least one seat is required"
    )
```

### Insufficient Seats

```python
if seats > event.available_seats:
    raise ValueError(
        "Not enough seats available"
    )
```

### Booking Not Found

```python
if not booking:
    raise LookupError(
        "Booking not found"
    )
```

These validations help maintain the consistency of the booking system.

---

# 🧩 Libraries and Functions Practiced

## Python `dataclasses`

| Feature      | Purpose                              |
| ------------ | ------------------------------------ |
| `@dataclass` | Creates the structured `Event` model |
| `field()`    | Creates a default booking list       |

Example:

```python
@dataclass
class Event:
    id: int
    name: str
    venue: str
    capacity: int
    bookings: list = field(
        default_factory=list
    )
```

---

## Python `property`

The `@property` decorator is used to calculate available seats dynamically.

```python
@property
def available_seats(self):
    return self.capacity - sum(
        b["seats"]
        for b in self.bookings
        if b["status"] == "confirmed"
    )
```

This allows the value to be accessed like an attribute:

```python
event.available_seats
```

instead of calling it like a function.

---

## Python `list`

Lists are used to store bookings.

```python
bookings: list = field(
    default_factory=list
)
```

New bookings are added using:

```python
event.bookings.append(booking)
```

---

## Python `dict`

Dictionaries are used for:

* Event storage
* Booking information
* JSON-style responses

Example:

```python
{
    "id": "BOOK-0001",
    "customer": "Mia Chen",
    "seats": 3,
    "status": "confirmed"
}
```

---

## Python `sum()`

The `sum()` function calculates the total number of confirmed seats.

```python
sum(
    b["seats"]
    for b in self.bookings
    if b["status"] == "confirmed"
)
```

---

## Python `next()`

The `next()` function is used to find a specific booking.

```python
next(
    (
        b
        for b in event.bookings
        if b["id"] == booking_id
    ),
    None
)
```

---

## Python `json`

The `json` module formats application responses.

```python
json.dumps(
    result,
    indent=2
)
```

---

# 📚 Concepts Practiced

This project helped practice:

* 🐍 Python Programming
* 🧱 Object-Oriented Programming
* 📦 Dataclasses
* 🎫 Event Management
* 📝 Booking Management
* 👤 Customer Information
* 💺 Seat Reservation
* 📊 Capacity Management
* ❌ Booking Cancellation
* 🔄 Booking Status
* 🧮 Dynamic Calculations
* 📋 Lists
* 🗂️ Dictionaries
* 🔍 Searching with `next()`
* ➕ `sum()` Function
* 🏷️ `@property`
* 📄 JSON Formatting
* ⚠️ Input Validation
* 🚨 Exception Handling
* 🧩 Service-Based Architecture
* 🗃️ In-Memory Storage
* 🆔 Sequential ID Generation
* 🏗️ Basic Backend Design
* 🔄 State Management
* 📈 Availability Tracking

---

# 🎯 Learning Outcome

This project helped me understand:

* How to build a basic event booking system using Python
* How to represent events using dataclasses
* How to store events using dictionaries
* How to store bookings using lists
* How to create and manage bookings
* How to validate the number of requested seats
* How to prevent bookings from exceeding event capacity
* How to generate sequential booking IDs
* How to maintain booking status
* How to cancel an existing booking
* How cancelled bookings can automatically release seats
* How to calculate available seats dynamically
* How Python properties can be used for calculated values
* How to search lists using `next()`
* How generator expressions can simplify calculations
* How to separate event and booking responsibilities using services
* How to use exceptions for invalid operations
* How to format backend-style responses using JSON
* How to simulate an event-booking backend without a database
* How to manage application state using in-memory data structures

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🌐 Build a REST API using Flask or FastAPI
* 🗄️ Add SQLite, MySQL, or PostgreSQL database support
* 👤 Add user registration and authentication
* 🔐 Add secure customer authentication
* 🎫 Add multiple events
* ➕ Add dynamic event creation
* ✏️ Add event editing
* 🗑️ Add event deletion
* 🏢 Add multiple venues
* 📅 Add event dates and times
* 🗓️ Add event calendar functionality
* 💺 Add seat categories such as VIP, Premium, and Regular
* 💰 Add ticket pricing
* 💳 Add online payment integration
* 🎟️ Generate digital tickets
* 📧 Send booking confirmation emails
* 📱 Send booking notifications
* 🔄 Add booking modification
* 🧾 Generate invoices
* 👥 Add customer booking history
* 🔎 Add event search
* 🏷️ Add event categories
* 📊 Add booking statistics
* 📈 Add revenue reports
* 🚫 Automatically close sold-out events
* ⏰ Add booking deadlines
* 🪑 Implement seat-level selection
* 📱 Build a web interface
* ⚛️ Build a React frontend
* 🔄 Add real-time seat availability
* 📊 Add an admin dashboard
* 🧪 Add unit and integration tests
* 📚 Add API documentation
* 🐳 Dockerize the application
* ☁️ Deploy the application to the cloud

---

# 🖥️ Example Application Output

The application produces output similar to:

```text
Day 89 - Event Booking App

REQUEST GET EVENT
RESPONSE 200
{
  "id": 101,
  "name": "Python Developer Conference",
  "available_seats": 50
}

REQUEST CREATE BOOKING
RESPONSE 201
{
  "id": "BOOK-0001",
  "customer": "Mia Chen",
  "seats": 3,
  "status": "confirmed"
}

REQUEST CANCEL BOOKING
RESPONSE 200
{
  "id": "BOOK-0001",
  "customer": "Mia Chen",
  "seats": 3,
  "status": "cancelled"
}

REQUEST GET AVAILABILITY
RESPONSE 200
{
  "available_seats": 50
}
```

The exact output remains the same except for values that depend on runtime state.

---

# 📈 Seat Availability Example

The event starts with:

```text
Capacity → 50
```

After booking 3 seats:

```text
Capacity        → 50
Confirmed Seats → 3
Available Seats → 47
```

After cancelling the booking:

```text
Capacity        → 50
Confirmed Seats → 0
Available Seats → 50
```

This demonstrates how the system dynamically calculates availability based on booking status.

---

# 🏗️ Backend Design

The project follows a simple service-based backend design:

```text
                    Event Booking App
                           │
                           ▼
                      main89.py
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       EventCatalog               BookingService
              │                         │
              ▼                         ▼
        Event Details             Create Booking
        Event Lookup              Cancel Booking
        Event Capacity            Validate Seats
              │                         │
              └────────────┬────────────┘
                           ▼
                    In-Memory Storage
```

### Event Layer

Handles:

```text
Event information
Event lookup
Event capacity
Booking collection
Seat availability
```

### Booking Layer

Handles:

```text
Booking creation
Seat validation
Booking IDs
Booking cancellation
Booking status
```

This design provides a simple foundation that can later be converted into a real web-based event booking API.

---

# 🧠 Key Python Concepts

Some of the most important Python concepts practiced in this project are:

### 1. Dataclasses

Used to create a structured `Event` model.

### 2. Lists

Used to maintain bookings for an event.

### 3. Dictionaries

Used for event storage and booking records.

### 4. Properties

Used to calculate available seats dynamically.

```python
@property
def available_seats(self):
    ...
```

### 5. Generator Expressions

Used to calculate confirmed seats:

```python
sum(
    b["seats"]
    for b in self.bookings
    if b["status"] == "confirmed"
)
```

### 6. `next()`

Used to locate a booking by its ID.

### 7. Exception Handling

Used to reject invalid bookings and missing resources.

### 8. State Management

Booking status changes from:

```text
confirmed → cancelled
```

and this state affects seat availability.

---

# 🔁 Booking State Management

The project demonstrates simple state management.

A newly created booking has:

```text
status = confirmed
```

After cancellation:

```text
status = cancelled
```

The event's availability calculation uses this state:

```python
if b["status"] == "confirmed"
```

Therefore:

```text
Confirmed Booking
       │
       ▼
Consumes Seats
```

while:

```text
Cancelled Booking
       │
       ▼
Does Not Consume Seats
```

This is an important concept for real-world reservation systems.

---

# 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, explore new technologies, and maintain consistency through daily coding.

**Day 89** focuses on building an **Event Booking App**, with an emphasis on **event management, seat reservation, booking creation, booking cancellation, availability calculation, validation, dataclasses, lists, dictionaries, properties, service-based architecture, state management, and in-memory data storage**.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🎫
