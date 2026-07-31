# 🚀 Day 20 - Event Countdown Timer

Welcome to **Day 20** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Event Countdown Timer** built with Python. It allows users to save upcoming events, view all saved events, and start a live countdown until an event begins. When the countdown reaches zero, the application plays an alert sound to notify the user.

---

## 📌 Project Overview

The application enables users to:

- 📅 Add future events with a specific date and time
- 📋 View all saved events
- ⏳ Start a real-time countdown for any saved event
- 🔔 Receive an alert when the countdown ends
- 💾 Store event information permanently using JSON

Events are saved in a JSON file so they remain available even after closing the application.

---

## ✨ Features

- 📅 Add events with custom date and time
- 📋 View all saved events
- ⏳ Live countdown updated every second
- 🔔 Audible notification when the countdown finishes
- 💾 Persistent event storage using JSON
- 🚫 Prevent duplicate events
- ✅ Validates future dates
- ⚠️ Handles invalid date formats and user input
- 🖥️ Simple menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- `datetime` Module
- `time` Module
- `json` Module
- `os` Module
- `winsound` Module (Windows)

---

## 📂 Project Structure

```text
DAY_20/
│── main20.py
│── events.json
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open the terminal in the project folder.
4. Run the application:

```bash
python main20.py
```

If `events.json` does not exist, it will be created automatically.

---

## 📅 Date Format

When adding an event, enter the date and time in the following format:

```text
YYYY-MM-DD HH:MM:SS
```

Example:

```text
2026-12-31 23:59:59
```

---

## 💻 Sample Output

```text
------ Event Countdown Timer ------

1. Add Event
2. View Events
3. Start Countdown
4. Exit

Enter choice : 1

Enter event name : New Year
Enter event date (YYYY-MM-DD HH:MM:SS) :
2026-12-31 23:59:59

Event saved successfully.
```

### Viewing Events

```text
------ Saved Events ------

1. New Year
   Date : 31 December 2026, 11:59 PM
```

### Countdown

```text
Starting countdown for New Year...

Time Remaining :
120 days, 15 hours, 22 minutes, 10 seconds
```

### Countdown Finished

```text
🎉 Countdown Complete! The event has started.
```

The program also plays a beep sound five times (Windows only).

---

## 📄 Data Storage

Events are stored in `events.json`.

Example:

```json
[
    {
        "Event": "New Year",
        "Date": "2026-12-31 23:59:59"
    }
]
```

---

## 📚 Concepts Practiced

- Functions
- JSON File Handling
- Reading & Writing JSON
- Date & Time Manipulation
- Countdown Timers
- Loops (`while`)
- Conditional Statements
- Exception Handling
- User Input Validation
- File Handling
- OS File Checking
- Real-Time Program Updates
- Windows Sound Notifications

---

## 🎯 Learning Outcome

This project helped me practice:

- Working with dates and times using the `datetime` module
- Building a real-time countdown timer
- Calculating time differences
- Storing structured data in JSON files
- Managing persistent application data
- Validating future dates
- Handling invalid user input gracefully
- Creating interactive command-line applications

---

## ⚠️ Note

- The application currently works best on **Windows** because it uses the `winsound` module.
- Event dates must be in the future.
- Duplicate events (same name and date) are not allowed.
- Events are automatically stored in `events.json`.
- Press **Ctrl + C** while a countdown is running to stop it.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 🔔 Desktop notifications
- 📱 Reminder alerts before the event starts
- 🌍 Time zone support
- ✏️ Edit existing events
- 🗑️ Delete saved events
- 🔁 Repeat yearly events (Birthdays, Anniversaries)
- 📊 Display countdown progress bars
- 🎵 Custom alarm sounds
- 🖥️ GUI version using Tkinter or CustomTkinter
- 🌐 Web-based countdown dashboard

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