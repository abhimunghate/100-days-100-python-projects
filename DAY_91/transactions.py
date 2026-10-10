from dataclasses import asdict, dataclass
from datetime import date

@dataclass
class Transaction:
    id: int
    account_id: int
    description: str
    category: str
    amount: float
    transaction_date: str
    
    def to_dict(self):
        data = asdict(self)
        data["amount"] = round(self.amount, 2)
        return data
    
class TransactionService:
    def __init__(self, accounts):
        self.accounts = accounts
        self.transactions = []
        
    def add(self, account_id, description, category, amount, transaction_date=None):
        account = self.accounts.get(account_id)
        
        if not description.strip() or not category.strip():
            raise ValueError("Description and category are required")
        if amount == 0:
            raise ValueError("Transaction amount cannot be zero")
        
        transaction = Transaction(
            id=len(self.transactions) + 1,
            account_id=account_id,
            description=description,
            category=category,
            amount=amount,
            transaction_date=transaction_date or date.today().isoformat()
        )
        self.transactions.append(transaction)
        account.balance += amount
        return transaction
    
    def list(self):
        return list(self.transactions)
    
# Done