# Day 62 - Automated Backup Tool
# Tkinter GUI

import os
import threading
import tkinter as tk

from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from backup_manager import (calculate_total_size, create_backup_zip, format_size, get_files, get_zip_backups, is_directory_inside, restore_backup, write_backup_history)

class BackupToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Backup and Restore Tool")
        self.root.geometry("850x650")
        self.root.minsize(750, 550)

        self.source_directory = tk.StringVar()
        self.backup_directory = tk.StringVar()
        self.restore_directory = tk.StringVar()
        self.selected_backup = tk.StringVar()

        self.status_text = tk.StringVar(value="Select a source directory and backup location.")
        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self.root, text="Automated Backup and Restore Tool", font=("Segoe UI", 18, "bold"))
        title_label.pack(pady=15)

        subtitle_label = ttk.Label(self.root, text="Create compressed ZIP backups and restore files easily", font=("Segoe UI", 10))
        subtitle_label.pack(pady=(0, 15))

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        backup_tab = ttk.Frame(notebook, padding=15)
        restore_tab = ttk.Frame(notebook, padding=15)

        notebook.add(backup_tab, text="Create Backup")
        notebook.add(restore_tab, text="Restore Backup")

        self.create_backup_tab(backup_tab)
        self.create_restore_tab(restore_tab)

        status_frame = ttk.LabelFrame(self.root, text="Status", padding=10)
        status_frame.pack(fill="x", padx=15, pady=(0, 15))

        ttk.Label(status_frame, textvariable=self.status_text,  wraplength=780).pack(anchor="w")

    def create_backup_tab(self, parent):
        source_frame = ttk.LabelFrame(parent, text="Source Directory", padding=10)
        source_frame.pack(fill="x", pady=10)

        ttk.Entry(source_frame, textvariable=self.source_directory).pack(side="left", fill="x", expand=True, padx=(0, 10))

        ttk.Button(source_frame, text="Browse", command=self.select_source_directory).pack(side="right")
        backup_frame = ttk.LabelFrame(parent, text="Backup Destination", padding=10)
        backup_frame.pack(fill="x", pady=10)

        ttk.Entry(backup_frame, textvariable=self.backup_directory).pack(side="left", fill="x", expand=True, padx=(0, 10))
        ttk.Button(backup_frame, text="Browse", command=self.select_backup_directory).pack(side="right")
        info_frame = ttk.LabelFrame(parent, text="Backup Information", padding=10)
        info_frame.pack(fill="x", pady=10)

        self.file_count_label = ttk.Label(info_frame, text="Files: 0")
        self.file_count_label.pack(anchor="w", pady=3)

        self.file_size_label = ttk.Label(info_frame, text="Original Size: 0 B")
        self.file_size_label.pack(anchor="w", pady=3)

        ttk.Button(info_frame, text="Analyze Source Folder", command=self.analyze_source_folder).pack(anchor="w", pady=8)

        self.backup_progress = ttk.Progressbar(parent, mode="indeterminate")
        self.backup_progress.pack(fill="x", pady=15)

        self.create_backup_button = ttk.Button(parent, text="Create ZIP Backup", command=self.start_backup)
        self.create_backup_button.pack(pady=10)

    def create_restore_tab(self, parent):
        backup_file_frame = ttk.LabelFrame(parent, text="ZIP Backup File", padding=10)
        backup_file_frame.pack(fill="x", pady=10)

        ttk.Entry(backup_file_frame, textvariable=self.selected_backup).pack(side="left", fill="x", expand=True, padx=(0, 10))
        ttk.Button(backup_file_frame, text="Browse", command=self.select_backup_file).pack(side="right")
        restore_frame = ttk.LabelFrame(parent, text="Restore Destination", padding=10)
        restore_frame.pack(fill="x", pady=10)

        ttk.Entry(restore_frame, textvariable=self.restore_directory).pack(side="left", fill="x", expand=True, padx=(0, 10))
        ttk.Button(restore_frame, text="Browse", command=self.select_restore_directory).pack(side="right")
        ttk.Label(parent, text=("Restoring a backup will extract all files from the selected ZIP file into the selected destination folder."), wraplength=700).pack(anchor="w", pady=15)

        self.restore_progress = ttk.Progressbar(parent, mode="indeterminate")
        self.restore_progress.pack(fill="x", pady=15)

        self.restore_button = ttk.Button(parent, text="Restore Backup", command=self.start_restore)
        self.restore_button.pack(pady=10)

        ttk.Button(parent, text="Show Available Backups", command=self.show_available_backups).pack(pady=5)

    def select_source_directory(self):
        directory = filedialog.askdirectory(title="Select Source Directory")
        if directory:
            self.source_directory.set(directory)
            self.status_text.set(f"Source selected: {directory}")

    def select_backup_directory(self):
        directory = filedialog.askdirectory(title="Select Backup Destination")
        if directory:
            self.backup_directory.set(directory)
            self.status_text.set(f"Backup destination selected: {directory}")

    def select_backup_file(self):
        file_path = filedialog.askopenfilename(title="Select ZIP Backup", filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")])
        if file_path:
            self.selected_backup.set(file_path)
            self.status_text.set(f"Backup selected: {file_path}")

    def select_restore_directory(self):
        directory = filedialog.askdirectory(title="Select Restore Destination")
        if directory:
            self.restore_directory.set(directory)
            self.status_text.set(f"Restore destination selected: {directory}")

    def analyze_source_folder(self):
        source = self.source_directory.get().strip()
        if not source:
            messagebox.showwarning("Missing Source", "Please select a source directory first.")
            return

        if not os.path.isdir(source):
            messagebox.showerror("Invalid Directory", "The selected source directory does not exist.")
            return

        files = get_files(source)
        total_size = calculate_total_size(files)

        self.file_count_label.config(text=f"Files: {len(files)}")
        self.file_size_label.config(text=f"Original Size: {format_size(total_size)}")
        self.status_text.set(f"Analysis completed. Found {len(files)} files.")
        
    def start_backup(self):
        source = self.source_directory.get().strip()
        backup_destination = self.backup_directory.get().strip()

        if not source or not backup_destination:
            messagebox.showwarning("Missing Information", "Please select both source and backup directories.")
            return

        if not os.path.isdir(source):
            messagebox.showerror("Invalid Source", "The source directory does not exist.")
            return

        if is_directory_inside(source, backup_destination):
            messagebox.showerror("Invalid Backup Location", "The backup destination cannot be inside the source directory.")
            return

        self.create_backup_button.config(state="disabled")
        self.backup_progress.start(10)
        self.status_text.set("Creating compressed ZIP backup...")

        backup_thread = threading.Thread(target=self.backup_worker, args=(source, backup_destination), daemon=True)
        backup_thread.start()

    def backup_worker(self, source, backup_destination):
        try:
            zip_file_path, files = create_backup_zip(source, backup_destination)
            total_size = calculate_total_size(files)
            history_file = Path(backup_destination) / "backup_history.csv"

            write_backup_history(history_file=history_file, zip_file_path=zip_file_path, source_directory=source, file_count=len(files), total_size=total_size)
            self.root.after(0, lambda: self.backup_completed(zip_file_path, len(files), total_size))
        except Exception as error:
            self.root.after(0, lambda: self.backup_failed(str(error)))

    def backup_completed(self, zip_file_path, file_count, total_size):
        self.backup_progress.stop()
        self.create_backup_button.config(state="normal")

        self.status_text.set(f"Backup completed: {zip_file_path}")
        messagebox.showinfo("Backup Completed",
            (
                f"Backup created successfully.\n\n"
                f"File count: {file_count}\n"
                f"Original size: {format_size(total_size)}\n"
                f"ZIP file: {zip_file_path}"
            )
        )

    def backup_failed(self, error_message):
        self.backup_progress.stop()
        self.create_backup_button.config(state="normal")

        self.status_text.set("Backup failed.")

        messagebox.showerror("Backup Error", error_message)

    def start_restore(self):
        zip_file = self.selected_backup.get().strip()
        restore_directory = self.restore_directory.get().strip()

        if not zip_file or not restore_directory:
            messagebox.showwarning("Missing Information", "Please select a ZIP file and restore directory.")
            return

        if not os.path.isfile(zip_file):
            messagebox.showerror("Invalid ZIP File", "The selected ZIP backup file does not exist.")
            return

        if not zip_file.lower().endswith(".zip"):
            messagebox.showerror("Invalid File", "Please select a valid ZIP backup file.")
            return

        confirmation = messagebox.askyesno("Confirm Restore", ("Are you sure you want to restore this backup?\n\n Existing files with the same names may be overwritten."))
        if not confirmation:
            return

        self.restore_button.config(state="disabled")
        self.restore_progress.start(10)
        self.status_text.set("Restoring backup...")

        restore_thread = threading.Thread(target=self.restore_worker, args=(zip_file, restore_directory), daemon=True)
        restore_thread.start()

    def restore_worker(self, zip_file, restore_directory):
        try:
            restored_directory = restore_backup(zip_file, restore_directory)
            self.root.after(0, lambda: self.restore_completed(restored_directory))
        except Exception as error:
            self.root.after(0, lambda: self.restore_failed(str(error)))

    def restore_completed(self, restored_directory):
        self.restore_progress.stop()
        self.restore_button.config(state="normal")

        self.status_text.set(f"Restore completed: {restored_directory}")
        messagebox.showinfo("Restore Completed", f"Files restored successfully to:\n{restored_directory}")

    def restore_failed(self, error_message):
        self.restore_progress.stop()
        self.restore_button.config(state="normal")

        self.status_text.set("Restore failed.")

        messagebox.showerror("Restore Error", error_message)

    def show_available_backups(self):
        backup_directory = self.backup_directory.get().strip()
        if not backup_directory:
            messagebox.showwarning("Missing Directory", "Please select a backup directory first.")
            return

        backups = get_zip_backups(backup_directory)
        if not backups:
            messagebox.showinfo("Available Backups", "No ZIP backups were found.")
            return

        backup_window = tk.Toplevel(self.root)
        backup_window.title("Available Backups")
        backup_window.geometry("650x350")

        ttk.Label(backup_window,text="Available ZIP Backups", font=("Segoe UI", 13, "bold")).pack(pady=10)

        listbox = tk.Listbox(backup_window, width=90, height=12)
        listbox.pack(fill="both", expand=True, padx=15, pady=10)

        for backup in backups:
            listbox.insert(tk.END, str(backup))

        def select_backup():
            selection = listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please select a backup file.")
                return

            selected_file = listbox.get(selection[0])
            self.selected_backup.set(selected_file)
            backup_window.destroy()

        ttk.Button(backup_window, text="Use Selected Backup", command=select_backup).pack(pady=10)
        
# Done