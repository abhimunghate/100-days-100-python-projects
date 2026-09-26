# This is Day 77 project : AI Chatbot with NLP

import re
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

import nltk
import torch
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import AutoTokenizer, AutoModelForCausalLM

def setup_nltk():
    """Download required NLTK resources if they are missing."""
    resources = [("tokenizers/punkt", "punkt"), ("tokenizers/punkt_tab", "punkt_tab"), ("corpora/stopwords", "stopwords")]
    for path, resource in resources:
        try:
            nltk.data.find(path)
        except LookupError:
            try:
                nltk.download(resource, quiet=True)
            except Exception:
                pass

setup_nltk()

MODEL_NAME = "microsoft/DialoGPT-small"
# If your computer can comfortably handle the larger model, you can change the above line to:
# MODEL_NAME = "microsoft/DialoGPT-medium"

tokenizer = None
model = None

conversation_history = []

model_ready = False
model_loading = False

def clean_text(text):
    """Clean text using basic NLP preprocessing."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    try:
        tokens = word_tokenize(text)
    except Exception:
        tokens = text.split()
        
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def simple_chatbot(user_input):
    """Handle common messages using predefined responses."""
    text = user_input.lower().strip()

    responses = {
        "hello": ("Hi there! 👋 How can I assist you?"),
        "hi": ("Hello! 👋 Nice to meet you."),
        "hey": ("Hey! How can I help you?"),
        "how are you": ("I'm doing great! Thanks for asking. 😊"),
        "what is your name": ("I'm an AI chatbot built with Python, NLP and a Transformer model."),
        "who are you": ("I'm a Python-based AI chatbot using NLP and DialoGPT."),
        "thanks": ("You're welcome! 😊"),
        "thank you": ("You're welcome! Let me know if you need anything else."),
        "bye": ("Goodbye! Have a wonderful day! 👋"),
        "goodbye": ("Goodbye! See you again! 👋"),
        "help": ("You can chat with me, ask simple questions, or just start a conversation.")
    }

    if text in responses:
        return responses[text]

    if "how are you" in text:
        return responses["how are you"]

    if "your name" in text:
        return responses["what is your name"]

    if "who are you" in text:
        return responses["who are you"]

    if "thank" in text:
        return responses["thanks"]

    if text.startswith("hello"):
        return responses["hello"]

    if text.startswith("hi"):
        return responses["hi"]

    if text.startswith("hey"):
        return responses["hey"]

    if "goodbye" in text or text == "bye":
        return responses["bye"]

    return None

def load_model():
    """Load tokenizer and DialoGPT model. This runs in a background thread so the GUI remains responsive."""
    global tokenizer
    global model
    global model_ready
    global model_loading

    try:
        model_loading = True
        update_status("Loading AI model... First startup may take a while.")

        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        model.eval()

        model_ready = True
        model_loading = False

        update_status("AI model ready. You can start chatting.")
        enable_send_button()
        append_message("AI", "Hello! 👋 I'm ready to chat. How can I help you?")
    except Exception as error:
        model_ready = False
        model_loading = False

        update_status("Could not load AI model.")
        append_message("System", f"Model loading error:\n{error}")
        messagebox.showerror("Model Error", ("The AI model could not be loaded.\n\n" "Check your internet connection and " "installed packages."))

def generate_ai_response(user_input):
    """Generate a response using DialoGPT."""
    global conversation_history

    if not model_ready:
        return ("The AI model is still loading. Please wait a moment.")

    try:
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

        if conversation_history:
            history_ids = torch.cat(conversation_history, dim=-1)
            input_ids = torch.cat([history_ids, new_input_ids], dim=-1)
        else:
            input_ids = new_input_ids

        max_context_length = 512

        if input_ids.shape[-1] > max_context_length:
            input_ids = input_ids[:, -max_context_length:]

        with torch.no_grad():
            output_ids = model.generate(input_ids, max_new_tokens=80, pad_token_id=tokenizer.eos_token_id, do_sample=True, top_k=50, top_p=0.95, temperature=0.75, repetition_penalty=1.1)

        response_ids = output_ids[:, input_ids.shape[-1]:]
        response = tokenizer.decode(response_ids[0], skip_special_tokens=True).strip()

        conversation_history.append(output_ids[:, -min(output_ids.shape[-1], 384):])

        if len(conversation_history) > 4:
            conversation_history = conversation_history[-4:]

        if not response:
            response = ("I'm not sure how to respond to that. Could you rephrase it?")
        return response
    except Exception as error:
        return ("Sorry, I encountered an error while generating a response.\n\n{error}")

def send_message(event=None):
    """Process the user's message."""
    user_input = input_box.get().strip()
    if not user_input:
        return

    input_box.delete(0, tk.END)
    append_message("You", user_input)

    if user_input.lower() in ["exit", "quit", "close"]:
        append_message("AI", "Goodbye! 👋")
        root.after(1000, root.destroy)
        return

    rule_response = simple_chatbot(user_input)
    if rule_response:
        append_message("AI", rule_response)
        update_status("Ready")
        return

    if not model_ready:
        append_message("AI", "The AI model is still loading. Please wait a moment.")
        return

    send_button.config(state="disabled")
    input_box.config(state="disabled")
    update_status("AI is thinking...")

    thread = threading.Thread(target=generate_and_display_response, args=(user_input,), daemon=True)
    thread.start()

