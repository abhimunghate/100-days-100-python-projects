# 🍽️ Day 97 - Restaurant Ordering System

Welcome to **Day 97** of my **100 Days, 100 Python Projects** challenge!

This project is a **Restaurant Ordering System** built using Python. It demonstrates how a restaurant can manage menu items, create customer orders, add food items with quantities, calculate order totals, and track an order through different kitchen preparation stages.

The application uses Python dataclasses, object-oriented programming, dictionaries, lists, properties, and class methods to implement a simple restaurant ordering backend. It simulates API-style requests and responses through formatted JSON output in the terminal.

The system includes three menu items: Margherita Pizza, Caesar Salad, and Chocolate Cake. The sample workflow creates an order for **Table 12**, adds two pizzas and one chocolate cake, calculates the total bill, and advances the order through the kitchen workflow until it is marked as served.

---

## 📌 Project Overview

A restaurant ordering system helps manage menu items, customer orders, item quantities, billing, and kitchen preparation statuses.

This project demonstrates the backend logic of a restaurant ordering application without requiring a web server or graphical user interface.

The application follows a simple workflow:

- 📋 Load the restaurant menu.
- 🍕 Display available menu items and their details.
- 🧾 Create a new order for a table.
- ➕ Add menu items to the order.
- 🔢 Specify the quantity of each item.
- 💰 Calculate the order total automatically.
- 🔄 Track the order through kitchen status transitions.
- 👨‍🍳 Update the order as it progresses through preparation.
- ✅ Mark the order as served.
- 📊 Display order details and status in JSON format.

**Note:** This is a terminal-based backend simulation. It does not currently provide a live website, interactive restaurant interface, database, payment gateway, or real HTTP endpoints.

---

## ✨ Features

- 🍽️ Restaurant ordering backend simulation
- 📋 Predefined restaurant menu
- 🍕 Multiple menu items and categories
- 💵 Item prices and availability tracking
- 🧾 Order creation with unique order IDs
- 🪑 Table-based order assignment
- ➕ Add multiple items to an order
- 🔢 Quantity validation
- 💰 Automatic bill calculation
- 🧮 Dynamic order total using a property
- 👨‍🍳 Kitchen workflow management
- 🔄 Order status transitions
- 📦 Order status tracking from creation to serving
- ⚠️ Error handling for unavailable items and invalid quantities
- 🔍 Order lookup by ID
- 📋 JSON-formatted terminal output
- 🔄 API-style request and response labels
- 🧩 Modular Python project structure
- 🐍 Python standard-library implementation

---

## 📋 Restaurant Menu

The `MenuItem` dataclass in `menu.py` defines the structure of each menu item.

```python
from dataclasses import asdict, dataclass

@dataclass
class MenuItem:
    id: int
    name: str
    category: str
    price: float
    available: bool = True

    def to_dict(self):
        return asdict(self)
```

### Menu Item Attributes

| Attribute | Description |
|---|---|
| `id` | Unique identifier for the menu item |
| `name` | Name of the food item |
| `category` | Category to which the item belongs |
| `price` | Price of one unit of the item |
| `available` | Indicates whether the item can be ordered |

The `available` attribute defaults to `True`, meaning menu items are available unless explicitly marked otherwise.

### Sample Menu

The application initializes the following menu:

| Item ID | Item Name | Category | Price |
|---:|---|---|---:|
| 1 | Margherita Pizza | Main | 14.50 |
| 2 | Caesar Salad | Starter | 8.00 |
| 3 | Chocolate Cake | Dessert | 6.50 |

The prices are illustrative values defined in the code. The application does not currently apply taxes, service charges, or discounts.

### The `to_dict()` Method

```python
def to_dict(self):
    return asdict(self)
```

The `asdict()` function converts a dataclass instance into a dictionary.

For example, the Margherita Pizza object is converted into a structure similar to:

```json
{
  "id": 1,
  "name": "Margherita Pizza",
  "category": "Main",
  "price": 14.5,
  "available": true
}
```

This makes the menu item easier to display as JSON.

---

## 🗂️ Menu Class

The `Menu` class in `menu.py` manages the restaurant's available menu items.

