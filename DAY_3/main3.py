# This is Day 3 project : Simple Calculator

num1 = float(input("Enter the first number  : "))
num2 = float(input("Enter the second number : "))

operation = input("Enter the operation (+, -, *, /, //, %, **) : ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
elif operation == "%":
    result = num1 % num2 if num2 != 0 else "undefined (cannot divide by zero)"
elif operation == "**":
    result = num1 ** num2
elif operation == "//":
    result = num1 // num2 if num2 != 0 else "undefined (cannot divide by zero)"
else:
    result = "Invalid operation"

print("\n------ Selected Operation ------")
print(f"{num1} {operation} {num2} = {result}")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
floor_div = num1 // num2 if num2 != 0 else "undefined (cannot divide by zero)"
modulus = num1 % num2 if num2 != 0 else "undefined (cannot divide by zero)"
exponential = num1 ** num2

print("\n------ Calculator Results ------\n")
print(f"Addition       : {num1} + {num2} = {addition}")
print(f"Subtraction    : {num1} - {num2} = {subtraction}")
print(f"Multiplication : {num1} * {num2} = {multiplication}")
print(f"Division       : {num1} / {num2} = {division}")
print(f"Modulus        : {num1} % {num2} = {modulus}")
print(f"Exponential    : {num1} **{num2} = {exponential}")
print(f"Floor Division : {num1} //{num2} = {floor_div}")
print("\n--------------------------------\n")