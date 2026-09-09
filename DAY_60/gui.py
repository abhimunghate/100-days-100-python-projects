# This is Day 60 project : Personal Diary App
# GUI Module

import tkinter as tk
from tkinter import ttk, messagebox

from diary_manager import (create_entry, get_entries, read_entry, update_entry, delete_entry, search_entries, extract_title, extract_date, extract_body,)
from cloud_backup import backup_entries, restore_entries

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Personal Diary")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)

        self.current_entry = None
        self.current_results = []

        self.setup_style()
        self.create_widgets()
        self.refresh_entries()

    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"),)
        style.configure("Subtitle.TLabel", font=("Segoe UI", 10),)
        style.configure("Section.TLabel", font=("Segoe UI", 11, "bold"),)
        style.configure("Action.TButton", font=("Segoe UI", 10, "bold"), padding=(12, 8),)
        style.configure("Small.TButton", font=("Segoe UI", 9), padding=(8, 5),)

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.grid(row=0, column=0, sticky="nsew")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        main_frame.rowconfigure(2, weight=1)
        main_frame.columnconfigure(0, weight=1)

        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        header_frame.columnconfigure(0, weight=1)

        title_label = ttk.Label(header_frame, text="🔐 Secure Personal Diary", style="Title.TLabel")
        title_label.grid(row=0, column=0, sticky="w")

        subtitle_label = ttk.Label(header_frame, text="Your private thoughts, securely encrypted.", style="Subtitle.TLabel")
        subtitle_label.grid(row=1, column=0, sticky="w", pady=(3, 0))

        search_frame = ttk.LabelFrame(main_frame, text="Search Diary", padding=8)
        search_frame.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        search_frame.columnconfigure(0, weight=1)

        self.search_var = tk.StringVar()

        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, font=("Segoe UI", 10))
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        self.search_entry.bind("<Return>", lambda event: self.search())
        search_button = ttk.Button(search_frame, text="🔍 Search", command=self.search, style="Small.TButton")
        search_button.grid(row=0, column=1, padx=(0, 5))
        clear_search_button = ttk.Button(search_frame, text="Clear", command=self.clear_search, style="Small.TButton")
        clear_search_button.grid(row=0, column=2)

        content_frame = ttk.Frame(main_frame)
        content_frame.grid(row=2, column=0, sticky="nsew", pady=(0, 12))
        content_frame.rowconfigure(0, weight=1)
        content_frame.columnconfigure(0, weight=0)
        content_frame.columnconfigure(1, weight=1)

        list_frame = ttk.LabelFrame(content_frame, text="Diary Entries", padding=8)
        list_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)

        self.entry_listbox = tk.Listbox(list_frame, font=("Segoe UI", 10), activestyle="dotbox", selectmode=tk.SINGLE, width=32)
        self.entry_listbox.grid(row=0, column=0, sticky="nsew")
        list_scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.entry_listbox.yview)
        list_scrollbar.grid(row=0, column=1, sticky="ns")
        self.entry_listbox.configure(yscrollcommand=list_scrollbar.set)
        self.entry_listbox.bind("<<ListboxSelect>>", self.select_entry)

        editor_frame = ttk.LabelFrame(content_frame, text="Diary Editor", padding=8)
        editor_frame.grid(row=0, column=1, sticky="nsew")
        editor_frame.rowconfigure(2, weight=1)
        editor_frame.columnconfigure(0, weight=1)

        title_label = ttk.Label(editor_frame, text="Title", style="Section.TLabel")
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.title_entry = ttk.Entry(editor_frame, font=("Segoe UI", 11))
        self.title_entry.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        content_header_frame = ttk.Frame(editor_frame)
        content_header_frame.grid(row=2, column=0, sticky="new")
        content_header_frame.columnconfigure(0, weight=1)

        content_label = ttk.Label(content_header_frame, text="Content", style="Section.TLabel")
        content_label.grid(row=0, column=0, sticky="w")

        text_frame = ttk.Frame(editor_frame)
        text_frame.grid(row=3, column=0, sticky="nsew", pady=(5, 0))
        editor_frame.rowconfigure(3, weight=1)
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)

        self.content_text = tk.Text(text_frame, wrap="word", font=("Segoe UI", 11), undo=True)
        self.content_text.grid(row=0, column=0, sticky="nsew")
        text_scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.content_text.yview)
        text_scrollbar.grid(row=0, column=1, sticky="ns")
        self.content_text.configure(yscrollcommand=text_scrollbar.set)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, sticky="ew", pady=(0, 8))

        for column in range(6):
            button_frame.columnconfigure(column, weight=1)

        new_button = ttk.Button(button_frame, text="📝 New Entry", command=self.new_entry, style="Action.TButton")
        new_button.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        save_button = ttk.Button(button_frame, text="💾 Save", command=self.save_entry, style="Action.TButton")
        save_button.grid(row=0, column=1, sticky="ew", padx=5)

        delete_button = ttk.Button(button_frame, text="🗑 Delete", command=self.delete_selected, style="Action.TButton")
        delete_button.grid(row=0, column=2, sticky="ew", padx=5)

        backup_button = ttk.Button(button_frame, text="☁ Backup", command=self.backup, style="Action.TButton")
        backup_button.grid(row=0, column=3, sticky="ew", padx=5)

        restore_button = ttk.Button(button_frame, text="↻ Restore", command=self.restore, style="Action.TButton")
        restore_button.grid(row=0, column=4, sticky="ew", padx=5)

        exit_button = ttk.Button(button_frame, text="✕ Exit", command=self.root.destroy, style="Action.TButton")
        exit_button.grid(row=0, column=5, sticky="ew", padx=(5, 0))

        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, sticky="ew")
        status_frame.columnconfigure(0, weight=1)

        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, style="Subtitle.TLabel")
        status_label.grid(row=0, column=0, sticky="w")

        self.root.bind("<Control-s>", lambda event: self.save_entry())
        self.root.bind("<Control-f>", lambda event: self.focus_search())

    def refresh_entries(self):
        self.entry_listbox.delete(0, tk.END)
        self.current_results = get_entries()

        if not self.current_results:
            self.status_var.set("No diary entries found.")
            return

        for entry in self.current_results:
            try:
                data = read_entry(entry)
                title = extract_title(data)
                date = extract_date(data)
                display_text = f"{title}  |  {date}"
            except Exception:
                display_text = entry.name
            self.entry_listbox.insert(tk.END, display_text)
        self.status_var.set(
            f"{len(self.current_results)} diary "
            f"entr{'y' if len(self.current_results) == 1 else 'ies'}"
        )

    def search(self):
        keyword = self.search_var.get().strip()
        if not keyword:
            self.refresh_entries()
            return

        try:
            results = search_entries(keyword)
            self.entry_listbox.delete(0, tk.END)
            self.current_results = results

            for entry in results:
                try:
                    data = read_entry(entry)
                    title = extract_title(data)
                    date = extract_date(data)
                    display_text = f"{title}  |  {date}"
                except Exception:
                    display_text = entry.name
                self.entry_listbox.insert(tk.END, display_text)

            if results:
                self.status_var.set(
                    f"Found {len(results)} matching "
                    f"entr{'y' if len(results) == 1 else 'ies'}."
                )
            else:
                self.status_var.set("No matching diary entries found.")
        except Exception as error:
            messagebox.showerror("Search Error", f"Unable to search entries.\n\n{error}")

    def clear_search(self):
        self.search_var.set("")
        self.refresh_entries()

    def focus_search(self):
        self.search_entry.focus_set()

    def select_entry(self, event=None):
        selection = self.entry_listbox.curselection()
        if not selection:
            return

        index = selection[0]
        if index >= len(self.current_results):
            return

        self.current_entry = self.current_results[index]

        try:
            data = read_entry(self.current_entry)
            title = extract_title(data)
            body = extract_body(data)

            self.title_entry.delete( 0,tk.END)
            self.title_entry.insert(0, title)
            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", body)
            self.status_var.set(f"Opened: {title}")
        except Exception as error:
            messagebox.showerror("Read Error", f"Unable to open diary entry.\n\n{error}")

    def new_entry(self):
        self.current_entry = None
        self.entry_listbox.selection_clear(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        self.title_entry.focus_set()

        self.status_var.set("Creating a new diary entry...")

    def save_entry(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not title:
            messagebox.showwarning("Missing Title", "Please enter a title for your diary entry.")
            self.title_entry.focus_set()
            return

        if not content:
            messagebox.showwarning("Missing Content", "Please write something in your diary entry.")
            self.content_text.focus_set()
            return

        try:
            if self.current_entry is None:
                new_entry_path = create_entry(title, content)
                self.current_entry = new_entry_path
                messagebox.showinfo("Entry Saved", "Your new diary entry has been saved securely.")
            else:
                update_entry(self.current_entry, title, content)
                messagebox.showinfo("Entry Updated", "Your diary entry has been updated successfully.")
            self.refresh_entries()
            self.select_current_entry()
            self.status_var.set("Entry saved successfully.")
        except Exception as error:
            messagebox.showerror("Save Error", f"Unable to save diary entry.\n\n{error}")

    def select_current_entry(self):
        if self.current_entry is None:
            return

        for index, entry in enumerate(self.current_results):
            if entry == self.current_entry:
                self.entry_listbox.selection_clear(0, tk.END)
                self.entry_listbox.selection_set(index)
                self.entry_listbox.see(index)
                break

    def delete_selected(self):
        if self.current_entry is None:
            messagebox.showwarning("No Entry Selected", "Please select a diary entry first.")
            return

        try:
            data = read_entry(self.current_entry)
            title = extract_title(data)
        except Exception:
            title = "this diary entry"

        confirmation = messagebox.askyesno("Delete Entry", f"Are you sure you want to delete\n '{title}'?\n\n This action cannot be undone.")
        if not confirmation:
            return

        try:
            delete_entry(self.current_entry)
            self.current_entry = None

            self.title_entry.delete(0, tk.END)
            self.content_text.delete("1.0", tk.END)
            self.refresh_entries()

            messagebox.showinfo("Entry Deleted", "The diary entry has been deleted.")
            self.status_var.set("Entry deleted successfully.")
        except Exception as error:
            messagebox.showerror("Delete Error", f"Unable to delete diary entry.\n\n{error}")

    def backup(self):
        confirmation = messagebox.askyesno("Backup Diary", "Backup your encrypted diary entries to Google Drive?")
        if not confirmation:
            return

        try:
            self.status_var.set("Creating Google Drive backup...")
            self.root.update_idletasks()
            backup_entries()
            messagebox.showinfo("Backup Complete", "Your encrypted diary entries have been backed up successfully.")
            self.status_var.set("Google Drive backup completed.")
        except Exception as error:
            messagebox.showerror("Backup Error", f"Unable to backup diary entries.\n\n {error}")
            self.status_var.set("Backup failed.")

    def restore(self):
        confirmation = messagebox.askyesno("Restore Diary", "Restore encrypted diary entries from Google Drive?\n\n Existing local files with the same name may be overwritten.")
        if not confirmation:
            return

        try:
            self.status_var.set("Restoring diary entries...")
            self.root.update_idletasks()
            restore_entries()
            self.refresh_entries()
            messagebox.showinfo("Restore Complete", "Diary entries have been restored successfully.")
            self.status_var.set("Google Drive restore completed.")
        except Exception as error:
            messagebox.showerror("Restore Error", f"Unable to restore diary entries.\n\n {error}")
            self.status_var.set("Restore failed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
    
# Done