import json
import random
import os
from datetime import datetime, timedelta


# Main Function

def generate_plan(user_data):
    """
    Generates a weekly training plan using exercise data from JSON.
    Adds real calender dates and supports 6/8/10/12-week durations.
    """
    goal = user_data["goal"]
    experience = user_data["experience"]

    # Load available exercises from JSON
    exercises = _load_exercises()

    # Select correct exercise list
    if goal in exercises and experience in exercises[goal]:
        selected_exercises = exercises[goal][experience]
    else:
        print("⚠️ No exercises found for this combination. Using default plan. ")
        selected_exercises = [
            {"name": "Walking", "sets": "30 min", "equipment": "None"}]

    # Generate plan with data
    plan = create_dated_plan(user_data, selected_exercises)
    return plan

# Helper function: Load exercises


def _load_exercises():
    """
    Reads exercises from the external JSON file (works from any location).
    Handles missing file or invalid format error gracefully.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "exercises.json")

    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"[ERROR] exercises.json not found at: {file_path}")
        return {}

    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON format in exercises.json.")
        return {}

    # Helper function: Generate plan with dates


def create_dated_plan(user_data, exercises):
    """
    Generates a plan with real calender dates.
    User can select training days and total duration in weeks.
    """
    days = user_data["training_days"]
    weeks = user_data["duration"]

    today = datetime.today()
    plan = []

    # Map weekdays to numbers
    day_map = {
        "Monday": 0, "Tuesday": 1, "Wednesdays": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }

    selected_day_numbers = [day_map[d] for d in days if d in day_map]

    current_date = today
    end_date = today + timedelta(weeks=weeks)

    while current_date <= end_date:
        if current_date.weekday() in selected_day_numbers:
            chosen = random.sample(exercises, min(len(exercises), 3))
            day_line = f"{current_date.strftime('%Y-%m-%d')} ({current_date.strftime('%A')}): " + \
                ", ".join(
                    [f"{ex['name']} ({ex['sets']})" for ex in chosen])
            plan.append(day_line)
        current_date += timedelta(days=1)

    return plan
