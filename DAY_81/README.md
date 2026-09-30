# 🚀 Day 81 - E-Commerce Backend System

Welcome to **Day 81** of my **100 Days, 100 Python Projects** challenge!

This project is a **CLI-based E-Commerce Backend System** built using **Python**. It simulates the core backend operations of an online shopping platform, including product listing, shopping cart creation, adding products to a cart, inventory validation, checkout, and order creation.

The project is designed using a **layered backend architecture** with separate modules for:

* API/request handling
* Business logic
* Data models
* Data storage/repository

The main purpose of this project is to gain practical experience with **backend development concepts, API design, object-oriented programming, data modeling, repository patterns, error handling, and e-commerce workflows**.

---

## 📌 Project Overview

An e-commerce backend is responsible for handling operations such as:

* Managing products
* Creating shopping carts
* Adding products to carts
* Checking product availability
* Validating inventory
* Processing checkout
* Creating orders
* Returning structured responses

This project simulates these operations without requiring an external database or web framework.

Instead, it uses an **in-memory repository** to store products, carts, and orders while the program is running.

The application provides API-like routes such as:

```text
GET  /api/products

POST /api/carts

POST /api/carts/{cart_id}/items

POST /api/orders/checkout/{cart_id}
```

Although this project runs through the command line, the `StoreAPI` class is designed to behave similarly to a small backend API layer.

---

## ✨ Features

* 🛒 Product listing
* 🧺 Shopping cart creation
* ➕ Add products to cart
* 🔢 Product quantity validation
* 📦 Inventory validation
* 💰 Automatic cart total calculation
* 🧾 Checkout processing
* 📋 Order creation
* 🆔 Unique Cart IDs
* 🆔 Unique Order IDs
* 🆔 Unique Request IDs
* ⏱️ UTC request timestamps
* 🚨 Custom backend error handling
* 📊 Structured API-like responses
* 💾 In-memory data storage
* 🧩 Layered project architecture
* 🖥️ CLI-based request/response simulation
* 📦 Dataclass-based data models
* 🔄 Repository pattern
* 🛡️ HTTP-style status codes

---

## 🏗️ Backend Architecture

The project follows a simple layered architecture:

```text
┌───────────────────────────┐
│       CLI / main81.py     │
│  Sends simulated requests │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│        StoreAPI           │
│ Request routing & response│
│       formatting          │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│       StoreService        │
│     Business logic        │
│ Cart / Checkout / Stock   │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│     StoreRepository       │
│    In-memory storage      │
│ Products / Carts / Orders │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│          Models           │
│ Product / Cart / Order    │
│        CartItem           │
└───────────────────────────┘
```

This separation makes the application easier to understand, maintain, and extend.

---

## 🔄 E-Commerce Workflow

The application follows this basic workflow:

```text
Start Application
       │
       ▼
List Products
       │
       ▼
Create Shopping Cart
       │
       ▼
Add Product to Cart
       │
       ▼
Validate Product
       │
       ▼
Validate Quantity
       │
       ▼
Check Inventory
       │
       ▼
Calculate Cart Total
       │
       ▼
Checkout
       │
       ▼
Reduce Product Stock
       │
       ▼
Create Order
       │
       ▼
Return Order Response
```

---

# 📡 API Endpoints

The project simulates four main API endpoints.

---

## 📦 1. Get Products

### Endpoint

```text
GET /api/products
```

This endpoint returns all available products.

Example response:

```json
{
  "status": 200,
  "request_id": "REQ-ABC12345",
  "timestamp": "2026-09-30T16:30:00+00:00",
  "data": {
    "products": [
      {
        "id": 101,
        "name": "Wireless Mouse",
        "price": 29.99,
        "stock": 12
      },
      {
        "id": 102,
        "name": "Mechanical Keyboard",
        "price": 79.99,
        "stock": 7
      },
      {
        "id": 103,
        "name": "USB-C Dock",
        "price": 119.0,
        "stock": 4
      }
    ]
  }
}
```

---

## 🛒 2. Create Cart

### Endpoint

```text
POST /api/carts
```

This creates a new empty shopping cart.

A unique cart ID is generated automatically.

Example:

```text
CART-8A12F4BC
```

The cart initially contains:

