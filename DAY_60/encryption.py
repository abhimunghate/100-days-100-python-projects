# Day 60 - Encryption Module

from pathlib import Path
from cryptography.fernet import Fernet

KEY_FILE = Path("secret.key")

def generate_key():
    """Generate an encryption key if one does not already exist."""
    if not KEY_FILE.exists():
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    """Load the encryption key."""
    if not KEY_FILE.exists():
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_text(text):
    """Encrypt plain text."""
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(text.encode("utf-8"))

def decrypt_text(encrypted_text):
    """Decrypt encrypted text."""
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode("utf-8")

# Done