def generate_and_display_response(user_input):
    """Generate AI response in background thread."""
    response = generate_ai_response(user_input)
    root.after(0, lambda: finish_ai_response(response))

def finish_ai_response(response):
    """Display generated response and restore GUI."""
    append_message("AI", response)
    input_box.config(state="normal")
    send_button.config(state="normal")
    input_box.focus()

    update_status("Ready")

def append_message(sender, message):
    """Add a message to the chat window."""
    chat_area.config(state="normal")

    if sender == "You":
        chat_area.insert(tk.END, f"You: {message}\n\n")
    elif sender == "AI":

        chat_area.insert(tk.END, f"AI: {message}\n\n")
    else:
        chat_area.insert(tk.END, f"{sender}: {message}\n\n")
    chat_area.see(tk.END)
    chat_area.config(state="disabled")

def clear_chat():
    """Clear chat history."""
    global conversation_history
    conversation_history = []

    chat_area.config(state="normal")
    chat_area.delete("1.0", tk.END)
    chat_area.config(state="disabled")
    append_message("AI", "Chat cleared. How can I help you?")
    update_status("Ready")

def update_status(message):
    """Safely update status label from any thread."""
    root.after(0, lambda: status_label.config(text=message))

def enable_send_button():
    """Enable send button after model loading."""
    root.after(0, lambda: send_button.config(state="normal"))

def on_closing():
    """Handle application closing."""
    root.destroy()

root = tk.Tk()
root.title("🤖 Day 77 - AI Chatbot with NLP")
root.geometry("900x700")
root.minsize(700, 550)

header_frame = tk.Frame(root, padx=15, pady=15)
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="🤖 AI CHATBOT WITH NLP", font=("Segoe UI", 22, "bold"))
title_label.pack()

subtitle_label = tk.Label(header_frame, text=("Python • NLTK • Transformers • DialoGPT"), font=("Segoe UI", 10))
subtitle_label.pack(pady=(5, 0))

chat_frame = tk.Frame(root, padx=15)
chat_frame.pack(fill="both", expand=True)

chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, font=("Segoe UI", 11), state="disabled", padx=10, pady=10)
chat_area.pack(fill="both", expand=True)

input_frame = tk.Frame(root, padx=15, pady=10)
input_frame.pack(fill="x")

input_box = tk.Entry(input_frame, font=("Segoe UI", 12))
input_box.pack(side="left", fill="x", expand=True, padx=(0, 10))

send_button = tk.Button(input_frame, text="Send", font=("Segoe UI", 10, "bold"), width=10, command=send_message, state="disabled")
send_button.pack(side="right")

input_box.bind("<Return>", send_message)

control_frame = tk.Frame(root, pady=5)
control_frame.pack()

clear_button = tk.Button(control_frame, text="🧹 Clear Chat", width=15, command=clear_chat)
clear_button.pack(side="left", padx=5)

exit_button = tk.Button(control_frame, text="❌ Exit", width=15, command=on_closing)
exit_button.pack(side="left", padx=5)

status_label = tk.Label(root, text="Loading AI model...", anchor="w", padx=15, pady=5, font=("Segoe UI", 9))
status_label.pack(fill="x")

root.protocol("WM_DELETE_WINDOW", on_closing)
model_thread = threading.Thread(target=load_model, daemon=True)
model_thread.start()

root.mainloop()

# Done