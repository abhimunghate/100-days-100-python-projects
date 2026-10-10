# 💰 Day 91 - Personal Finance Dashboard

Welcome to **Day 91** of my **100 Days, 100 Python Projects** challenge!

This project is a **Personal Finance Dashboard** built using Python. It demonstrates how financial accounts, income, expenses, transactions, spending categories, budgets, and savings rates can be managed and summarized through a modular backend application.

The project uses Python dataclasses, object-oriented programming, in-memory storage, and financial calculations to generate a structured dashboard summary. It also generates request IDs and UTC timestamps for API-style terminal responses.

---

## 📌 Project Overview

A personal finance dashboard helps users understand their financial situation by organizing account balances, tracking income and expenses, monitoring spending, and comparing expenses against budgets.

This project simulates the backend logic of a personal finance application. It starts with three sample accounts:

- 🏦 Everyday Checking
- 💰 Emergency Savings
- 💳 Rewards Card

The application adds sample transactions to these accounts and updates their balances. It then calculates financial summaries, including net worth, income, expenses, cash flow, savings rate, category-wise spending, and budget status.

The dashboard provides a consolidated view of financial activity through a JSON-formatted response.

**Note:** This project is a terminal-based backend simulation. It does not currently include a graphical dashboard, a web interface, a database, or real bank integration.

---

## ✨ Features

- 💰 Personal finance summary
- 🏦 Multiple financial accounts
- 💳 Checking, savings, and credit account types
- 🧾 Transaction management
- 📈 Income tracking
- 📉 Expense tracking
- 🧮 Automatic account balance updates
- 💵 Net worth calculation
- 🔄 Monthly cash flow calculation
- 📊 Savings rate calculation
- 🗂️ Category-wise expense tracking
- 🎯 Budget monitoring
- ⚠️ Over-budget detection
- ✅ Budget status reporting
- 🆔 Unique request IDs
- 🕒 UTC timestamps
- 🧾 JSON-formatted responses
- 🧩 Modular service-based architecture
- 🐍 Python standard-library implementation

---

## 🏦 Financial Accounts

The application initializes three accounts in `accounts.py`.

| Account ID | Account Name | Account Type | Initial Balance |
|---:|---|---|---:|
| 101 | Everyday Checking | Checking | $4,200.00 |
| 102 | Emergency Savings | Savings | $12,000.00 |
| 103 | Rewards Card | Credit | -$850.00 |

Each account contains four attributes:

- `id` — unique account identifier
- `name` — account name
- `account_type` — type of financial account
- `balance` — current balance

The balances are updated whenever a transaction is added to an account.

The sample balances and transactions are illustrative data for learning purposes. They are not connected to actual bank accounts.

---

## 🧾 Transaction Management

The `TransactionService` class manages financial transactions.

Each transaction contains the following information:

| Field | Description |
|---|---|
| `id` | Transaction identifier |
| `account_id` | Account associated with the transaction |
| `description` | Description of the transaction |
| `category` | Financial category |
| `amount` | Transaction amount |
| `transaction_date` | Date of the transaction |

The `Transaction` dataclass is defined in `transactions.py`.

```python
from dataclasses import asdict, dataclass

@dataclass
class Transaction:
    id: int
    account_id: int
    description: str
    category: str
    amount: float
    transaction_date: str
```

The dataclass provides a structured way to store transaction information.

Its `to_dict()` method converts the transaction into a dictionary and rounds the amount to two decimal places for output.

### Income and expenses

The project represents income using positive amounts and expenses using negative amounts.

Examples:

```python
(101, "Monthly salary", "Income", 6500.00)
(101, "Apartment rent", "Housing", -2200.00)
(101, "Grocery store", "Groceries", -460.00)
```

When a transaction is added, its amount is applied to the associated account balance.

For example, an expense of `-2200.00` reduces the account balance by $2,200.00.

---

## 💸 Account Balance Updates

The `TransactionService.add()` method updates the account balance after creating and storing a transaction.

```python
self.transactions.append(transaction)
account.balance += amount
return transaction
```

This means:

- Positive transaction amounts increase the account balance.
- Negative transaction amounts decrease the account balance.
- The updated balance is reflected in the final dashboard summary.

For example, the checking account starts with a balance of $4,200.00. After adding the salary, rent, grocery, and utility transactions, its balance becomes $7,800.00.

The rewards card starts with a balance of -$850.00. After the dining expense of -$180.00, its balance becomes -$1,030.00.

The emergency savings account receives no sample transactions, so its balance remains $12,000.00.

---

## 📊 Dashboard Summary

The `DashboardService` class combines account information and transaction activity to calculate the financial summary.

