# This is Day 19 project : Weather App using API

import requests
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

if not API_KEY:
    print("Please add your OpenWeather API key.")
    exit()

def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City" : data['name'],
                "Temperature" : f"{data['main'] ['temp']}°C",
                "Feels Like"  : f"{data['main']['feels_like']}°C",
                "Weather"     : data['weather'] [0] ['description'].title(),
                "Humidity"    : f"{data['main'] ['humidity']}%",
                "Wind Speed"  : f"{data['wind'] ['speed']} m/s",
                "Pressure"    : f"{data['main']['pressure']} hPa",
                "Visibility"  : f"{data['visibility']/1000:.1f} km",
                "Sunrise"     : datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
                "Sunset"      : datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p")
            }
            return weather
        
        elif response.status_code == 404:
            print(f"'{city}' was not found.")
            
        elif response.status_code == 401:
            print("Invalid API key.")
            
        else:
            print("An error occurred, Status Code : ",response.status_code)
            
    except requests.exceptions.RequestException as e:
        print("Network Error:", e)

def get_forecast(city):
    try:
        url = f"{FORECAST_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            report = f"5-Day Forecast for {city.title()}\n\n"
            
            print("\n------ 5-Day Weather Forecast ------\n")
            
            for forecast in data['list']:
                if "12:00:00" in forecast["dt_txt"]:
                    date = forecast["dt_txt"].split()[0]
                    temp = forecast["main"]["temp"]
                    weather = forecast["weather"][0]["description"].title()

                    print(f"Date        : {date}")
                    print(f"Temperature : {temp}°C")
                    print(f"Weather     : {weather}")
                    print("-" * 40)

                    report += (
                        f"Date        : {date}\n"
                        f"Temperature : {temp}°C\n"
                        f"Weather     : {weather}\n"
                        + "-" * 40 + "\n"
                    )

            return report

        elif response.status_code == 404:
            print(f"'{city}' was not found.")
            
        elif response.status_code == 401:
            print("Invalid API key.")
            
        else:
            print("Error : ",response.status_code)
    
    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        
def save_weather(weather):
    file_name = "weather_history.txt"

    with open(file_name, "a") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Weather Report - {datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')}\n")
        file.write("=" * 50 + "\n")

        for key, value in weather.items():
            file.write(f"{key}: {value}\n")

    print(f"\nWeather report saved to '{file_name}'.")
    
def save_to_history(text):
    with open("weather_history.txt", "a") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Saved On : {datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')}\n")
        file.write("=" * 50 + "\n")
        file.write(text)
        file.write("\n")

def display_weather(weather):
    print("\n------ Weather Information ------\n")
    for key, value in weather.items():
        print(f"{key} : {value}")
        
def show_menu():
    print("\n------ Weather App ------\n")
    print("1. Current Weather")
    print("2. 5-Day Forecast")
    print("3. Exit")
        
while True:
    show_menu()
    choice = input("\nEnter your choice (1/2/3) : ").strip()
    
    if choice == "1":
        city = input("\nEnter a city name (or 'b' to go back) : ").strip().title()
        
        if not city:
            print("City name cannot be empty.")
            continue
        
        if city.lower() == 'b':
            continue
        weather = get_weather(city)
        if weather:
            display_weather(weather)
            
            choice = input("\nSave this report? (Y/N): ").strip().upper()

            if choice == "Y":
                save_weather(weather)
    
    elif choice == "2":
        city = input("\nEnter a city name (or 'b' to go back) : ").strip().title()
        
        if not city:
            print("City name cannot be empty.")
            continue
        
        if city.lower() == 'b':
            continue
        forecast = get_forecast(city)
        
        if forecast:
            choice = input("\nSave this report? (Y/N): ").strip().upper()

            if choice == "Y":
                save_to_history(forecast)
                print("\nForecast saved successfully.")
                
    elif choice == "3":
        print("\nExiting the Weather App. Goodbye!")
        break

    else:
        print("\nInvalid input. Please enter a value (1/2/3)")
        
# Done