# 🏋️‍♂️ Ultimate Fitness Plan Generator

The Personalized Ultimate Fitness Plan Generator is a console-based Python application that creates a customized multi-week training program based on user inputs such as gender, age, fitness goal, experience level and available training days.

The app reads exercises from a structured JSON file, builds a tailored workout plan, displays it in the console and allows the user to save it as TXT, JSON or PDF.

# Problem Analysis
Users who want to improve their fitness often struggle to create a structured, personlized workout plan. Many tools online are either too generic, too complex or not adaptable to personal data such as goals, experience level or available training days. 
This application solves the problem by generating a fully personalized fitness plan ussing simple console input and data-driven training logic. 

# Scenario 
A user starts the program in the console. 
The app asks for essentials: 
	- gender, age, height, weight
	- fitness goal (Weight loss/ Muscle gain / Endurance)
	- experience level
	- available training days
	- program duration 

Using this information, the application generates a structured weekly plan based on the exercises data stored in exercises.json.
Finally, the user can view the plan in the console and export it as TXT, JSON and PDF.

# User Stories
1. As a user, I want to enter my personal data and training preferences.
2. As a user, I want the system to generate a personlized fitness plan.
3. As a user, I want to see my plan immediately in the console
4. As a user, I want to save the plan as .txt, .json or .pdf file.
5. As a user, I want the program to prevent invalid input so I don't cause errors.

# Use Cases
- Collect User Date
  Handled in input_data.get_user_data() with validation
- Load Exercise Database
  Implemented in training_logic.generate_plan()
- Display Plan
  Printed via display_plan() in output_handler.py
- Save Plan
  Exported as TXT, JSON or PDF via save_plan() in output_handler.py

# Project Requirments
# 1. Interactive App (Console input)
Our program fulfills this requirement extensively: 
- All user data is collected via input() prompts in input_data.py
- The user selects the outputs file format in save_plan() through console input
- The whole application flow (main() is interactive:
  	- enter personal data
  	- view plan
  	- choose saving option
This meets the requirement for a fully interactive console application.

# Data Validation 
Our code contains strong validation mechanisms: 
# Gender validation 
    
    gender = input("Gender(m/f/diverse): ").lower()

# Numerica validation (age, height, weight)

	age = get_valid_number("Age(>10): ", 10)
    height = get_valid_number("Height in cm (>100): ", 100)
    weight = get_valid_number("Weight in kg (>300): ", 30)

# Experience level validation
Requires correct capitalization & valid options: 
	
	experience = input(
        "Experience (Beginner/Intermediate/Advanced): ").capitalize()
    while experience not in ["Beginner", "Intermediate", "Advanced"]:
        experience = input(
            "Invalid input. Please choose Beginner, Intermediate, or Advanced: ").capitalize()

# Goal validation 
Matches exercise categories in the JSON file: 

	goal = input("Goal (Weight Loss/Muscle Gain/Endurance): 		").capitalize()
    while goal not in ["Weight loss", "Muscle gain", "Endurance"]:
        goal = input(
            "Invalid input. Please choose Weight Loss, Muscle Gain, or Endurance: ").capitalize()

# Duration validation

	duration = int(input("Duration (6 / 8 / 10 / 12 weeks): "))
    	while duration not in [6, 8, 10, 12]:
        	duration = int(input("Please choose 6, 8, 10, or 12 weeks: "))
Overall, our application prevents invalid inputs at every step, meeting this requirement strongly. 

# File Processing 
We use multiples types of file I/O:
# Reading (Input Files)
exercises.json is read to access the exercises database 
Stored as structured data with categories and levels

This supports goal-based plan generation. 

# Writing (Output Files)
In output_handler.save_plan(), the user can save their plan as:

TXT: 

		with open(f"{filename}.txt", "w") as file:

JSON: 
 
 		with open(f"{filename}.json", "w") as file:
            		json.dump({

PDF: 
Using fpdf():
			
			pdf = FDPF()
			pdf.output(f"{filename}.pdf")

#⚙️ Implementation

Technology 
	- Python 3.13.7
	- No external moduls except fpdf (installed via requirements.txt)
	- Console-based interaction 

# Repository Structure 

├── main.py                # main program flow (start here)
├── input_data.py          # handles input & validation
├── training_logic.py      # generates plan 
├── output_handler.py      # saving & displaying plans
├── exercises.json         # exercise database
├── requirements.txt       # project dependencies (fpdf)


#▶️ How to Run 
1. Open terminal
2. Navigate to the project folder
3. Run:

		python3 main.py 


📚 Libraries Used

# Standard Libraries
- json -- Reading/writing structured data
-  datetime -- Timestamp for files

# Third-Party Libraries 

- fdpf -- Generating PDF output

Install via: 
		
		pip install -r requirements.txt		


✔️ Summary

This application guides users from entering their personal details to receiving a complete, personalized training plan that matches their goals and experience. 
It ensures: 
	- Reliable input validation 
	- Data-driven plan creation
	- Multiple output formats
	- Clean console interaction 

The project demonstrates full mastery of console programming, file handling and data validation. 


















## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
