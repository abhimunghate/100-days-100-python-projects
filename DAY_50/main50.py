# This is Day 50 project : Weather Dashboard App

import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
ICON_URL = "https://openweathermap.org/img/wn/{}@2x.png"

def fetch_weather(city):
    """Fetch weather information for a city."""
    if not API_KEY:
        raise ValueError("OpenWeather API key is not configured.")

    if not city or not city.strip():
        raise ValueError("Please enter a city name.")
    
    params = {
        "q" : city,
        "appid" : API_KEY,
        "units" : "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.Timeout:
        raise ConnectionError("Weather service took too long to respond.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Unable to connect to the weather service.")
    except requests.exceptions.RequestException as error:
        raise ConnectionError(f"Request failed: {error}")
    
    if response.status_code == 200:
        return response.json()
    if response.status_code == 400:
        raise ValueError("Invalid weather request.")
    if response.status_code == 401:
        raise ValueError("Invalid OpenWeather API key.")
    if response.status_code == 404:
        raise ValueError(f"City '{city.strip()}' was not found.")
    if response.status_code == 429:
        raise ValueError("Weather API request limit exceeded. Please try again later.")
    raise ValueError(f"Weather service returned error : {response.status_code}.")
    
def parse_weather(data):
    """Convert API response into simpler weather data."""
    weather_info = data["weather"][0]
    icon_code = weather_info["icon"]
    return {
        "city": data["name"],
        "country": data["sys"].get("country", ""),
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": weather_info["description"].title(),
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "visibility": data.get("visibility", 0) / 1000,
        "icon": ICON_URL.format(icon_code),
        "icon_code": icon_code
    }
    
@app.route('/', methods=["GET", "POST"])
def home():
    weather = None
    error = None
    searched_city = ""
    
    if request.method == "POST":
        searched_city = request.form.get("city", "").strip()
        
        try:
            data = fetch_weather(searched_city)
            weather = parse_weather(data)
        except (ValueError, ConnectionError) as exception:
            error = str(exception)
        except KeyError:
            error = ("The weather service returned unexpected data.")
        except Exception as exception:
            error = (f"An unexpected error occurred : {exception}")
    return render_template("index.html", weather=weather, error=error, searched_city=searched_city)

@app.errorhandler(404)
def page_not_found(error):
    return (render_template("index.html", weather=None, error="Page not found.", searched_city=""), 404)

@app.errorhandler(500)
def internal_server_error(error):
    return (render_template("index.html", weather=None, error="Internal server error. Please try again.", searched_city=""), 500)

if __name__ == "__main__":
    app.run(debug=True)
    
# Done