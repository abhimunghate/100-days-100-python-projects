# This is Day 74 project : Voice Assistant

import os
import subprocess
import threading
import webbrowser
from datetime import datetime

import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import tkinter as tk

from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

engine = pyttsx3.init()
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8
recognizer.energy_threshold = 300

def speak(text):
    engine.say(text)
    engine.runAndWait()

def add_message(sender, message):
    conversation_text.config(state="normal")
    conversation_text.insert(tk.END, f"{sender}: {message}\n\n")
    conversation_text.see(tk.END)
    conversation_text.config(state="disabled")

def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    response = (f"The current time is {current_time}.")
    add_message("Assistant", response)
    speak(response)

def search_wikipedia(query):
    try:
        search_results = wikipedia.search(query, results=5)
        if not search_results:
            response = (f"I could not find any Wikipedia results for {query}.")
            add_message("Assistant", response)
            speak(response)
            return

        page_title = search_results[0]
        result = wikipedia.summary(page_title, sentences=2, auto_suggest=False)
        response = (f"According to Wikipedia, {result}")
        add_message("Assistant", response)
        speak(response)
    except wikipedia.exceptions.DisambiguationError as e:
        if e.options:
            try:
                result = wikipedia.summary(e.options[0], sentences=2, auto_suggest=False)
                add_message("Assistant", result)
                speak(result)
            except Exception as error:
                print("Wikipedia error:", error)
                response = ("There are multiple results. Please be more specific.")
                add_message("Assistant", response)
                speak(response)
        else:
            response = ("There are multiple results. Please be more specific.")
            add_message("Assistant", response)
            speak(response)
    except wikipedia.exceptions.PageError:
        response = ("I could not find that page on Wikipedia.")
        add_message("Assistant", response)
        speak(response)
    except Exception as e:
        print("Wikipedia Error:", type(e).__name__, str(e))
        response = ("Sorry, I could not search Wikipedia.")
        add_message("Assistant", response)
        speak(response)

def open_application(application):
    application = application.lower()
    if "chrome" in application:
        try:
            chrome_paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")]

            chrome_path = None
            for path in chrome_paths:
                if os.path.exists(path):
                    chrome_path = path
                    break

            if chrome_path:
                subprocess.Popen([chrome_path])
            else:
                webbrowser.open("https://www.google.com")

            response = "Opening Google Chrome."
        except Exception:
            response = ("I could not open Google Chrome.")
    elif "notepad" in application:
        try:
            subprocess.Popen(["notepad.exe"])
            response = "Opening Notepad."
        except Exception:
            response = "I could not open Notepad."
    elif "calculator" in application:
        try:
            subprocess.Popen(["calc.exe"])
            response = "Opening Calculator."
        except Exception:
            response = "I could not open Calculator."
    else:
        response = ("I currently support Chrome, Notepad and Calculator.")
    add_message("Assistant", response)
    speak(response)

def get_weather(city):
    if not WEATHER_API_KEY:
        response = ("Weather API key is not configured. Please add WEATHER_API_KEY to your .env file.")
        add_message("Assistant", response)
        speak(response)
        return

    url = ("https://api.openweathermap.org/data/2.5/weather")
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if response.status_code != 200:
            message = data.get("message", "Unable to get weather information.")
            add_message("Assistant", message)
            speak(message)
            return

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        weather_message = (f"The weather in {city} is {description}. The temperature is {temperature:.1f} degrees Celsius, feels like {feels_like:.1f} degrees, with {humidity}% humidity.")
        add_message("Assistant", weather_message)
        speak(weather_message)
    except requests.exceptions.RequestException:
        message = ("I could not connect to the weather service.")
        add_message("Assistant", message)
        speak(message)
    except Exception:
        message = ("Sorry, I could not retrieve the weather.")
        add_message("Assistant", message)
        speak(message)

