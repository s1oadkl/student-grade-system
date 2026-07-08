"""
Student Grade System

A simple Python program to calculate a student's total marks,
average marks, grade, and pass/fail result.
"""
def main():
    """Main function to run the student grade system."""
    
    name, math, english, science = student_info()
    total, average = calculate_total_and_average(math, english, science)
    grade = determine_grade(average)
    result = determine_pass_fail(average)
    display_results(name, total, average, grade, result)


def get_marks(subject):
    """ Get marks for a specific subject from the user."""

    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            
            else:
                print("Marks must be between 0 and 100. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def student_info():
    """ Get the student's name and marks from the user. """

    name = input("Enter student's name: ").strip()
    
    while not name:
        print("Name cannot be empty. Please enter a valid name.")
        name = input("Enter student's name: ").strip()

    math = get_marks("Math")
    english = get_marks("English")
    science = get_marks("Science")

    return name, math, english, science

def calculate_total_and_average(math, english, science):
    """ Calculate total and average marks. """

    total = math + english + science
    average = total / 3
    return total, average

def determine_grade(average):
    """ Determine the grade based on average marks. """
    
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def determine_pass_fail(average):
    """ Determine if the student has passed or failed based on average marks. """

    return "Pass" if average >= 60 else "Fail"


def display_results(name, total, average, grade, result):
    """Display the student's results in a formatted manner."""
    
    print("\nStudent Results")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    

if __name__ == "__main__":
    main()
    