```json
{
  "cart_id": "CART-8A12F4BC",
  "items": [],
  "total": 0,
  "currency": "USD"
}
```

---

## ➕ 3. Add Product to Cart

### Endpoint

```text
POST /api/carts/{cart_id}/items
```

Example:

```text
POST /api/carts/CART-8A12F4BC/items
```

Request body:

```json
{
  "product_id": 102,
  "quantity": 2
}
```

The service checks:

1. Whether the cart exists
2. Whether the product exists
3. Whether quantity is at least 1
4. Whether enough inventory is available
5. Whether the product already exists in the cart

If the product already exists, its quantity is increased.

---

## 💳 4. Checkout

### Endpoint

```text
POST /api/orders/checkout/{cart_id}
```

Example:

```text
POST /api/orders/checkout/CART-8A12F4BC
```

During checkout, the system:

1. Finds the cart
2. Checks whether the cart contains items
3. Validates inventory again
4. Reduces product stock
5. Creates a new order
6. Stores the order
7. Returns the order details

Example order ID:

```text
ORD-52F91A8C
```

---

# 🧱 Project Components

The project is divided into four main Python files.

```text
main81.py
models.py
repository.py
services.py
```

Each file has a specific responsibility.

---

# 📄 main81.py

`main81.py` acts as the main application entry point.

It contains:

* `StoreAPI`
* `send()`
* `main()`

### StoreAPI

The `StoreAPI` class simulates a small web API.

```python
class StoreAPI:
```

It connects the API layer with the service layer.

The constructor creates:

```python
self.service = StoreService(StoreRepository())
```

This means:

```text
StoreAPI
   ↓
StoreService
   ↓
StoreRepository
```

---

## 🔀 Request Routing

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
    "/api/products"
)
```

The method checks the HTTP-style request and routes it to the appropriate service method.

---

## 🆔 Request ID

Every request receives a unique request ID.

```python
request_id = f"REQ-{uuid4().hex[:8].upper()}"
```

Example:

```text
REQ-A8F31C22
```

This is useful for identifying individual requests in backend systems.

---

## ⏱️ Request Timestamp

Every response contains a UTC timestamp.

```python
datetime.now(timezone.utc).isoformat()
```

Example:

```text
2026-09-30T16:30:21.452321+00:00
```

---

## 📦 Structured Response

The `_response()` method creates a consistent response format.

```python
{
    "status": status,
    "request_id": request_id,
    "timestamp": timestamp,
    "data": data
}
```

This provides a basic example of how backend APIs can return standardized responses.

---

# 📄 models.py

`models.py` contains the application's data models.

The project uses Python's `dataclasses` module.

The main models are:

```text
Product
CartItem
Cart
Order
```

---

## 📦 Product

The `Product` model represents a product in the store.

```python
@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
```

Example:

```text
ID:     102
Name:   Mechanical Keyboard
Price:  79.99
Stock:  7
```

The `to_dict()` method converts the dataclass into a dictionary.

---

## 🧺 CartItem

`CartItem` represents a product inside a shopping cart.

It contains:

```text
product_id
name
price
quantity
```

It also calculates the line total:

```python
self.price * self.quantity
```

For example:

```text
Price:    $79.99
Quantity: 2

