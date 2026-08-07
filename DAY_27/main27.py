# This is Day 27 project : Inventory Management System

import json
import csv
from datetime import datetime, timedelta

INVENTORY_FILE = "inventory.json"
LOW_STOCK_THRESHOLD = 5

class Inventory:
    total_items = 0
    
    def __init__(self, product_name, price, quantity, is_perishable=False, expiry_date=None):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.is_perishable = is_perishable
        self.expiry_date = expiry_date
        Inventory.total_items += quantity
        
    def to_dict(self): 
        return {"product_name": self.product_name, "price": self.price, "quantity": self.quantity, "is_perishable": self.is_perishable, "expiry_date": self.expiry_date }
        
    def show_product_details(self):
        print("\n------ Product Details ------\n")
        print(f"Product Name : {self.product_name}")
        print(f"Price : ${self.price:.2f}")
        print(f"Quantity : {self.quantity}")
        
        if self.is_perishable:
            print(f"\nPerishable : Yes")
            print(f"Expiry Date : {self.expiry_date}")
        else:
            print("Perishable : No")
        
    def sell_product(self, amount):
        if amount <= 0:
            print("Sale amount must be greater than 0.")
            return False
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount
            print(f"\n{amount} {self.product_name}(s) sold.")
            self.check_low_stock()
            save_inventory()
            return True
        print("Insufficient quantity.")
        return False
            
    def check_low_stock(self):
        if self.quantity == 0:
            print(f"\n⚠ OUT OF STOCK:")
            print(f"{self.product_name} is completely out of stock.")
        elif 0 < self.quantity <= LOW_STOCK_THRESHOLD:
            print(f"\n⚠ Low stock alert : ")
            print(f"{self.product_name} has only {self.quantity} item(s) left.")
            
    def check_expiry(self):
        if not self.is_perishable or not self.expiry_date:
            return
        try:
            today = datetime.today().date()
            expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
        except ValueError:
            print(f"Invalid expiry date for {self.product_name}.")
            return

        if expiry < today:
            print(f"\n⚠ EXPIRED: {self.product_name} ")
            print(f"Expired on {self.expiry_date}.")
        elif expiry == today:
            print(f"\n⚠ EXPIRING TODAY: {self.product_name}.")
        else:
            remaining_days = (expiry - today).days
            if remaining_days <= 3:
                print(f"\n⚠ EXPIRY ALERT: {self.product_name} ")
                print(f"Expires in {remaining_days} day(s).")
            
    @staticmethod
    def calculate_discount(price, discount_percentage):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount must be between 0 and 100.")
        return price * (1 - discount_percentage / 100)
    
    @classmethod
    def total_items_report(cls):
        print(f"\nTotal Items : {cls.total_items}")
        
products = []

def save_inventory():
    data = [product.to_dict() for product in products]
    with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("\nInventory saved successfully.")
    
def load_inventory():
    global products
    products.clear()
    Inventory.total_items = 0
    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("\nNo existing inventory found.")
        print("Starting with an empty inventory.")
        return
    except json.JSONDecodeError:
        print("Inventory file is corrupted.")
        print("Starting with an empty inventory.")
        return

    for item in data:
        try:
            product = Inventory(item["product_name"], item["price"], item["quantity"], item.get("is_perishable", False), item.get("expiry_date"))
            products.append(product)
        except (KeyError, TypeError, ValueError):
            print("Skipping invalid product record.")
    print(f"{len(products)} product type(s) loaded successfully.")
    
def export_csv():
    if not products:
        print("No products to export.")
        return

    with open("inventory.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Quantity", "Perishable", "Expiry Date"])

        for product in products:
            writer.writerow([product.product_name, product.price, product.quantity, product.is_perishable, product.expiry_date])
    print("Inventory exported to inventory.csv successfully.")
    
def check_inventory_alerts():
    if not products:
        print("\nNo products in inventory.")
        return
    print("\n------ Inventory Alerts ------")
    alerts_found = False
    today = datetime.today().date()
    for product in products:
        if 0 < product.quantity <= LOW_STOCK_THRESHOLD:
            print(f"\n⚠ Low stock: {product.product_name} ")
            print(f"Has only {product.quantity} item(s).")
            alerts_found = True

        if product.is_perishable:
            if not product.expiry_date:
                print(f"\n⚠ Missing expiry date: ")
                print(f"{product.product_name}")
                alerts_found = True
                continue
            try:
                expiry = datetime.strptime(product.expiry_date, "%Y-%m-%d").date()
            except (ValueError, TypeError):
                print(f"⚠ Invalid expiry date for ")
                print(f"{product.product_name}.")
                alerts_found = True
                continue
            
            remaining_days = (expiry - today).days
            if remaining_days < 0:
                print(f"\n⚠ EXPIRED : {product.product_name} ")
                print(f"Expired on {product.expiry_date}.")
                alerts_found = True
            elif remaining_days == 0:
                print(f"\n⚠ EXPIRING TODAY : ")
                print(f"{product.product_name}.")
                alerts_found = True
            elif remaining_days <= 3:
                print(f"\n⚠ Expiry alert: ")
                print(f"{product.product_name}")
                print(f"Expires in {remaining_days} day(s).")
                alerts_found = True

    if not alerts_found:
        print("No inventory alerts.")

