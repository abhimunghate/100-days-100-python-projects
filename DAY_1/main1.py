# This is Day 1 project : Welcome Message Generator

import time

name = (input("What is your name? : ").upper())
hobby = (input("What is your favorite hobby? : ").upper())
color = (input("What is your favorite color? : ").upper())

print("\n------ Welcome Message ------\n")
print("Current time is : ",time.strftime("%H:%M:%S"))
print(f"Hello, {name}!🙂 Welcome to the world of Python programming.")
print(f"It's great to know that you love {hobby}.")
print(f"Your favorite color is {color}, which is a beautiful choice!")
print("Get ready to build something amazing today.")

# Done