# This is Day 91 project : Personal Finance Dashboard

import json
from datetime import datetime, timezone
from uuid import uuid4

from accounts import AccountService
from dashboard import DashboardService
from transactions import TransactionService

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

def main():
    print("Day 91 - Personal Finance Dashboard")
    
    accounts = AccountService()
    transactions = TransactionService(accounts)
    dashboard = DashboardService(accounts, transactions)
    
    sample_transactions = [
        (101, "Monthly salary", "Income", 6500.00),
        (101, "Apartment rent", "Housing", -2200.00),
        (101, "Grocery store", "Groceries", -460.00),
        (101, "Electric and internet", "Utilities", -240.00),
        (103, "Weekend dining", "Dining", -180.00)
    ]
    
    for account_id, description, category, amount in sample_transactions:
        transaction = transactions.add(account_id, description, category, amount)
        respond("POST /api/transactions", transaction.to_dict(), 201)
        
    budgets = {
        "Housing": 2200.00,
        "Groceries": 500.00,
        "Utilities": 300.00,
        "Dining": 150.00
    }
    respond("GET /api/dashboard", dashboard.summary(budgets))
    
if __name__ == "__main__":
    main()
    
# Done