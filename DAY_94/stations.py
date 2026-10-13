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
    
# Done