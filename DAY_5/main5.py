# This is Day 5 project : Countdown Timer

import time

start = int(input("Enter the number to start the countdown from : "))
n = float(input("Enter the number of seconds to delay the timer (e.g. 0.5s, 1s, 1.5s,...) : "))
custom_message = input("Enter the message to display when the countdown ends : ")
half = (start // 2) + 1

if start > 0:
    print("\n------ Countdown Begins ------\n")
    while start > 0:
        print(start)
        time.sleep(n)
        
        if start == half:
            print("You are Halfway there! 👋")
            
        start -= 1
        
    print(f"\n{custom_message}")
    print("\nCountdown Finished! 🎉")

elif start == 0:
    print("\nPlease enter a number greater than 0.")
elif start < 0:
    print("\nStarting number cannot be negative.")

# Done