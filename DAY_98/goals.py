class GoalService:
    def __init__(self, weekly_minutes=150, weekly_workouts=4):
        self.weekly_minutes, self.weekly_workouts = weekly_minutes, weekly_workouts
        
    def progress(self, workouts):
        minutes = sum(w.duration_minutes for w in workouts)
        count = len(workouts)
        return {
            "minutes": {
                "current": minutes,
                "goal": self.weekly_minutes,
                "percent": min(round(minutes / self.weekly_minutes * 100, 1), 100)
            },
            "workouts": {
                "current": count,
                "goal": self.weekly_workouts,
                "percent": min(round(count / self.weekly_workouts * 100, 1), 100)
            }
        }
        
# Done