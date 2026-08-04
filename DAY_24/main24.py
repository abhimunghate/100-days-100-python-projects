# This is Day 24 project : Employee Management System

import json
import os

EMPLOYEE_FILE = "employees.json"

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        
    def display_info(self):
        print("\n------ Employee Details ------\n")
        print(f"Name : {self.name}")
        print(f"Employee ID : {self.emp_id}")
        print(f"Salary : ${self.salary:.2f}")
        print(f"Employee Type : {type(self).__name__}")
        
    def calculate_bonus(self):
        return self.salary * 0.1
    
    def to_dict(self):
        return {"type": type(self).__name__, "name": self.name, "emp_id": self.emp_id, "salary": self.salary}
    
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f"Department : {self.department}")
        
    def calculate_bonus(self):
        return self.salary * 0.2
    
    def to_dict(self):
        data = super().to_dict()
        data["department"] = self.department
        return data
    
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language
        
    def display_info(self):
        super().display_info()
        print(f"Programming language : {self.programming_language}")
        
    def calculate_bonus(self):
        return self.salary * 0.5
    
    def to_dict(self):
        data = super().to_dict()
        data["programming_language"] = self.programming_language
        return data
    
class Intern(Employee):
    STIPEND = 15000

    def __init__(self, name, emp_id, duration):
        super().__init__(name, emp_id, Intern.STIPEND)
        self.duration = duration

    def display_info(self):
        print("\n------ Employee Details ------\n")
        print(f"Name : {self.name}")
        print(f"Employee ID : {self.emp_id}")
        print(f"Employee Type : Intern")
        print(f"Monthly Stipend : ${self.salary:.2f}")
        print(f"Duration : {self.duration} months")

    def calculate_bonus(self):
        return 0
    
    def to_dict(self):
        data = super().to_dict()
        data["duration"] = self.duration
        return data

def save_employees():
    with open(EMPLOYEE_FILE, "w", encoding="utf-8") as file:
        json.dump([employee.to_dict() for employee in employees], file, indent=4, ensure_ascii=False)
        
def load_employees():
    employees.clear()

    if not os.path.exists(EMPLOYEE_FILE):
        return

    try:
        with open(EMPLOYEE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    for item in data:
        employee_type = item["type"]
        if employee_type == "Employee":
            employee = Employee(item["name"], item["emp_id"], item["salary"])
        elif employee_type == "Manager":
            employee = Manager(item["name"], item["emp_id"], item["salary"], item["department"])
        elif employee_type == "Developer":
            employee = Developer(item["name"], item["emp_id"], item["salary"], item["programming_language"])
        elif employee_type == "Intern":
            employee = Intern(item["name"], item["emp_id"], item["duration"])
        else:
            continue
        employees.append(employee)
        
employees = []

load_employees()

def get_salary():
    while True:
        try:
            salary = float(input("Enter Employee Salary : "))
            if salary < 0:
                print("Salary cannot be negative.")
            else:
                return salary
        except ValueError:
            print("Please enter a valid salary.")

def add_employee():
    print("\n------ Choose Employee Type ------\n")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")
    print("4. Intern")
    try:
        choice = int(input("\nEnter your choice : ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return
    
    name = input("\nEnter Employee Name : ").strip().title()
    if not name:
        print("Employee name cannot be empty.")
        return

    emp_id = input("Enter Employee ID : ").strip()
    if not emp_id:
        print("Employee ID cannot be empty.")
        return
    
    for employee in employees:
        if employee.emp_id == emp_id:
            print("Employee ID already exists.")
            return
    
    if choice == 1:
        salary = get_salary()
        employees.append(Employee(name, emp_id, salary))
    elif choice == 2:
        salary = get_salary()
        department = input("Enter Department : ").strip().title()
        if not department:
            print("Department cannot be empty.")
            return
        employees.append(Manager(name, emp_id, salary, department))
    elif choice == 3:
        salary = get_salary()
        programming_language = input("Enter Programming Language : ").strip().title()
        if not programming_language:
            print("Programming language cannot be empty.")
            return
        employees.append(Developer(name, emp_id, salary, programming_language))
    elif choice == 4:
        try:
            duration = int(input("Enter Internship Duration (months) : "))
            if duration <=0:
                print("Duration must be a greater than 0.")
                return
        except ValueError:
            print("Please enter a valid duration.")
            return
            
        employees.append(Intern(name, emp_id, duration))
    else:
        print("Invalid choice")
        
    save_employees()
    print("\nEmployee added successfully!")
        
def display_all_employees():
    print("\n------ All Employees ------")
    if not employees:
        print("No employees found.")
        return
    
    print(f"\nTotal Employees : {len(employees)}")
    
    for employee in employees:
        employee.display_info()
        print(f"Bonus : ${employee.calculate_bonus():.2f}")
        
def search_employee():
    emp_id = input("\nEnter Employee ID : ").strip().lower()

    for employee in employees:
        if employee.emp_id.lower() == emp_id.lower():
            employee.display_info()
            print(f"Bonus : ${employee.calculate_bonus():.2f}")
            return
    print("Employee not found.")
            
while True:
    print("\n------ Employee Management System ------\n")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Exit")
    try:
        choice = int(input("\nEnter your choice (1-4) : ").strip())
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        print("\nExiting the program.")
        break
    else:
        print("Invalid choice")
        
# Done