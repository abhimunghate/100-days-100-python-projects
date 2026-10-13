# This is Day 94 project : Real-Time Weather Monitoring Dashboard

import json
from alerts import WeatherAlerts
from monitoring import WeatherMonitor
from stations import WeatherStation

def show(action, data, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(data,indent=2)}")

def main():
    print("Day 94 — Real-Time Weather Monitoring Dashboard")
    monitor = WeatherMonitor([WeatherStation("Austin"), WeatherStation("Houston")])
    for reading in [("Austin", 97, 42, 14, "Sunny"), ("Houston", 88, 74, 34, "Thunderstorm")]:
        item = monitor.ingest(*reading)
        show(
            "POST /api/readings",
            {"reading": item.to_dict(), "alerts": WeatherAlerts.evaluate(item)},
            201,
        )
    show("GET /api/dashboard", monitor.dashboard())

if __name__ == "__main__":
    main()
    
# Done