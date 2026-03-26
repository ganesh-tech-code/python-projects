# Simple Calculator Project
# I built this to practice basic Python concepts like functions, loops, and conditions

def add(a, b):
    # adding two numbers
    return a + b

def subtract(a, b):
    # subtracting second number from first
    return a - b

def multiply(a, b):
    # multiplying two numbers
    return a * b

def divide(a, b):
    # checking division by zero (common mistake I learned to handle)
    if b == 0:
        return "Error! Division by zero is not allowed"
    return a / b


# running the calculator continuously until user wants to exit
while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    # asking user what they want to do
    choice = input("Enter your choice (1-5): ")

    # exit condition
    if choice == "5":
        print("Exiting calculator... 👋")
        break

    # checking if user selected a valid operation
    if choice in ["1", "2", "3", "4"]:
        try:
            # taking inputs from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # performing operation based on user choice
            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))

        except ValueError:
            # if user enters something other than number
            print("Invalid input! Please enter numbers only.")

    else:
        # if wrong menu option is selected
        print("Invalid choice! Please select a valid option.")