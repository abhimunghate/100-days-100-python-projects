from dataclasses import asdict, dataclass

@dataclass
class Account:
    id: int
    name: str
    account_type: str
    balance: float
    
    def to_dict(self):
        data = asdict(self)
        data["balance"] = round(self.balance, 2)
        return data
    
class AccountService:
    def __init__(self):
        self.accounts = {
            101: Account(101, "Everyday Checking", "checking", 4200.00),
            102: Account(102, "Emergency Savings", "savings", 12000.00),
            103: Account(103, "Rewards Card", "credit", -850.00)
        }
        
    def get(self, account_id):
        account = self.accounts.get(account_id)
        if not account:
            raise LookupError("Account not found")
        return account
    
    def list(self):
        return list(self.accounts.values())
    
    def net_worth(self):
        return round(sum(account.balance for account in self.accounts.values()), 2)
    
# Done