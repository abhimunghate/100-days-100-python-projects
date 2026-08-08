# This is Day 28 project : Mini ATM Machine

from datetime import datetime
import json
import os

ATM_FILE = "atm_data.json"

class Transaction:
    def __init__(self, transaction_type, amount, description=""):
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display(self):
        print(f"{self.timestamp} | {self.transaction_type:<15} | ₹{self.amount:.2f} | {self.description}")
        
    def to_dict(self):
        return {"transaction_type": self.transaction_type, "amount": self.amount, "description": self.description, "timestamp": self.timestamp}

class BankAccount:
    def __init__(self, account_number, account_type):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
        self.is_frozen = False
        self.transactions = []
        
    def to_dict(self):
        return {"account_number": self.account_number, "account_type": self.account_type, "balance": self.balance, "is_frozen": self.is_frozen, "transactions": [transaction.to_dict() for transaction in self.transactions]}
        
    def add_transaction(self, transaction_type, amount, description=""):
        transaction = Transaction(transaction_type, amount, description)
        self.transactions.append(transaction)
        
    def check_balance(self):
        print(f"\nAccount Number : {self.account_number}")
        print(f"Account Type     : {self.account_type}")
        print(f"Balance          : ₹{self.balance:.2f}")

        if self.is_frozen:
            print("Status : FROZEN")
        else:
            print("Status : ACTIVE")
    
    def deposit(self, amount):
        if self.is_frozen:
            print("Account is frozen.")
            return
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        self.add_transaction("DEPOSIT", amount, "Cash deposit")
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New Balance : ₹{self.balance:.2f}")
            
    def withdraw(self, amount):
        if self.is_frozen:
            print("Account is frozen.")
            return
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.add_transaction("WITHDRAWAL", amount, "Cash withdrawal")
        
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"New Balance : ₹{self.balance:.2f}")
        
    def show_transactions(self):
        print("\n------ Transaction History ------")
        if not self.transactions:
            print("No transactions found.")
            return
        for transaction in self.transactions:
            transaction.display()
            
class SavingsAccount(BankAccount):
    def __init__(self, account_number):
        super().__init__(account_number, "Savings")

    def add_interest(self, rate=4):
        interest = self.balance * rate / 100
        self.balance += interest
        self.add_transaction("INTEREST", interest, f"{rate}% savings interest") 
        print(f"₹{interest:.2f} interest added.")
        
class CheckingAccount(BankAccount):
    def __init__(self, account_number):
        super().__init__(account_number, "Checking")
        
class CreditCardAccount(BankAccount):
    def __init__(self, account_number, credit_limit=50000):
        super().__init__(account_number, "Credit Card")
        self.credit_limit = credit_limit
        self.credit_used = 0
        
    def to_dict(self):
        data = super().to_dict()
        data["credit_limit"] = self.credit_limit
        data["credit_used"] = self.credit_used
        return data

    def show_balance(self):
        available_credit = (self.credit_limit - self.credit_used)
        print(f"\nCredit Limit     : ₹{self.credit_limit:.2f}")
        print(f"Credit Used        : ₹{self.credit_used:.2f}")
        print(f"Available Credit   : ₹{available_credit:.2f}")

    def make_purchase(self, amount):
        if self.is_frozen:
            print("Credit card is frozen.")
            return
        if amount <= 0:
            print("Invalid purchase amount.")
            return

        available_credit = (self.credit_limit - self.credit_used)
        if amount > available_credit:
            print("Credit limit exceeded.")
            return

        self.credit_used += amount
        self.add_transaction("PURCHASE", amount, "Credit card purchase")
        print(f"Purchase of ₹{amount:.2f} successful.")
        self.show_balance()

    def make_payment(self, amount):
        if self.is_frozen:
            print("Credit card is frozen.")
            return
        if amount <= 0:
            print("Invalid payment amount.")
            return
        if amount > self.credit_used:
            print("Payment cannot exceed ")
            print("outstanding credit.")
            return

        self.credit_used -= amount
        self.add_transaction("PAYMENT", amount, "Credit card payment")
        print(f"₹{amount:.2f} credit card payment successful.")
        self.show_balance()

    def check_balance(self):
        self.show_balance()
        
class User:
    def __init__(self, user_id, name, pin):
        self.user_id = user_id
        self.name = name
        self.__pin = pin
        self.accounts = {}

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "pin": self.__pin, "accounts": list(self.accounts.keys())}

    def validate_pin(self, pin):
        return pin == self.__pin

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def show_accounts(self):
        print(f"\n------ {self.name}'s Accounts ------")

        if not self.accounts:
            print("No accounts found.")
            return

        for account in self.accounts.values():
            print(f"{account.account_number} | {account.account_type}")
            
class ATM:
    def __init__(self):
        self.users = {}
        self.accounts = {}
        self.load_data()
        self.next_account_number = self.get_next_account_number()
        self.admin_username = "admin"
        self.admin_password = "admin123"
        
    def get_next_account_number(self):
        if not self.accounts:
            return 1001
        numbers = []
        for account_number in self.accounts:
            if account_number.startswith("ACC"):
                try:
                    numbers.append(int(account_number[3:]))
                except ValueError:
                    continue
        return max(numbers, default=1000) + 1
        
    def save_data(self):
        data = {"users": {user_id: user.to_dict() for user_id, user in self.users.items()}, "accounts": {account_number: account.to_dict() for account_number, account in self.accounts.items()}}
        with open(ATM_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("ATM data saved successfully.")
    
    def load_data(self):
        if not os.path.exists(ATM_FILE):
            return
        try:
            with open(ATM_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.users = {}
            self.accounts = {}
            for user_id, user_data in data.get("users", {}).items():
                user = User(user_data["user_id"], user_data["name"], user_data["pin"])
                self.users[user_id] = user

            for account_number, account_data in data.get("accounts", {}).items():
                account_type = account_data["account_type"]
                if account_type == "Savings":
                    account = SavingsAccount(account_number)
                elif account_type == "Checking":
                    account = CheckingAccount(account_number)
                elif account_type == "Credit Card":
                    account = CreditCardAccount(account_number, account_data.get("credit_limit", 50000))
                    account.credit_used = account_data.get("credit_used", 0)
                else:
                    account = BankAccount(account_number, account_type)
                account.balance = account_data.get("balance", 0)
                account.is_frozen = account_data.get("is_frozen", False)

                for transaction_data in account_data.get("transactions", []):
                    transaction = Transaction(transaction_data["transaction_type"], transaction_data["amount"], transaction_data.get("description", ""))
                    transaction.timestamp = transaction_data.get("timestamp", transaction.timestamp)
                    account.transactions.append(transaction)
                self.accounts[account_number] = account

            for user_id, user_data in data.get("users", {}).items():
                user = self.users[user_id]
                for account_number in user_data.get("accounts", []):
                    if account_number in self.accounts:
                        user.add_account(self.accounts[account_number])
            print("ATM data loaded successfully.")
        except (json.JSONDecodeError, KeyError, TypeError):
            print("ATM data file is corrupted.")
            self.users = {}
            self.accounts = {}
        
    def create_user(self):
        user_id = input("\nEnter user ID : ").strip()
        if user_id in self.users:
            print("User already exists.")
            return

        name = input("Enter name : ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        pin = input("Set 4-digit PIN : ").strip()
        if len(pin) != 4 or not pin.isdigit():
            print("PIN must contain exactly 4 digits.")
            return

        self.users[user_id] = User(user_id, name, pin)
        self.save_data()
        print("\nUser created successfully.")
            
    def authenticate_user(self):
        user_id = input("\nEnter User ID : ").strip()
        pin = input("Enter PIN : ").strip()
        user = self.users.get(user_id)
        if user and user.validate_pin(pin):
            print(f"\nWelcome, {user.name}!")
            self.user_menu(user)
        else:
            print("Invalid User ID or PIN.")
            
    def create_account(self, user):
        print("\n------ Create Account ------\n")
        print("1. Checking Account")
        print("2. Savings Account")
        print("3. Credit Card")

        choice = input("Choose account type : ").strip()

        account_number = (f"ACC{self.next_account_number}")
        self.next_account_number += 1

        if choice == "1":
            account = CheckingAccount(account_number)
        elif choice == "2":
            account = SavingsAccount(account_number)
        elif choice == "3":
            try:
                limit = float(input("Enter credit limit : "))
                if limit <= 0:
                    print("Credit limit must be positive.")
                    return
            except ValueError:
                print("Invalid credit limit.")
                return

            account = CreditCardAccount(account_number, limit)
        else:
            print("Invalid choice.")
            return

        user.add_account(account)
        self.accounts[account.account_number] = account
        self.save_data()
        print(f"\n{account.account_type} created successfully.")
        print(f"Account Number : {account.account_number}")
        
    def select_account(self, user):
        user.show_accounts()
        account_number = input("\nEnter account number : ").strip()
        account = user.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return None
        return account
    
    def user_menu(self, user):
        while True:
            print("\n------ User Dashboard ------\n")
            print("1. View Accounts")
            print("2. Create Account")
            print("3. Account Operations")
            print("4. Logout")

            choice = input("\nChoose option : ").strip()
            if choice == "1":
                user.show_accounts()
            elif choice == "2":
                self.create_account(user)
            elif choice == "3":
                account = self.select_account(user)
                if account:
                    self.account_operations(account)
            elif choice == "4":
                print("\nLogging out...")
                break
            else:
                print("Invalid choice.")
                
    def account_operations(self, account):
        while True:
            print(f"\n------{account.account_type} ------\n")
            print("1. Check Balance")
            if not isinstance(account, CreditCardAccount):
                print("2. Deposit")
                print("3. Withdraw")
            print("4. Transaction History")

            if isinstance(account, SavingsAccount):
                print("5. Add Interest")
            elif isinstance(account, CreditCardAccount):
                print("5. Make Purchase")
                print("6. Make Payment")
            print("0. Back")

            choice = input("\nChoose option : ").strip()

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter amount : "))
                    account.deposit(amount)
                    self.save_data()
                except ValueError:
                    print("Invalid amount.")
            elif choice == "3":
                try:
                    amount = float(input("Enter amount : "))
                    account.withdraw(amount)
                    self.save_data()
                except ValueError:
                    print("Invalid amount.")
            elif choice == "4":
                account.show_transactions()
            elif choice == "5" and isinstance(account, SavingsAccount):
                account.add_interest()
                self.save_data()
            elif choice == "5" and isinstance(account, CreditCardAccount):
                try:
                    amount = float(input("Purchase amount : "))
                    account.make_purchase(amount)
                    self.save_data()
                except ValueError:
                    print("Invalid amount.")
            elif choice == "6" and isinstance(account, CreditCardAccount):
                try:
                    amount = float(input("Payment amount : "))
                    account.make_payment(amount)
                    self.save_data()
                except ValueError:
                    print("Invalid amount.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
                
    def admin_login(self):
        username = input("\nAdmin username : ").strip()
        password = input("Admin password : ").strip()
        if (username == self.admin_username and password == self.admin_password):
            print("\nAdmin authentication successful.")
            self.admin_dashboard()
        else:
            print("Invalid admin credentials.")
            
    def admin_dashboard(self):
        while True:
            print("\n====== ADMIN DASHBOARD ======")
            print("1. View All Users")
            print("2. View All Accounts")
            print("3. View All Transactions")
            print("4. Freeze Account")
            print("5. Unfreeze Account")
            print("6. Logout")

            choice = input("\nChoose option : ").strip()
            if choice == "1":
                self.view_all_users()
            elif choice == "2":
                self.view_all_accounts()
            elif choice == "3":
                self.view_all_transactions()
            elif choice == "4":
                self.change_account_status(True)
            elif choice == "5":
                self.change_account_status(False)
            elif choice == "6":
                print("\nAdmin logged out.")
                break
            else:
                print("Invalid choice.")
                
    def view_all_users(self):
        print("\n------ All Users ------")
        if not self.users:
            print("No users found.")
            return

        for user in self.users.values():
            print(f"ID: {user.user_id} | Name: {user.name} | Accounts: {len(user.accounts)}")

    def view_all_accounts(self):
        print("\n------ All Accounts ------")
        for user in self.users.values():
            for account in user.accounts.values():
                print(f"User: {user.name} | Account: {account.account_number} | Type: {account.account_type} | Status: {'FROZEN' if account.is_frozen else 'ACTIVE'}")

                if isinstance(account,CreditCardAccount):
                    print(f"Credit Limit: ₹{account.credit_limit:.2f} | Used: ₹{account.credit_used:.2f}")
                else:
                    print(f"Balance: ₹{account.balance:.2f}")

    def view_all_transactions(self):
        print("\n====== ALL TRANSACTIONS ======")
        found = False
        for user in self.users.values():
            for account in user.accounts.values():
                if account.transactions:
                    found = True
                    print(f"\nUser: {user.name}")

                    print(f"Account: {account.account_number}")

                    for transaction in account.transactions:
                        transaction.display()
        if not found:
            print("No transactions found.")

    def change_account_status(self, freeze):
        account_number = input("\nEnter account number : ").strip()
        for user in self.users.values():
            account = user.accounts.get(account_number)
            if account:
                account.is_frozen = freeze
                self.save_data()
                if freeze:
                    print("Account frozen successfully.")
                else:
                    print("Account unfrozen successfully.")
                return
        print("Account not found.")
        
    def main_menu(self):
        while True:
            print("\n====== MINI BANKING SYSTEM ======")
            print("1. Create User")
            print("2. User Login")
            print("3. Admin Login")
            print("4. Exit")

            choice = input("\nChoose option : ").strip()

            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.authenticate_user()
            elif choice == "3":
                self.admin_login()
            elif choice == "4":
                print("\nThank you for using Mini Banking System.")
                break
            else:
                print("Invalid choice.")
                
if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
    
# Done