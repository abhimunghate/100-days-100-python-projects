# 🚀 Day 19 - Weather App using API

Welcome to **Day 19** of my **100 Days, 100 Python Projects** challenge!

This project is a command-line **Weather App** built with Python that uses the **OpenWeather API** to fetch real-time weather information and a **5-day weather forecast** for any city around the world. Users can also save weather reports locally for future reference.

---

## 📌 Project Overview

The application connects to the **OpenWeather API** to retrieve live weather data based on a city name.

Users can:

- 🌤️ View the current weather
- 📅 View a 5-day weather forecast
- 💾 Save weather reports locally
- 🌍 Search weather information for any city
- 🚪 Exit the application using a simple menu

---

## ✨ Features

- 🌡️ Current weather information
- 📅 5-day weather forecast
- 🌍 Search weather by city name
- 🌅 Sunrise and sunset timings
- 💨 Wind speed
- 💧 Humidity
- 🌡️ Feels-like temperature
- 🌫️ Visibility
- 📈 Atmospheric pressure
- 💾 Save weather reports to a text file
- ⚠️ Error handling for:
  - Invalid city names
  - Invalid API keys
  - Network errors
- 🖥️ Menu-driven interface

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- OpenWeather API
- Datetime Module
- File Handling

---

## 📂 Project Structure

```text
DAY_19/
│── main19.py
│── weather_history.txt
└── README.md
```

---

## 📦 Requirements

Install the required library:

```bash
pip install requests
```

---

## 🔑 API Setup

This project uses the **OpenWeather API**.

1. Create a free account on OpenWeather.
2. Generate your API key.
3. Replace:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

with

```python
API_KEY = "YOUR_ACTUAL_API_KEY"
```

---

## ▶️ How to Run

1. Install Python 3.
2. Install the `requests` library.
3. Add your OpenWeather API key.
4. Open the terminal inside the project folder.
5. Run:

```bash
python main19.py
```

---

## 💻 Sample Output

### Current Weather

```text
------ Weather App ------

1. Current Weather
2. 5-Day Forecast
3. Exit

Enter your choice : 1

Enter a city name : Nagpur

------ Weather Information ------

City         : Nagpur
Temperature  : 31°C
Feels Like   : 34°C
Weather      : Broken Clouds
Humidity     : 68%
Wind Speed   : 3.5 m/s
Pressure     : 1006 hPa
Visibility   : 10.0 km
Sunrise      : 06:00 AM
Sunset       : 06:56 PM
```

---

### 5-Day Forecast

```text
------ 5-Day Weather Forecast ------

Date        : 2026-07-31
Temperature : 30°C
Weather     : Light Rain
----------------------------------------

Date        : 2026-08-01
Temperature : 29°C
Weather     : Moderate Rain
----------------------------------------
```

---

## 📄 Weather History

If the user chooses to save the report, it is stored in:

```text
weather_history.txt
```

Each saved report includes:

- Timestamp
- Weather details
- Forecast information (if selected)

---

## 📚 Concepts Practiced

- REST APIs
- HTTP GET Requests
- JSON Parsing
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- File Handling
- Date & Time Formatting
- User Input Validation
- Working with Third-Party Libraries

---

## 🎯 Learning Outcome

This project helped me practice:

- Consuming REST APIs
- Working with live JSON data
- Parsing nested dictionaries
- Handling API responses
- Managing HTTP status codes
- Handling network exceptions
- Formatting weather data for users
- Saving reports to text files
- Building a real-world API-based application

---

## ⚠️ Note

- An active internet connection is required.
- A valid OpenWeather API key is required.
- Weather reports are fetched in **metric units (°C)**.
- Saved reports are stored in `weather_history.txt`.
- Invalid city names and API errors are handled gracefully.

---

## 🔮 Future Improvements

Possible enhancements for future versions:

- 🌍 Search weather by GPS coordinates
- 📍 Automatically detect current location
- ⏰ Hourly weather forecast
- 🌧️ Rain probability
- 🌦️ Weather icons in terminal
- ⭐ Favorite cities
- 📊 Weather charts using Matplotlib
- 📤 Export reports to PDF
- 🌐 GUI using Tkinter or CustomTkinter
- 🌐 Web version using Flask or Django

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen problem-solving abilities, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