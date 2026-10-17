from dataclasses import asdict, dataclass
from datetime import date

@dataclass
class Workout:
    id: int
    activity: str
    duration_minutes: int
    calories: int
    workout_date: str
    
    def to_dict(self):
        return asdict(self)
    
class WorkoutService:
    def __init__(self):
        self.workouts = []
        
    def log(self, activity, duration_minutes, calories, workout_date=None):
        if duration_minutes <= 0 or calories < 0:
            raise ValueError("Workout values must be positive")
        workout = Workout(
            len(self.workouts) + 1,
            activity,
            duration_minutes,
            calories,
            workout_date or date.today().isoformat()
        )
        self.workouts.append(workout)
        return workout
    
# Done