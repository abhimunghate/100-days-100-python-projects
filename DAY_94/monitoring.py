from datetime import datetime, timezone
from stations import Reading

class WeatherMonitor:
    def __init__(self, stations):
        self.stations = {s.name: s for s in stations}

    def ingest(self, station, temperature_f, humidity_percent, wind_mph, condition):
        target = self.stations.get(station)
        if not target:
            raise LookupError("Station not found")
        if not -100 <= temperature_f <= 150 or not 0 <= humidity_percent <= 100:
            raise ValueError("Reading is outside valid range")
        reading = Reading(station, temperature_f, humidity_percent, wind_mph, condition, datetime.now(timezone.utc).isoformat(),)
        return target.record(reading)

    def dashboard(self):
        return {"stations": [station.latest().to_dict() for station in self.stations.values()]}
    
# Done