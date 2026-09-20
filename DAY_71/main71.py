# This is Day 71 project : Spam Email Detector

import pandas as pd
import re
import nltk
import tkinter as tk
from tkinter import messagebox
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

nltk.download("stopwords", quiet=True)
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "message"]
df["label"] = df["label"].map({"ham": 0, "spam": 1})

def preprocess_text(text):
    text = re.sub(r"\W", " ", text)
    text = text.lower()
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

df["cleaned_message"] = df["message"].apply(preprocess_text)

vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df["cleaned_message"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))

def predict_email(email_text):
    processed_text = preprocess_text(email_text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)
    return "SPAM" if prediction[0] == 1 else "NOT SPAM"

def check_email():
    email_text = email_input.get("1.0", tk.END).strip()
    if not email_text:
        messagebox.showwarning("Empty Input", "Please enter an email message.")
        return

    result = predict_email(email_text)
    if result == "SPAM":
        result_label.config(text="⚠ SPAM EMAIL", fg="#ff4d4d")
    else:
        result_label.config(text="✓ NOT SPAM", fg="#2ecc71")

def clear_email():
    email_input.delete("1.0", tk.END)
    result_label.config(text="Enter an email to check", fg="#ffffff")

root = tk.Tk()
root.title("Spam Email Detector")
root.geometry("700x550")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="Spam Email Detector", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="#ffffff")
title_label.pack(pady=(30, 5))

subtitle_label = tk.Label(root, text="Machine Learning based Email Classification", font=("Arial", 11), bg="#1e1e1e", fg="#aaaaaa")
subtitle_label.pack(pady=(0, 25))

email_label = tk.Label(root, text="Enter Email Message", font=("Arial", 13, "bold"), bg="#1e1e1e", fg="#ffffff")
email_label.pack(anchor="w", padx=50)

email_input = tk.Text(root, height=10, width=70, font=("Arial", 11), bg="#2b2b2b", fg="#ffffff", insertbackground="#ffffff", relief="flat", padx=10, pady=10, wrap="word")
email_input.pack(padx=50, pady=10)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=15)

check_button = tk.Button(button_frame, text="Check Email", command=check_email, font=("Arial", 11, "bold"), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", relief="flat", padx=25, pady=10, cursor="hand2")
check_button.pack(side="left", padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_email, font=("Arial", 11, "bold"), bg="#555555", fg="white", activebackground="#444444", activeforeground="white", relief="flat", padx=30, pady=10, cursor="hand2")
clear_button.pack(side="left", padx=10)

result_label = tk.Label(root, text="Enter an email to check", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#ffffff")
result_label.pack(pady=15)

accuracy_label = tk.Label(root, text=f"Model Accuracy: {accuracy * 100:.2f}%", font=("Arial", 10), bg="#1e1e1e", fg="#aaaaaa")
accuracy_label.pack(pady=5)

root.mainloop()

# Done