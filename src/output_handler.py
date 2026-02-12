# Handles all OUTPUT tasks:
#    - Display plan in console
#    - Save as text (.txt)
#    - Save as JSON (.json)
#    - Save as PDF (.pdf)

import datetime
import json
from fpdf import FPDF


def display_plan(user_data, plan):
    """
    Prints the personalized plan to the console.
    """
    print("\n=== Your Personalized Fitness Plann ===")
    print(f"Goal: {user_data['goal']}")
    print(f"Experience: {user_data['experience']}\n")

    for day in plan:
        print("-", day)


def save_plan(user_data, plan):
    """
    Saves the plan in the chosen format (TXT, JSON, PDF).
    """
    filename = f"plan_{user_data['goal'].replace(' ',' ')}_{user_data['experience']}"
    print("\nChoose a file format:")
    print("1 = Text (.txt)")
    print("2 = JSON (.json)")
    print("3 = PDF (.pdf)")
    choice = input("Your choice: ")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # JSON output
    if choice == "2":
        with open(f"{filename}.json", "w") as file:
            json.dump({
                "user_data": user_data,
                "plan": plan,
                "data": timestamp
            }, file, indent=4)
        print(f"✅ Plan saved as {filename}.json")

    # PDF output
    elif choice == "3":
        _save_as_pdf(filename, user_data, plan, timestamp)
        print(f"✅ Plan saved as {filename}.pdf")

    # Default TXT output
    else:
        with open(f"{filename}.txt", "w") as file:
            file.write(f"Generated: {timestamp}\n\n")
            file.write(f"Goal: {user_data['goal']}\n")
            file.write(f"Experience: {user_data['experience']}\n\n")
            for day in plan:
                file.write(f"-{day}\n")
        print(f"✅ Plan saved as {filename}.txt")

    # Helper: Save as PDF


def _save_as_pdf(filename, user_data, plan, timestamp):
    """
    Generates a simple PDF file using FPDF:
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=14)

    # Title
    pdf.cell(200, 10, txt="Personalized Fitness Plan", ln=True, align="C")
    pdf.ln(8)

    # User info
    pdf.set_font("Helvetica", size=12)
    pdf.cell(200, 10, txt=f"Generated: {timestamp}", ln=True)
    pdf.cell(200, 10, txt=f"Goal: {user_data['goal']}", ln=True)
    pdf.cell(200, 10, txt=f"Experience: {user_data['experience']}", ln=True)
    pdf.ln(5)

    # Weekly plan
    pdf.cell(200, 10, txt="Weekly Plan:", ln=True)
    pdf.ln(5)
    for day in plan:
        pdf.multi_cell(0, 8, f"-{day}")

    # Save PDF
    pdf.output(f"{filename}.pdf")
