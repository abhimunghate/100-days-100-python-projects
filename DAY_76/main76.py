# This is Day 76 project : Hybrid Book Recommendation System

import os
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

BOOKS_FILE = os.path.join(DATA_DIR, "books.csv")
RATINGS_FILE = os.path.join(DATA_DIR, "ratings.csv")

CONTENT_RECOMMENDATIONS = 5
USER_RECOMMENDATIONS = 5
SIMILAR_USERS = 20

books_df = None
ratings_df = None

book_indices = None
tfidf_matrix = None

rating_matrix = None
user_ids = None
user_to_index = None

book_id_to_index = None
book_index_to_id = None

book_titles = []
user_list = []

def load_data():
    """Load books and ratings from the dataset."""
    global books_df
    global ratings_df
    global book_indices
    global tfidf_matrix
    global rating_matrix
    global user_ids
    global user_to_index
    global book_id_to_index
    global book_index_to_id
    global book_titles
    global user_list

    try:
        if not os.path.exists(BOOKS_FILE):
            raise FileNotFoundError(f"Could not find:\n{BOOKS_FILE}")
        if not os.path.exists(RATINGS_FILE):
            raise FileNotFoundError(f"Could not find:\n{RATINGS_FILE}")
        status_label.config(text="Loading books...")

        books_df = pd.read_csv(BOOKS_FILE)
        required_book_columns = ["book_id", "title", "authors"]
        for column in required_book_columns:
            if column not in books_df.columns:
                raise ValueError(f"Missing column '{column}' in books.csv")

        books_df = books_df[["book_id", "title", "authors", "average_rating", "ratings_count", "original_publication_year"]].copy()
        books_df["title"] = books_df["title"].fillna("")
        books_df["authors"] = books_df["authors"].fillna("")
        books_df["average_rating"] = pd.to_numeric(books_df["average_rating"], errors="coerce").fillna(0)
        books_df["ratings_count"] = pd.to_numeric(books_df["ratings_count"], errors="coerce").fillna(0)
        books_df["original_publication_year"] = pd.to_numeric(books_df["original_publication_year"], errors="coerce").fillna(0)

        books_df["content"] = (books_df["title"] + " " + books_df["authors"])

        status_label.config(text="Building content-based recommendation model...")
        vectorizer = TfidfVectorizer(stop_words="english", max_features=20000)
        tfidf_matrix = vectorizer.fit_transform(books_df["content"])

        book_indices = pd.Series(books_df.index, index=books_df["title"]).drop_duplicates()

        status_label.config(text="Loading ratings...")
        ratings_df = pd.read_csv(RATINGS_FILE,usecols=["user_id", "book_id", "rating"], dtype={"user_id": "int32", "book_id": "int32", "rating": "int8"})

        status_label.config(text="Preparing collaborative filtering model...")

        user_ids = ratings_df["user_id"].unique()
        book_ids = books_df["book_id"].values

        user_to_index = {user_id: index for index, user_id in enumerate(user_ids)}
        book_id_to_index = {book_id: index for index, book_id in enumerate(book_ids)}
        book_index_to_id = {index: book_id for book_id, index in book_id_to_index.items()}

        ratings_df = ratings_df[ratings_df["book_id"].isin(book_id_to_index)].copy()

        row_indices = ratings_df["user_id"].map(user_to_index)
        col_indices = ratings_df["book_id"].map(book_id_to_index)

        valid = (row_indices.notna() & col_indices.notna())

        row_indices = row_indices[valid].astype(int).values
        col_indices = col_indices[valid].astype(int).values
        rating_values = ratings_df.loc[valid, "rating"].astype(np.float32).values

        from scipy.sparse import csr_matrix
        rating_matrix = csr_matrix((rating_values, (row_indices, col_indices)), shape=(len(user_ids), len(book_ids)), dtype=np.float32)

        book_titles = books_df["title"].tolist()
        user_list = [str(user_id) for user_id in user_ids]

        book_combo["values"] = book_titles
        user_combo["values"] = user_list

        if book_titles:
            book_combo.current(0)

        if user_list:
            user_combo.current(0)

        status_label.config(text=(f"Loaded {len(books_df):,} books and {len(ratings_df):,} ratings."))

        recommend_book_button.config(state="normal")
        recommend_user_button.config(state="normal")
        search_button.config(state="normal")

        messagebox.showinfo("Dataset Loaded", (f"Dataset loaded successfully!\n\n Books: {len(books_df):,}\n Users: {len(user_ids):,}\n Ratings: {len(ratings_df):,}"))
    except Exception as error:
        status_label.config(text="Error loading dataset.")
        messagebox.showerror("Dataset Error", str(error))

