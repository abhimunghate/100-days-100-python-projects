# 🌦️ Day 94 - Real-Time Weather Monitoring Dashboard

Welcome to **Day 94** of my **100 Days, 100 Python Projects** challenge!

This project is a **Real-Time Weather Monitoring Dashboard** built using Python. It demonstrates how weather readings from multiple monitoring stations can be collected, stored, evaluated for weather alerts, and displayed in a consolidated dashboard.

The application uses Python dataclasses, object-oriented programming, dictionaries, lists, datetime handling, validation, and JSON serialization to implement a simple weather monitoring system. It simulates API-style requests and responses through formatted JSON output in the terminal.

The dashboard monitors two weather stations: **Austin** and **Houston**. It processes temperature, humidity, wind speed, and weather conditions, generates alerts based on predefined rules, and displays the latest reading from each station.

**Note:** Although the project is named a real-time weather monitoring dashboard, the current implementation processes sample readings provided directly by the Python program. It does not connect to a live weather API, physical weather sensors, or a graphical dashboard.

---

## 📌 Project Overview

A weather monitoring system collects environmental readings from different locations and helps users understand current conditions. It can also identify potentially dangerous weather situations and provide alerts based on predefined thresholds.

This project implements the backend logic of a weather monitoring dashboard without requiring a web server, external weather service, or graphical user interface.

The application follows a simple workflow:

- 🌍 Initialize multiple weather stations.
- 🌡️ Receive temperature readings in Fahrenheit.
- 💧 Record humidity percentages.
- 💨 Record wind speed in miles per hour.
- 🌤️ Store the reported weather condition.
- 🕒 Generate a UTC timestamp for each reading.
- ✅ Validate station names and selected measurement ranges.
- 🚨 Evaluate weather readings against alert rules.
- 📋 Store readings in their respective stations.
- 📊 Display the latest reading from every station.
- 🧾 Format operations and results as JSON in the terminal.

The sample data includes sunny weather in Austin and a thunderstorm in Houston.

---

## ✨ Features

- 🌦️ Weather monitoring backend simulation
- 🌍 Multiple weather stations
- 🌡️ Temperature monitoring
- 💧 Humidity monitoring
- 💨 Wind speed monitoring
- 🌤️ Weather condition tracking
- 🕒 UTC timestamps for observations
- 📥 Weather reading ingestion
- 📚 Per-station reading history
- 📊 Latest-reading dashboard
- 🚨 Automatic heat advisories
- 💨 High wind advisories
- ⛈️ Severe weather watch alerts
- ✅ Temperature and humidity range validation
- 🔍 Weather station lookup by name
- ⚠️ Exception handling for invalid operations
- 🧾 JSON-formatted terminal output
- 🔄 API-style request and response labels
- 🧩 Modular Python architecture
- 🐍 Python standard-library implementation

---

## 🌡️ Weather Reading Dataclass

The `Reading` dataclass in `stations.py` defines the structure of each weather observation.

```python
from dataclasses import asdict, dataclass

@dataclass
class Reading:
    station: str
    temperature_f: float
    humidity_percent: int
    wind_mph: float
    condition: str
    observed_at: str

    def to_dict(self):
        return asdict(self)
```

### Attributes

| Attribute | Description |
|---|---|
| `station` | Name of the weather monitoring station |
| `temperature_f` | Recorded temperature in degrees Fahrenheit |
| `humidity_percent` | Recorded relative humidity percentage |
| `wind_mph` | Recorded wind speed in miles per hour |
| `condition` | Reported weather condition |
| `observed_at` | Timestamp representing when the reading was ingested |

### Example Reading

A reading for Austin may contain the following information:

```json
{
  "station": "Austin",
  "temperature_f": 97,
  "humidity_percent": 42,
  "wind_mph": 14,
  "condition": "Sunny",
  "observed_at": "2026-10-13T00:00:00+00:00"
}
```

The timestamp above is illustrative; the application generates the actual timestamp when the reading is processed.

### The `to_dict()` Method

```python
def to_dict(self):
    return asdict(self)
```

The `asdict()` function converts a dataclass instance into a dictionary containing its fields and values.

This makes the reading suitable for JSON serialization and structured API-style responses.

---

## 📍 WeatherStation Class

The `WeatherStation` class manages the readings collected for an individual station.

