# This is Day 98 project : Fitness Tracker App

import json
from goals import GoalService
from reports import FitnessReport
from workouts import WorkoutService

def show(action, data, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(data, indent=2)}")
    
def main():
    print("Day 98 - Fitness Tracker App")
    workouts = WorkoutService()
    goals = GoalService()
    for item in [
        ("Running", 35, 360),
        ("Strength Training", 45, 280),
        ("Cycling", 50, 420)
    ]:
        show("POST /api/workouts", workouts.log(*item).to_dict(), 201)
    show("GET /api/dashboard", FitnessReport.build(workouts.workouts, goals))
    
if __name__ == "__main__":
    main()
    
# Done