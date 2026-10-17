# 🏃 Day 98 - Fitness Tracker App

Welcome to **Day 98** of my **100 Days, 100 Python Projects** challenge!

This project is a **Fitness Tracker App** built using Python. It demonstrates how workout activities can be recorded, fitness statistics can be calculated, and weekly fitness goals can be monitored through a structured reporting system.

The application uses Python dataclasses, object-oriented programming, lists, dictionaries, date handling, and JSON serialization to implement a simple fitness-tracking backend. It simulates API-style requests and responses through formatted JSON output in the terminal.

The application records three sample workouts: Running, Strength Training, and Cycling. It calculates the total workout count, exercise duration, calories burned, activity types, and progress toward weekly fitness goals.

---

## 📌 Project Overview

A fitness tracker helps users monitor physical activities, measure workout duration, track calories burned, and evaluate progress toward fitness targets.

This project demonstrates the backend logic of a fitness tracker without requiring a web server or graphical user interface.

The application follows a simple workflow:

- 🏃 Record workout activities.
- ⏱️ Store workout duration in minutes.
- 🔥 Record calories burned.
- 📅 Assign a date to each workout.
- 🆔 Generate a unique sequential workout ID.
- 📊 Calculate total workouts, minutes, and calories.
- 🧩 Identify the different activities performed.
- 🎯 Compare workout statistics against weekly goals.
- 📈 Calculate goal completion percentages.
- 🧾 Display fitness statistics as formatted JSON.

**Note:** This is a terminal-based backend simulation. It does not currently provide a live website, interactive GUI, database, user accounts, or real HTTP endpoints.

---

## ✨ Features

- 🏃 Workout logging system
- ⏱️ Workout duration tracking
- 🔥 Calorie tracking
- 📅 Automatic workout date assignment
- 🆔 Automatic workout ID generation
- 📋 Structured workout records using dataclasses
- 📊 Fitness dashboard report
- 🎯 Weekly exercise-minute goal tracking
- 💪 Weekly workout-count goal tracking
- 📈 Goal completion percentage calculation
- 🧩 Unique activity identification
- ⚠️ Validation of workout duration and calories
- 🧾 JSON-formatted terminal output
- 🔄 API-style request and response labels
- 🏗️ Modular project structure
- 🐍 Python standard-library implementation

---

## 🏃 Workout Management

The `workouts.py` module defines the `Workout` dataclass and the `WorkoutService` class.

The `WorkoutService` is responsible for recording workout activities and maintaining the list of workouts during program execution.

### 🧩 Workout Dataclass

The `Workout` dataclass defines the structure of a workout record.

```python
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
```

### Attributes

| Attribute | Description |
|---|---|
| `id` | Unique sequential workout identifier |
| `activity` | Name of the physical activity |
| `duration_minutes` | Duration of the workout in minutes |
| `calories` | Number of calories recorded as burned |
| `workout_date` | Date on which the workout was logged |

The `to_dict()` method uses `asdict()` to convert a workout object into a dictionary. This makes the workout data suitable for JSON serialization.

### Example Workout Record

```python
Workout(
    id=1,
    activity="Running",
    duration_minutes=35,
    calories=360,
    workout_date="2026-10-17"
)
```

The date above is an illustrative example. The actual application uses the date returned by `date.today()` when a workout is logged without a specified date.

---

## 📋 WorkoutService Class

The `WorkoutService` class manages workout records.

```python
class WorkoutService:
    def __init__(self):
        self.workouts = []

    def log(
        self,
        activity,
        duration_minutes,
        calories,
        workout_date=None
    ):
        if duration_minutes <= 0 or calories < 0:
            raise ValueError(
                "Workout values must be positive"
            )

        workout = Workout(
            len(self.workouts) + 1,
            activity,
            duration_minutes,
            calories,
            workout_date or date.today().isoformat()
        )

        self.workouts.append(workout)
        return workout
```

### Responsibilities