It is defined in `dashboard.py`.

The dashboard returns the following information:

| Metric | Description |
|---|---|
| `net_worth` | Sum of all account balances |
| `monthly_income` | Sum of positive transaction amounts |
| `monthly_expenses` | Absolute total of negative transaction amounts |
| `monthly_cash_flow` | Income minus expenses |
| `savings_rate_percent` | Cash flow as a percentage of income |
| `spending_by_category` | Total expenses for each spending category |
| `budget_status` | Budget limits and spending comparisons |
| `accounts` | List of accounts with their updated balances |

**Implementation note:** Although the output fields use the word `monthly`, the current code sums all transactions in memory. It does not filter transactions by month. The sample data is used as a demonstration of the summary calculations.

---

## 🧮 Net Worth Calculation

Net worth is calculated by adding the balances of all accounts.

The implementation in `accounts.py` is:

```python
def net_worth(self):
    return round(
        sum(account.balance for account in self.accounts.values()),
        2
    )
```

Using the initial account balances:

- Checking: $4,200.00
- Savings: $12,000.00
- Rewards Card: -$850.00

The initial net worth is:

```text
$4,200 + $12,000 - $850 = $15,350
```

After the sample transactions, the account balances are:

| Account | Updated Balance |
|---|---:|
| Everyday Checking | $7,800.00 |
| Emergency Savings | $12,000.00 |
| Rewards Card | -$1,030.00 |
| **Total Net Worth** | **$18,770.00** |

The project calculates net worth by summing account balances, so the negative credit-account balance reduces the total.

---

## 📈 Income Tracking

The dashboard calculates income by summing all positive transaction amounts.

```python
income = sum(
    item.amount
    for item in activity
    if item.amount > 0
)
```

The sample transaction list contains one income transaction:

```text
Monthly salary: $6,500.00
```

Therefore, the dashboard reports:

```text
Total Income: $6,500.00
```

Positive transaction amounts contribute to income and increase the associated account balance.

---

## 📉 Expense Tracking

Expenses are represented by negative transaction amounts.

The dashboard calculates their total using:

```python
expenses = abs(
    sum(
        item.amount
        for item in activity
        if item.amount < 0
    )
)
```

The sample expenses are:

| Description | Category | Amount |
|---|---|---:|
| Apartment rent | Housing | -$2,200.00 |
| Grocery store | Groceries | -$460.00 |
| Electric and internet | Utilities | -$240.00 |
| Weekend dining | Dining | -$180.00 |
| **Total Expenses** | | **$3,080.00** |

The application converts the negative total into a positive expense figure for the dashboard summary.

---

## 💵 Cash Flow Calculation

Cash flow represents the difference between income and expenses.

The project calculates it using:

```python
cash_flow = income - expenses
```

For the sample transactions:

```text
Income   = $6,500.00
Expenses = $3,080.00

Cash Flow = $6,500.00 - $3,080.00
          = $3,420.00
```

The dashboard therefore reports a positive cash flow of **$3,420.00**.

A positive cash flow means the recorded income exceeds the recorded expenses in the current transaction dataset.

---

## 📊 Savings Rate Calculation

The savings rate is calculated as cash flow divided by income, multiplied by 100.

```python
savings_rate = (
    cash_flow / income * 100
) if income else 0
```

Using the sample data:

```text
Savings Rate = ($3,420 / $6,500) × 100
             = 52.615...%
             ≈ 52.6%
```

The dashboard rounds the result to one decimal place.

If there is no income, the code returns a savings rate of `0` to avoid division by zero.

This is a simplified cash-flow-based savings rate, not a calculation based on a user's complete financial history.

---

## 🗂️ Spending by Category

The dashboard groups expenses by category.

The implementation iterates through all transactions and includes only negative amounts.

```python
spending_by_category = {}

for item in activity:
    if item.amount < 0:
        spending_by_category[item.category] = round(
            spending_by_category.get(item.category, 0)
            + abs(item.amount),
            2
        )
```

The sample spending breakdown is:

| Category | Spending |
|---|---:|
| Housing | $2,200.00 |
| Groceries | $460.00 |
| Utilities | $240.00 |
| Dining | $180.00 |
| **Total** | **$3,080.00** |

The category totals help identify where money is being spent.

Income transactions are excluded from this calculation because only negative amounts are counted as expenses.

---

## 🎯 Budget Monitoring

The application defines spending budgets in `main91.py`.

```python
budgets = {
    "Housing": 2200.00,
    "Groceries": 500.00,
    "Utilities": 300.00,
    "Dining": 150.00
}
```

The dashboard compares each budget with the actual spending in its category.

For every category, it calculates:

- `budget` — allowed spending limit
- `spent` — recorded expenses
- `remaining` — budget minus spending
- `status` — whether the category is on track or over budget

The remaining amount is calculated using:

```python
remaining = round(limit - spent, 2)
```

The status is determined by:

```python
status = (
    "over budget"
    if spent > limit
    else "on track"
)
```

### Sample budget analysis

| Category | Budget | Spent | Remaining | Status |
|---|---:|---:|---:|---|
| Housing | $2,200.00 | $2,200.00 | $0.00 | On track |
| Groceries | $500.00 | $460.00 | $40.00 | On track |
| Utilities | $300.00 | $240.00 | $60.00 | On track |
| Dining | $150.00 | $180.00 | -$30.00 | Over budget |

The dining category exceeds its budget by $30.00.

Housing is considered on track because the code marks a category as over budget only when spending is strictly greater than its limit.

---

## 🆔 Request IDs

The application generates a request ID for every response using Python's `uuid` module.

```python
f"REQ-{uuid4().hex[:8].upper()}"
```

The generated request ID has this format:

```text
REQ-A1B2C3D4
```

This is an illustrative example; the actual value changes each time a response is generated.

Request IDs make individual operations easier to identify when reading terminal output or reviewing logs.

The code uses a random UUID as the source of the identifier and takes eight hexadecimal characters, converting them to uppercase.

---

## 🕒 UTC Timestamps

Each response includes a timestamp generated using Python's `datetime` module.

```python
datetime.now(timezone.utc).isoformat()
```

This produces an ISO 8601 timestamp in UTC.

An example timestamp format is:

```text
2026-10-10T10:00:00+00:00
```

The value above is only an example of the format.

Timestamps provide response metadata that can be useful when tracking operations or debugging applications.

---

## 🧾 Standardized Response Format

The `respond()` function creates a common structure for all terminal responses.

```python
def respond(action, data, status=200):
    payload = {
        "status": status,
        "request_id": f"REQ-{uuid4().hex[:8].upper()}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data": data
    }

    print(f"\nREQUEST {action}")
    print(f"RESPONSE {status}")
    print(json.dumps(payload, indent=2))

    return payload
```

Every response contains:

| Field | Purpose |
|---|---|
| `status` | Simulated response status code |
| `request_id` | Generated identifier for the operation |
| `timestamp` | UTC timestamp |
| `data` | Transaction or dashboard information |

The application uses `201` for transaction creation and `200` for the dashboard summary.

These are API-style labels printed in the terminal. The application does not currently send actual HTTP requests or responses.

---

## 🔄 Application Workflow

The complete workflow is:

```text
Start Application
        |
        v
Create AccountService
        |
        v
Create TransactionService
        |
        v
Create DashboardService
        |
        v
Add Sample Transactions
        |
        v
Update Account Balances
        |
        v
Generate Transaction Responses
        |
        v
Calculate Dashboard Summary
        |
        v
Calculate Net Worth and Cash Flow
        |
        v
Analyze Spending and Budgets
        |
        v
Display Final JSON Summary
```

The three services work together to produce the final dashboard output.

---

## 🏗️ Project Architecture

The project separates responsibilities into three service modules and one entry-point file.

```text
                 main91.py
                     |
          +----------+----------+
          |                     |
          v                     v
   AccountService       TransactionService
          |                     |
          |<--------------------+
          |        Updates balances
          |
          +------------+
                       |
                       v
                DashboardService
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Net Worth   Cash Flow    Budget Status
                       |
                       v
                JSON Dashboard
```

### Module responsibilities

- **`accounts.py`** — account records, account lookup, account listing, and net worth.
- **`transactions.py`** — transaction records, validation, storage, and balance updates.
- **`dashboard.py`** — financial calculations, category-wise spending, and budget analysis.
- **`main91.py`** — sample data, service initialization, and terminal responses.

This structure keeps the business logic separate from the main application workflow.

---

## 🛠️ Technologies Used

### Python

Python is used to implement the complete application, including account management, transaction processing, financial calculations, and response generation.

### `dataclasses`

Used to define structured `Account` and `Transaction` objects.

### `datetime`

Used to generate transaction dates and UTC response timestamps.

### `uuid`

Used to generate request identifiers.

### `json`

Used to format the transaction and dashboard payloads for terminal display.

### Python Dictionaries and Lists

- Dictionaries store accounts and budgets.
- Lists store transactions and dashboard budget-status records.

### Object-Oriented Programming

The project uses separate service classes to organize account, transaction, and dashboard functionality.

---

## 📦 Requirements

This project uses only Python's standard library and does not require external packages.

Check your Python version:

```bash
python --version
```

### `requirements.txt`