```python
class Menu:
    def __init__(self):
        self.items = {
            1: MenuItem(1, "Margherita Pizza", "Main", 14.5),
            2: MenuItem(2, "Caesar Salad", "Starter", 8.0),
            3: MenuItem(3, "Chocolate Cake", "Dessert", 6.5)
        }
```

The menu stores its items in a dictionary, using each item's ID as the key.

### Responsibilities

- Maintain the restaurant menu.
- Store menu items by ID.
- Retrieve individual items.
- Check whether an item is available.
- Return the collection of menu items.

### The `get()` Method

```python
def get(self, item_id):
    item = self.items.get(item_id)

    if not item or not item.available:
        raise LookupError("Menu item unavailable")

    return item
```

The `get()` method retrieves a menu item by its ID.

If the item does not exist or its `available` attribute is `False`, the method raises a `LookupError`.

Example:

```python
item = menu.get(1)
print(item.name)
```

Output:

```text
Margherita Pizza
```

This method ensures that an order can only include items that exist in the menu and are marked as available.

### The `list()` Method

```python
def list(self):
    return list(self.items.values())
```

The `list()` method returns a list containing all menu item objects.

The main application uses this method to display the restaurant menu:

```python
show(
    "GET /api/menu",
    {"items": [i.to_dict() for i in menu.list()]}
)
```

The list comprehension converts every menu item into a dictionary before formatting the result as JSON.

**Important:** The current implementation lists all menu items, including any that might be marked unavailable. Availability is checked when an item is retrieved through `get()`.

---

## 🧾 Order Data Model

The `Order` dataclass in `orders.py` defines the structure of a customer order.

```python
from dataclasses import dataclass, field

@dataclass
class Order:
    id: str
    table: int
    items: list = field(default_factory=list)
    status: str = "created"

    @property
    def total(self):
        return round(
            sum(
                i["price"] * i["quantity"]
                for i in self.items
            ),
            2
        )
```

### Order Attributes

| Attribute | Description |
|---|---|
| `id` | Unique order identifier generated by the application |
| `table` | Table number associated with the order |
| `items` | List of ordered item records |
| `status` | Current order status |
| `total` | Calculated total price of all order items |

The `items` attribute uses `field(default_factory=list)` to create a separate empty list for each order.

The default status is `created`, which represents the initial stage of the order lifecycle.

### Example Order

When an order is created for Table 12, its initial structure is similar to:

```json
{
  "order_id": "ORD-0001",
  "table": 12,
  "items": [],
  "total": 0,
  "status": "created"
}
```

The order initially contains no items, so its total is zero.

**Note:** The order ID format uses a prefix followed by a four-digit number, such as `ORD-0001`.

---

## 🛒 OrderService Class

The `OrderService` class in `orders.py` manages order creation and item additions.

```python
class OrderService:
    def __init__(self, menu):
        self.menu, self.orders = menu, {}
```

The constructor receives a `Menu` object and initializes an empty dictionary for storing orders.

### Responsibilities

- Create new orders.
- Generate order IDs.
- Associate orders with table numbers.
- Store orders in memory.
- Retrieve orders using their IDs.
- Validate item quantities.
- Check menu item availability.
- Add items to existing orders.

### The `create()` Method

```python
def create(self, table):
    order = Order(f"ORD-{len(self.orders)+1:04}", table)
    self.orders[order.id] = order
    return order
```

The method creates a new order and stores it in the `orders` dictionary.

For the first order, the generated ID is:

```text
ORD-0001
```

For the second order, it would be:

```text
ORD-0002
```

The order is indexed by its ID, allowing it to be retrieved later.

Example:

```python
order = orders.create(12)
```

This creates an order associated with Table 12.

**Limitation:** The ID is based on the current number of orders stored in memory. If orders are removed in a future implementation, this approach could produce duplicate IDs unless the ID-generation strategy is updated.

---

## ➕ Adding Items to an Order

The `add_item()` method adds a menu item and quantity to an existing order.

