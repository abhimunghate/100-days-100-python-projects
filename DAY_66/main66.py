# This is Day 66 project : Flashcards Learning App

import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from pathlib import Path

FLASHCARDS_FILE = Path("flashcards.json")
REVIEW_LOG_FILE = Path("review_logs.json")

def load_json(file_path, default_value):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_value
    except json.JSONDecodeError:
        messagebox.showerror("File Error", f"Could not read {file_path}. The file may be corrupted.")
        return default_value

def save_json(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_flashcards():
    """Load all flashcards."""
    return load_json(FLASHCARDS_FILE, [])

def save_flashcards(flashcards):
    """Save all flashcards."""
    save_json(FLASHCARDS_FILE, flashcards)

def load_review_logs():
    """Load review history."""
    return load_json(REVIEW_LOG_FILE, [])

def save_review_logs(logs):
    """Save review history."""
    save_json(REVIEW_LOG_FILE, logs)

def add_flashcard_data(question, answer, category):
    """Create and save a new flashcard."""
    flashcards = load_flashcards()
    existing_ids = [card.get("id", 0) for card in flashcards]
    next_id = max(existing_ids, default=0) + 1
    
    new_flashcard = {"id": next_id, "question": question, "answer": answer, "category": category, "learned": False, "review_count": 0, "correct_count": 0, "incorrect_count": 0}
    flashcards.append(new_flashcard)
    save_flashcards(flashcards)

def get_categories(flashcards):
    """Return sorted categories."""
    categories = {card.get("category", "General") for card in flashcards}
    return sorted(categories)

def save_review_result(card, result):
    """Save the result of a flashcard review."""
    flashcards = load_flashcards()
    logs = load_review_logs()

    for saved_card in flashcards:
        if saved_card["id"] == card["id"]:
            saved_card["review_count"] = saved_card.get("review_count", 0) + 1

            if result == "correct":
                saved_card["correct_count"] = saved_card.get("correct_count", 0) + 1
            elif result == "incorrect":
                saved_card["incorrect_count"] = saved_card.get("incorrect_count", 0) + 1
            break

    review_entry = {"flashcard_id": card["id"], "question": card["question"], "category": card.get("category", "General"), "result": result, "reviewed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    logs.append(review_entry)
    save_flashcards(flashcards)
    save_review_logs(logs)

class AddFlashcardWindow:
    def __init__(self, parent, refresh_callback):
        self.parent = parent
        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel(parent)
        self.window.title("Add Flashcard")
        self.window.geometry("500x420")
        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self.window, text="Add New Flashcard", font=("Arial", 18, "bold"))
        title_label.pack(pady=15)

        form_frame = ttk.Frame(self.window, padding=20)
        form_frame.pack(fill="both", expand=True)

        ttk.Label(form_frame, text="Category:").pack(anchor="w", pady=(5, 3))

        self.category_entry = ttk.Entry(form_frame)
        self.category_entry.pack(fill="x", pady=(0, 12))

        ttk.Label(form_frame, text="Question:").pack(anchor="w", pady=(5, 3))

        self.question_entry = tk.Text(form_frame, height=4, width=50)
        self.question_entry.pack(fill="x", pady=(0, 12))

        ttk.Label(form_frame, text="Answer:").pack(anchor="w", pady=(5, 3))

        self.answer_entry = tk.Text(form_frame, height=4, width=50)
        self.answer_entry.pack(fill="x", pady=(0, 12))

        ttk.Button(form_frame, text="Save Flashcard", command=self.save_flashcard).pack(pady=10)

    def save_flashcard(self):
        category = self.category_entry.get().strip()
        question = self.question_entry.get("1.0", tk.END).strip()
        answer = self.answer_entry.get("1.0", tk.END).strip()

        if not category or not question or not answer:
            messagebox.showwarning("Missing Information", "Please fill in the category, question, and answer.")
            return

        add_flashcard_data(question, answer, category)
        messagebox.showinfo("Success", "Flashcard added successfully!")
        self.refresh_callback()
        self.window.destroy()

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcards Learning App")
        self.root.geometry("850x650")
        self.root.minsize(700, 550)

        self.flashcards = []
        self.filtered_flashcards = []
        self.current_index = 0
        self.answer_visible = False

        self.create_widgets()
        self.refresh_flashcards()

    def create_widgets(self):
        title_label = ttk.Label(self.root, text="Flashcards Learning App", font=("Arial", 24, "bold"))
        title_label.pack(pady=15)

        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Select Category:").pack(side="left", padx=(0, 10))

        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(top_frame, textvariable=self.category_var, state="readonly", width=25)
        self.category_combo.pack(side="left")
        self.category_combo.bind("<<ComboboxSelected>>", self.category_changed)

        ttk.Button(top_frame, text="Add Flashcard", command=self.open_add_window).pack(side="right")

        self.progress_label = ttk.Label(self.root, text="No flashcards available", font=("Arial", 11))
        self.progress_label.pack(pady=10)

        self.card_frame = ttk.LabelFrame(self.root, text="Flashcard", padding=25)
        self.card_frame.pack(fill="both", expand=True, padx=30, pady=10)

        self.category_label = ttk.Label(self.card_frame, text="Category: -", font=("Arial", 11, "italic"))
        self.category_label.pack(pady=10)

        self.question_label = ttk.Label(self.card_frame, text="No question available", font=("Arial", 20, "bold"), wraplength=650, justify="center")
        self.question_label.pack(fill="both", expand=True, pady=20)

        self.answer_label = ttk.Label(self.card_frame, text="", font=("Arial", 16), wraplength=650, justify="center")
        self.answer_label.pack(pady=15)
        
        self.user_answer_entry = ttk.Entry(self.card_frame, width=60)
        self.user_answer_entry.pack(pady=10)
        self.user_answer_entry.bind("<Return>", lambda event: self.submit_answer())

        self.submit_answer_button = ttk.Button(self.card_frame, text="Submit Answer", command=self.submit_answer)
        self.submit_answer_button.pack(pady=5)

        self.stats_label = ttk.Label(self.card_frame, text="", font=("Arial", 10))
        self.stats_label.pack(pady=10)

        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.pack(fill="x")
        ttk.Button(button_frame, text="Previous", command=self.previous_card).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reveal Answer", command=self.reveal_answer).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Mark as Learned", command=self.mark_as_learned).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Next", command=self.next_card).pack(side="right", padx=5)

        self.status_label = ttk.Label(self.root, text="Ready to study", font=("Arial", 10))
        self.status_label.pack(pady=10)

    def refresh_flashcards(self):
        self.flashcards = load_flashcards()
        categories = ["All Categories"] + get_categories(self.flashcards)
        self.category_combo["values"] = categories

        if not self.category_var.get():
            self.category_var.set("All Categories")
        self.apply_category_filter()

    def category_changed(self, event=None):
        self.apply_category_filter()

    def apply_category_filter(self):
        selected_category = self.category_var.get()
        if selected_category == "All Categories":
            self.filtered_flashcards = [card for card in self.flashcards if not card.get("learned", False)]
        else:
            self.filtered_flashcards = [card for card in self.flashcards if card.get("category", "General") == selected_category and not card.get("learned", False)]
        self.current_index = 0
        self.show_current_card()

    def show_current_card(self):
        if hasattr(self, "user_answer_entry"):
            self.user_answer_entry.delete(0, tk.END)
            
        if not self.filtered_flashcards:
            self.category_label.config(text="Category: -")
            self.question_label.config(text="No flashcards available")
            self.answer_label.config(text="")
            self.stats_label.config(text="")
            self.progress_label.config(text="No flashcards available")
            return

        card = self.filtered_flashcards[self.current_index]
        self.answer_visible = False

        self.category_label.config(text=f"Category: {card.get('category', 'General')}")
        self.question_label.config(text=card["question"])
        self.answer_label.config(text="Answer hidden. Click 'Reveal Answer'.")
        
        review_count = card.get("review_count", 0)
        correct_count = card.get("correct_count", 0)
        incorrect_count = card.get("incorrect_count", 0)
        learned_status = "Learned" if card.get("learned", False) else "Not learned"

        self.stats_label.config(text=(f"Reviews: {review_count} | Correct: {correct_count} | Incorrect: {incorrect_count} | Status: {learned_status}"))
        self.progress_label.config(text=(f"Card {self.current_index + 1} of {len(self.filtered_flashcards)}"))

    def reveal_answer(self):
        if not self.filtered_flashcards:
            return

        card = self.filtered_flashcards[self.current_index]
        self.answer_visible = True
        self.answer_label.config(text=f"Answer: {card['answer']}")

    def next_card(self):
        if not self.filtered_flashcards:
            return
        self.current_index = (self.current_index + 1) % len(self.filtered_flashcards)
        self.show_current_card()

    def previous_card(self):
        if not self.filtered_flashcards:
            return
        self.current_index = (self.current_index - 1) % len(self.filtered_flashcards)
        self.show_current_card()

    def mark_as_learned(self):
        if not self.filtered_flashcards:
            return

        card = self.filtered_flashcards[self.current_index]
        flashcards = load_flashcards()

        for saved_card in flashcards:
            if saved_card["id"] == card["id"]:
                saved_card["learned"] = True
                break

        save_flashcards(flashcards)
        self.status_label.config(text="Flashcard marked as learned!")
        self.refresh_flashcards()

    def open_add_window(self):
        AddFlashcardWindow(self.root, self.refresh_flashcards)
        
    def submit_answer(self):
        if not self.filtered_flashcards:
            messagebox.showwarning("No Flashcards", "There are no flashcards available.")
            return
        user_answer = self.user_answer_entry.get().strip()

        if not user_answer:
            messagebox.showwarning("Empty Answer", "Please enter an answer before submitting.")
            return

        card = self.filtered_flashcards[self.current_index]
        correct_answer = card["answer"].strip()

        if " ".join(user_answer.lower().split()) == " ".join(correct_answer.lower().split()):
            save_review_result(card, "correct")

            self.status_label.config(text="Correct answer!")
            messagebox.showinfo("Result", "Correct! Well done.")
        else:
            save_review_result(card, "incorrect")
            self.status_label.config(text="Incorrect answer.")
            messagebox.showerror("Result", f"Incorrect.\n\nCorrect answer: {correct_answer}")

        self.user_answer_entry.delete(0, tk.END)
        self.refresh_flashcards()

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
# Done