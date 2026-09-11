# Day 62 - Automated Backup Tool
# Backup, compression, restore, and history functions

import csv
import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

def get_files(source_directory):
    """Returns all files inside the source directory recursively."""
    source_directory = Path(source_directory)

    files = []

    for file_path in source_directory.rglob("*"):
        if file_path.is_file():
            files.append(file_path)
    return files

def calculate_total_size(files):
    """Calculates the total size of all files in bytes."""
    total_size = 0

    for file_path in files:
        try:
            total_size += file_path.stat().st_size
        except OSError:
            pass
    return total_size

def create_backup_zip(source_directory, backup_directory):
    """Creates a compressed ZIP backup of the source directory."""
    source_directory = Path(source_directory)
    backup_directory = Path(backup_directory)

    backup_directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_file_name = f"backup_{timestamp}.zip"
    zip_file_path = backup_directory / zip_file_name

    files = get_files(source_directory)

    with zipfile.ZipFile(zip_file_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in files:
            relative_path = file_path.relative_to(source_directory)
            zip_file.write(file_path, arcname=relative_path)
    return zip_file_path, files

def is_directory_inside(parent_directory, child_directory):
    """Checks whether child_directory is inside parent_directory."""
    parent_directory = Path(parent_directory).resolve()
    child_directory = Path(child_directory).resolve()

    try:
        child_directory.relative_to(parent_directory)
        return True
    except ValueError:
        return False

def restore_backup(zip_file_path, restore_directory):
    """Extracts a ZIP backup into the selected restore directory."""
    zip_file_path = Path(zip_file_path)
    restore_directory = Path(restore_directory)

    restore_directory.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, mode="r") as zip_file:
        zip_file.extractall(restore_directory)
    return restore_directory

def get_zip_backups(backup_directory):
    """Returns all ZIP backup files sorted by newest first."""
    backup_directory = Path(backup_directory)

    if not backup_directory.exists():
        return []

    backups = list(backup_directory.glob("*.zip"))
    backups.sort(key=lambda file: file.stat().st_mtime, reverse=True)
    return backups

def write_backup_history(history_file, zip_file_path, source_directory, file_count, total_size):
    """Saves backup details into a CSV history file."""
    history_file = Path(history_file)
    history_file.parent.mkdir(parents=True, exist_ok=True)

    file_exists = history_file.exists()

    with open(history_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Source Directory", "Backup File", "File Count", "Original Size"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(source_directory), str(zip_file_path), file_count, total_size])

def format_size(size_in_bytes):
    """Converts bytes into a readable size."""
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"

    if size_in_bytes < 1024 ** 2:
        return f"{size_in_bytes / 1024:.2f} KB"

    if size_in_bytes < 1024 ** 3:
        return f"{size_in_bytes / (1024 ** 2):.2f} MB"

    return f"{size_in_bytes / (1024 ** 3):.2f} GB"

# Done