def recommend_books(book_name, number_of_recommendations=5):
    """Find books similar to the selected book using TF-IDF and cosine similarity."""
    if book_name not in book_indices:
        return []

    book_index = book_indices[book_name]
    similarity_scores = cosine_similarity(tfidf_matrix[book_index], tfidf_matrix).flatten()
    similar_indices = similarity_scores.argsort()[::-1]
    recommendations = []

    for index in similar_indices:
        if index == book_index:
            continue

        score = similarity_scores[index]
        recommendations.append(
            {
                "title": books_df.iloc[index]["title"],
                "author": books_df.iloc[index]["authors"],
                "score": float(score),
                "rating": float(books_df.iloc[index]["average_rating"])
            }
        )

        if len(recommendations) >= number_of_recommendations:
            break
    return recommendations

def recommend_for_user(user_id, number_of_recommendations=5):
    """Recommend books using similar users. The target user's already-rated books are excluded."""
    try:
        user_id = int(user_id)
    except ValueError:
        return []

    if user_id not in user_to_index:
        return []

    target_index = user_to_index[user_id]
    target_vector = rating_matrix[target_index]

    similarities = cosine_similarity(target_vector, rating_matrix).flatten()
    similarities[target_index] = 0
    similar_user_indices = np.argsort(similarities)[::-1]
    similar_user_indices = [index for index in similar_user_indices if similarities[index] > 0]
    similar_user_indices = similar_user_indices[:SIMILAR_USERS]

    if len(similar_user_indices) == 0:
        return []

    rated_books = set(target_vector.indices)
    recommendation_scores = {}

    for user_index in similar_user_indices:
        similarity_score = similarities[user_index]
        user_row = rating_matrix[user_index]
        for book_index, rating in zip(user_row.indices, user_row.data):
            if book_index in rated_books:
                continue

            if rating >= 4:
                weighted_score = (similarity_score * float(rating))
                if book_index not in recommendation_scores:
                    recommendation_scores[book_index] = 0

                recommendation_scores[book_index] += (weighted_score)

    sorted_recommendations = sorted(recommendation_scores.items(), key=lambda item: item[1], reverse=True)
    recommendations = []
    for book_index, score in sorted_recommendations:
        book_id = book_index_to_id[book_index]
        book_row = books_df[books_df["book_id"] == book_id]

        if book_row.empty:
            continue

        book = book_row.iloc[0]
        recommendations.append(
            {
                "title": book["title"],
                "author": book["authors"],
                "score": float(score),
                "rating": float(book["average_rating"])
            }
        )

        if len(recommendations) >= number_of_recommendations:
            break
    return recommendations

def display_results(title, recommendations):
    """Display recommendation results in the text box."""
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)

    result_text.insert(tk.END, f"{title}\n")
    result_text.insert(tk.END, "=" * 75 + "\n\n")
    if not recommendations:
        result_text.insert(tk.END, "No recommendations found.\n")
        result_text.config(state="disabled")
        return

    for number, book in enumerate(recommendations, start=1):
        result_text.insert(tk.END, f"{number}. {book['title']}\n")
        result_text.insert(tk.END, f"   Author: {book['author']}\n")
        result_text.insert(tk.END, f"   Recommendation Score: {book['score']:.4f}\n")
        result_text.insert(tk.END, f"   Average Rating: {book['rating']:.2f}/5\n\n")
    result_text.config(state="disabled")

def get_content_recommendations():
    """Handle content-based recommendation button."""
    if books_df is None:
        messagebox.showwarning("Dataset Not Loaded", "Please load the dataset first.")
        return

    selected_book = book_combo.get().strip()
    if not selected_book:
        messagebox.showwarning("Book Required", "Please select a book.")
        return

    status_label.config(text="Finding similar books...")
    root.update_idletasks()

    recommendations = recommend_books(selected_book, CONTENT_RECOMMENDATIONS)
    display_results(f"📚 Books Similar To: {selected_book}", recommendations)
    status_label.config(text="Content-based recommendations generated.")

def get_user_recommendations():
    """Handle collaborative filtering button."""
    if ratings_df is None:
        messagebox.showwarning("Dataset Not Loaded", "Please load the dataset first.")
        return

    selected_user = user_combo.get().strip()
    if not selected_user:
        messagebox.showwarning("User Required", "Please select a user.")
        return

    status_label.config(text="Finding similar users and recommendations...")
    root.update_idletasks()

    recommendations = recommend_for_user(selected_user, USER_RECOMMENDATIONS)
    display_results(f"👤 Personalized Recommendations For User {selected_user}", recommendations)
    status_label.config(text="Personalized recommendations generated.")