```python
class WeatherStation:
    def __init__(self, name):
        self.name, self.readings = name, []

    def record(self, reading):
        self.readings.append(reading)
        return reading

    def latest(self):
        if not self.readings:
            raise LookupError("No readings available")
        return self.readings[-1]
```

### Responsibilities

- Store the station name.
- Maintain a list of weather readings.
- Add new readings to the station's history.
- Return the most recent reading.
- Raise an exception when no reading is available.

### The `record()` Method

The `record()` method appends a new reading to the station's `readings` list and returns that reading.

```python
self.readings.append(reading)
return reading
```

The application can therefore retain multiple readings for the same station during a single run.

### The `latest()` Method

```python
return self.readings[-1]
```

The method returns the last item in the list, which represents the most recently recorded reading.

If the station has no readings, it raises:

```python
LookupError("No readings available")
```

The dashboard uses this method to retrieve the current stored reading for every configured station.

---

## 🛰️ WeatherMonitor Class

The `WeatherMonitor` class in `monitoring.py` coordinates the weather stations, validates incoming readings, and prepares dashboard data.

```python
from datetime import datetime, timezone
from stations import Reading

class WeatherMonitor:
    def __init__(self, stations):
        self.stations = {s.name: s for s in stations}
```

The constructor receives a list of `WeatherStation` objects and stores them in a dictionary keyed by station name.

For example, the two configured stations are accessible using:

```python
self.stations["Austin"]
self.stations["Houston"]
```

This dictionary makes it convenient to locate a station by its name.

### Responsibilities

- Manage multiple weather stations.
- Locate the target station.
- Validate selected measurement ranges.
- Generate UTC observation timestamps.
- Create and record weather readings.
- Generate a dashboard containing the latest reading from each station.

---

## 📥 Weather Reading Ingestion

The `ingest()` method processes a new weather observation.

```python
def ingest(
    self,
    station,
    temperature_f,
    humidity_percent,
    wind_mph,
    condition
):
    target = self.stations.get(station)

    if not target:
        raise LookupError("Station not found")

    if (
        not -100 <= temperature_f <= 150
        or not 0 <= humidity_percent <= 100
    ):
        raise ValueError("Reading is outside valid range")

    reading = Reading(
        station,
        temperature_f,
        humidity_percent,
        wind_mph,
        condition,
        datetime.now(timezone.utc).isoformat(),
    )

    return target.record(reading)
```

### How It Works

1. Look up the station by its name.
2. Raise a `LookupError` if the station does not exist.
3. Validate the temperature and humidity ranges.
4. Generate a timestamp in UTC.
5. Create a `Reading` object.
6. Record the reading at the target station.
7. Return the recorded reading.

### Validation Rules

| Measurement | Accepted Range |
|---|---|
| Temperature | -100°F to 150°F |
| Humidity | 0% to 100% |

Both boundaries are inclusive.

If a temperature or humidity value falls outside its accepted range, the method raises:

```python
ValueError("Reading is outside valid range")
```

**Important:** Wind speed, condition text, and the data types of the incoming values are not explicitly validated. The temperature and humidity checks are basic application-level checks, not a comprehensive weather-data validation system.

### UTC Timestamp Generation

The application uses:

```python
datetime.now(timezone.utc).isoformat()
```

This creates an ISO 8601 timestamp using the UTC timezone.

For example:

```text
2026-10-13T18:15:00+00:00
```

The example is illustrative. The actual timestamp depends on when the program runs.

Using UTC makes timestamps consistent across stations in different geographic locations.

---

## 🚨 WeatherAlerts Class

The `WeatherAlerts` class in `alerts.py` evaluates each weather reading against predefined alert rules.

```python
class WeatherAlerts:
    @staticmethod
    def evaluate(reading):
        alerts = []

        if reading.temperature_f >= 95:
            alerts.append("Heat advisory")

        if reading.wind_mph >= 30:
            alerts.append("High wind advisory")

        if reading.condition.lower() in {
            "storm",
            "thunderstorm"
        }:
            alerts.append("Severe weather watch")

        return alerts or ["No active alerts"]
```

The class uses a static method because the evaluation does not require an instance of `WeatherAlerts`.

### Alert Rules

| Condition | Threshold or Rule | Generated Alert |
|---|---|---|
| High temperature | Temperature ≥ 95°F | `Heat advisory` |
| High wind speed | Wind speed ≥ 30 mph | `High wind advisory` |
| Storm condition | Condition is `storm` or `thunderstorm`, ignoring capitalization | `Severe weather watch` |
| No matching rules | No alert conditions are met | `No active alerts` |

