# This is Day 22 project : Bank Account Simulator

class BankAccount:
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.history = []
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
            print(f"Current balance : ${self.balance:.2f}")
            self.history.append(f"Deposited ${amount:.2f} | Balance : ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"New balance : ${self.balance:.2f}")
            self.history.append(f"Withdrew ${amount:.2f} | Balance : ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            
    def show_history(self):
        print("\n------ Transaction History ------\n")
        if not self.history:
            print("No transactions yet.")
            return
        for transaction in self.history:
            print(transaction)
            
    def add_interest(self, rate=4):
        interest = self.balance * rate / 100
        if self.balance <=0:
            print("Interest cannot be applied.")
            return
        self.balance += interest
        self.history.append(f"Interest {rate}% added | +${interest:.2f} | Balance : ${self.balance:.2f}")
        print(f"Interest Added : ${interest:.2f}")
        print(f"New Balance : ${self.balance:.2f}")
            
    def show_details(self):
        print("\n------ Account Details ------\n")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Balance : ${self.balance:.2f}")
            
accounts = {}

def create_account():
    name = input("\nEnter account holder's name : ").strip().title()
    if not name:
        print("Account holder name cannot be empty.")
        return
    try:
        initial_deposit = float(input("Enter initial Deposit Amount : "))
        
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return
    if name in accounts:
        print("Account already exists.")
        return
    account = BankAccount(name, initial_deposit)
    accounts[name] = account
    account.history.append(f"Account created | Initial Balance : ${initial_deposit:.2f}")
    print("\nAccount created successfully!")
    
def transfer_money(sender):
    receiver_name = input("\nEnter receiver name: ").strip().title()
    if receiver_name not in accounts:
        print("Receiver account not found.")
        return
        
    if receiver_name == sender.account_holder:
        print("You cannot transfer money to yourself.")
        return
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return
    
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    if amount > sender.balance:
        print("Insufficient balance.")
        return
    sender.balance -= amount
    accounts[receiver_name].balance += amount
    
    print(f"\nTransferred ${amount:.2f} to {receiver_name}.")
    print(f"Current Balance : ${sender.balance:.2f}")
    
    sender.history.append(f"Transferred ${amount:.2f} to {receiver_name} | Balance : ${sender.balance:.2f}")
    accounts[receiver_name].history.append(f"Received ${amount:.2f} from {sender.account_holder} | Balance : ${accounts[receiver_name].balance:.2f}")
    
def access_account():
    name = input("\nEnter your name : ").strip().title()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n------ Account Menu ------\n")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer Money")
            print("4. Add Interest")
            print("5. Show Details")
            print("6. Transaction History")
            print("7. Exit")
            choice = input("\nEnter your choice (1-7) : ")
            
            if choice == "1":
                try:
                    amount = float(input("\nEnter deposit amount : "))
                except ValueError:
                    print("Please enter a valid amount.")
                    continue
                account.deposit(amount)
            elif choice == "2":
                try:
                    amount = float(input("\nEnter withdrawal amount : "))
                except ValueError:
                    print("Please enter a valid amount.")
                    continue
                account.withdraw(amount)
            elif choice == "3":
                transfer_money(account)
            elif choice == "4":
                account.add_interest()
            elif choice == "5":
                account.show_details()
            elif choice == "6":
                account.show_history()
            elif choice == "7":
                print("Exiting account menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("\nAccount not found. Please create an account first.")
    
while True:
    print("\n------ Bank Account Simulator ------\n")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    choice = input("\nEnter your choice (1-3) : ")
    
    if choice == "1":
        create_account()
    elif choice == "2":
        access_account()
    elif choice == "3":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        
# Done