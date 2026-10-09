"""
CodeSoft Internship - Task 2: Calculator
------------------------------------------
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("========== SIMPLE CALCULATOR ==========")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        print("\nChoose an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == "4":
            result = divide(num1, num2)
            symbol = "/"
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.\n")
            continue

        print(f"\nResult: {num1} {symbol} {num2} = {result}\n")

        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
