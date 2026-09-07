# This is Day 58 project : Pomodoro Timer

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

try:
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False
    
WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60

HISTORY_FILE = "session_history.json"

session_count = 0
completed_pomodoros = 0

timer_running = False
timer_paused = False

current_seconds = WORK_TIME
total_seconds = WORK_TIME

current_session_type = "Work"

timer_after_id = None

def play_notification():
    """Play a sound when a session changes."""
    if SOUND_AVAILABLE:
        try:
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        except Exception:
            window.bell()
    else:
        window.bell()

def load_history():
    """Load previous session history from JSON."""
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_history(history):
    """Save session history to JSON."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

def add_session_to_history(productivity, task, notes):
    """Save completed work session details."""
    history = load_history()
    session_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "session": completed_pomodoros,
        "duration_minutes": WORK_TIME // 60,
        "productivity": productivity,
        "task": task,
        "notes": notes
    }
    history.append(session_data)
    save_history(history)

def update_timer_display():
    """Update timer label and progress bar."""
    mins, secs = divmod(current_seconds, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")

    progress = ((total_seconds - current_seconds) / total_seconds) * 100
    progress_bar["value"] = progress

    session_label.config(text=f"Session {session_count + 1}")
    
def start_timer():
    global timer_running, timer_paused
    if timer_running:
        return
    timer_running = True
    timer_paused = False
    
    start_button.config(state="disabled", text="▶ Running")
    pause_button.config(state="normal")
    
    status_label.config(text=current_session_type, fg=get_session_color())
    countdown()

def countdown():
    global current_seconds
    global timer_running
    global timer_after_id
    
    if not timer_running:
        return
    update_timer_display()
    
    if current_seconds > 0:
        current_seconds -= 1
        timer_after_id = window.after(1000, countdown)
    else:
        timer_running = False
        timer_after_id = None
        
        play_notification()
        finish_session()
        
def finish_session():
    global session_count
    global completed_pomodoros

    if current_session_type == "Work":
        completed_pomodoros += 1
        session_count += 1

        completed_label.config(text=f"Completed Pomodoros: {completed_pomodoros}")
        status_label.config(text="Work Session Complete!", fg="green")
        show_productivity_dialog()
    else:
        status_label.config(text=f"{current_session_type} Complete!", fg="blue")
        messagebox.showinfo("Session Complete", f"{current_session_type} is complete!\n\n Take a moment before starting the next session.")
        prepare_work_session()
    
def prepare_work_session():
    global current_session_type
    global current_seconds
    global total_seconds
    global timer_paused

    timer_paused = False

    current_session_type = "Work"
    current_seconds = WORK_TIME
    total_seconds = WORK_TIME

    status_label.config(text="Work", fg="green")
    progress_bar["value"] = 0

    start_button.config(state="normal", text="▶ Start")
    pause_button.config(state="disabled")

    update_timer_display()
        
def show_productivity_dialog():
    """Ask the user how productive the completed session was."""
    dialog = tk.Toplevel(window)
    dialog.title("Session Review")
    dialog.geometry("450x500")
    dialog.resizable(False, False)
    dialog.transient(window)
    dialog.grab_set()
    
    def close_review():
        messagebox.showwarning("Session Review Required", "Please save your session review before continuing.")
    dialog.protocol("WM_DELETE_WINDOW", close_review)

    title = tk.Label(dialog, text="🎯 Session Complete!", font=("Arial", 22, "bold"))
    title.pack(pady=(20, 5))
    subtitle = tk.Label(dialog, text="How productive were you during this session?", font=("Arial", 11))
    subtitle.pack(pady=5)

    tk.Label(dialog, text="Productivity Rating (1-5)", font=("Arial", 11, "bold")).pack(pady=(20, 5))
    productivity_var = tk.IntVar(value=3)

    rating_frame = tk.Frame(dialog)
    rating_frame.pack()

    for rating in range(1, 6):
        tk.Radiobutton(rating_frame, text=str(rating), variable=productivity_var, value=rating, font=("Arial", 12)).pack(side="left", padx=8)
    tk.Label(dialog, text="What did you work on?", font=("Arial", 11, "bold")).pack(anchor="w", padx=35, pady=(20, 5))

    task_entry = tk.Entry(dialog, width=45, font=("Arial", 11))
    task_entry.pack(padx=35)

    tk.Label(dialog, text="Notes", font=("Arial", 11, "bold")).pack(anchor="w", padx=35, pady=(15, 5))
    notes_entry = tk.Text(dialog, width=40, height=5, font=("Arial", 10))
    notes_entry.pack(padx=35)

    def save_review():
        productivity = productivity_var.get()
        task = task_entry.get().strip()
        notes = notes_entry.get("1.0", tk.END).strip()
        if not task:
            task = "Not specified"
        add_session_to_history(productivity, task, notes)
        dialog.destroy()
        prepare_next_session()
        
    tk.Button(dialog, text="Save Session", command=save_review, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=20, pady=8).pack(pady=20)
    
def prepare_next_session():
    global current_session_type
    global current_seconds
    global total_seconds
    global timer_paused

    timer_paused = False

    if completed_pomodoros > 0 and completed_pomodoros % 4 == 0:
        current_session_type = "Long Break"
        current_seconds = LONG_BREAK
        total_seconds = LONG_BREAK
    else:
        current_session_type = "Short Break"
        current_seconds = SHORT_BREAK
        total_seconds = SHORT_BREAK
        
    status_label.config(text=current_session_type, fg=get_session_color())
    progress_bar["value"] = 0
    start_button.config(state="normal", text="▶ Start")
    pause_button.config(state="disabled")
    update_timer_display()

def pause_timer():
    global timer_running
    global timer_paused
    global timer_after_id

    if not timer_running:
        return
    timer_running = False
    timer_paused = True

    if timer_after_id is not None:
        window.after_cancel(timer_after_id)
        timer_after_id = None

    status_label.config(text=f"{current_session_type} - Paused", fg="purple")
    start_button.config(state="normal", text="▶ Resume")
    pause_button.config(state="disabled")

def reset_timer():
    global session_count
    global completed_pomodoros
    global timer_running
    global timer_paused
    global current_seconds
    global total_seconds
    global current_session_type
    global timer_after_id

    if timer_after_id is not None:
        window.after_cancel(timer_after_id)
        timer_after_id = None

    session_count = 0
    completed_pomodoros = 0

    timer_running = False
    timer_paused = False

    current_session_type = "Work"

    current_seconds = WORK_TIME
    total_seconds = WORK_TIME

    timer_label.config(text="25:00")

    progress_bar["value"] = 0

    status_label.config(text="Ready", fg="black")
    completed_label.config(text="Completed Pomodoros: 0")
    session_label.config(text="Session 1")
    start_button.config(state="normal", text="▶ Start")
    pause_button.config(state="disabled")

def skip_session():
    global timer_running
    global timer_paused
    global current_session_type
    global current_seconds
    global total_seconds
    global timer_after_id

    if timer_after_id is not None:
        window.after_cancel(timer_after_id)
        timer_after_id = None

    timer_running = False
    timer_paused = False

    if current_session_type == "Work":
        prepare_next_session()
    else:
        current_session_type = "Work"
        current_seconds = WORK_TIME
        total_seconds = WORK_TIME

        status_label.config(text="Work", fg="green")
        progress_bar["value"] = 0

        update_timer_display()

        start_button.config(state="normal", text="▶ Start")
        pause_button.config(state="disabled")

def get_session_color():
    if current_session_type == "Work":
        return "green"

    if current_session_type == "Short Break":
        return "orange"

    return "blue"

def show_history():
    history = load_history()
    history_window = tk.Toplevel(window)
    history_window.title("Productivity History")
    history_window.geometry("850x500")

    title = tk.Label(history_window, text="📊 Productivity History", font=("Arial", 20, "bold"))
    title.pack(pady=15)

    columns = ("date", "time", "session", "duration", "rating", "task", "notes")
    tree = ttk.Treeview(history_window, columns=columns, show="headings")
    headings = {"date": "Date", "time": "Time", "session": "Session", "duration": "Minutes", "rating": "Rating", "task": "Task", "notes": "Notes"}

    for column in columns:
        tree.heading(column, text=headings[column])
        tree.column(column, width=100)
    tree.column("task", width=180)
    tree.column("notes", width=220)

    for item in history:
        tree.insert("", tk.END, values=(item.get("date", ""), item.get("time", ""), item.get("session", ""), item.get("duration_minutes", ""),
                item.get("productivity", ""), item.get("task", ""), item.get("notes", "")))

    scrollbar = ttk.Scrollbar(history_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", fill="both", expand=True, padx=(15, 0), pady=10)
    scrollbar.pack(side="right", fill="y", padx=(0, 15), pady=10)
    
window = tk.Tk()
window.title("Pomodoro Productivity Timer")
window.geometry("550x650")
window.resizable(False, False)
window.configure(bg="#f4f4f4")

title_label = tk.Label(window, text="🍅 Pomodoro Timer", font=("Arial", 28, "bold"), bg="#f4f4f4")
title_label.pack(pady=(25, 5))
subtitle_label = tk.Label(window, text="Focus • Work • Rest • Repeat", font=("Arial", 11), fg="#666666", bg="#f4f4f4")
subtitle_label.pack()

session_label = tk.Label(window, text="Session 1", font=("Arial", 14, "bold"), bg="#f4f4f4")
session_label.pack(pady=(25, 5))

status_label = tk.Label(window, text="Ready", font=("Arial", 18, "bold"), fg="black", bg="#f4f4f4")
status_label.pack(pady=5)

timer_label = tk.Label(window, text="25:00", font=("Arial", 65, "bold"), bg="#f4f4f4")
timer_label.pack(pady=15)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=420, mode="determinate", maximum=100)
progress_bar.pack(pady=10)

progress_text = tk.Label(window, text="Session Progress", font=("Arial", 10), fg="#666666", bg="#f4f4f4")
progress_text.pack()

completed_label = tk.Label(window, text="Completed Pomodoros: 0", font=("Arial", 12, "bold"), bg="#f4f4f4")
completed_label.pack(pady=15)

button_frame = tk.Frame(window, bg="#f4f4f4")
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="▶ Start", command=start_timer, font=("Arial", 13, "bold"), width=10, padx=5, pady=8)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="⏸ Pause", command=pause_timer, font=("Arial", 13, "bold"), width=10, padx=5, pady=8, state="disabled")
pause_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="🔄 Reset", command=reset_timer, font=("Arial", 13, "bold"), width=10, padx=5, pady=8)
reset_button.grid(row=0, column=2, padx=5)

second_button_frame = tk.Frame(window, bg="#f4f4f4")
second_button_frame.pack(pady=10)

skip_button = tk.Button(second_button_frame, text="⏭ Skip Session", command=skip_session, font=("Arial", 11), width=15, pady=6)
skip_button.grid(row=0, column=0, padx=10)

history_button = tk.Button(second_button_frame, text="📊 View History", command=show_history, font=("Arial", 11), width=15, pady=6)
history_button.grid(row=0, column=1, padx=10)

window.mainloop()

# Done