### 1. Heat Advisory

The application generates a heat advisory when:

```python
reading.temperature_f >= 95
```

For example, Austin has a temperature of 97°F, so it triggers a heat advisory.

### 2. High Wind Advisory

The application generates a high wind advisory when:

```python
reading.wind_mph >= 30
```

Houston has a wind speed of 34 mph, so it triggers a high wind advisory.

### 3. Severe Weather Watch

The application checks whether the lowercased weather condition is either `storm` or `thunderstorm`.

```python
reading.condition.lower() in {
    "storm",
    "thunderstorm"
}
```

Houston's condition is `Thunderstorm`, so it triggers a severe weather watch.

The condition check is case-insensitive for these two exact words. Other descriptions, such as `Heavy Thunderstorms`, do not match the current rule.

### 4. No Active Alerts

If none of the conditions match, the method returns:

```python
["No active alerts"]
```

This ensures that the response always contains a list of alert messages.

**Note:** These are simplified demonstration rules. They are not official meteorological warning criteria and should not be used for real-world emergency decisions.

---

## 📊 Dashboard Generation

The `dashboard()` method returns the latest reading for every configured weather station.

```python
def dashboard(self):
    return {
        "stations": [
            station.latest().to_dict()
            for station in self.stations.values()
        ]
    }
```

### How It Works

1. Iterate over all configured weather stations.
2. Retrieve each station's latest reading.
3. Convert the reading into a dictionary.
4. Collect the dictionaries into a list.
5. Return the list under the `stations` key.

### Example Dashboard Structure

```json
{
  "stations": [
    {
      "station": "Austin",
      "temperature_f": 97,
      "humidity_percent": 42,
      "wind_mph": 14,
      "condition": "Sunny",
      "observed_at": "..."
    },
    {
      "station": "Houston",
      "temperature_f": 88,
      "humidity_percent": 74,
      "wind_mph": 34,
      "condition": "Thunderstorm",
      "observed_at": "..."
    }
  ]
}
```

The timestamps are represented by `...` because the application generates actual timestamps at runtime.

The dashboard reports the latest readings, not the complete history of each station. The stored historical readings remain available in each station's `readings` list while the program is running.

**Limitation:** If a configured station has no recorded readings, calling `latest()` for that station raises a `LookupError`, preventing the dashboard method from returning its complete result.

---

## 🖥️ Sample Weather Data

The application initializes two stations and processes two sample readings.

```python
monitor = WeatherMonitor([
    WeatherStation("Austin"),
    WeatherStation("Houston")
])
```

The sample readings are:

```python
[
    ("Austin", 97, 42, 14, "Sunny"),
    ("Houston", 88, 74, 34, "Thunderstorm")
]
```

### Austin Weather Reading

| Measurement | Value |
|---|---|
| Station | Austin |
| Temperature | 97°F |
| Humidity | 42% |
| Wind speed | 14 mph |
| Condition | Sunny |
| Expected alert | Heat advisory |

Austin triggers the heat advisory because its temperature is at least 95°F.

### Houston Weather Reading

| Measurement | Value |
|---|---|
| Station | Houston |
| Temperature | 88°F |
| Humidity | 74% |
| Wind speed | 34 mph |
| Condition | Thunderstorm |
| Expected alerts | High wind advisory, Severe weather watch |

Houston triggers two alerts: its wind speed reaches the 30 mph threshold, and its weather condition matches the thunderstorm rule.

---

## 🧾 API-Style Request and Response Format

The `show()` helper function in `main94.py` prints operation labels, response status codes, and JSON-formatted results.

```python
def show(action, data, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(data, indent=2)}"
    )
```

### Operations Demonstrated

| Operation | Status Label | Purpose |
|---|---:|---|
| `POST /api/readings` | `201` | Displays the recorded Austin reading and its alerts |
| `POST /api/readings` | `201` | Displays the recorded Houston reading and its alerts |
| `GET /api/dashboard` | `200` | Displays the latest reading from each station |

The status codes are simulated labels printed in the terminal. The application does not implement a real HTTP API or transmit requests over a network.

### Example Reading Response

The response for Austin will contain data similar to:

```json
{
  "reading": {
    "station": "Austin",
    "temperature_f": 97,
    "humidity_percent": 42,
    "wind_mph": 14,
    "condition": "Sunny",
    "observed_at": "..."
  },
  "alerts": [
    "Heat advisory"
  ]
}
```