```python
def add_item(self, order_id, item_id, quantity):
    order = self.orders.get(order_id)

    if not order:
        raise LookupError("Order not found")

    if quantity < 1:
        raise ValueError("Quantity must be positive")

    item = self.menu.get(item_id)

    order.items.append(
        {
            "item_id": item.id,
            "name": item.name,
            "price": item.price,
            "quantity": quantity
        }
    )

    return order
```

### How It Works

1. Find the order using its ID.
2. Raise a `LookupError` if the order does not exist.
3. Check that the quantity is at least one.
4. Retrieve the requested menu item.
5. Verify that the item exists and is available.
6. Append the item's details and quantity to the order.
7. Return the updated order.

### Example 1 — Add Two Pizzas

```python
orders.add_item(order.id, 1, 2)
```

This adds two Margherita Pizzas to the order.

| Property | Value |
|---|---|
| Item ID | 1 |
| Item | Margherita Pizza |
| Unit price | 14.50 |
| Quantity | 2 |
| Subtotal | 29.00 |

### Example 2 — Add One Chocolate Cake

```python
orders.add_item(order.id, 3, 1)
```

This adds one Chocolate Cake.

| Property | Value |
|---|---|
| Item ID | 3 |
| Item | Chocolate Cake |
| Unit price | 6.50 |
| Quantity | 1 |
| Subtotal | 6.50 |

### Validation Rules

The method checks for two main errors:

- **Order not found:** The supplied order ID is not present in the order dictionary.
- **Invalid quantity:** The quantity is less than one.

It also uses `Menu.get()` to reject nonexistent or unavailable menu items.

**Important:** The current code does not explicitly validate that `quantity` is an integer. It checks only whether the value is less than one. It also does not prevent items from being added after the order has reached the `served` status.

---

## 💰 Automatic Bill Calculation

The `Order` class uses a property named `total` to calculate the order's current cost.

```python
@property
def total(self):
    return round(
        sum(
            i["price"] * i["quantity"]
            for i in self.items
        ),
        2
    )
```

### How It Works

1. Iterate through the items in the order.
2. Multiply each item's unit price by its quantity.
3. Add all item subtotals.
4. Round the final value to two decimal places.
5. Return the calculated total.

Because `total` is a property, it can be accessed like an attribute:

```python
print(order.total)
```

There is no need to call `order.total()`.

### Example Bill

The sample order contains two pizzas and one chocolate cake.

| Item | Unit Price | Quantity | Subtotal |
|---|---:|---:|---:|
| Margherita Pizza | 14.50 | 2 | 29.00 |
| Chocolate Cake | 6.50 | 1 | 6.50 |
| **Total** | | | **35.50** |

The total is calculated as:

```text
(14.50 × 2) + (6.50 × 1)
= 29.00 + 6.50
= 35.50
```

The expected order total is **35.50** in the example's unspecified currency units.

**Note:** The project uses floating-point numbers for prices and does not specify a currency. A production billing system would typically use integer minor units or `Decimal` to handle monetary values reliably.

---

## 👨‍🍳 Kitchen Class

The `Kitchen` class in `kitchen.py` manages the progression of an order through the kitchen workflow.

```python
class Kitchen:
    transitions = {
        "created": "submitted",
        "submitted": "preparing",
        "preparing": "ready",
        "ready": "served"
    }
```

The `transitions` dictionary defines the next permitted status for each stage.

### Order Statuses

| Current Status | Next Status | Meaning |
|---|---|---|
| `created` | `submitted` | Order is submitted to the kitchen workflow |
| `submitted` | `preparing` | Kitchen preparation begins |
| `preparing` | `ready` | Order is ready for serving |
| `ready` | `served` | Order has been served |

The `served` status is the final stage in the current workflow.

### The `advance()` Method

```python
@classmethod
def advance(cls, order):
    next_status = cls.transitions.get(order.status)

    if not next_status:
        raise ValueError("Order is already complete")

    order.status = next_status

    return {
        "order_id": order.id,
        "status": order.status
    }
```

### How It Works

1. Read the order's current status.
2. Look up the next status in the `transitions` dictionary.
3. Raise a `ValueError` if no next status exists.
4. Update the order's status.
5. Return the order ID and new status.