Line Total: $159.98
```

---

## 🛒 Cart

The `Cart` model represents a customer's shopping cart.

It contains:

```text
id
items
```

The total is calculated automatically using:

```python
@property
def total(self):
```

The cart total is the sum of all item totals.

---

## 🧾 Order

The `Order` model represents a completed checkout.

It contains:

```text
order ID
cart ID
items
total
status
```

The default order status is:

```text
confirmed
```

---

# 📄 repository.py

`repository.py` contains the data storage layer.

The project intentionally uses an **in-memory repository** instead of a real database.

```python
class StoreRepository:
```

This keeps the project lightweight and allows the backend concepts to be demonstrated without database configuration.

---

## 📦 Product Storage

The repository starts with three sample products:

|  ID | Product             |   Price | Stock |
| --: | ------------------- | ------: | ----: |
| 101 | Wireless Mouse      |  $29.99 |    12 |
| 102 | Mechanical Keyboard |  $79.99 |     7 |
| 103 | USB-C Dock          | $119.00 |     4 |

These products are stored in a Python dictionary.

---

## 🛒 Cart Storage

Carts are stored using:

```python
self.carts: dict[str, Cart] = {}
```

The cart ID is used as the dictionary key.

---

## 🧾 Order Storage

Orders are stored using:

```python
self.orders: dict[str, Order] = {}
```

The order ID is used as the dictionary key.

---

## 🔍 Repository Operations

The repository provides methods for:

```text
list_products()
get_product()
save_cart()
get_cart()
save_order()
```

This keeps data-access logic separate from business logic.

---

# 📄 services.py

`services.py` contains the main business logic of the application.

It defines:

```text
StoreError
StoreService
```

---

# ⚙️ StoreService

The `StoreService` class handles operations such as:

* Listing products
* Creating carts
* Adding items
* Validating inventory
* Checkout
* Creating orders

---

## 📋 List Products

```python
def list_products(self):
```

This retrieves products from the repository and converts them into dictionaries.

---

## 🛒 Create Cart

```python
def create_cart(self):
```

A unique cart ID is generated using UUID.

Example:

```text
CART-7A93D4F1
```

The new cart is then saved in the repository.

---

## ➕ Add Item

```python
def add_item(self, cart_id, product_id, quantity):
```

This method performs several validations.

### Cart validation

```python
if not cart:
    raise StoreError(404, "Cart not found")
```

### Product validation

```python
if not product:
    raise StoreError(404, "Product not found")
```

### Quantity validation

```python
if quantity < 1:
    raise StoreError(400, "Quantity must be at least 1")
```

### Inventory validation

```python
if quantity > product.stock:
    raise StoreError(409, "Insufficient inventory")
```

These validations simulate common backend API validation rules.

---

# 📦 Inventory Management

The system checks product stock before adding an item to a cart.

For example:

```text
Available stock = 7
Requested quantity = 10
```

The request is rejected because the requested quantity exceeds available inventory.

The system returns:

```text
409 Insufficient inventory
```

---

# 💳 Checkout Processing

The `checkout()` method handles order creation.

Before completing checkout, the application verifies:

* Cart exists
* Cart is not empty
* Products still have sufficient stock

This second inventory check is important because inventory may have changed after an item was added to the cart.

---

## 📉 Updating Stock

After successful validation, product stock is reduced:

```python
product.stock -= item.quantity
```

For example:

```text
Before checkout:
Stock = 7

Purchased:
Quantity = 2

After checkout:
Stock = 5
```

---

# 🧾 Order Creation

After successful checkout, an `Order` object is created.

Example:

```text
Order ID: ORD-8F21A7BC
Cart ID:  CART-4C82D911
Status:   confirmed
Total:    $159.98
```

The order is then stored in the repository.

---

# 🚨 Error Handling

The project uses a custom exception:

```python
class StoreError(Exception):
```

This allows business errors to contain both:

```text
status
message
```

For example:

```python
StoreError(404, "Cart not found")
```

---

## HTTP-Style Status Codes

The project uses status codes similar to web APIs.

| Status | Meaning     | Example                    |
| -----: | ----------- | -------------------------- |
|    200 | Success     | Product listing            |
|    201 | Created     | Cart/order creation        |
|    400 | Bad Request | Invalid quantity           |
|    404 | Not Found   | Cart/product doesn't exist |
|    409 | Conflict    | Insufficient inventory     |

These codes are returned as part of the simulated API response.

---

# 🔐 Request/Response Simulation

Although this is not a real web server, the project simulates API communication through the `send()` function.

Example:

```python
send(
    api,
    "GET",
    "/api/products"
)
```

The application prints:

```text
REQUEST GET /api/products
```

and then:

```text
RESPONSE 200
```

followed by the JSON response.

This provides a simple way to understand how backend APIs process requests and return responses.

---

# 🖥️ Example Application Flow

When the program starts, the following operations are performed automatically:

### Step 1 — List Products

```text
GET /api/products
```

### Step 2 — Create Cart

```text
POST /api/carts
```

### Step 3 — Add Product

```text
POST /api/carts/{cart_id}/items
```

with:

```json
{
  "product_id": 102,
  "quantity": 2
}
```

### Step 4 — Checkout

```text
POST /api/orders/checkout/{cart_id}
```

The order is then created and the product inventory is reduced.

---

# 📊 Example Shopping Calculation

Suppose the customer purchases:

```text
Mechanical Keyboard
Price: $79.99
Quantity: 2
```

The calculation is:

```text
79.99 × 2 = 159.98
```

Therefore:

```text
Cart Total = $159.98
```

The generated order contains the same total.

---

# 📂 Project Structure

```text
DAY_81/

