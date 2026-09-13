import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from pdf_merger import (get_pdf_page_count, merge_selected_pdfs)

class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.root.geometry("950x600")
        self.root.minsize(800, 500)

        self.pdf_files = []
        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self.root, text="PDF Merger Tool", font=("Arial", 20, "bold"))
        title_label.pack(pady=15)

        instruction_label = ttk.Label(self.root, text=("Select PDF files, set page ranges, reorder files, and merge them into one PDF."))
        instruction_label.pack(pady=5)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Add PDF Files", command=self.add_pdf_files).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Remove Selected", command=self.remove_selected).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Move Up", command=self.move_up).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Move Down", command=self.move_down).grid(row=0, column=3, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).grid(row=0, column=4, padx=5)
        
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = ("file", "pages", "start", "end")

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("file", text="PDF File")
        self.tree.heading("pages", text="Total Pages")
        self.tree.heading("start", text="Start Page")
        self.tree.heading("end", text="End Page")

        self.tree.column("file", width=450)
        self.tree.column("pages", width=100, anchor="center")
        self.tree.column("start", width=100, anchor="center")
        self.tree.column("end", width=100, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        range_frame = ttk.LabelFrame(self.root, text="Edit Selected PDF Page Range")
        range_frame.pack(fill="x", padx=15, pady=5)

        ttk.Label(range_frame, text="Start Page:").grid(row=0, column=0, padx=5, pady=10)

        self.start_entry = ttk.Entry(range_frame, width=10)
        self.start_entry.grid(row=0, column=1, padx=5, pady=10)

        ttk.Label(range_frame, text="End Page:").grid(row=0, column=2, padx=5, pady=10)

        self.end_entry = ttk.Entry(range_frame, width=10)
        self.end_entry.grid(row=0, column=3, padx=5, pady=10)

        ttk.Button(range_frame, text="Apply Range", command=self.apply_range).grid(row=0, column=4, padx=10, pady=10)
        self.remove_blank_var = tk.BooleanVar(value=True)

        ttk.Checkbutton(self.root, text="Remove blank pages before merging", variable=self.remove_blank_var).pack(pady=5)
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(pady=15)

        ttk.Button(bottom_frame, text="Merge PDFs", command=self.merge_pdfs).grid(row=0, column=0, padx=10)
        ttk.Button(bottom_frame, text="Exit", command=self.root.destroy).grid(row=0, column=1, padx=10)
        self.status_label = ttk.Label(self.root, text="No PDF files selected.")
        self.status_label.pack(pady=5)

        self.tree.bind("<<TreeviewSelect>>", self.load_selected_range)
        
    def add_pdf_files(self):
        selected_files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])

        for pdf_path in selected_files:
            if pdf_path in [item["path"] for item in self.pdf_files]:
                continue

            try:
                page_count = get_pdf_page_count(pdf_path)
                self.pdf_files.append({"path": pdf_path, "pages": page_count, "start": 1, "end": page_count})
            except Exception as error:
                messagebox.showerror("Error", f"Could not read:\n{pdf_path}\n\n{error}")
        self.refresh_tree()

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, pdf_data in enumerate(self.pdf_files):
            self.tree.insert("", "end", iid=str(index), values=(os.path.basename(pdf_data["path"]), pdf_data["pages"], pdf_data["start"], pdf_data["end"]))

        self.status_label.config(text=f"{len(self.pdf_files)} PDF file(s) selected.")

    def get_selected_index(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return None
        return int(selected_item[0])

    def load_selected_range(self, event=None):
        index = self.get_selected_index()
        if index is None:
            return

        pdf_data = self.pdf_files[index]

        self.start_entry.delete(0, tk.END)
        self.start_entry.insert(0, str(pdf_data["start"]))

        self.end_entry.delete(0, tk.END)
        self.end_entry.insert(0, str(pdf_data["end"]))

    def apply_range(self):
        index = self.get_selected_index()
        if index is None:
            messagebox.showwarning("No Selection", "Please select a PDF file first.")
            return

        try:
            start_page = int(self.start_entry.get())
            end_page = int(self.end_entry.get())

            total_pages = self.pdf_files[index]["pages"]

            if start_page < 1 or end_page > total_pages:
                raise ValueError(f"Page range must be between 1 and {total_pages}.")

            if start_page > end_page:
                raise ValueError("Start page cannot be greater than end page.")

            self.pdf_files[index]["start"] = start_page
            self.pdf_files[index]["end"] = end_page

            self.refresh_tree()
            self.tree.selection_set(str(index))
        except ValueError as error:
            messagebox.showerror("Invalid Page Range", str(error))

    def remove_selected(self):
        index = self.get_selected_index()
        if index is None:
            messagebox.showwarning("No Selection", "Please select a PDF file to remove.")
            return

        del self.pdf_files[index]
        self.refresh_tree()

    def move_up(self):
        index = self.get_selected_index()
        if index is None or index == 0:
            return

        self.pdf_files[index - 1], self.pdf_files[index] = (self.pdf_files[index], self.pdf_files[index - 1])

        self.refresh_tree()
        self.tree.selection_set(str(index - 1))

    def move_down(self):
        index = self.get_selected_index()
        if index is None or index == len(self.pdf_files) - 1:
            return

        self.pdf_files[index + 1], self.pdf_files[index] = (self.pdf_files[index], self.pdf_files[index + 1])

        self.refresh_tree()
        self.tree.selection_set(str(index + 1))

    def clear_all(self):
        self.pdf_files.clear()
        self.refresh_tree()

        self.start_entry.delete(0, tk.END)
        self.end_entry.delete(0, tk.END)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("No Files", "Please add at least one PDF file.")
            return

        output_file = filedialog.asksaveasfilename(title="Save Merged PDF", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_file:
            return

        try:
            total_pages = merge_selected_pdfs(self.pdf_files, output_file, self.remove_blank_var.get())
            messagebox.showinfo("Success", (f"PDFs merged successfully!\n\n Output file:\n{output_file}\n\n Pages added: {total_pages}"))
            self.status_label.config(text=f"Merge completed: {total_pages} pages added.")
        except Exception as error:
            messagebox.showerror("Merge Error", str(error))
            
# Done