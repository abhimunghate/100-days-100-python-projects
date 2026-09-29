# This is Day 80 project : Fake News Detector
# Tkinter GUI

import os
import re
import joblib
import nltk
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

MODEL_PATH = "models/fake_news_model.pkl"
VECTORIZER_PATH = ("models/tfidf_vectorizer.pkl")

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

try:
    nltk.download("punkt_tab", quiet=True)
except Exception:
    pass

stop_words = set(stopwords.words("english"))

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except FileNotFoundError:
    model = None
    vectorizer = None

def clean_text(text):
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    return " ".join(tokens)

def predict_news():
    if model is None or vectorizer is None:
        messagebox.showerror("Model Not Found", "Please train the model first using:\n\n python train_model.py")
        return

    title = title_entry.get().strip()
    article = article_text.get("1.0", tk.END).strip()
    if not title and not article:
        messagebox.showwarning("Input Required", "Please enter a news headline or article.")
        return

    combined_text = (title + " " + article)
    cleaned = clean_text(combined_text)
    if not cleaned:
        messagebox.showwarning("Invalid Input", "The provided text could not be processed.")
        return

    try:
        features = vectorizer.transform([cleaned])
        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]
        confidence = max(probabilities) * 100

        if prediction == 1:
            result = "REAL NEWS"
        else:
            result = "FAKE NEWS"

        result_label.config(text=result)
        confidence_label.config(text=f"Model confidence: {confidence:.2f}%")
        status_label.config(text="Prediction completed.")
    except Exception as error:
        messagebox.showerror("Prediction Error", str(error))

def load_file():
    file_path = filedialog.askopenfilename(title="Select News Text File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        article_text.delete("1.0", tk.END)
        article_text.insert(tk.END, content)
        status_label.config(text="Text file loaded.")
    except Exception as error:
        messagebox.showerror("File Error", str(error))

def clear_all():
    title_entry.delete(0, tk.END)
    article_text.delete("1.0", tk.END)
    result_label.config(text="---")
    confidence_label.config(text="Model confidence: ---")
    status_label.config(text="Ready")

root = tk.Tk()
root.title("Day 80 - Fake News Detector")
root.geometry("800x700")
root.minsize(700, 600)

title_label = tk.Label(root, text="📰 Fake News Detector", font=("Arial", 24, "bold"))
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(root, text=("Machine-learning based news classification using TF-IDF + Random Forest"), font=("Arial", 11))
subtitle_label.pack(pady=(0, 20))

headline_label = tk.Label(root, text="News Headline", font=("Arial", 12, "bold"))
headline_label.pack(anchor="w", padx=35)

title_entry = tk.Entry(root, font=("Arial", 11))
title_entry.pack(fill="x", padx=35, pady=8)

article_label = tk.Label(root, text="News Article", font=("Arial", 12, "bold"))
article_label.pack(anchor="w", padx=35)

article_frame = tk.Frame(root)
article_frame.pack(fill="x", padx=35, pady=8)

scrollbar = tk.Scrollbar(article_frame)
scrollbar.pack(side="right", fill="y")

article_text = tk.Text(article_frame, height=22, wrap="word", font=("Arial", 11), yscrollcommand=scrollbar.set)
article_text.pack(side="left", fill="x", expand=True)

scrollbar.config(command=article_text.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

predict_button = tk.Button(button_frame, text="Check News", command=predict_news, font=("Arial", 12, "bold"), width=18)
predict_button.grid(row=0, column=0, padx=5)

load_button = tk.Button(button_frame, text="Load .TXT", command=load_file, width=15)
load_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_all, width=15)
clear_button.grid(row=0, column=2, padx=5)

result_title = tk.Label(root, text="Prediction", font=("Arial", 12, "bold"))
result_title.pack(pady=(5, 2))

result_label = tk.Label(root, text="---", font=("Arial", 22, "bold"))
result_label.pack()

confidence_label = tk.Label(root, text="Model confidence: ---", font=("Arial", 11))
confidence_label.pack(pady=5)

disclaimer = tk.Label(root, text=("Note: This is a machine-learning prediction, not a factual verification service."), font=("Arial", 9))
disclaimer.pack(pady=5)

status_label = tk.Label(root, text="Ready", font=("Arial", 10))
status_label.pack(pady=(5, 10))

root.mainloop()

# Done