│
├── main81.py
├── models.py
├── repository.py
├── services.py
├── requirements.txt
└── README.md
 
```

### File Description

| File / Folder      | Purpose                                                  |
| ------------------ | -------------------------------------------------------- |
| `main81.py`        | Application entry point, API simulation and CLI workflow |
| `models.py`        | Defines Product, CartItem, Cart and Order models         |
| `repository.py`    | Provides in-memory data storage                          |
| `services.py`      | Contains business logic and validation                   |
| `requirements.txt` | Python dependencies                                      |
| `README.md`        | Project documentation                                    |

---

# 📦 requirements.txt

This project uses Python's standard library.

The main modules used are:

```text
json
datetime
uuid
dataclasses
```

Therefore, **no external Python packages are required**.

Your `requirements.txt` can simply contain:

```text
# No external dependencies required
```

The project uses only Python's built-in modules.

---

# ▶️ How to Run

## 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

---

## 2. Open the project folder

Open a terminal inside the `DAY_81` directory.

---

## 3. Run the application

```bash
python main81.py
```

The CLI simulation will start automatically.

---

# 🖥️ Example Output

The application will display requests and responses similar to:

```text
E-Commerce Backend System - CLI Simulation

REQUEST GET /api/products
RESPONSE 200
{
    ...
}

REQUEST POST /api/carts
RESPONSE 201
{
    ...
}

REQUEST POST /api/carts/CART-XXXXXXXX/items
{
    "product_id": 102,
    "quantity": 2
}
RESPONSE 200
{
    ...
}

REQUEST POST /api/orders/checkout/CART-XXXXXXXX
RESPONSE 201
{
    ...
}
```

The exact IDs and timestamps will be different each time because UUIDs and timestamps are generated dynamically.

---

# 🧩 Python Concepts Practiced

This project uses several important Python concepts.

### Object-Oriented Programming

Classes are used for:

```text
StoreAPI
StoreRepository
StoreService
StoreError
```

### Dataclasses

The application uses:

```python
@dataclass
```

for its data models.

### Type Hints

Examples include:

```python
dict[str, Cart]
list[CartItem]
```

### Properties

The cart total uses:

```python
@property
```

### Exception Handling

The API layer uses:

```python
try
except
```

to handle application errors.

### UUID Generation

Unique IDs are generated using:

```python
uuid4()
```

### JSON Formatting

The `json` module is used to display structured request data and responses.

### Dictionary Data Storage

Products, carts and orders are stored using Python dictionaries.

---

# 🏗️ Backend Concepts Practiced

This project focuses on several backend development concepts:

* API routing
* Request handling
* Response formatting
* HTTP-style status codes
* Service layer
* Repository layer
* Data models
* Business logic
* Input validation
* Error handling
* Inventory management
* Shopping cart workflow
* Checkout workflow
* Order creation
* Unique request IDs
* Timestamps
* In-memory storage
* Separation of concerns

---

# 🔍 Separation of Responsibilities

One of the important concepts practiced in this project is **separation of concerns**.

Instead of putting all the code into one file, the application separates responsibilities.

```text
main81.py
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

This structure makes the application easier to maintain and provides a foundation for expanding it into a larger backend application.

---

# 📚 Important Python Functions and Concepts

## UUID

```python
uuid4()
```

Used for generating unique identifiers.

---

## Dataclasses

```python
@dataclass
```

Used to create structured data models with less boilerplate code.

---

## asdict()

```python
asdict(self)
```

Converts dataclass objects into dictionaries.

---

## Dictionary Storage

```python
self.products = {}
self.carts = {}
self.orders = {}
```

Used to simulate persistent collections in memory.

---

## List Comprehension

Example:

```python
[product.to_dict() for product in self.repository.list_products()]
```

Used to convert product objects into dictionaries.

---

## Generator Expression

The application uses:

