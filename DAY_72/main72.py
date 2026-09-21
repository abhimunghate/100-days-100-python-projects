# This is Day 72 project : Text Sentiment Analyzer

import tkinter as tk
from tkinter import messagebox
from sentiment_model import predict_sentiment, accuracy

def analyze_sentiment():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text.")
        return

    sentiment, confidence = predict_sentiment(text)
    if sentiment == "positive":
        result = "Positive 😊"
        result_color = "#2ecc71"
    elif sentiment == "negative":
        result = "Negative 😡"
        result_color = "#e74c3c"
    else:
        result = "Neutral 😐"
        result_color = "#f1c40f"

    result_label.config(text=result, fg=result_color)
    confidence_label.config(text=f"Confidence: {confidence:.2f}%")

def clear_text():
    text_input.delete("1.0", tk.END)
    result_label.config(text="Enter text to analyze", fg="white")
    confidence_label.config(text="")

root = tk.Tk()
root.title("Text Sentiment Analyzer")
root.geometry("700x600")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="Text Sentiment Analyzer", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=(30, 5))

subtitle_label = tk.Label(root, text="Custom Machine Learning Sentiment Classifier", font=("Arial", 11), bg="#1e1e1e", fg="#aaaaaa")
subtitle_label.pack(pady=(0, 25))

input_label = tk.Label(root, text="Enter Text", font=("Arial", 13, "bold"), bg="#1e1e1e", fg="white")
input_label.pack(anchor="w", padx=50)

text_input = tk.Text(root, height=10, width=70, font=("Arial", 11), bg="#2b2b2b", fg="white", insertbackground="white", relief="flat", padx=10, pady=10, wrap="word")
text_input.pack(padx=50, pady=10)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=15)

analyze_button = tk.Button(button_frame, text="Analyze Sentiment", command=analyze_sentiment, font=("Arial", 11, "bold"), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", relief="flat", padx=25, pady=10, cursor="hand2")
analyze_button.pack(side="left", padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text, font=("Arial", 11, "bold"), bg="#555555", fg="white", activebackground="#444444", activeforeground="white", relief="flat", padx=30, pady=10, cursor="hand2")
clear_button.pack(side="left", padx=10)

result_label = tk.Label(root, text="Enter text to analyze", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white")
result_label.pack(pady=15)

confidence_label = tk.Label(root, text="", font=("Arial", 11), bg="#1e1e1e", fg="#aaaaaa")
confidence_label.pack(pady=5)

accuracy_label = tk.Label(root, text=f"Model Accuracy: {accuracy * 100:.2f}%", font=("Arial", 10), bg="#1e1e1e", fg="#aaaaaa")
accuracy_label.pack(pady=5)

root.mainloop()

# Done