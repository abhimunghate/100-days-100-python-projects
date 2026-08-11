# This is Day 31 project : BMI Calculator

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x500")
root.configure(bg="#f0f4c3")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def get_bmi_tip(status):
    tips = {
        "Underweight":
            "Tip: Focus on a balanced, nutritious diet and consider consulting a healthcare professional.",
        "Normal weight":
            "Tip: Maintain a balanced diet, regular physical activity, and a healthy lifestyle.",
        "Overweight":
            "Tip: Focus on balanced meals, regular physical activity, and gradual healthy lifestyle changes.",
        "Obesity":
            "Tip: Consider discussing a healthy weight-management plan with a healthcare professional."
    }
    return tips.get(status, "")

title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

weight_label = tk.Label(root, text="Enter your weight (kg) : ", font=("Arial", 12), bg="#f0f4c3")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 12), width=15)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Enter your height (m) : ", font=("Arial", 12), bg="#f0f4c3")
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 12), width=15)
height_entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f4c3")
result_label.pack(pady=20)

tip_label = tk.Label(root, text="", font=("Arial", 10), bg="#f0f4c3", wraplength=420, justify="center")
tip_label.pack(pady=5)

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be greater than 0.")
            return
        
        bmi = weight / (height ** 2)
        status = get_bmi_category(bmi)
        tip = get_bmi_tip(status)
            
        result_label.config(text=f"BMI : {bmi:.2f}\nStatus : {status}", fg="green")
        tip_label.config(text=tip)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")
        
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Arial", 12), bg="#4caf50", fg="black")
calculate_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text=""), tip_label.config(text="")], font=("Arial", 12), bg="#f44336", fg="white")
reset_button.pack(pady=5)

root.mainloop()

# Done