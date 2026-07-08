__doc__ = """
A simple calculator program in Python.
"""

def show_menu():
    """Display the calculator menu."""
    print("\n=== Python Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def get_numbers():
    """Ask the user for two numbers."""
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    return first_number, second_number


def calculate(choice, first_number, second_number):
    """Perform the selected calculation."""
    if choice == "1":
        return first_number + second_number

    if choice == "2":
        return first_number - second_number

    if choice == "3":
        return first_number * second_number

    if choice == "4":
        if second_number == 0:
            return None
        return first_number / second_number


def main():
    """Run the calculator."""
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye! / さようなら！")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid option. Please choose from 1 to 5.")
            continue

        try:
            first_number, second_number = get_numbers()
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        result = calculate(choice, first_number, second_number)

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Answer: {result}")


if __name__ == "__main__":
    main()
    
    