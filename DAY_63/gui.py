# Day 63 - Movie Recommendation System
# Tkinter GUI

import tkinter as tk
from tkinter import messagebox, ttk

from recommendation_engine import (build_recommendation_data, calculate_genre_similarity, calculate_item_similarity, load_genres, load_ratings, prepare_genre_matrix, prepare_ratings_matrix)

class MovieRecommendationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")
        self.root.geometry("850x600")
        self.root.minsize(700, 500)

        self.ratings_file = "movie_ratings.csv"
        self.genres_file = "movie_genres.csv"

        self.ratings = None
        self.genres = None
        self.ratings_matrix = None
        self.genre_matrix = None
        self.rating_similarity = None
        self.genre_similarity = None

        self.user_id_var = tk.StringVar()
        self.count_var = tk.StringVar(value="5")
        self.status_var = tk.StringVar(value="Loading movie data...")

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        title_label = ttk.Label(self.root, text="Movie Recommendation System", font=("Segoe UI", 20, "bold"))
        title_label.pack(pady=15)

        subtitle_label = ttk.Label(self.root, text="Item-based collaborative filtering using ratings and genres")
        subtitle_label.pack(pady=(0, 15))

        input_frame = ttk.LabelFrame(self.root, text="Recommendation Settings", padding=15)
        input_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(input_frame, text="User ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.user_combo = ttk.Combobox(input_frame, textvariable=self.user_id_var, state="readonly", width=20)
        self.user_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(input_frame, text="Number of Movies:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.count_combo = ttk.Combobox(input_frame, textvariable=self.count_var, values=["3", "5", "10"], state="readonly", width=10)
        self.count_combo.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.recommend_button = ttk.Button(input_frame, text="Recommend Movies", command=self.generate_recommendations)
        self.recommend_button.grid(row=0, column=4, padx=10, pady=5)
        
        result_frame = ttk.LabelFrame(self.root, text="Recommended Movies", padding=10)
        result_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        columns = ("rank", "movie", "genres", "score")
        self.result_tree = ttk.Treeview(result_frame, columns=columns, show="headings")
        self.result_tree.heading("rank", text="Rank")
        self.result_tree.heading("movie", text="Movie")
        self.result_tree.heading("genres", text="Genres")
        self.result_tree.heading("score", text="Recommendation Score")
        self.result_tree.column("rank", width=70, anchor="center")
        self.result_tree.column("movie", width=220)
        self.result_tree.column("genres", width=250)
        self.result_tree.column("score", width=160, anchor="center")
        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=self.result_tree.yview)
        self.result_tree.configure(yscrollcommand=scrollbar.set)
        self.result_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        status_frame = ttk.LabelFrame(self.root, text="Status", padding=10)
        status_frame.pack(fill="x", padx=20, pady=(0, 15))
        ttk.Label(status_frame, textvariable=self.status_var).pack(anchor="w")

    def load_data(self):
        try:
            self.ratings = load_ratings(self.ratings_file)
            self.genres = load_genres(self.genres_file)

            self.ratings_matrix = prepare_ratings_matrix(self.ratings)
            self.genre_matrix = prepare_genre_matrix(self.genres)
            self.rating_similarity = calculate_item_similarity(self.ratings_matrix)
            self.genre_similarity = calculate_genre_similarity(self.genre_matrix)
            user_ids = list(self.ratings_matrix.columns)

            self.user_combo["values"] = user_ids
            if user_ids:
                self.user_combo.current(0)

            self.status_var.set(f"Loaded {len(user_ids)} users and {len(self.ratings_matrix.index)} movies.")
        except FileNotFoundError as error:
            self.recommend_button.config(state="disabled")
            messagebox.showerror("File Not Found", f"Required file was not found:\n{error.filename}")
            self.status_var.set("Could not load the required CSV files.")
        except Exception as error:
            self.recommend_button.config(state="disabled")
            messagebox.showerror("Loading Error", str(error))
            self.status_var.set("An error occurred while loading data.")
            
    def generate_recommendations(self):
        if self.ratings_matrix is None:
            messagebox.showerror("Data Error", "Movie data has not been loaded.")
            return

        try:
            user_id = int(self.user_id_var.get())
            recommendation_count = int(self.count_var.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please select a valid user ID and recommendation count.")
            return

        recommendations = build_recommendation_data(user_id=user_id, ratings_matrix=self.ratings_matrix, rating_similarity=self.rating_similarity, genre_similarity=self.genre_similarity, genres=self.genres, recommendation_count=recommendation_count)
        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        if not recommendations:
            messagebox.showinfo("No Recommendations", "No new movie recommendations are available for this user.")
            self.status_var.set(f"No recommendations available for User {user_id}.")
            return

        for index, recommendation in enumerate(recommendations, start=1):
            self.result_tree.insert("", "end", values=(index, recommendation["movie"], recommendation["genres"], recommendation["score"]))
        self.status_var.set(f"Generated {len(recommendations)} recommendations for User {user_id}.")
        
# Done