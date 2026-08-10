# This is Day 30 project : Click Counter App

import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Click Counter App")
root.geometry("500x450")
root.configure(bg="#e3f2fd")

counter = 0
highest = 0

start_time = datetime.now()

def increment():
    global counter, highest
    counter += 1
    
    if counter > highest:
        highest = counter
        highest_score.config(text=f"Highest Score : {highest}")
    
    counter_label.config(text=f"Clicks : {counter}")
    
def decrement():
    global counter
    if counter > 0:
        counter -= 1
    counter_label.config(text=f"Clicks : {counter}")
    
def reset():
    global counter
    counter = 0
    counter_label.config(text="Clicks : 0")
    
def exit_app():
    end_time = datetime.now()
    runtime = end_time - start_time
    
    print(f"\nApplication was running for: {runtime}")
    print(f"Highest Score: {highest}")
    root.destroy()
    
title_label = tk.Label(root, text="Click Counter", font=("Arial", 20), bg="#e3f2fd")
title_label.pack(pady=20)

highest_score = tk.Label(root, text="Highest Score : 0", font=("Arial", 16), bg="#e3f2fd")
highest_score.pack(pady=20)

counter_label = tk.Label(root, text="Clicks : 0", font=("Arial", 16), bg="#e3f2fd")
counter_label.pack(pady=10)

increment_button = tk.Button(root, text="Increment", command=increment, font=("Arial", 14), bg="#4caf50", fg="black")
increment_button.pack(pady=10)

decrement_button = tk.Button(root, text="Decrement", command=decrement, font=("Arial", 14), bg="#ff9800", fg="black")
decrement_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 14), bg="#f44336", fg="black")
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app, font=("Arial", 14), bg="#607d8b", fg="black")
exit_button.pack(pady=20)

root.mainloop()

# Done