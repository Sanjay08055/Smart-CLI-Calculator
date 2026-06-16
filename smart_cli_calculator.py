import math


def arithmetic_operation():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == '+':
        print("Result:", num1 + num2)

    elif operation == '-':
        print("Result:", num1 - num2)

    elif operation == '*':
        print("Result:", num1 * num2)

    elif operation == '/':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid operation selected.")


def trigo_operation():
    choice = input(
        "Select function (sin/cos/tan/log/sqrt/power): "
    ).lower()

    if choice == 'sin':
        angle = float(input("Enter angle in degrees: "))
        result = math.sin(math.radians(angle))
        print("Result:", result)

    elif choice == 'cos':
        angle = float(input("Enter angle in degrees: "))
        result = math.cos(math.radians(angle))
        print("Result:", result)

    elif choice == 'tan':
        angle = float(input("Enter angle in degrees: "))
        result = math.tan(math.radians(angle))
        print("Result:", result)

    elif choice == 'log':
        value = float(input("Enter value: "))
        if value > 0:
            result = math.log(value)
            print("Result:", result)
        else:
            print("Log is defined only for positive numbers.")

    elif choice == 'sqrt':
        value = float(input("Enter value: "))
        if value >= 0:
            result = math.sqrt(value)
            print("Square Root:", result)
        else:
            print("Square root of negative number is not possible.")

    elif choice == 'power':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        result = math.pow(base, exponent)
        print(f"{base} ^ {exponent} = {result}")

    else:
        print("Please select a valid operation.")


def conversion_operator():
    print("\n1. cm <-> inch")
    print("2. kg <-> lb")
    print("3. Celsius <-> Fahrenheit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        unit = input("Convert to (cm/inch): ").lower()

        if unit == 'cm':
            value = float(input("Enter value in inch: "))
            result = value * 2.54
            print("Length in cm:", result)

        elif unit == 'inch':
            value = float(input("Enter value in cm: "))
            result = value / 2.54
            print("Length in inch:", result)

        else:
            print("Invalid unit selected.")

    elif choice == 2:
        unit = input("Convert to (kg/lb): ").lower()

        if unit == 'kg':
            value = float(input("Enter value in lb: "))
            result = value / 2.20462
            print("Weight in kg:", result)

        elif unit == 'lb':
            value = float(input("Enter value in kg: "))
            result = value * 2.20462
            print("Weight in lb:", result)

        else:
            print("Invalid unit selected.")

    elif choice == 3:
        unit = input("Convert to (c/f): ").lower()

        if unit == 'c':
            value = float(input("Enter temperature in Fahrenheit: "))
            result = (value - 32) * 5 / 9
            print("Temperature in Celsius:", result)

        elif unit == 'f':
            value = float(input("Enter temperature in Celsius: "))
            result = (value * 9 / 5) + 32
            print("Temperature in Fahrenheit:", result)

        else:
            print("Invalid unit selected.")

    else:
        print("Invalid choice.")


def main():

    print("\n========== SMART CLI CALCULATOR ==========")
    print("\n========== CREATED BY SANJAY JANGID ======\n")
    print("1. Basic Arithmetic Operations")
    print("2. Scientific Functions")
    print("3. Unit Conversion")
    print("4. Exit")
    print("==========================================")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            arithmetic_operation()

        elif choice == "2":
            trigo_operation()

        elif choice == "3":
            conversion_operator()

        elif choice == "4":
            print("Thank you for using Smart CLI Calculator!")
            break

        else:
            print("Invalid choice! Please try again.")

        again = input(
            "\nDo you want another calculation? (y/n): "
        ).lower()

        if again != 'y':
            print("Thank you for using Smart CLI Calculator!")
            break


main()
