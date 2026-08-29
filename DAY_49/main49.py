# This is Day 49 project : Global Weather Dashboard

import os
import webbrowser
import requests
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import folium

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CURRENT_WEATHER_URL = ("https://api.openweathermap.org/data/2.5/weather")
FORECAST_URL = ("https://api.openweathermap.org/data/2.5/forecast")

def fetch_current_weather(city):
    """Fetch current weather information for a city."""
    if not API_KEY:
        raise ValueError("OpenWeather API key not found.\n\nSet the OPENWEATHER_API_KEY environment variable.")
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(CURRENT_WEATHER_URL, params=params, timeout=10)
    if response.status_code == 401:
        raise ValueError("Invalid OpenWeather API key.")
    if response.status_code == 404:
        raise ValueError("City not found.")
    if response.status_code != 200:
        raise ValueError(f"Weather API error: {response.status_code}")
    return response.json()

def fetch_forecast(city):
    """Fetch 5-day / 3-hour weather forecast."""
    if not API_KEY:
        raise ValueError("OpenWeather API key not found.")
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    if response.status_code == 401:
        raise ValueError("Invalid OpenWeather API key.")
    if response.status_code == 404:
        raise ValueError("City not found.")
    if response.status_code != 200:
        raise ValueError(f"Forecast API error: {response.status_code}")
    return response.json()

def format_time(timestamp):
    """Convert Unix timestamp into readable time."""
    return datetime.fromtimestamp(timestamp).strftime("%I:%M %p")

class WeatherDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Weather Dashboard")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        self.weather_data = None
        self.forecast_data = None
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="🌍 Global Weather Dashboard", font=("Arial", 26, "bold"))
        title.pack(pady=15)

        search_frame = tk.LabelFrame(self.root, text="Search City", padx=10, pady=10)
        search_frame.pack(fill="x", padx=20, pady=5)
        tk.Label(search_frame, text="City:").pack(side="left", padx=5)
        self.city_entry = tk.Entry(search_frame, width=35, font=("Arial", 12))
        self.city_entry.pack(side="left", padx=5)
        self.city_entry.insert(0, "Nagpur")
        tk.Button(search_frame, text="Get Weather", command=self.get_weather, width=15).pack(side="left", padx=5)
        tk.Button(search_frame, text="Forecast", command=self.show_forecast, width=15).pack(side="left", padx=5)
        tk.Button(search_frame, text="Show Map", command=self.show_map, width=15).pack(side="left", padx=5)
        tk.Button(search_frame, text="Clear", command=self.clear_dashboard, width=15).pack(side="left", padx=5)

        info_frame = tk.LabelFrame(self.root, text="Current Weather", padx=15, pady=15)
        info_frame.pack(fill="x", padx=20, pady=10)
        self.city_label = tk.Label(info_frame, text="City: --", font=("Arial", 18, "bold"))
        self.city_label.grid(row=0, column=0, padx=20, pady=8, sticky="w")
        self.temperature_label = tk.Label(info_frame, text="Temperature: --", font=("Arial", 16))
        self.temperature_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.feels_like_label = tk.Label(info_frame, text="Feels Like: --", font=("Arial", 13))
        self.feels_like_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        self.weather_label = tk.Label(info_frame, text="Weather: --", font=("Arial", 13))
        self.weather_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        self.humidity_label = tk.Label(info_frame, text="Humidity: --", font=("Arial", 13))
        self.humidity_label.grid(row=1, column=1, padx=20, pady=5, sticky="w")
        self.pressure_label = tk.Label(info_frame, text="Pressure: --", font=("Arial", 13))
        self.pressure_label.grid(row=2, column=1, padx=20, pady=5, sticky="w")
        self.wind_label = tk.Label(info_frame, text="Wind Speed: --", font=("Arial", 13))
        self.wind_label.grid(row=3, column=1, padx=20, pady=5, sticky="w")
        self.coordinates_label = tk.Label(info_frame, text="Coordinates: --", font=("Arial", 13))
        self.coordinates_label.grid(row=1, column=2, padx=20, pady=5, sticky="w")
        self.sunrise_label = tk.Label(info_frame, text="Sunrise: --", font=("Arial", 13))
        self.sunrise_label.grid(row=2, column=2, padx=20, pady=5, sticky="w")
        self.sunset_label = tk.Label(info_frame, text="Sunset: --", font=("Arial", 13))
        self.sunset_label.grid(row=3, column=2, padx=20, pady=5, sticky="w")

        forecast_frame = tk.LabelFrame(self.root, text="5-Day Forecast", padx=10, pady=10)
        forecast_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.forecast_text = tk.Text(forecast_frame, height=8, font=("Consolas", 11))
        self.forecast_text.pack(fill="x", padx=10, pady=5)

        self.figure = plt.Figure(figsize=(9, 3.5), dpi=100)
        self.axis = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=forecast_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=5)

        self.status_label = tk.Label(self.root, text="Enter a city to get weather information.", anchor="w")
        self.status_label.pack(fill="x", padx=20, pady=5)

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        try:
            self.status_label.config(text="Fetching weather data...")
            self.root.update_idletasks()
            data = fetch_current_weather(city)
            self.weather_data = data
            self.display_weather(data)
            self.status_label.config(text="Weather data updated successfully.")
        except Exception as error:
            messagebox.showerror("Weather Error", str(error))
            self.status_label.config(text="Failed to fetch weather data.")

    def display_weather(self, data):
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = (data["weather"][0]["description"].title())
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        latitude = data["coord"]["lat"]
        longitude = data["coord"]["lon"]
        sunrise = format_time(data["sys"]["sunrise"])
        sunset = format_time(data["sys"]["sunset"])

        self.city_label.config(text=f"City: {city}, {country}")
        self.temperature_label.config(text=f"Temperature: {temperature:.1f} °C")
        self.feels_like_label.config(text=f"Feels Like: {feels_like:.1f} °C")
        self.weather_label.config(text=f"Weather: {weather}")
        self.humidity_label.config(text=f"Humidity: {humidity}%")
        self.pressure_label.config(text=f"Pressure: {pressure} hPa")
        self.wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
        self.coordinates_label.config(text=f"Coordinates: {latitude:.4f}, {longitude:.4f}")
        self.sunrise_label.config(text=f"Sunrise: {sunrise}")
        self.sunset_label.config(text=f"Sunset: {sunset}")

    def show_forecast(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        try:
            self.forecast_data = fetch_forecast(city)
            forecast_list = (self.forecast_data["list"])
            self.forecast_text.delete("1.0", tk.END)
            self.forecast_text.insert(tk.END, "DATE & TIME          TEMP      WEATHER\n")
            self.forecast_text.insert(tk.END, "-" * 55 + "\n")

            dates = []
            temperatures = []

            for item in forecast_list:
                date_time = datetime.strptime(item["dt_txt"],"%Y-%m-%d %H:%M:%S")
                temperature = item["main"]["temp"]
                weather = (item["weather"][0]["description"].title())
                dates.append(date_time.strftime("%d %b"))
                temperatures.append(temperature)

                self.forecast_text.insert(tk.END,
                    f"{item['dt_txt']:<20}"
                    f"{temperature:>7.1f} °C   "
                    f"{weather}\n"
                )

            self.plot_forecast(dates, temperatures)
            self.status_label.config(text="5-day forecast loaded successfully.")
        except Exception as error:
            messagebox.showerror("Forecast Error", str(error))

    def plot_forecast(self, dates, temperatures):
        self.axis.clear()
        self.axis.plot(dates, temperatures, marker="o", label="Temperature")
        self.axis.set_title("5-Day Temperature Forecast")
        self.axis.set_xlabel("Date / Time")
        self.axis.set_ylabel("Temperature (°C)")
        self.axis.tick_params(axis="x", rotation=45)
        self.axis.grid(True)
        self.axis.legend()
        self.figure.tight_layout()
        self.canvas.draw()

    def show_map(self):
        if not self.weather_data:
            messagebox.showwarning("No Weather Data", "Please get weather information first.")
            return

        try:
            latitude = (self.weather_data["coord"]["lat"])
            longitude = (self.weather_data["coord"]["lon"])
            city = self.weather_data["name"]
            temperature = (self.weather_data["main"]["temp"])
            weather = (self.weather_data["weather"][0]["description"].title())
            weather_map = folium.Map(location=[latitude, longitude], zoom_start=10)
            popup_text = (
                f"<b>{city}</b><br>"
                f"Temperature: {temperature:.1f} °C<br>"
                f"Weather: {weather}"
            )

            folium.Marker([latitude, longitude], popup=popup_text, tooltip=city).add_to(weather_map)
            map_file = "weather_map.html"
            weather_map.save(map_file)
            webbrowser.open(map_file)
            self.status_label.config(text="Interactive weather map opened in browser.")
        except Exception as error:
            messagebox.showerror("Map Error", str(error))

    def clear_dashboard(self):
        self.weather_data = None
        self.forecast_data = None
        self.city_label.config(text="City: --")
        self.temperature_label.config(text="Temperature: --")
        self.feels_like_label.config(text="Feels Like: --")
        self.weather_label.config(text="Weather: --")
        self.humidity_label.config(text="Humidity: --")
        self.pressure_label.config(text="Pressure: --")
        self.wind_label.config(text="Wind Speed: --")
        self.coordinates_label.config(text="Coordinates: --")
        self.sunrise_label.config(text="Sunrise: --")
        self.sunset_label.config(text="Sunset: --")
        self.forecast_text.delete("1.0", tk.END)
        self.axis.clear()
        self.canvas.draw()
        self.status_label.config(text="Dashboard cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDashboard(root)
    root.mainloop()
    
# Done