The method uses `@classmethod`, so it accesses the shared transition mapping through the class parameter `cls`.

### Example

```python
Kitchen.advance(order)
```

If the order status is `created`, the method changes it to `submitted`.

The response is:

```json
{
  "order_id": "ORD-0001",
  "status": "submitted"
}
```

Subsequent calls advance the same order through `preparing`, `ready`, and `served`.

**Important:** This is a simulated kitchen workflow. It does not connect to kitchen displays, notify staff, or perform actual food preparation.

---

## 🔄 Complete Application Workflow

The application follows this workflow:

```text
Start Application
        |
        v
Initialize Menu
        |
        v
Initialize OrderService
        |
        v
Display Restaurant Menu
        |
        v
Create Order for Table 12
        |
        v
Generate Order ID
        |
        v
Add 2 Margherita Pizzas
        |
        v
Add 1 Chocolate Cake
        |
        v
Calculate Order Total
        |
        v
Display Order Details
        |
        v
Advance Kitchen Status
        |
        v
created → submitted
        |
        v
submitted → preparing
        |
        v
preparing → ready
        |
        v
ready → served
        |
        v
End Application
```

This workflow demonstrates how menu management, order processing, billing, and kitchen status tracking work together.

---

## 🧾 API-Style Request and Response Format

The `show()` helper function in `main97.py` displays each operation in a structured format.

```python
def show(action, data, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(data, indent=2)}"
    )
```

The helper prints:

- The simulated request label.
- The response status label.
- The returned data formatted as JSON.

### The `order_data()` Function

The application uses another helper to format order information:

```python
def order_data(order):
    return {
        "order_id": order.id,
        "table": order.table,
        "items": order.items,
        "total": order.total,
        "status": order.status
    }
```

This function converts the order object into a dictionary containing the order ID, table number, items, total, and current status.

### Operations Demonstrated

| Operation | Status Label | Purpose |
|---|---:|---|
| `GET /api/menu` | `200` | Displays all menu items |
| `POST /api/orders` | `201` | Displays the created order with its items and total |
| `PATCH /api/kitchen/status` | `200` | Displays each kitchen status transition |

These request labels resemble REST API operations, but they are printed by Python code. The application does not run an HTTP server or implement actual endpoints.

**Important:** The order response is displayed after the two items have been added. Although the label is `POST /api/orders`, the displayed data represents the order's state after those additions.

---

## 📊 Example Order Results

The main program creates an order and adds the following items:

```python
order = orders.create(12)
orders.add_item(order.id, 1, 2)
orders.add_item(order.id, 3, 1)
```

### Order Summary

| Property | Expected Value |
|---|---|
| Order ID | `ORD-0001` |
| Table | 12 |
| Margherita Pizza | 2 |
| Chocolate Cake | 1 |
| Total | 35.50 |
| Initial status | `created` |

### Example Order Response

The order response should contain data similar to the following:

```json
{
  "order_id": "ORD-0001",
  "table": 12,
  "items": [
    {
      "item_id": 1,
      "name": "Margherita Pizza",
      "price": 14.5,
      "quantity": 2
    },
    {
      "item_id": 3,
      "name": "Chocolate Cake",
      "price": 6.5,
      "quantity": 1
    }
  ],
  "total": 35.5,
  "status": "created"
}
```

### Kitchen Status Progression

The main program advances the order four times:

```python
for _ in range(4):
    show(
        "PATCH /api/kitchen/status",
        Kitchen.advance(order)
    )
```

The expected status sequence is:

```text
created
   |
   v
submitted
   |
   v
preparing
   |
   v
ready
   |
   v
served
```

The four displayed responses are:

```json
{
  "order_id": "ORD-0001",
  "status": "submitted"
}
```

```json
{
  "order_id": "ORD-0001",
  "status": "preparing"
}
```

```json
{
  "order_id": "ORD-0001",
  "status": "ready"
}
```

```json
{
  "order_id": "ORD-0001",
  "status": "served"
}
```

The order finishes with a total of `35.5` and a status of `served`.

---

## 🏗️ Project Architecture

The project contains four main Python modules.