```python
next(
    (item for item in cart.items
     if item.product_id == product_id),
    None
)
```

to find an existing product in a cart.

---

## Exception Handling

The API catches application errors using:

```python
except StoreError as error:
```

and converts them into structured responses.

---

# ⚠️ Validation and Error Scenarios

The backend handles several invalid situations.

### Cart Does Not Exist

```text
404
Cart not found
```

### Product Does Not Exist

```text
404
Product not found
```

### Invalid Quantity

For example:

```json
{
    "product_id": 102,
    "quantity": 0
}
```

returns:

```text
400
Quantity must be at least 1
```

### Insufficient Inventory

If the customer requests more products than available:

```text
409
Insufficient inventory
```

### Empty Cart Checkout

Attempting to checkout an empty cart returns:

```text
400
Cart is empty
```

### Invalid Request Data

Invalid request values are handled by the API layer:

```text
400
Invalid request data
```

---

# 🗃️ Data Storage

This project currently uses **in-memory storage**.

That means:

```text
Program Starts
      ↓
Data Created in Memory
      ↓
Requests Process Data
      ↓
Program Ends
      ↓
Data Is Lost
```

No external database is currently required.

This keeps the project simple while demonstrating backend architecture and business logic.

---

# 🔮 Future Improvements

Possible enhancements for future versions include:

* 🗄️ Add SQLite/PostgreSQL database
* 🌐 Convert the simulated API into a real REST API
* ⚡ Add FastAPI or Flask
* 🔐 Add user authentication
* 👤 Add customer accounts
* 🔑 Add JWT authentication
* 🛍️ Add product creation/update/delete operations
* 🔎 Add product search
* 🏷️ Add product categories
* 💰 Add discount and coupon support
* 📦 Add advanced inventory management
* 💳 Add payment gateway integration
* 🚚 Add shipping and delivery management
* 📍 Add customer addresses
* 🧾 Add invoice generation
* 📊 Add admin dashboard
* 📝 Add order history
* 🔄 Add order cancellation
* 📈 Add sales analytics
* 🧪 Add automated unit tests
* 🔌 Add API documentation using Swagger/OpenAPI
* 🐳 Dockerize the backend
* ☁️ Deploy the backend to the cloud
* 🔒 Add authentication and authorization middleware
* 🧱 Add database migrations
* 📋 Add logging system
* 🚦 Add rate limiting
* 🔁 Add transaction handling

---

# 🧪 Testing Improvements

A future version can include automated tests for important backend scenarios.

For example:

```text
Test product listing
Test cart creation
Test adding valid product
Test invalid product
Test invalid quantity
Test insufficient inventory
Test empty cart checkout
Test successful checkout
Test stock reduction
Test order creation
```

A testing structure could look like:

```text
DAY_81/

├── main81.py
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

* How an e-commerce backend works
* How API-like request routing works
* How to structure a Python backend project
* How to separate API, service and repository layers
* How to create data models using dataclasses
* How to manage products and inventory
* How shopping carts work
* How cart totals can be calculated
* How checkout processing works
* How orders can be created
* How to validate user input
* How to handle backend errors
* How HTTP-style status codes can be used
* How unique IDs can be generated with UUID
* How timestamps can be added to responses
* How to simulate a database using dictionaries
* How business logic can be separated from data storage
* How structured JSON responses can be generated
* How backend workflows can be simulated through the CLI

---

# 💡 Key Takeaway

The main concept learned from this project is that a backend application should not place all its logic in one location.

Instead, responsibilities can be separated into layers:

```text
API Layer
    ↓
Business Logic Layer
    ↓
Repository / Data Layer
    ↓
Data Models
```

This makes the application easier to understand, test, maintain, and extend.

The current project uses an in-memory repository, but the same architecture can later be connected to a real database and web framework.

---

# 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to:

* Improve Python programming skills
* Strengthen problem-solving abilities
* Learn software development concepts
* Explore different Python libraries and technologies
* Practice writing structured and maintainable code
* Build practical projects
* Maintain consistency through daily coding

**Day 81** focuses on **Backend Development and E-Commerce System Design**, combining **Python classes, dataclasses, API-style routing, service-layer business logic, repository patterns, inventory validation, shopping carts, and checkout processing** into a practical backend simulation.

---

# 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🛒
