def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("--- Calculator By Kalpesh Borse ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        choice = int(input("Select operation (1. Addition, 2. Subtraction, 3. Multiplication, 4. Division): "))
    except ValueError:
        print("Invalid input. Please enter valid numbers and a valid choice.")
        return

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        return

    print(f"Result: {result}")

calculator()
