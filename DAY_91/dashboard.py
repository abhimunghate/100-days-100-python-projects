class DashboardService:
    def __init__(self, accounts, transactions):
        self.accounts = accounts
        self.transactions = transactions
        
    def summary(self, budgets):
        activity = self.transactions.list()
        income = sum(item.amount for item in activity if item.amount > 0)
        expenses = abs(sum(item.amount for item in activity if item.amount < 0))
        cash_flow = income - expenses
        savings_rate = (cash_flow / income * 100) if income else 0
        
        spending_by_category = {}
        for item in activity:
            if item.amount < 0:
                spending_by_category[item.category] = round(spending_by_category.get(item.category, 0) + abs(item.amount), 2)
                
        budget_status = []
        for category, limit in budgets.items():
            spent = spending_by_category.get(category, 0)
            budget_status.append(
                {
                    "category": category,
                    "budget": limit,
                    "spent": spent,
                    "remaining": round(limit - spent, 2),
                    "status": "over budget" if spent > limit else "on track"
                }
            )
            
        return {
            "net_worth": self.accounts.net_worth(),
            "monthly_income": round(income, 2),
            "monthly_expenses": round(expenses, 2),
            "monthly_cash_flow": round(cash_flow, 2),
            "savings_rate_percent": round(savings_rate, 1),
            "spending_by_category": spending_by_category,
            "budget_status": budget_status,
            "accounts": [account.to_dict() for account in self.accounts.list()]
        }
        
# Done