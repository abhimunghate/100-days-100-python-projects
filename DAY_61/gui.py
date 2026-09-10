# Day 61 - Social Media Scraper
# Tkinter GUI

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import csv

from scraper import load_html, extract_posts

class SocialMediaScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Scraper")
        self.root.geometry("1150x700")
        self.root.minsize(950, 600)

        self.posts = []
        self.filtered_posts = []

        self.file_var = tk.StringVar(value="No file selected")
        self.keyword_var = tk.StringVar(value="")
        self.stats_var = tk.StringVar(value="No data loaded")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        main_frame.columnconfigure(0, weight=1)

        title_label = ttk.Label(main_frame, text="📱 Social Media Scraper", font=("Segoe UI", 22, "bold"))
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        subtitle_label = ttk.Label(main_frame, text=("Extract and analyze posts from a local HTML file"))
        subtitle_label.grid(row=1, column=0, sticky="w", pady=(0, 12))

        controls_frame = ttk.LabelFrame(main_frame, text="File & Search", padding=10)
        controls_frame.grid(row=2, column=0, sticky="new", pady=(0, 10))
        controls_frame.columnconfigure(1, weight=1)

        select_button = ttk.Button(controls_frame, text="📂 Select HTML File", command=self.select_file)
        select_button.grid(row=0, column=0, padx=(0, 8))

        file_label = ttk.Label(controls_frame, textvariable=self.file_var)
        file_label.grid(row=0, column=1, sticky="ew")

        scrape_button = ttk.Button(controls_frame, text="🔎 Scrape", command=self.scrape_file)
        scrape_button.grid(row=0, column=2, padx=8)

        search_label = ttk.Label(controls_frame, text="Keyword:")
        search_label.grid(row=1, column=0, pady=(10, 0), sticky="w")

        self.search_entry = ttk.Entry(controls_frame, textvariable=self.keyword_var)
        self.search_entry.grid(row=1, column=1, sticky="ew", pady=(10, 0))
        self.search_entry.bind("<KeyRelease>", lambda event: self.filter_posts())

        clear_button = ttk.Button(controls_frame, text="Clear", command=self.clear_search)
        clear_button.grid(row=1, column=2, padx=8, pady=(10, 0))

        results_frame = ttk.LabelFrame(main_frame, text="Scraped Posts", padding=8)
        results_frame.grid(row=3, column=0, sticky="nsew", pady=(0, 10))
        main_frame.rowconfigure(3, weight=1)
        results_frame.rowconfigure(0, weight=1)
        results_frame.columnconfigure(0, weight=1)

        columns = ("post_id", "username", "content", "timestamp", "likes")
        self.tree = ttk.Treeview(results_frame, columns=columns, show="headings")
        self.tree.heading("post_id", text="Post ID")
        self.tree.heading("username", text="Username")
        self.tree.heading("content", text="Post Content")
        self.tree.heading("timestamp", text="Timestamp")
        self.tree.heading("likes", text="Likes")
        self.tree.column("post_id", width=100, anchor="center")
        self.tree.column("username", width=120, anchor="center")
        self.tree.column("content", width=450)
        self.tree.column("timestamp", width=160, anchor="center")
        self.tree.column("likes", width=80, anchor="center")
        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.grid(row=4, column=0, sticky="ew")
        bottom_frame.columnconfigure(0, weight=1)

        stats_label = ttk.Label(bottom_frame, textvariable=self.stats_var)
        stats_label.grid(row=0, column=0, sticky="w")

        export_button = ttk.Button(bottom_frame, text="💾 Export CSV", command=self.export_csv)
        export_button.grid(row=0, column=1, padx=5)

        clear_results_button = ttk.Button(bottom_frame, text="Clear Results", command=self.clear_results)
        clear_results_button.grid(row=0, column=2, padx=5)

        exit_button = ttk.Button(bottom_frame, text="Exit", command=self.root.destroy)
        exit_button.grid(row=0, column=3)

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select Social Media HTML File", filetypes=[("HTML Files", "*.html *.htm"), ("All Files", "*.*")])
        if file_path:
            self.file_var.set(file_path)
            self.stats_var.set("HTML file selected. Click Scrape.")

    def scrape_file(self):
        file_path = self.file_var.get()
        if (not file_path or file_path == "No file selected"):
            messagebox.showwarning("No File", "Please select an HTML file first.")
            return

        try:
            html_content = load_html(file_path)
            self.posts = extract_posts(html_content)
            self.filtered_posts = self.posts.copy()

            self.display_posts(self.filtered_posts)
            self.update_statistics()
        except FileNotFoundError:
            messagebox.showerror("File Error", "The selected file could not be found.")
        except Exception as error:
            messagebox.showerror("Scraping Error", f"Unable to scrape the file.\n\n{error}")

    def display_posts(self, posts):
        for item in self.tree.get_children():
            self.tree.delete(item)

        keyword = (self.keyword_var.get().strip())
        for post in posts:
            content = post["content"]

            if keyword:
                content = self.highlight_keyword(content, keyword)
            self.tree.insert("", tk.END, values=(post["post_id"], post["username"], content, post["timestamp"], post["likes"]))

    def highlight_keyword(self, text, keyword):
        if not keyword:
            return text
        words = text.split()
        highlighted_words = []

        for word in words:
            if keyword.lower() in word.lower():
                highlighted_words.append(f"【{word}】")
            else:
                highlighted_words.append(word)
        return " ".join(highlighted_words)

    def filter_posts(self):
        keyword = (self.keyword_var.get().strip().lower())
        if not keyword:
            self.filtered_posts = (self.posts.copy())
        else:
            self.filtered_posts = [post for post in self.posts
                if (
                    keyword in post["username"].lower()
                    or keyword in post["content"].lower()
                    or keyword in post["post_id"].lower()
                )
            ]
        self.display_posts(self.filtered_posts)
        self.update_statistics()

    def clear_search(self):
        self.keyword_var.set("")
        self.filtered_posts = (self.posts.copy())
        self.display_posts(self.filtered_posts)
        self.update_statistics()

    def update_statistics(self):
        total_posts = len(self.filtered_posts)
        total_likes = sum(post["likes"] for post in self.filtered_posts)
        if total_posts > 0:
            average_likes = (total_likes / total_posts)
        else:
            average_likes = 0

        self.stats_var.set(f"Posts: {total_posts}   |   Total Likes: {total_likes}   |   Average Likes: {average_likes:.1f}")

    def export_csv(self):
        if not self.filtered_posts:
            messagebox.showwarning("No Data", "There are no posts to export.")
            return

        file_path = filedialog.asksaveasfilename(title="Save Scraped Posts", defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["post_id", "username", "content", "timestamp", "likes"])
                writer.writeheader()
                writer.writerows(self.filtered_posts)

            messagebox.showinfo("Export Complete", "Posts exported successfully.")
        except Exception as error:
            messagebox.showerror("Export Error", f"Unable to export CSV.\n\n{error}")

    def clear_results(self):
        self.posts = []
        self.filtered_posts = []
        self.file_var.set("No file selected")
        self.keyword_var.set("")

        for item in self.tree.get_children():
            self.tree.delete(item)
        self.stats_var.set("No data loaded")
        
# Done