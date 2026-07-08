# Student Grade System

A simple Python program that calculates a student's total marks, average marks, grade, and pass/fail result.

## About the Project

This project is a beginner-friendly Python program created to practice:

- Taking user input
- Validating input
- Using functions
- Working with conditional statements
- Formatting output

The program asks for a student's name and marks in Math, English, and Science. It then calculates the total marks, average marks, grade, and final pass/fail result.

## Features

- Accepts student name
- Validates that the name is not empty
- Accepts marks for three subjects
- Validates that marks are between 0 and 100
- Calculates total marks
- Calculates average marks
- Assigns a grade based on the average
- Displays whether the student passed or failed

## Grade Criteria

| Average Marks | Grade |
| --- | --- |
| 90 and above | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| Below 60 | F |

## Pass/Fail Criteria

The student passes if the average mark is 60 or above.

The student fails if the average mark is below 60.

## How to Run

1. Make sure Python is installed on your computer.
2. Save the program in a file, for example:

```bash
student_grade_system.py
```

3. Open a terminal or command prompt in the same folder.
4. Run the program:

```bash
python student_grade_system.py
```

## Example Output

```text
Enter student's name: Alex
Enter marks for Math (0-100): 85
Enter marks for English (0-100): 90
Enter marks for Science (0-100): 78

Student Results
Name: Alex
Total Marks: 253.0
Average Marks: 84.33
Grade: B
Result: Pass
```

## What I Learned

While building this project, I practiced how to:

- Organize code using functions
- Reuse code with helper functions
- Handle invalid user input using `try` and `except`
- Use `if`, `elif`, and `else` conditions
- Format numbers using f-strings
- Write cleaner and more readable Python code

## Future Improvements

Possible improvements for this project:

- Add more subjects
- Store results in a file
- Support multiple students
- Show the highest and lowest marks
- Create a simple graphical user interface

## Technologies Used

- Python

## Author

Created as a beginner Python practice project.
