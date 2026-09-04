# This is Day 55 project : Music Playlist Organizer

import os
import shutil
import json
import hashlib
import threading
import re
import tkinter as tk

from tkinter import ttk, filedialog, messagebox
from mutagen import File

SUPPORTED_EXTENSIONS = (".mp3", ".flac", ".wav", ".aac", ".ogg", ".m4a", ".wma", ".aiff", ".aif")

def scan_directory(directory):
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                music_files.append(os.path.join(root, file))
    return music_files

def get_tag(audio, tag, default):
    try:
        value = audio.get(tag)
        if value and value[0]:
            return str(value[0]).strip()
    except Exception:
        pass
    return default

def extract_metadata(file_path):
    try:
        audio = File(file_path, easy=True)
        if audio is None:
            return None
        return {
            "title" : get_tag(audio, "title", "Unknown Title"),
            "artist" : get_tag(audio, "artist", "Unknown Artist"),
            "album" : get_tag(audio, "album", "Unknown Album"),
            "genre" : get_tag(audio, "genre", "Unknown Genre"),
            "file" : file_path
        }
    except Exception as e:
        print(f"Error extracting metadata for {file_path} : {e}")
        return None

def sanitize_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = name.strip()
    if not name:
        name = "Unknown"
    return name

def get_unique_destination(destination):
    if not os.path.exists(destination):
        return destination
    directory = os.path.dirname(destination)
    filename = os.path.basename(destination)

    name, extension = os.path.splitext(filename)
    counter = 1

    while True:
        new_filename = f"{name}_{counter}{extension}"
        new_destination = os.path.join(directory, new_filename)
        if not os.path.exists(new_destination):
            return new_destination
        counter += 1

def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(1024 * 1024)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return None

def find_duplicates(music_files, log_callback=None):
    hashes = {}
    duplicates = []
    total = len(music_files)

    for index, file_path in enumerate(music_files, start=1):
        file_hash = calculate_file_hash(file_path)
        if file_hash is None:
            continue
        
        if file_hash in hashes:
            duplicates.append({"duplicate": file_path, "original": hashes[file_hash]})
        else:
            hashes[file_hash] = file_path

        if log_callback:
            log_callback(f"Checking duplicates: {index}/{total}")
    return duplicates

def remove_duplicates(duplicates, log_callback=None):
    removed = []
    for item in duplicates:
        duplicate = item["duplicate"]

        try:
            os.remove(duplicate)
            removed.append(duplicate)
            if log_callback:
                log_callback(f"Removed duplicate: {duplicate}")
        except Exception as e:
            if log_callback:
                log_callback(f"Could not remove {duplicate}: {e}")
    return removed

def create_organization_plan(music_files, output_directory):
    plan = []

    for file_path in music_files:
        metadata = extract_metadata(file_path)
        
        if not metadata:
            continue
        artist = sanitize_filename(metadata["artist"])
        album = sanitize_filename(metadata["album"])
        artist_folder = os.path.join(output_directory, artist)
        album_folder = os.path.join(artist_folder, album)
        destination = os.path.join(album_folder, os.path.basename(file_path))
        plan.append({"source": file_path, "destination": destination, "metadata": metadata})
    return plan

def organize_files(plan, log_callback=None):
    moved_files = []
    
    for item in plan:
        source = item["source"]
        destination = item["destination"]

        try:
            destination_folder = os.path.dirname(destination)
            os.makedirs(destination_folder, exist_ok=True)
            destination = get_unique_destination(destination)
            shutil.move(source, destination)
            moved_files.append({"source": source, "destination": destination, "metadata": item["metadata"]})

            if log_callback:
                log_callback(f"Moved: {os.path.basename(source)}")
        except Exception as e:
            if log_callback:
                log_callback(f"Error moving {source}: {e}")
    return moved_files

def save_summary_to_json(organized_files, duplicates, output_file):
    summary = {
        "organized_files": organized_files,
        "duplicates": duplicates,
        "statistics": {
            "organized_count": len(organized_files),
            "duplicate_count": len(duplicates)
        }
    }

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(summary, json_file, indent=4, ensure_ascii=False)

class MusicPlaylistOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Music Playlist Organizer")
        self.root.geometry("950x700")
        self.root.minsize(850, 600)
        self.music_files = []
        self.duplicates = []
        self.organization_plan = []
        self.organized_files = []
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="🎵 Music Playlist Organizer", font=("Arial", 24, "bold"))
        title.pack(pady=(20, 5))

        subtitle = tk.Label(self.root, text="Organize your music library using Artist and Album metadata", font=("Arial", 11))
        subtitle.pack(pady=(0, 15))

        folder_frame = ttk.LabelFrame(self.root, text="Folders", padding=15)
        folder_frame.pack(fill="x", padx=25, pady=10)

        ttk.Label(folder_frame, text="Music Folder:").grid(row=0, column=0, sticky="w", pady=5)
        self.music_path_var = tk.StringVar()
        ttk.Entry(folder_frame, textvariable=self.music_path_var).grid(row=0, column=1, sticky="ew", padx=10)
        ttk.Button(folder_frame, text="Browse", command=self.select_music_folder).grid(row=0, column=2)
        ttk.Label(folder_frame, text="Output Folder:").grid(row=1, column=0, sticky="w", pady=5)
        self.output_path_var = tk.StringVar()
        ttk.Entry(folder_frame, textvariable=self.output_path_var).grid(row=1, column=1, sticky="ew", padx=10)
        ttk.Button(folder_frame, text="Browse", command=self.select_output_folder).grid(row=1, column=2)
        folder_frame.columnconfigure(1, weight=1)

        formats_text = ("Supported: MP3 • FLAC • WAV • AAC • OGG • M4A • WMA • AIFF")
        ttk.Label(self.root, text=formats_text).pack(pady=5)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=15)

        self.scan_button = ttk.Button(button_frame, text="🔍 Scan Music", command=self.start_scan)
        self.scan_button.grid(row=0, column=0, padx=5)

        self.duplicate_button = ttk.Button(button_frame, text="🧹 Find Duplicates", command=self.start_duplicate_scan, state="disabled")
        self.duplicate_button.grid(row=0, column=1, padx=5)

        self.remove_button = ttk.Button(button_frame, text="🗑 Remove Duplicates", command=self.remove_duplicate_files, state="disabled")
        self.remove_button.grid(row=0, column=2, padx=5)

        self.preview_button = ttk.Button(button_frame, text="👀 Preview", command=self.show_preview, state="disabled")
        self.preview_button.grid(row=0, column=3, padx=5)

        self.organize_button = ttk.Button(button_frame, text="📁 Organize Music", command=self.start_organization, state="disabled")
        self.organize_button.grid(row=0, column=4, padx=5)

        stats_frame = ttk.Frame(self.root)
        stats_frame.pack(fill="x", padx=25, pady=5)

        self.stats_label = ttk.Label(stats_frame, text="No music scanned yet.")
        self.stats_label.pack(anchor="w")

        self.progress = ttk.Progressbar(self.root, mode="indeterminate")
        self.progress.pack(fill="x", padx=25, pady=10)

        log_frame = ttk.LabelFrame(self.root, text="Activity Log", padding=10)
        log_frame.pack(fill="both", expand=True, padx=25, pady=(5, 20))

        self.log_text = tk.Text(log_frame, height=15, wrap="word", state="disabled")
        self.log_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        scrollbar.pack(side="right", fill="y")

        self.log_text.configure(yscrollcommand=scrollbar.set)

    def log(self, message):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def select_music_folder(self):
        folder = filedialog.askdirectory(title="Select Music Folder")
        if folder:
            self.music_path_var.set(folder)

    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_path_var.set(folder)

    def start_scan(self):
        directory = self.music_path_var.get().strip()
        if not directory:
            messagebox.showwarning("Missing Folder", "Please select a music folder.")
            return

        if not os.path.isdir(directory):
            messagebox.showerror("Invalid Folder", "The selected music folder does not exist.")
            return

        self.scan_button.config(state="disabled")
        self.progress.start()
        
        thread = threading.Thread(target=self.scan_music, args=(directory,), daemon=True)
        thread.start()

    def scan_music(self, directory):
        self.music_files = scan_directory(directory)
        self.root.after(0, self.scan_complete)

    def scan_complete(self):
        self.progress.stop()
        self.scan_button.config(state="normal")

        count = len(self.music_files)
        self.log(f"Found {count} music file(s).")

        self.stats_label.config(text=f"Music files found: {count}")

        if count == 0:
            messagebox.showinfo("Scan Complete", "No supported music files were found.")
            return

        self.duplicate_button.config(state="normal")
        self.preview_button.config(state="normal")
        self.organize_button.config(state="normal")

        messagebox.showinfo("Scan Complete", f"Found {count} music file(s).")

    def start_duplicate_scan(self):
        if not self.music_files:
            return

        self.duplicate_button.config(state="disabled")
        self.progress.start()

        thread = threading.Thread(target=self.scan_duplicates, daemon=True)
        thread.start()

    def scan_duplicates(self):
        self.duplicates = find_duplicates(self.music_files, self.log)
        self.root.after(0, self.duplicate_scan_complete)

    def duplicate_scan_complete(self):
        self.progress.stop()
        self.duplicate_button.config(state="normal")

        count = len(self.duplicates)
        self.log(f"Duplicate scan complete: {count} duplicate file(s) found.")

        self.stats_label.config(
            text=(
                f"Music files: {len(self.music_files)} | "
                f"Duplicates: {count}"
            )
        )

        if count > 0:
            self.remove_button.config(state="normal")
            messagebox.showinfo("Duplicates Found", f"{count} duplicate file(s) found.")
        else:
            messagebox.showinfo("No Duplicates", "No duplicate files were found.")

    def remove_duplicate_files(self):
        if not self.duplicates:
            return
        
        answer = messagebox.askyesno("Remove Duplicates", (f"{len(self.duplicates)} duplicate file(s) will be permanently deleted.\n\n Do you want to continue?"))
        if not answer:
            return

        removed = remove_duplicates(self.duplicates, self.log)
        self.log(f"Removed {len(removed)} duplicate file(s).")
        self.remove_button.config(state="disabled")
        self.stats_label.config(
            text=(
                f"Music files: {len(self.music_files)} | "
                f"Duplicates removed: {len(removed)}"
            )
        )

        messagebox.showinfo("Duplicates Removed", f"{len(removed)} duplicate file(s) removed.")

    def show_preview(self):
        output_directory = self.output_path_var.get().strip()
        if not output_directory:
            messagebox.showwarning("Missing Output Folder", "Please select an output folder first.")
            return
        self.organization_plan = create_organization_plan(self.music_files, output_directory)

        if not self.organization_plan:
            messagebox.showinfo("Preview", "No files could be prepared for organization.")
            return

        preview_window = tk.Toplevel(self.root)
        preview_window.title("Organization Preview")
        preview_window.geometry("850x500")

        ttk.Label(preview_window, text="Organization Preview", font=("Arial", 16, "bold")).pack(pady=10)
        tree_frame = ttk.Frame(preview_window)
        tree_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = ("file", "artist", "album", "destination")

        tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

        tree.heading("file", text="File")
        tree.heading("artist", text="Artist")
        tree.heading("album", text="Album")
        tree.heading("destination", text="Destination")

        tree.column("file", width=180)
        tree.column("artist", width=140)
        tree.column("album", width=140)
        tree.column("destination", width=350)

        for item in self.organization_plan:
            metadata = item["metadata"]
            tree.insert("", "end", values=(os.path.basename(item["source"]), metadata["artist"], metadata["album"], item["destination"]))

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def start_organization(self):
        output_directory = self.output_path_var.get().strip()
        if not output_directory:
            messagebox.showwarning("Missing Output Folder", "Please select an output folder.")
            return

        if not self.music_files:
            messagebox.showwarning("No Music", "Please scan a music folder first.")
            return

        answer = messagebox.askyesno("Organize Music", (f"{len(self.music_files)} music file(s) will be organized.\n\n Do you want to continue?"))
        if not answer:
            return

        self.organize_button.config(state="disabled")
        self.progress.start()

        thread = threading.Thread(target=self.organize_music, args=(output_directory,), daemon=True)
        thread.start()

    def organize_music(self, output_directory):
        self.organization_plan = create_organization_plan(self.music_files, output_directory)
        self.organized_files = organize_files(self.organization_plan, self.log)
        summary_file = os.path.join(output_directory, "music_summary.json")
        save_summary_to_json(self.organized_files, self.duplicates, summary_file)
        self.root.after(0, lambda: self.organization_complete(summary_file))

    def organization_complete(self, summary_file):
        self.progress.stop()
        self.organize_button.config(state="normal")

        count = len(self.organized_files)

        self.log(f"Organization complete. {count} file(s) organized.")
        self.log(f"Summary saved to: {summary_file}")

        messagebox.showinfo("Organization Complete", (
                f"{count} music file(s) organized successfully!\n\n"
                f"Summary:\n{summary_file}"))

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlaylistOrganizer(root)
    root.mainloop()
    
# Done