def search_book():
    """Search for a book by title."""
    search_term = search_entry.get().strip().lower()
    if not search_term:
        messagebox.showwarning("Search", "Enter a book title to search.")
        return

    matches = [title for title in book_titles if search_term in title.lower()]
    if not matches:
        messagebox.showinfo("Search Result", "No matching books found.")
        return

    matches = matches[:20]

    book_combo["values"] = matches
    book_combo.current(0)

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)

    result_text.insert(tk.END, "🔎 Search Results\n")
    result_text.insert(tk.END, "=" * 75 + "\n\n")
    for number, title in enumerate(matches, start=1):
        result_text.insert(tk.END, f"{number}. {title}\n")

    result_text.config(state="disabled")
    status_label.config(text=f"Found {len(matches)} matching books.")

def clear_results():
    """Clear the GUI."""
    search_entry.delete(0, tk.END)

    if book_titles:
        book_combo["values"] = book_titles
        book_combo.current(0)

    if user_list:
        user_combo.current(0)

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")

    status_label.config(text="Ready.")

def exit_application():
    """Close the application."""
    root.destroy()

root = tk.Tk()
root.title("📚 Day 76 - Book Recommendation System")
root.geometry("1050x750")
root.minsize(900, 650)
root.configure(padx=20, pady=15)

title_label = tk.Label(root, text="📚 BOOK RECOMMENDATION SYSTEM", font=("Segoe UI", 22, "bold"))
title_label.pack(pady=(0, 5))

subtitle_label = tk.Label(root, text=("Hybrid Recommendation System using Content-Based and Collaborative Filtering"), font=("Segoe UI", 10))
subtitle_label.pack(pady=(0, 15))

load_button = ttk.Button(root, text="📂 Load Dataset", command=load_data)
load_button.pack(pady=(0, 15))

search_frame = ttk.LabelFrame(root, text="🔎 Search Books", padding=10)
search_frame.pack(fill="x", pady=5)
search_entry = ttk.Entry(search_frame, width=70)
search_entry.pack(side="left", padx=(0, 10), fill="x", expand=True)
search_button = ttk.Button(search_frame, text="Search", command=search_book, state="disabled")
search_button.pack(side="right")

content_frame = ttk.LabelFrame(root, text="📖 Content-Based Recommendation", padding=10)
content_frame.pack(fill="x", pady=5)
book_label = ttk.Label(content_frame, text="Select Book:")
book_label.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
book_combo = ttk.Combobox(content_frame, width=75, state="readonly")
book_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
recommend_book_button = ttk.Button(content_frame, text="📚 Get Similar Books", command=get_content_recommendations, state="disabled")
recommend_book_button.grid(row=0, column=2, padx=(10, 0), pady=5)
content_frame.columnconfigure(1, weight=1)

user_frame = ttk.LabelFrame(root, text="👤 Personalized Recommendation", padding=10)
user_frame.pack(fill="x", pady=5)
user_label = ttk.Label(user_frame, text="Select User:")
user_label.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
user_combo = ttk.Combobox(user_frame, width=30, state="readonly")
user_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
recommend_user_button = ttk.Button(user_frame, text="👤 Recommend For User", command=get_user_recommendations, state="disabled")
recommend_user_button.grid(row=0, column=2, padx=10, pady=5)

result_frame = ttk.LabelFrame(root, text="📊 Recommendation Results", padding=10)
result_frame.pack(fill="both", expand=True, pady=5)
result_text = tk.Text(result_frame, height=15, wrap="word", font=("Consolas", 10))
result_text.pack(side="left", fill="both", expand=True)
scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
scrollbar.pack(side="right", fill="y")
result_text.configure(yscrollcommand=scrollbar.set, state="disabled")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
clear_button = ttk.Button(button_frame, text="🧹 Clear", command=clear_results)
clear_button.pack(side="left", padx=10)
exit_button = ttk.Button(button_frame, text="❌ Exit", command=exit_application)
exit_button.pack(side="left", padx=10)

status_label = tk.Label(root, text="Place the Kaggle dataset inside the data folder.", font=("Segoe UI", 9), anchor="w")
status_label.pack(fill="x", pady=(5, 0))

root.mainloop()

# Done