```text
                  main97.py
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       menu.py     orders.py   kitchen.py
          |           |           |
          v           v           v
      MenuItem     OrderService   Kitchen
      Menu         Order          Status Flow
          |           |           |
          v           v           v
      Menu Data   Order Items   Status Updates
                      |
                      v
                Total Calculation
                      |
                      v
                 JSON Output
```

### Module Responsibilities

- **`main97.py`** — initializes the menu and order service, displays the menu, creates an order, adds items, and advances kitchen statuses.
- **`menu.py`** — defines `MenuItem` and `Menu`, including menu lookup and availability checks.
- **`orders.py`** — defines `Order` and `OrderService`, including order creation, item addition, quantity validation, and total calculation.
- **`kitchen.py`** — defines the kitchen status transition mapping and the `advance()` method.

This modular structure separates menu data, order management, and kitchen workflow logic, making the project easier to maintain and extend.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement menu management, order processing, price calculation, and kitchen status tracking.

### 🧩 Dataclasses

The `dataclasses` module defines structured records for menu items and orders.

```python
from dataclasses import asdict, dataclass, field
```

The `@dataclass` decorator automatically generates useful methods for data-oriented classes.

The `field(default_factory=list)` expression creates a separate list for each order.

### 🏗️ Object-Oriented Programming

The project uses classes to organize responsibilities:

- `MenuItem` — represents an individual menu item.
- `Menu` — manages menu records.
- `Order` — represents an order and calculates its total.
- `OrderService` — creates orders and adds items.
- `Kitchen` — advances order statuses.

### 🗂️ Dictionaries

Dictionaries store menu items, orders, item details, and permitted status transitions.

### 📋 Lists

Lists store the items included in each order and the collection returned by the menu.

### 🧮 Properties and Generators

The `@property` decorator allows the order total to be accessed as an attribute.

The generator expression inside `sum()` calculates each item's subtotal before adding them together.

### 🏷️ Class Methods

The `@classmethod` decorator allows the kitchen status method to access the shared transition mapping using `cls`.

### 🧾 JSON

The built-in `json` module converts Python dictionaries and lists into readable terminal output.

### ⚠️ Exception Handling

The project uses:

- `LookupError` when an order or menu item cannot be found.
- `ValueError` when a quantity is less than one or an order has already completed its workflow.

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
DAY_97/
│
├── main97.py
├── menu.py
├── orders.py
├── kitchen.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Purpose |
|---|---|
| `main97.py` | Entry point and sample restaurant ordering workflow |
| `menu.py` | Menu item dataclass and menu management |
| `orders.py` | Order model, order creation, item addition, and bill calculation |
| `kitchen.py` | Kitchen workflow and order status transitions |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

No external data files are required. Menu items and orders are initialized and stored in memory.

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Ensure that Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal in your `DAY_97` folder.

```bash
cd DAY_97
```

### Step 3 — Check the Files

Make sure the following Python files are present:

```text
main97.py
menu.py
orders.py
kitchen.py
```

### Step 4 — Run the Application

Execute the following command:

```bash
python main97.py
```

### Step 5 — Review the Terminal Output

The terminal displays:

- The project title.
- The restaurant menu.
- The created order and its item details.
- The calculated order total.
- The first kitchen status update.
- The second kitchen status update.
- The third kitchen status update.
- The final `served` status.

### Step 6 — Verify the Order

Confirm that the order contains two Margherita Pizzas and one Chocolate Cake, with a total of `35.5`.

The order should progress through all four transitions and finish with the status `served`.

---

## ⚠️ Important Notes and Limitations

### 1. No Graphical Interface

The current application is terminal-based. It does not provide a graphical menu, table layout, or interactive ordering screen.

### 2. No Actual HTTP API

The request labels are simulated terminal output. The application does not run a web server or expose actual endpoints.

### 3. No Database

Menu items and orders are stored in memory. All order information is lost when the application terminates.

### 4. Predefined Menu

The menu contains three hardcoded items. There is no functionality for adding, editing, or deleting menu items dynamically.

### 5. No Payment Processing

The system calculates the order total but does not accept payments, generate payment confirmations, or integrate with a payment gateway.

### 6. Limited Price Handling

