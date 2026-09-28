# This is Day 79 project : Language Translator Tool

import tkinter as tk
from tkinter import ttk, messagebox
import speech_recognition as sr
from translator import translate_text

LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Russian": "ru",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa"
}

def translate():
    """Translate the entered text."""
    text = input_text.get("1.0", tk.END).strip()
    target_language = target_lang_var.get()

    if not text:
        messagebox.showwarning("Input Required", "Please enter some text to translate.")
        return

    if not target_language:
        messagebox.showwarning("Language Required", "Please select a target language.")
        return

    target_code = LANGUAGES[target_language]

    try:
        status_label.config(text="Translating...")
        root.update_idletasks()
        result = translate_text(text, target_code)
        translated_text = result["translated_text"]

        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
        output_text.config(state="disabled")
        status_label.config(text=f"Translated from {result['source_language']} to {target_language}")
    except Exception as error:
        status_label.config(text="Translation failed.")
        messagebox.showerror("Translation Error", f"Unable to translate the text.\n\n{error}")

def speech_to_text():
    """Capture speech from the microphone and convert it into text."""
    recognizer = sr.Recognizer()

    try:
        status_label.config(text="Listening...")
        root.update_idletasks()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
        status_label.config(text="Recognizing speech...")
        root.update_idletasks()

        text = recognizer.recognize_google(audio)
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, text)
        status_label.config(text="Speech converted to text successfully.")
    except sr.WaitTimeoutError:
        status_label.config(text="No speech detected.")
        messagebox.showwarning("Speech Input", "No speech was detected. Please try again.")
    except sr.UnknownValueError:
        status_label.config(text="Could not understand the speech.")
        messagebox.showwarning("Speech Recognition", "Sorry, I could not understand the speech.")
    except sr.RequestError:
        status_label.config(text="Speech recognition service unavailable.")
        messagebox.showerror("Speech Recognition Error", "The speech recognition service is currently unavailable.")
    except Exception as error:
        status_label.config(text="Microphone error.")
        messagebox.showerror("Microphone Error", str(error))

def copy_translation():
    """Copy translated text to clipboard."""
    text = output_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Nothing to Copy", "There is no translation to copy.")
        return

    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    status_label.config(text="Translation copied to clipboard.")

def clear_all():
    """Clear input and output text."""
    input_text.delete("1.0", tk.END)
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")
    status_label.config(text="Ready")

root = tk.Tk()
root.title("Day 79 - Language Translator")
root.geometry("700x650")
root.minsize(600, 550)

title_label = tk.Label(root, text="🌐 Language Translator", font=("Arial", 22, "bold"))
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(root, text="Translate text or use your voice as input", font=("Arial", 11))
subtitle_label.pack(pady=(0, 15))

input_label = tk.Label(root, text="Enter Text", font=("Arial", 12, "bold"))
input_label.pack(anchor="w", padx=30)

input_text = tk.Text(root, height=7, width=70, wrap="word", font=("Arial", 11))
input_text.pack(padx=30, pady=8)

speech_button = tk.Button(root, text="🎤 Speak", command=speech_to_text, font=("Arial", 11, "bold"), width=18)
speech_button.pack(pady=5)

language_frame = tk.Frame(root)
language_frame.pack(pady=15)

target_label = tk.Label(language_frame, text="Translate To:", font=("Arial", 11, "bold"))
target_label.grid(row=0, column=0, padx=5)

target_lang_var = tk.StringVar()
target_lang_var.set("Spanish")

language_dropdown = ttk.Combobox(language_frame, textvariable=target_lang_var, values=list(LANGUAGES.keys()), state="readonly", width=20)
language_dropdown.grid(row=0, column=1, padx=5)

translate_button = tk.Button(root, text="Translate", command=translate, font=("Arial", 12, "bold"), width=20)
translate_button.pack(pady=5)

output_label = tk.Label(root, text="Translation", font=("Arial", 12, "bold"))
output_label.pack(anchor="w", padx=30, pady=(15, 0))

output_text = tk.Text(root, height=7, width=70, wrap="word", font=("Arial", 11), state="disabled")
output_text.pack(padx=30, pady=8)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

copy_button = tk.Button(button_frame, text="Copy Translation", command=copy_translation, width=18)
copy_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_all, width=18)
clear_button.grid(row=0, column=1, padx=5)

status_label = tk.Label(root, text="Ready", font=("Arial", 10))
status_label.pack(pady=8)

root.mainloop()

# Done