# This is Day 20 project : Event Countdown Timer

from datetime import datetime
import time
import json
import os
import winsound

EVENT_FILE = "events.json"

if not os.path.exists(EVENT_FILE):
    with open(EVENT_FILE, "w") as file:
        json.dump([], file)
        
def load_events():
    with open(EVENT_FILE, "r") as file:
        return json.load(file)

def save_events(events):
    with open(EVENT_FILE, "w") as file:
        json.dump(events, file, indent=4)
        
def add_event():
    event_name = input("\nEnter event name : ").strip()

    if not event_name:
        print("Event name cannot be empty.")
        return
    date_input = input("Enter event date (YYYY-MM-DD HH:MM:SS) : ")

    try:
        event_date = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
        if event_date <= datetime.now():
            print("Event date must be in the future.")
            return
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS format")
        return
    
    events = load_events()
    for event in events:
        if (event["Event"].lower() == event_name.lower() and event["Date"] == date_input):
            print("Event already exists.")
            return

    events.append({"Event": event_name, "Date": date_input})

    save_events(events)
    print("Event saved successfully.")
    
def view_events():
    events = load_events()
    if not events:
        print("\nNo saved events.")
        return

    print("\n------ Saved Events ------\n")

    for i, event in enumerate(events, start=1):
        print(f"{i}. {event['Event']}")
        print(f"   Date : {datetime.strptime(event['Date'], '%Y-%m-%d %H:%M:%S').strftime('%d %B %Y, %I:%M %p')}")
        print()
        
def start_saved_event():
    events = load_events()

    if not events:
        print("\nNo saved events.")
        return
    view_events()

    try:
        choice = int(input("\nChoose an event : ")) - 1
        if choice < 0 or choice >= len(events):
            print("Invalid choice.")
            return
        event = events[choice]

        event_date = datetime.strptime(event["Date"], "%Y-%m-%d %H:%M:%S")
        if event_date <= datetime.now():
            print("This event has already passed.")
            return

        print(f"\nStarting countdown for {event['Event']}...\n")
        start_countdown(event_date)
    except KeyboardInterrupt:
        print("\nCountdown Stopped.")
    except ValueError:
        print("Invalid input.")

def calculate_time_remaining(event_date):
    current_datetime = datetime.now()
    time_difference = event_date - current_datetime
    return time_difference

def display_countdown(time_left):
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\rTime Remaining : {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="")
    
def start_countdown(event_date):
    while True:
        time_left = calculate_time_remaining(event_date)
        if time_left.total_seconds() <= 0:
            print("\n🎉 Countdown Complete! The event has started.")
            
            for _ in range(5):
                winsound.Beep(1000, 500)
            break
        display_countdown(time_left)
        time.sleep(1)
        
def show_menu():
    print("\n------ Event Countdown Timer ------\n")
    print("1. Add Event")
    print("2. View Events")
    print("3. Start Countdown")
    print("4. Exit")
    
while True:
    show_menu()
    choice = input("\nEnter choice : ")

    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        start_saved_event()
    elif choice == "4":
        print("\nThank you for using Event Countdown Timer. Goodbye!")
        break
    else:
        print("Invalid choice.")
        
# Done