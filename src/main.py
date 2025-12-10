# Main program for the Fitness Plan Generator.
# Controls the full process: input, logic and output.

from input_data import get_user_data
from training_logic import generate_plan
from output_handler import save_plan, display_plan


def main():
    """
    Main flow of the application.
    1. Collect user data
    2. Generate training plan
    3. Display and save plan
    """
    print("=== Personalized Fitness Plan Generator ===")

    # Step 1: Ask user for input data
    user_data = get_user_data()

    # Step 2: Create plan based on user input
    plan = generate_plan(user_data)

    # Step 3: Show plan in console
    display_plan(user_data, plan)

    # Step 4: Save plan as TXT, JSON, or PDF
    save_plan(user_data, plan)

    print("\✅ Your personalized fitness plan has been generated and saved!")


# Program starts here
if __name__ == "__main__":
    main()