The timestamp will be generated at runtime.

### Example Houston Alerts

```json
{
  "alerts": [
    "High wind advisory",
    "Severe weather watch"
  ]
}
```

This demonstrates how one weather reading can trigger multiple alerts when several conditions are met.

---

## 🔄 Complete Application Workflow

The application follows this workflow:

```text
Start Application
        |
        v
Initialize Austin and Houston Stations
        |
        v
Create WeatherMonitor
        |
        v
Receive Sample Weather Reading
        |
        v
Validate Station Name
        |
        v
Validate Temperature and Humidity
        |
        v
Generate UTC Timestamp
        |
        v
Create Reading Object
        |
        v
Store Reading in Station History
        |
        v
Evaluate Weather Alert Rules
        |
        v
Display Reading and Alerts
        |
        v
Process Next Weather Reading
        |
        v
Retrieve Latest Reading per Station
        |
        v
Display Dashboard JSON
```

This workflow separates data ingestion, storage, alert evaluation, and dashboard generation into different components.

---

## 🏗️ Project Architecture

The project contains four main Python modules.

```text
                    main94.py
                        |
             +----------+----------+
             |          |          |
             v          v          v
       monitoring.py  alerts.py  stations.py
             |          |          |
             v          v          v
       WeatherMonitor WeatherAlerts Reading
             |                     |
             v                     v
       WeatherStation <------ WeatherStation
             |
             v
       Stored Readings
             |
             v
      Dashboard Snapshot
             |
             v
         JSON Output
```

### Module Responsibilities

- **`main94.py`** — initializes the monitoring stations, processes sample readings, displays alerts, and prints dashboard information.
- **`stations.py`** — defines the `Reading` dataclass and `WeatherStation` class.
- **`monitoring.py`** — implements station management, input validation, timestamp generation, reading ingestion, and dashboard generation.
- **`alerts.py`** — evaluates weather readings against the predefined alert rules.

This modular design separates the weather data model, monitoring operations, and alert logic, making the application easier to extend.

---

## 📊 Expected Alert Summary

The alert results for the supplied sample data are:

| Station | Temperature | Wind Speed | Condition | Expected Alerts |
|---|---:|---:|---|---|
| Austin | 97°F | 14 mph | Sunny | Heat advisory |
| Houston | 88°F | 34 mph | Thunderstorm | High wind advisory; Severe weather watch |

The application evaluates the rules independently. A reading can therefore trigger more than one alert.

For Austin, only the temperature rule matches. For Houston, both the wind speed and weather condition rules match.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement station management, weather reading ingestion, alert evaluation, and dashboard generation.

### 🧩 Dataclasses

The `dataclasses` module defines the structured weather reading model.

```python
from dataclasses import asdict, dataclass
```

### 📋 Lists

Lists store the readings recorded at each station and the alert messages generated for a reading.

### 🗂️ Dictionaries

Dictionaries manage the weather stations by name and structure the dashboard response.

### 🕒 Datetime and Timezones

The `datetime` module generates timestamps, while `timezone.utc` ensures that observation timestamps use UTC.

### 🧾 JSON

The `json` module converts Python data structures into readable JSON output in the terminal.

### 🏗️ Object-Oriented Programming

The project separates responsibilities across `WeatherMonitor`, `WeatherStation`, `Reading`, and `WeatherAlerts`.

### ⚠️ Exceptions

The application uses:

- `LookupError` when a station is not found or a station has no readings.
- `ValueError` when temperature or humidity falls outside the accepted range.

---

## 📦 Requirements

This project uses Python's standard library and does not require any external Python packages.

Check your Python version:

```bash
python --version
```

### `requirements.txt`

```text
# No external dependencies required.
```

No API key, database, weather service subscription, or third-party package installation is required.

---

## 📂 Project Structure

```text
DAY_94/
│
├── main94.py
├── alerts.py
├── monitoring.py
├── stations.py
├── requirements.txt
└── README.md
```

The `screenshots/` folder is optional and can be created to document the project.

### File Description

| File / Folder | Purpose |
|---|---|
| `main94.py` | Entry point and sample monitoring workflow |
| `alerts.py` | Weather alert evaluation rules |
| `monitoring.py` | Reading ingestion, validation, and dashboard generation |
| `stations.py` | Reading dataclass and station history management |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Ensure that Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal in the `DAY_94` folder.

```bash
cd DAY_94
```