Prices are represented using Python floating-point values. A production billing system should consider `Decimal` or integer minor currency units to avoid floating-point rounding issues in financial calculations.

### 7. Limited Quantity Validation

The code rejects quantities below one but does not explicitly check that quantities are integers. Additional validation would be needed to prevent unexpected input types.

### 8. No Order Modification or Cancellation

The current implementation can add items but does not provide dedicated methods to remove items, change quantities, or cancel an order.

### 9. Orders Can Be Modified After Serving

The `add_item()` method does not check the order's status before adding new items. Therefore, the current code can add items to an order even after it has reached `served`.

### 10. No Duplicate Item Consolidation

If the same menu item is added multiple times, it is stored as a separate entry instead of automatically increasing the quantity of an existing entry.

### 11. Basic Order ID Generation

Order IDs are generated using the current number of orders plus one. This is sufficient for the demonstration but may produce duplicates if order deletion or more complex persistence is introduced.

### 12. No Real Kitchen Integration

Kitchen progression is manually simulated through four calls to `Kitchen.advance()`. There is no automatic preparation timer, staff assignment, kitchen display system, or notification mechanism.

### 13. No Multi-User Support

The application does not implement separate customer, waiter, cashier, or kitchen staff accounts. Multiple users cannot interact with the same order through a shared server.

### 14. No Taxes or Discounts

The total includes only the prices of ordered items multiplied by their quantities. Taxes, service charges, delivery fees, and discounts are not included.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Python dataclasses
- Object-oriented programming
- Lists and dictionaries
- Default factories
- Instance attributes and class attributes
- Properties using `@property`
- Class methods using `@classmethod`
- Menu data management
- Order creation and lookup
- Unique ID formatting
- Adding items to collections
- Quantity validation
- Generator expressions
- The `sum()` function
- Floating-point rounding
- State transition dictionaries
- Order lifecycle management
- Exception handling
- JSON serialization
- Modular programming
- API-style request and response formatting
- Basic restaurant workflow modeling

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Define structured menu item and order models using dataclasses.
- Maintain menu items in a dictionary.
- Retrieve menu items by ID.
- Check whether menu items are available.
- Create orders for specific tables.
- Generate formatted order IDs.
- Add items and quantities to an order.
- Validate order existence and item quantities.
- Calculate an order's total dynamically.
- Use properties to expose calculated values.
- Define valid order status transitions.
- Advance an order through a kitchen workflow.
- Handle invalid operations using exceptions.
- Format menu and order information as JSON.
- Separate menu management, order processing, and kitchen operations into modules.
- Understand the limitations of an in-memory restaurant ordering system.
- Build a foundation for a more complete restaurant management application.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🌐 Build a web interface using Flask, Django, or FastAPI.
- 🎨 Create a responsive restaurant menu and ordering page.
- 🗄️ Store menu items and orders in SQLite or PostgreSQL.
- 👤 Add customer registration and login.
- 👨‍🍳 Create separate customer, waiter, cashier, and kitchen dashboards.
- 🪑 Manage tables and table availability.
- ➕ Add menu item creation, editing, and deletion.
- 🗑️ Allow items to be removed from orders.
- 🔢 Allow customers or staff to update item quantities.
- 💰 Use `Decimal` for reliable monetary calculations.
- 🧾 Add tax, service charges, discounts, and delivery fees.
- 💳 Integrate a secure payment gateway.
- 🖨️ Generate printable bills and receipts.
- 🔔 Add order notifications and kitchen alerts.
- ⏱️ Track preparation time for each order.
- 📊 Build sales reports and order analytics.
- 📦 Add inventory and ingredient tracking.
- 🚫 Prevent changes to orders after they are finalized.
- 🔄 Add order cancellation and refund workflows.
- 🧪 Write automated unit and integration tests.
- 🔐 Implement authentication and role-based access control.
- 📱 Develop a mobile-friendly ordering interface.
- 🚀 Deploy the application as a restaurant management service.

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 97** focuses on **Restaurant Ordering System Development**, combining menu management, order creation, item quantity handling, automatic bill calculation, and kitchen status tracking using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🍽️