def recognize_speech():
    try:
        with sr.Microphone() as source:
            update_status("Listening...")
            add_message("System", "Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        update_status("Processing...")
        text = recognizer.recognize_google(audio)
        text = text.lower()

        add_message("You", text)
        update_status("Ready")
        return text
    except sr.WaitTimeoutError:
        update_status("No speech detected")
        add_message("Assistant", "I didn't hear anything.")
        return None
    except sr.UnknownValueError:
        update_status("Could not understand")
        add_message("Assistant", "Sorry, I could not understand you.")
        return None
    except sr.RequestError:
        update_status("Speech service unavailable")
        add_message("Assistant", "Speech recognition service is unavailable.")
        return None
    except Exception as e:
        update_status("Microphone error")
        add_message("Assistant", f"Microphone error: {e}")
        return None

def process_command(command):
    if not command:
        return

    if "time" in command:
        get_time()
    elif ("open chrome" in command or "open google chrome" in command):
        open_application("chrome")
    elif "open notepad" in command:
        open_application("notepad")
    elif ("open calculator" in command or "open calc" in command):
        open_application("calculator")
    elif "wikipedia" in command:
        query = command
        query = query.replace("search wikipedia for", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("wikipedia", "")
        query = query.strip()
        if query:
            search_wikipedia(query)
        else:
            response = ("Please tell me what you want to search on Wikipedia.")
            add_message("Assistant", response)
            speak(response)
    elif "weather" in command:
        city = command
        city = city.replace("what is the weather in", "")
        city = city.replace("what is the weather of", "")
        city = city.replace("weather in", "")
        city = city.replace("weather of", "")
        
        city = city.strip()
        if city:
            get_weather(city)
        else:
            response = ("Please specify a city. For example, say weather in Nagpur.")
            add_message("Assistant", response)
            speak(response)
    elif ("exit" in command or "stop" in command or "goodbye" in command or "quit" in command):
        response = "Goodbye! Have a nice day."
        add_message("Assistant", response)
        speak(response)
        root.after(1000, root.destroy)
    else:
        response = ("Sorry, I don't understand that command.")
        add_message("Assistant", response)
        speak(response)

def listen_button():
    def listen_thread():
        command = recognize_speech()
        if command:
            process_command(command)
        update_status("Ready")

    threading.Thread(target=listen_thread, daemon=True).start()

def update_status(status):
    root.after(0, lambda: status_label.config(text=f"Status: {status}"))

def clear_conversation():
    conversation_text.config(state="normal")
    conversation_text.delete("1.0", tk.END)
    conversation_text.config(state="disabled")

root = tk.Tk()
root.title("Voice Assistant")
root.geometry("800x650")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

title_label = tk.Label(root, text="🎙 Voice Assistant", font=("Arial", 26, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=(25, 5))

subtitle_label = tk.Label(root, text="Speech Recognition • Applications • Weather • Wikipedia", font=("Arial", 11), bg="#1e1e1e", fg="#aaaaaa")
subtitle_label.pack(pady=(0, 20))

conversation_text = tk.Text(root, width=85, height=22, font=("Arial", 11), bg="#2b2b2b", fg="white", insertbackground="white", relief="flat", wrap="word", padx=12, pady=12)
conversation_text.pack(padx=30)
conversation_text.config(state="disabled")

status_label = tk.Label(root, text="Status: Ready", font=("Arial", 11), bg="#1e1e1e", fg="#aaaaaa")
status_label.pack(pady=12)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=5)

listen_btn = tk.Button(button_frame, text="🎙 Listen", command=listen_button, font=("Arial", 11, "bold"), bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", relief="flat", padx=25, pady=10, cursor="hand2")
listen_btn.pack(side="left", padx=8)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_conversation, font=("Arial", 11, "bold"), bg="#555555", fg="white", activebackground="#444444", activeforeground="white", relief="flat", padx=25, pady=10, cursor="hand2")
clear_btn.pack(side="left", padx=8)

exit_btn = tk.Button(button_frame, text="Exit", command=root.destroy, font=("Arial", 11, "bold"), bg="#c0392b", fg="white", activebackground="#a93226", activeforeground="white", relief="flat", padx=25, pady=10, cursor="hand2")
exit_btn.pack(side="left", padx=8)

startup_message = ("Hello! I am your voice assistant. Click Listen and give me a command.")
add_message("Assistant", startup_message)
threading.Thread(target=speak, args=(startup_message,), daemon=True).start()

root.mainloop()

# Done