### Step 3 — Check the Files

Make sure the following Python files are present:

```text
main94.py
alerts.py
monitoring.py
stations.py
```

### Step 4 — Run the Application

Execute:

```bash
python main94.py
```

### Step 5 — Review the Terminal Output

The terminal displays:

- The application title.
- The recorded Austin weather reading.
- Austin's generated heat advisory.
- The recorded Houston weather reading.
- Houston's generated high wind advisory and severe weather watch.
- The latest reading from both stations.

### Step 6 — Review the Results

Confirm that the dashboard contains both stations and that the alert messages match the configured rules.

No database setup, API key, external dependency installation, or server configuration is required.

---

## ⚠️ Important Notes and Limitations

### 1. No Live Weather Data

The application processes hardcoded sample readings. It does not fetch current weather information from an external API or physical sensors.

### 2. No Graphical Dashboard

The dashboard is returned as structured data and displayed in the terminal. It does not contain charts, gauges, maps, or visual weather cards.

### 3. No Actual HTTP API

The request labels are simulated. The project does not run a web server or expose actual HTTP endpoints.

### 4. Limited Validation

Temperature and humidity are checked against specified ranges. Wind speed, weather condition text, and input data types are not comprehensively validated.

### 5. Simple Alert Rules

The alert thresholds are predefined demonstration rules. They do not account for official weather warning criteria, location-specific conditions, or advanced meteorological calculations.

### 6. In-Memory Storage

Weather readings are stored in Python lists. The data is lost when the program exits.

### 7. Dashboard Shows Only Latest Readings

The dashboard returns the most recent reading for each station rather than its complete reading history.

### 8. Empty Stations Can Cause Errors

If a station has no recorded readings, `latest()` raises a `LookupError`. The dashboard does not currently handle this condition.

### 9. No Automated Background Monitoring

The application does not continuously collect readings on a schedule. It processes the two sample readings supplied by `main94.py`.

### 10. No Notifications

Alerts are returned as text in the program output. The application does not send SMS messages, emails, push notifications, or external alerts.

### 11. No Historical Analytics

Although each station stores readings during execution, the project does not currently calculate averages, trends, maximum values, or historical summaries.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Python dataclasses
- Object-oriented programming
- Lists and dictionaries
- Dictionary comprehensions
- List comprehensions
- Static methods
- Weather data modeling
- Multiple station management
- Input validation
- Exception handling
- Datetime handling
- UTC timezone awareness
- ISO 8601 timestamps
- Rule-based alert evaluation
- Conditional logic
- JSON serialization
- API-style response formatting
- Modular programming
- In-memory data storage
- Dashboard data aggregation

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Define structured weather readings using a dataclass.
- Create and manage multiple weather stations.
- Store multiple readings for each station.
- Retrieve the latest recorded observation.
- Validate station names and selected measurement ranges.
- Generate UTC timestamps for weather readings.
- Apply predefined rules to evaluate weather conditions.
- Generate multiple alerts from a single reading.
- Aggregate the latest readings into a dashboard response.
- Convert Python objects into dictionaries.
- Format monitoring results as JSON.
- Handle invalid stations and invalid measurement ranges.
- Separate monitoring, station management, and alert logic into modules.
- Build a foundation for a future live weather monitoring system.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🌐 Integrate a live weather API.
- 📡 Collect readings from physical weather sensors.
- 🔄 Add continuous monitoring at scheduled intervals.
- 🎨 Build a graphical dashboard using Streamlit, Flask, or React.
- 📈 Display temperature and humidity charts.
- 💨 Add wind speed visualizations.
- 🗺️ Show weather stations on an interactive map.
- 🗄️ Store readings in SQLite, PostgreSQL, or MongoDB.
- 📊 Calculate daily and weekly weather statistics.
- 📉 Track historical weather trends.
- 🚨 Configure customizable alert thresholds.
- 📧 Send email notifications for critical alerts.
- 📱 Add push notifications.
- 🌡️ Support Celsius and Fahrenheit conversions.
- 🧪 Add automated tests for validation and alert rules.
- 🔐 Add authentication and station access controls.
- 🧰 Improve input validation and error handling.
- ☁️ Deploy the dashboard to a cloud platform.
- 🚀 Build a production-ready weather monitoring service.

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 94** focuses on **Weather Monitoring System Development**, combining weather data modeling, station management, input validation, rule-based alerts, UTC timestamps, and dashboard data aggregation using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🌦️