def add_product():
    product_name = input("\nEnter product name : ").strip()
    if not product_name:
        print("Product name cannot be empty.")
        return
    try:
        price = float(input("Enter price : ").strip())
        if price <= 0:
            print("Price must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid price.")
        return
    try:
        quantity = int(input("Enter quantity : ").strip())
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid quantity.")
        return
    
    perishable_input = input("Is this a perishable item? (y/n) : ").strip().lower()
    if perishable_input not in ("y", "n"):
        print("Please enter y or n.")
        return
    
    is_perishable = perishable_input == "y"
    expiry_date = None
    
    if is_perishable:
        try:
            days = int(input("How many days will it last? : ").strip())
            if days <= 0:
                print("Number of days must be greater than 0.")
                return
            expiry_date = (datetime.today().date() + timedelta(days=days)).isoformat()
        except ValueError:
            print("Please enter a valid number of days.")
            return
    
    for product in products:
        if product.product_name.lower() == product_name.lower():
            product.quantity += quantity
            Inventory.total_items += quantity
            
            product.price = price
            product.is_perishable = is_perishable
            product.expiry_date = expiry_date
            
            print(f"\n{quantity} more {product_name}(s) added.")
            print(f"Total quantity : {product.quantity}")
            
            if product.is_perishable: 
                print(f"Perishable : Yes")
                print(f"Expiry Date : {product.expiry_date}")
            else:
                print("Perishable : No")
            product.check_low_stock()
            save_inventory()
            return
    
    product = Inventory(product_name, price, quantity, is_perishable, expiry_date)
    products.append(product)
    print(f"\n{quantity} {product_name}(s) added to inventory.")
    if product.is_perishable:
        print("Perishable : Yes")
        print(f"Expiry Date : {product.expiry_date}")
    else:
        print("Perishable : No")
    product.check_low_stock()
    save_inventory()
    
def view_products():
    print("\n------ Inventory ------\n")
    if not products:
        print("No products in inventory.")
        return
    
    print(f"Total Product Types : {len(products)}")
    for product in products:
        product.show_product_details()
        product.check_low_stock()
        product.check_expiry()
            
def sell_product():
    product_name = input("\nEnter product name to sell : ").strip()
    if not product_name:
        print("Product name cannot be empty.")
        return
    for product in products:
        if product.product_name.lower() == product_name.lower():
            try:
                amount = int(input("Enter amount to sell : "))
                if amount <= 0:
                        print("Amount must be greater than 0.")
                        return
            except ValueError:
                print("Please enter a valid amount.")
                return
            product.sell_product(amount)
            return
    print("Product not found in inventory.")
            
def discount_price():
    try:
        price = float(input("\nEnter price : ").strip())
        if price <= 0:
            print("Price must be greater than 0.")
            return
        
        discount_percentage = float(input("Enter discount percentage : ").strip())
        if discount_percentage < 0 or discount_percentage > 100:
            print("Discount must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid numbers.")
        return
    discounted_price = Inventory.calculate_discount(price, discount_percentage)
    print(f"\nDiscounted Price : ${discounted_price:.2f}")
    
load_inventory()
check_inventory_alerts()
    
while True:
    print("\n------ Inventory Management System ------\n")
    print("1. Add Product")
    print("2. View Products")
    print("3. Sell Product")
    print("4. Calculate Discount")
    print("5. Total Items Report")
    print("6. Export Inventory to CSV")
    print("7. Check Inventory Alerts")
    print("8. Exit")
    
    choice = input("\nEnter your choice (1-8) : ").strip()
    
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        sell_product()
    elif choice == "4":
        discount_price()
    elif choice == "5":
        Inventory.total_items_report()
    elif choice == "6":
        export_csv()
    elif choice == "7":
        check_inventory_alerts()
    elif choice == "8":
        print("\nExiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        
# Done