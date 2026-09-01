# This is Day 52 project : File Organizer Tool

import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

DEFAULT_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

class FileOrganizer:
    def __init__(self, base_path, categories):
        self.base_path = base_path
        self.categories = categories

    def get_folder_for_file(self, file_name):
        extension = os.path.splitext(file_name)[1].lower()
        for folder, extensions in self.categories.items():
            if extension in [ext.lower() for ext in extensions]:
                return folder
        return "Others"

    def get_file_plan(self):
        file_plan = []
        
        try:
            files = os.listdir(self.base_path)
        except OSError as error:
            raise OSError(f"Unable to read folder:\n{error}")

        for file_name in files:
            file_path = os.path.join(self.base_path, file_name)
            if not os.path.isfile(file_path):
                continue
            folder_name = (self.get_folder_for_file(file_name))
            destination = os.path.join(self.base_path, folder_name)
            file_plan.append({"file": file_name, "source": file_path, "folder": folder_name, "destination": destination})
        return file_plan

    def create_folders(self, file_plan):
        folders = set(item["folder"] for item in file_plan)
        for folder in folders:
            folder_path = os.path.join(self.base_path, folder)
            os.makedirs(folder_path, exist_ok=True)

    def get_unique_destination(self, destination_folder, file_name):
        destination = os.path.join(destination_folder, file_name)
        if not os.path.exists(destination):
            return destination
        name, extension = os.path.splitext(file_name)
        counter = 1
        
        while True:
            new_name = (f"{name}_{counter}{extension}")
            destination = os.path.join(destination_folder, new_name)
            if not os.path.exists(destination):
                return destination
            counter += 1

    def organize(self, file_plan):
        moved_files = []
        failed_files = []
        self.create_folders(file_plan)

        for item in file_plan:
            try:
                destination_folder = item["destination"]
                destination = (self.get_unique_destination(destination_folder, item["file"]))
                shutil.move(item["source"], destination)
                moved_files.append({"file": item["file"], "folder": item["folder"], "destination": destination})
            except Exception as error:
                failed_files.append({"file": item["file"], "error": str(error)})
        return moved_files, failed_files

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer Tool")
        self.root.geometry("1000x700")
        self.root.minsize(850, 600)
        self.categories = (DEFAULT_CATEGORIES.copy())
        self.file_plan = []
        self.create_widgets()

    def create_widgets(self):
        header = ttk.Frame(self.root, padding=20)
        header.pack(fill="x")
        ttk.Label(header, text="File Organizer Tool", font=("Arial", 24, "bold")).pack(anchor="w")
        ttk.Label(header, text=("Preview, customize and safely organize your files."), font=("Arial", 11)).pack(anchor="w", pady=(5, 0))

        folder_frame = ttk.LabelFrame(self.root, text="Select Folder", padding=15)
        folder_frame.pack(fill="x", padx=20, pady=10)
        self.path_var = tk.StringVar()
        ttk.Entry(folder_frame, textvariable=self.path_var).pack(side="left", fill="x", expand=True, padx=(0, 10))
        ttk.Button(folder_frame, text="Browse", command=self.browse_folder).pack(side="left")

        action_frame = ttk.Frame(self.root, padding=(20, 5))
        action_frame.pack(fill="x")
        ttk.Button(action_frame, text="Preview Files", command=self.preview_files).pack(side="left", padx=(0, 10))
        ttk.Button(action_frame, text="Manage Categories", command=self.manage_categories).pack(side="left", padx=(0, 10))
        ttk.Button(action_frame, text="Organize Files", command=self.organize_files).pack(side="left")

        preview_frame = ttk.LabelFrame(self.root, text="Dry Run Preview", padding=10)
        preview_frame.pack(fill="both", expand=True, padx=20, pady=10)
        columns = ("file", "category", "destination")

        self.tree = ttk.Treeview(preview_frame, columns=columns, show="headings")
        self.tree.heading("file", text="File")
        self.tree.heading("category", text="Category")
        self.tree.heading("destination", text="Destination Folder")
        self.tree.column("file", width=300)
        self.tree.column("category", width=180)
        self.tree.column("destination", width=300)

        scrollbar = ttk.Scrollbar(preview_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.status_var = tk.StringVar(value="Select a folder to begin.")
        ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w", padding=8).pack(fill="x", side="bottom")

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder to Organize")
        if folder:
            self.path_var.set(folder)
            self.status_var.set(f"Selected: {folder}")
            self.clear_preview()

    def clear_preview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def preview_files(self):
        base_path = self.path_var.get().strip()
        if not base_path:
            messagebox.showwarning("Folder Required", "Please select a folder first.")
            return

        if not os.path.isdir(base_path):
            messagebox.showerror("Invalid Folder", "The selected folder does not exist.")
            return

        try:
            organizer = FileOrganizer(base_path, self.categories)
            self.file_plan = (organizer.get_file_plan())
        except OSError as error:
            messagebox.showerror("Error", str(error))
            return
        self.clear_preview()

        if not self.file_plan:
            self.status_var.set("No files found to organize.")
            messagebox.showinfo("No Files", "There are no files to organize.")
            return

        for item in self.file_plan:
            self.tree.insert("", "end", values=(item["file"], item["folder"], item["folder"]))
        self.status_var.set(f"Preview ready: {len(self.file_plan)} files found.")

    def manage_categories(self):
        window = tk.Toplevel(self.root)
        window.title("Manage Categories")
        window.geometry("650x500")
        window.transient(self.root)

        list_frame = ttk.Frame(window, padding=15)
        list_frame.pack(fill="both", expand=True)

        category_list = tk.Listbox(list_frame, height=12)
        category_list.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=category_list.yview)
        scrollbar.pack(side="right", fill="y")
        category_list.configure(yscrollcommand=scrollbar.set)

        def refresh_categories():
            category_list.delete(0, tk.END)
            for category, extensions in (self.categories.items()):
                extension_text = ", ".join(extensions)
                category_list.insert(tk.END, f"{category}: {extension_text}")
        refresh_categories()

        form_frame = ttk.LabelFrame(window, text="Add Custom Category", padding=15)
        form_frame.pack(fill="x", padx=15, pady=10)
        ttk.Label(form_frame, text="Category Name:").grid(row=0, column=0, sticky="w", pady=5)

        category_entry = ttk.Entry(form_frame)
        category_entry.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(form_frame, text="Extensions:").grid(row=1, column=0, sticky="w", pady=5)

        extension_entry = ttk.Entry(form_frame)
        extension_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(form_frame, text="Example: .py, .js, .html").grid(row=2, column=1, sticky="w")
        form_frame.columnconfigure(1, weight=1)

        def add_category():
            category = (category_entry.get().strip())
            extensions_text = (extension_entry.get().strip())
            if not category:
                messagebox.showwarning("Category Required", "Enter a category name.", parent=window)
                return

            if not extensions_text:
                messagebox.showwarning("Extensions Required", "Enter at least one extension.", parent=window)
                return

            extensions = []
            for extension in (extensions_text.split(",")):
                extension = (extension.strip().lower())
                if not extension:
                    continue
                if not extension.startswith("."):
                    extension = "." + extension
                extensions.append(extension)
                
            self.categories[category] = (extensions)
            refresh_categories()
            category_entry.delete(0, tk.END)
            extension_entry.delete(0, tk.END)

        def delete_category():
            selection = (category_list.curselection())

            if not selection:
                messagebox.showwarning("Select Category", "Select a category to delete.", parent=window)
                return
            selected_text = (category_list.get(selection[0]))
            category = selected_text.split(":", 1)[0]

            if category not in self.categories:
                return
            del self.categories[category]
            refresh_categories()

        button_frame = ttk.Frame(window, padding=15)
        button_frame.pack(fill="x")
        ttk.Button(button_frame, text="Add Category", command=add_category).pack(side="left", padx=(0, 10))
        ttk.Button(button_frame, text="Delete Category", command=delete_category).pack(side="left")

    def organize_files(self):
        base_path = self.path_var.get().strip()
        if not base_path:
            messagebox.showwarning("Folder Required", "Please select a folder first.")
            return

        if not self.file_plan:
            self.preview_files()
            if not self.file_plan:
                return

        preview_lines = []
        for item in self.file_plan:
            preview_lines.append(f"• {item['file']} → {item['folder']}/")
        preview_text = "\n".join(preview_lines)

        if len(preview_text) > 3000:
            preview_text = (preview_text[:3000] + "\n... and more files")

        confirmation = messagebox.askyesno("Confirm Organization", ("The following files will be moved:\n\n"
                f"{preview_text}\n\n"
                "Do you want to continue?"))

        if not confirmation:
            self.status_var.set("Organization cancelled.")
            return

        try:
            organizer = FileOrganizer(base_path, self.categories)
            moved, failed = (organizer.organize(self.file_plan))
        except Exception as error:
            messagebox.showerror("Organization Error", str(error))
            return
        self.clear_preview()

        for item in moved:
            self.tree.insert("", "end", values=(item["file"], item["folder"], item["folder"]))

        if failed:
            error_text = "\n".join(f"{item['file']}: {item['error']}" for item in failed)
            messagebox.showwarning("Completed with Errors", (
                    f"{len(moved)} files moved.\n"
                    f"{len(failed)} files failed.\n\n"
                    f"{error_text}"))
        else:
            messagebox.showinfo("Organization Complete", (f"Successfully moved {len(moved)} files."))

        self.status_var.set(f"Organization complete: {len(moved)} files moved.")
        self.file_plan = []

def main():
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()