multi_utility_toolkit/
│
├── main.py
│
├── utilities/
│   ├── __init__.py
│   ├── datetime_tools.py
│   ├── math_tools.py
│   ├── random_tools.py
│   ├── uuid_tools.py
│   └── file_tools.py

from utilities.datetime_tools import datetime_menu
from utilities.math_tools import math_menu
from utilities.random_tools import random_menu
from utilities.uuid_tools import uuid_menu
from utilities.file_tools import file_menu

def explore_module():
    module_name = input("\nEnter module name to explore: ")
    try:
        module = __import__(module_name)
        print("\nAvailable Attributes in", module_name, ":")
        print(dir(module))
    except ModuleNotFoundError:
        print("Error: Module not found.")

def main():
    while True:
        print("\n=========================")
        print("Welcome to Multi-Utility Toolkit")
        print("=========================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("=========================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            datetime_menu()
        elif choice == 2:
            math_menu()
        elif choice == 3:
            random_menu()
        elif choice == 4:
            uuid_menu()
        elif choice == 5:
            file_menu()
        elif choice == 6:
            explore_module()
        elif choice == 7:
            print("\nThank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

    # Package initializer

    import datetime
import time

def display_current_datetime():
    now = datetime.datetime.now()
    print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def date_difference():
    d1 = input("\nEnter the first date (YYYY-MM-DD): ")
    d2 = input("Enter the second date (YYYY-MM-DD): ")

    try:
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
        diff = abs((date2 - date1).days)
        print("Difference:", diff, "days")
    except ValueError:
        print("Invalid date format.")

def format_date():
    d = input("\nEnter a date (YYYY-MM-DD): ")
    try:
        date_obj = datetime.datetime.strptime(d, "%Y-%m-%d")
        print("Formatted:", date_obj.strftime("%A, %B %d, %Y"))
    except ValueError:
        print("Invalid date format.")

def stopwatch():
    input("\nPress Enter to start the stopwatch...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    print("Elapsed Time:", round(end - start, 2), "seconds")

def countdown():
    try:
        sec = int(input("\nEnter countdown time in seconds: "))
        while sec > 0:
            print(sec)
            time.sleep(1)
            sec -= 1
        print("Time's up!")
    except ValueError:
        print("Invalid number.")

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_current_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            format_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown()
        elif choice == "6":
            break
        else:
            print("Invalid option.")

            import math

def factorial_calc():
    try:
        n = int(input("\nEnter a number: "))
        print("Factorial:", math.factorial(n))
    except ValueError:
        print("Invalid number.")

def compound_interest():
    try:
        p = float(input("\nEnter principal amount: "))
        r = float(input("Enter rate of interest (in %): "))
        t = float(input("Enter time (in years): "))
        amount = p * ((1 + r/100) ** t)
        print("Compound Interest:", round(amount, 2))
    except ValueError:
        print("Invalid input.")

def trig_calc():
    try:
        angle = float(input("\nEnter angle in degrees: "))
        rad = math.radians(angle)
        print("sin:", math.sin(rad))
        print("cos:", math.cos(rad))
        print("tan:", math.tan(rad))
    except ValueError:
        print("Invalid number.")

def area_shapes():
    print("\n1. Circle\n2. Square\n3. Rectangle")
    choice = input("Choose shape: ")

    try:
        if choice == "1":
            r = float(input("Enter radius: "))
            print("Area:", math.pi * r * r)
        elif choice == "2":
            s = float(input("Enter side: "))
            print("Area:", s * s)
        elif choice == "3":
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            print("Area:", l * b)
        else:
            print("Invalid option.")
    except ValueError:
        print("Invalid number.")

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            factorial_calc()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trig_calc()
        elif choice == "4":
            area_shapes()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

            import random
import string

def random_number():
    print("\nRandom Number:", random.randint(1, 100))

def random_list():
    lst = [random.randint(1, 50) for _ in range(5)]
    print("\nRandom List:", lst)

def random_password():
    length = int(input("\nEnter password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = "".join(random.choice(chars) for _ in range(length))
    print("Generated Password:", pwd)

def random_otp():
    otp = "".join(str(random.randint(0, 9)) for _ in range(6))
    print("\nGenerated OTP:", otp)

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            random_number()
        elif choice == "2":
            random_list()
        elif choice == "3":
            random_password()
        elif choice == "4":
            random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

            import uuid

def uuid_menu():
    print("\nGenerated UUID:", uuid.uuid4())

    import os

def create_file():
    name = input("\nEnter file name: ")
    try:
        with open(name, "x") as f:
            pass
        print("File created successfully!")
    except FileExistsError:
        print("File already exists.")

def write_file():
    name = input("\nEnter file name: ")
    data = input("Enter data to write: ")
    try:
        with open(name, "w") as f:
            f.write(data)
        print("Data written successfully!")
    except FileNotFoundError:
        print("File not found.")

def read_file():
    name = input("\nEnter file name: ")
    try:
        with open(name, "r") as f:
            print("\nFile Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

def append_file():
    name = input("\nEnter file name: ")
    data = input("Enter data to append: ")
    try:
        with open(name, "a") as f:
            f.write("\n" + data)
        print("Data appended successfully!")
    except FileNotFoundError:
        print("File not found.")

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