```text
# No external dependencies required.
```

---

## 📂 Project Structure

```text
DAY_91/
│
├── main91.py
├── accounts.py
├── transactions.py
├── dashboard.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Purpose |
|---|---|
| `main91.py` | Entry point and sample application workflow |
| `accounts.py` | Account model and account service |
| `transactions.py` | Transaction model and transaction service |
| `dashboard.py` | Financial summary and budget calculations |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Make sure Python is installed.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal inside your `DAY_91` directory.

```bash
cd DAY_91
```

### Step 3 — Check the Project Files

Make sure these four Python files are present:

```text
main91.py
accounts.py
transactions.py
dashboard.py
```

### Step 4 — Run the Program

Execute:

```bash
python main91.py
```

### Step 5 — Review the Results

The terminal displays five transaction-creation responses followed by a dashboard summary response.

Each response contains a status label, request ID, timestamp, and data payload.

The final summary includes the updated account balances and calculated financial metrics.

---

## 📋 Sample Dashboard Results

Based on the supplied initial account balances and sample transactions, the final dashboard values should include:

```text
Net Worth:             $18,770.00
Income:                 $6,500.00
Expenses:               $3,080.00
Cash Flow:               $3,420.00
Savings Rate:                52.6%
```

The spending categories should total $3,080.00, with Dining marked as over budget because its spending is $180.00 against a $150.00 budget.

The request IDs and timestamps will vary on each run.

---

## ⚠️ Important Notes and Limitations

### 1. In-Memory Storage

Accounts and transactions are stored in memory. Changes are not saved after the program exits.

### 2. Sample Financial Data

The account balances, transaction descriptions, and budgets are sample values for demonstrating the application's logic.

### 3. Monthly Calculations

The dashboard labels income and expenses as monthly metrics, but the current implementation does not filter transactions by date or month.

### 4. Currency Handling

The examples use dollar amounts for readability, but the code does not store a currency symbol or perform currency conversion.

### 5. Transaction Validation

The code checks that descriptions and categories are not blank and that transaction amounts are not zero. It does not currently validate transaction dates, enforce numeric types explicitly, or prevent every possible invalid input.

### 6. Credit Account Modeling

The credit account uses a negative balance, and expenses reduce that balance further. This is a simplified account model rather than a complete credit-card accounting system.

### 7. No Real Bank Integration

The project does not connect to bank accounts, import bank statements, or retrieve live financial data.

### 8. No Graphical Interface

The current version is a terminal-based backend simulation. Charts, graphs, and interactive dashboard controls are possible future additions.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Object-oriented programming
- Dataclasses and object serialization
- Lists and dictionaries
- Financial arithmetic
- Income and expense calculations
- Account balance updates
- Net worth calculation
- Cash flow analysis
- Savings rate calculation
- Category-based aggregation
- Budget comparison
- Date and time handling
- UUID generation
- JSON serialization
- Input validation
- Modular programming
- Service-based architecture
- API-style response design
- In-memory data management

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Create and manage multiple financial accounts
- Represent account and transaction records using dataclasses
- Add transactions to specific accounts
- Update account balances automatically
- Calculate net worth across accounts
- Separate income and expenses using signed amounts
- Calculate cash flow and savings rate
- Group expenses by category
- Compare spending with budget limits
- Identify over-budget categories
- Generate request IDs and UTC timestamps
- Build standardized JSON responses
- Separate account, transaction, and dashboard logic into modules
- Coordinate multiple services in a Python application
- Understand the backend logic behind personal finance applications

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 📊 Add an interactive dashboard using Streamlit or Flask
- 📈 Visualize income and expenses with charts
- 🗄️ Store financial data in SQLite or PostgreSQL
- 📅 Filter transactions by month and year
- 💳 Add account creation and deletion
- ✏️ Add transaction editing and deletion
- 🔍 Search and filter transactions
- 📤 Import transactions from CSV files
- 📥 Export reports to CSV or Excel
- 🎯 Support customizable budgets
- 🔔 Notify users when budgets are exceeded
- 📈 Compare spending across months
- 💰 Track financial goals
- 🏦 Add recurring transactions
- 💱 Support multiple currencies
- 🧾 Generate monthly financial reports
- 🔐 Add user authentication
- 🛡️ Protect sensitive financial information
- 🧪 Add automated unit tests
- 📝 Add logging and exception handling
- 📱 Build a responsive web interface
- ☁️ Deploy the application to a cloud platform

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to improve programming skills, strengthen problem-solving abilities, and gain practical experience with different areas of software development.

**Day 91** focuses on **Personal Finance Management**, combining account management, transaction processing, financial calculations, budget monitoring, and structured response generation using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍💰
