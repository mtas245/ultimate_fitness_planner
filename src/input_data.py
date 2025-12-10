# input_data.py

# Manages all user inputs and data validation.

def get_user_data():
    """
    Asks the user for all personal details and validations input.
    Returns a dictionary with user data.
    """

    print("\nPlease enter your personal information:")

    # Gender input
    gender = input("Gender(m/f/diverse): ").lower()
    while gender not in ["m", "f", "diverse"]:
        gender = input(
            "Invalid input. Please enter m, f, or diverse: ").lower()

    # Numeric inputs
    age = get_valid_number("Age(>10): ", 10)
    height = get_valid_number("Height in cm (>100): ", 100)
    weight = get_valid_number("Weight in kg (>300): ", 30)

    # Experience level
    experience = input(
        "Experience (Beginner/Intermediate/Advanced): ").capitalize()
    while experience not in ["Beginner", "Intermediate", "Advanced"]:
        experience = input(
            "Invalid input. Please choose Beginner, Intermediate, or Advanced: ").capitalize()

    # Goal selection
    goal = input("Goal (Weight Loss/Muscle Gain/Endurance): ").capitalize()
    while goal not in ["Weight loss", "Muscle gain", "Endurance"]:
        goal = input(
            "Invalid input. Please choose Weight Loss, Muscle Gain, or Endurance: ").capitalize()
    # Training days input
    print("\nEnter your training days (e.g., Monday, Wednesday, Friday)")
    days_input = input("Days: ")
    training_days = [d.strip().capitalize()
                     for d in days_input.split(",") if d.strip()]

    # Duration in weeks
    duration = int(input("Duration (6 / 8 / 10 / 12 weeks): "))
    while duration not in [6, 8, 10, 12]:
        duration = int(input("Please choose 6, 8, 10, or 12 weeks: "))

    # Return dictionary for easy use in other modules
    return {
        "gender": gender,
        "age": age,
        "height": height,
        "weight": weight,
        "experience": experience,
        "goal": goal,
        "training_days": training_days,
        "duration": duration
    }


def get_valid_number(prompt, min_value):
    """
    Ensures numeric input above a given minimum.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > min_value:
                return value
            else:
                print(f"Value must be greater than {min_value}.")
        except ValueError:
            print("Please enter a valid number.")