- Maintain a list of workout records.
- Generate sequential workout IDs.
- Validate workout duration and calorie values.
- Assign the current date when no date is supplied.
- Store the workout in memory.
- Return the newly created workout object.

### Workout ID Generation

The application generates workout IDs using:

```python
len(self.workouts) + 1
```

For example:

- First workout: `1`
- Second workout: `2`
- Third workout: `3`

These IDs are sequential within the current application run. They are not stored permanently.

### Workout Validation

The application checks:

```python
if duration_minutes <= 0 or calories < 0:
    raise ValueError(
        "Workout values must be positive"
    )
```

This means:

- A workout duration must be greater than zero.
- Calories cannot be negative.
- A duration of `0` or a negative duration raises a `ValueError`.
- Negative calories raise a `ValueError`.
- A calorie value of `0` is allowed, despite the error message saying the values must be positive.

The current implementation does not validate the activity name, the type of each input, or a manually supplied workout date.

---

## 📝 Sample Workout Data

The main program records three sample workouts.

| Workout ID | Activity | Duration | Calories |
|---:|---|---:|---:|
| 1 | Running | 35 minutes | 360 |
| 2 | Strength Training | 45 minutes | 280 |
| 3 | Cycling | 50 minutes | 420 |
| **Total** | **3 workouts** | **130 minutes** | **1,060 calories** |

These are predefined sample values used to demonstrate the application's functionality. The calorie values are recorded inputs, not measurements calculated from a person's body data or activity intensity.

### How Workouts Are Logged

The main program uses the following list:

```python
for item in [
    ("Running", 35, 360),
    ("Strength Training", 45, 280),
    ("Cycling", 50, 420)
]:
    show(
        "POST /api/workouts",
        workouts.log(*item).to_dict(),
        201
    )
```

Each tuple contains:

1. Activity name
2. Duration in minutes
3. Calories burned

The `*item` syntax unpacks each tuple into the arguments expected by the `log()` method.

The resulting workout object is converted into a dictionary using `to_dict()` and displayed as formatted JSON.

---

## 🎯 Fitness Goal Management

The `goals.py` module contains the `GoalService` class, which tracks progress toward weekly fitness targets.

### GoalService Class

```python
class GoalService:
    def __init__(
        self,
        weekly_minutes=150,
        weekly_workouts=4
    ):
        self.weekly_minutes = weekly_minutes
        self.weekly_workouts = weekly_workouts
```

The application initializes two default goals:

| Goal | Target |
|---|---:|
| Weekly workout duration | 150 minutes |
| Weekly workout count | 4 workouts |

These targets can be customized by passing different values when creating a `GoalService` object.

For example:

```python
goals = GoalService(
    weekly_minutes=200,
    weekly_workouts=5
)
```

This creates a goal of 200 workout minutes and five workouts.

### Progress Calculation

The `progress()` method calculates the current progress using the recorded workouts.

```python
def progress(self, workouts):
    minutes = sum(
        w.duration_minutes for w in workouts
    )
    count = len(workouts)

    return {
        "minutes": {
            "current": minutes,
            "goal": self.weekly_minutes,
            "percent": min(
                round(
                    minutes / self.weekly_minutes * 100,
                    1
                ),
                100
            )
        },
        "workouts": {
            "current": count,
            "goal": self.weekly_workouts,
            "percent": min(
                round(
                    count / self.weekly_workouts * 100,
                    1
                ),
                100
            )
        }
    }
```

The method calculates:

- Total workout minutes.
- Number of recorded workouts.
- Percentage of the weekly minute goal completed.
- Percentage of the weekly workout-count goal completed.

The `min()` function caps the displayed percentage at 100%, so the progress value will not exceed 100% even if the user surpasses a target.

**Important:** The current implementation sums all workouts in memory, regardless of their date. It does not filter records to the current week. Therefore, the goal progress represents all recorded workouts in the current session, not necessarily the actual current week's progress.

The percentage calculation also assumes both goal values are greater than zero. Setting either goal to zero would cause a division-by-zero error.

---

## 📊 Fitness Report and Dashboard

The `reports.py` module defines the `FitnessReport` class, which generates a summary of recorded fitness activities.

### FitnessReport Class

```python
class FitnessReport:
    @staticmethod
    def build(workouts, goals):
        return {
            "total_workouts": len(workouts),
            "total_minutes": sum(
                w.duration_minutes for w in workouts
            ),
            "total_calories": sum(
                w.calories for w in workouts
            ),
            "activities": sorted({
                w.activity for w in workouts
            }),
            "goal_progress": goals.progress(workouts)
        }
```

### Dashboard Fields

| Field | Description |
|---|---|
| `total_workouts` | Total number of recorded workouts |
| `total_minutes` | Combined duration of all workouts |
| `total_calories` | Sum of the recorded calorie values |
| `activities` | Sorted list of distinct activity names |
| `goal_progress` | Progress toward weekly minute and workout-count targets |

### How the Dashboard Works

The dashboard uses Python's built-in operations to summarize the workout list.

**Total workouts**

```python
len(workouts)
```

Counts the workout records.

**Total minutes**

```python
sum(w.duration_minutes for w in workouts)
```

Adds the duration of every workout.

**Total calories**

```python
sum(w.calories for w in workouts)
```

Adds all recorded calorie values.

**Unique activities**

```python
sorted({w.activity for w in workouts})
```

A set removes duplicate activity names, and `sorted()` arranges the remaining names alphabetically.

The report combines these statistics with the goal progress returned by `GoalService`.

---

## 🧮 Fitness Statistics Calculation

Based on the sample data, the dashboard calculates the following values.

### Total Workout Duration

\[
35 + 45 + 50 = 130 \text{ minutes}
\]

### Total Calories

\[
360 + 280 + 420 = 1060
\]

### Workout Count

\[
1 + 1 + 1 = 3 \text{ workouts}
\]

### Weekly Minute Goal Progress

The default target is 150 minutes.

\[
\frac{130}{150}\times100 = 86.7\%
\]

The user has completed 130 out of the target 150 minutes.

### Weekly Workout Goal Progress

The default target is four workouts.

\[
\frac{3}{4}\times100 = 75\%
\]

The user has completed three out of the target four workouts.

### Summary

| Metric | Current Value | Goal | Progress |
|---|---:|---:|---:|
| Workout duration | 130 minutes | 150 minutes | 86.7% |
| Workout count | 3 workouts | 4 workouts | 75% |
| Calories recorded | 1,060 | Not configured | Not applicable |

The application does not define a calorie goal, so it reports total calories without calculating a calorie-goal percentage.

---

## 🧾 API-Style Request and Response Format

The application uses the `show()` helper function in `main98.py` to display operations.

```python
def show(action, data, status=200):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE {status}\n"
        f"{json.dumps(data, indent=2)}"
    )
```

The function displays:

- The simulated request name.
- A response status label.
- The result formatted as readable JSON.

### Operations Demonstrated

| Operation | Status Label | Purpose |
|---|---:|---|
| `POST /api/workouts` | `201` | Displays a newly recorded workout |
| `GET /api/dashboard` | `200` | Displays the overall fitness report |

The three workout logging operations each display a `201` status label. The dashboard uses the default status of `200`.

**Note:** These are simulated API-style labels printed in the terminal. The program does not create actual HTTP endpoints, run a web server, or send network requests.

---

## 📄 Example Dashboard Response

After all three workouts are recorded, the dashboard data will have the following structure. The workout dates will depend on the date each record is created.

```json
{
  "total_workouts": 3,
  "total_minutes": 130,
  "total_calories": 1060,
  "activities": [
    "Cycling",
    "Running",
    "Strength Training"
  ],
  "goal_progress": {
    "minutes": {
      "current": 130,
      "goal": 150,
      "percent": 86.7
    },
    "workouts": {
      "current": 3,
      "goal": 4,
      "percent": 75.0
    }
  }
}
```

This is the data returned by `FitnessReport.build()` for the sample workouts and default goals. The `show()` function wraps this data in the terminal output with the request label `GET /api/dashboard` and response status `200`.

---

## 🔄 Complete Application Workflow

The application follows this sequence:

```text
Start Application
        |
        v
Create WorkoutService
        |
        v
Create GoalService
        |
        v
Log Running Workout
        |
        v
Log Strength Training Workout
        |
        v
Log Cycling Workout
        |
        v
Validate and Store Each Workout
        |
        v
Generate Fitness Dashboard
        |
        v
Calculate Workout Statistics
        |
        v
Calculate Goal Progress
        |
        v
Display JSON Report
```

The workflow separates workout recording, goal tracking, and report generation into different modules.

---

## 🏗️ Project Architecture

The project contains four Python modules.

```text
                  main98.py
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      workouts.py   goals.py   reports.py
          |           |           |
          v           v           v
    Workout Records  Goal Data  Report Builder
          |           |           |
          +-----------+-----------+
                      |
                      v
              Fitness Dashboard
                      |
                      v
                JSON Output
```

### Module Responsibilities

- **`main98.py`** — entry point; creates services, logs sample workouts, and displays the dashboard.
- **`workouts.py`** — defines the `Workout` dataclass and `WorkoutService` for workout validation and storage.
- **`goals.py`** — defines `GoalService` and calculates progress toward fitness goals.
- **`reports.py`** — defines `FitnessReport` and summarizes workout statistics.

This modular design separates data management, goal calculations, and reporting logic, making the project easier to understand and extend.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement workout logging, fitness statistics, validation, and goal tracking.

### 🧩 Dataclasses

The `dataclasses` module provides a structured way to represent workout records.

```python
from dataclasses import asdict, dataclass
```

The `asdict()` function converts a dataclass instance into a dictionary.

### 📅 Date Handling

The `datetime` module provides the current date.

```python
from datetime import date
```

The expression `date.today().isoformat()` produces a date string in `YYYY-MM-DD` format.

### 📋 Lists

Lists store workout objects in memory and allow the program to iterate over recorded activities.

### 🗂️ Dictionaries and Sets

Dictionaries structure the dashboard report, while sets identify unique activity names.

### 🧮 Built-in Functions

The project uses:

- `sum()` to calculate total minutes and calories.
- `len()` to count workout records.
- `sorted()` to arrange activity names.
- `min()` to cap goal percentages at 100%.
- `round()` to round percentages to one decimal place.

### 🧾 JSON Serialization

The `json` module formats dictionaries and lists into readable JSON output.

### 🏗️ Object-Oriented Programming

The project separates workout management, goal tracking, and reporting into dedicated classes.

### ⚠️ Exception Handling

The workout service raises `ValueError` when the duration is non-positive or the calorie value is negative.

---

## 📦 Requirements

This project uses Python's standard library and does not require any external Python packages.

### Check Python Installation

```bash
python --version
```

Python 3.7 or later supports the syntax used in this project, including dataclasses and f-strings.

### `requirements.txt`

```text
# No external dependencies required.
```

---

## 📂 Project Structure

```text
DAY_98/
│
├── main98.py
├── workouts.py
├── goals.py
├── reports.py
├── requirements.txt
└── README.md
```

### File Description

| File / Folder | Purpose |
|---|---|
| `main98.py` | Main entry point and sample workout workflow |
| `workouts.py` | Workout dataclass and workout logging service |
| `goals.py` | Weekly fitness goal configuration and progress calculations |
| `reports.py` | Dashboard statistics and report generation |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Ensure Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal in the `DAY_98` project folder.

```bash
cd DAY_98
```

### Step 3 — Check the Project Files

Make sure these Python files are present:

```text
main98.py
workouts.py
goals.py
reports.py
```

### Step 4 — Run the Application

Execute the main file:

```bash
python main98.py
```

### Step 5 — Review the Output

The terminal displays:

- Three workout creation responses.
- Workout IDs and dates.
- Activity names, durations, and calorie values.
- Total workout count.
- Total exercise duration.
- Total recorded calories.
- A sorted list of activities.
- Weekly minute-goal progress.
- Weekly workout-count progress.

No database setup, API key, external dependency installation, or server configuration is required.

---

## ⚠️ Important Notes and Limitations

### 1. In-Memory Storage

Workout records are stored in a Python list. All records are lost when the program exits.

### 2. No User Accounts

The application does not currently support registration, login, or individual user profiles.

### 3. No Actual HTTP API

Request names such as `POST /api/workouts` and `GET /api/dashboard` are labels for terminal output. They do not correspond to live endpoints.

### 4. No Weekly Date Filtering

Although every workout contains a date, the goal calculations currently include every workout in the list. They do not filter workouts by the current week.

### 5. No Calorie Estimation

The application accepts calorie values as input. It does not estimate calories from activity type, workout intensity, body weight, or heart rate.

### 6. Workout Validation Is Limited

The service checks duration and calorie values, but it does not validate activity names, input types, or the format of manually supplied dates.

### 7. Goal Values Must Be Positive

The percentage calculation divides by the configured goal. Setting `weekly_minutes` or `weekly_workouts` to zero will cause a division-by-zero error.

### 8. No Calorie Goal

The dashboard calculates total calories but does not compare them with a target.

### 9. No Graphical Dashboard

The current version displays information in the terminal. It does not contain charts, a GUI, or a web-based dashboard.

### 10. No Workout Editing or Deletion

The application can log workouts but does not currently provide methods for editing or deleting existing records.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Python dataclasses
- Object-oriented programming
- Lists and dictionaries
- Sets and set comprehensions
- List comprehensions and generator expressions
- Date and time handling
- Input validation
- Exception handling
- Sequential ID generation
- Aggregation using `sum()`
- Counting records using `len()`
- Sorting data
- Percentage calculations
- Numeric rounding
- Dictionary construction
- JSON serialization
- Static methods
- Modular programming
- API-style request and response formatting

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Define structured workout records using a dataclass.
- Record physical activities with duration, calories, and dates.
- Generate sequential workout identifiers.
- Validate workout values before storing records.
- Maintain an in-memory collection of workout objects.
- Calculate total workout duration and calories.
- Identify distinct activities from recorded data.
- Configure weekly fitness goals.
- Calculate goal progress percentages.
- Generate a consolidated fitness dashboard.
- Convert Python objects into dictionaries.
- Format structured results as JSON.
- Separate workout management from goal calculations and reporting.
- Build the backend foundation of a fitness-tracking application.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🌐 Build a web interface using Flask or Django.
- 🎨 Create a desktop interface using Tkinter or CustomTkinter.
- 🗄️ Store workout records in SQLite or PostgreSQL.
- 👤 Add user registration and authentication.
- 📆 Filter workouts by week, month, or custom date range.
- ✏️ Add workout editing and deletion.
- 🏃 Support more workout categories and activity details.
- 🔥 Estimate calories using configurable activity factors.
- ❤️ Integrate heart-rate and wearable-device data.
- 🎯 Add daily, weekly, and monthly fitness goals.
- 📈 Display progress charts using Matplotlib.
- 📊 Track personal records and workout trends.
- 🧮 Add distance, pace, steps, and heart-rate metrics.
- 🔔 Add goal reminders and progress notifications.
- 📤 Export workout reports to CSV or PDF.
- 🧪 Add automated unit tests for workout validation and goal calculations.
- 🔐 Implement secure user-specific workout storage.
- 🚀 Deploy the application as a web service.

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 98** focuses on **Fitness Tracking and Goal Monitoring**, combining workout logging, fitness statistics, goal progress calculations, and report generation using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍🏃