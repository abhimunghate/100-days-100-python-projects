# Day 60 - Diary Manager

from pathlib import Path
from datetime import datetime
import re

from encryption import encrypt_text, decrypt_text

ENTRIES_FOLDER = Path("data/entries")

def initialize_storage():
    """Create the diary storage folder."""
    ENTRIES_FOLDER.mkdir(parents=True, exist_ok=True)

def sanitize_filename(title):
    """Remove characters that are unsafe for filenames."""
    title = re.sub(r'[\\/:*?"<>|]', "", title)
    title = title.strip()
    if not title:
        title = "Untitled"
    return title

def create_entry(title, content):
    """Create and save an encrypted diary entry."""
    initialize_storage()
    title = title.strip()
    if not title:
        raise ValueError("Diary title cannot be empty.")

    if not content.strip():
        raise ValueError("Diary content cannot be empty.")

    timestamp = datetime.now()
    date_string = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    safe_title = sanitize_filename(title)
    filename = f"{date_string}_{safe_title}.diary"
    file_path = ENTRIES_FOLDER / filename
    entry_data = (
        f"TITLE:{title}\n"
        f"DATE:{timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"\n"
        f"{content}"
    )

    encrypted_data = encrypt_text(entry_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    return file_path

def get_entries():
    """Return all diary entry files."""
    initialize_storage()
    entries = list(ENTRIES_FOLDER.glob("*.diary"))
    entries.sort(reverse=True)
    return entries

def read_entry(file_path):
    """Read and decrypt a diary entry."""
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    return decrypt_text(encrypted_data)

def delete_entry(file_path):
    """Delete a diary entry."""
    if file_path.exists():
        file_path.unlink()
        return True
    return False

def update_entry(file_path, title, content):
    """Update an existing diary entry."""
    if not file_path.exists():
        raise FileNotFoundError("Diary entry not found.")

    timestamp = datetime.now()
    entry_data = (
        f"TITLE:{title.strip()}\n"
        f"DATE:{timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"\n"
        f"{content}"
    )

    encrypted_data = encrypt_text(entry_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def search_entries(keyword):
    """Search diary entries by title or content."""
    keyword = keyword.strip().lower()
    if not keyword:
        return []
    results = []

    for file_path in get_entries():
        try:
            content = read_entry(file_path)
            if keyword in content.lower():
                results.append(file_path)
        except Exception:
            # Ignore corrupted/unreadable entries
            continue
    return results

def extract_title(entry_content):
    """Extract the title from decrypted diary content."""
    for line in entry_content.splitlines():
        if line.startswith("TITLE:"):
            return line.replace("TITLE:", "", 1).strip()
    return "Untitled"

def extract_date(entry_content):
    """Extract the date from decrypted diary content."""
    for line in entry_content.splitlines():
        if line.startswith("DATE:"):
            return line.replace("DATE:", "", 1).strip()
    return "Unknown date"

def extract_body(entry_content):
    """Extract the actual diary content."""
    parts = entry_content.split("\n\n", 1)
    if len(parts) == 2:
        return parts[1]
    return entry_content

# Done