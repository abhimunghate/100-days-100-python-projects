class FitnessReport:
    @staticmethod
    def build(workouts, goals):
        return {
            "total_workouts": len(workouts),
            "total_minutes": sum(w.duration_minutes for w in workouts),
            "total_calories": sum(w.calories for w in workouts),
            "activities": sorted({w.activity for w in workouts}),
            "goal_progress": goals.progress(workouts)
        }
        
# Done