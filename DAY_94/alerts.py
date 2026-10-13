class WeatherAlerts:
    @staticmethod
    def evaluate(reading):
        alerts = []
        if reading.temperature_f >= 95:
            alerts.append("Heat advisory")
        if reading.wind_mph >= 30:
            alerts.append("High wind advisory")
        if reading.condition.lower() in {"storm", "thunderstorm"}:
            alerts.append("Severe weather watch")
        return alerts or ["No active alerts"]
    
# Done