# This is Day 11 project : Safe Calculator

import time

LOG_FILE = "error_log.txt"

def log_error(error_type, error_message):
    timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
    
    with open(LOG_FILE, 'a') as file:
        file.write(f"[{timestamp}] {error_type} : {error_message}\n")

def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def modulus(x,y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x % y

def exponentiation(x,y):
    return x ** y

def show_menu():
    print("\n------ Safe Calculator Menu ------\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Exit")
    
while True:
    show_menu()
    choice = input("\nEnter your choice (1-7) : ")
    
    if choice == "7":
        print("\nExiting the calculator. Goodbye!")
        break
    
    elif choice not in ["1", "2", "3", "4", "5", "6"]:
        print("\nInvalid choice")
        continue
    
    try:
        num1 = float(input("\nEnter first number : "))
        num2 = float(input("Enter second number : "))
        
        if choice == "1":
            print("\nResult : ", add(num1,num2))
        elif choice == "2":
            print("\nResult : ", subtract(num1,num2))
        elif choice == "3":
            print("\nResult : ", multiply(num1,num2))
        elif choice == "4":
            print("\nResult : ", divide(num1,num2))
        elif choice == "5":
            print("\nResult : ", modulus(num1,num2))
        elif choice == "6":
            print("\nResult : ", exponentiation(num1,num2))
            
    except ValueError as e:
        print("Invalid input. Please enter valid numbers.")
        log_error("ValueError", str(e))
        
    except ZeroDivisionError as e:
        print(f"Error : {e}")
        log_error("ZeroDivisionError", str(e))
        
    except Exception as e:
        print(f"An unexpected error occurred : {e}")
        log_error(type(e).__name__, str(e))
        
    finally:
        print("\n----------------------------------------")
        
# Done