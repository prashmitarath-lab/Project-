print("Welcome to the Pattern Generator and Number Analyzer!\n")

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            rows = int(input("Enter the number of rows for the pattern: "))

            if rows <= 0:
                print("Invalid row count! Stopping pattern generation.")
                break  # Using break as required

            print("\nPattern:")
            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()

        except ValueError:
            print("Invalid input! Please enter a positive number.")
            continue  # Using continue as required

    elif choice == "2":
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            if end < start:
                print("End of range must be greater than start!")
                continue

            total_sum = 0

            for num in range(start, end + 1):
                if num == 0:
                    pass  # Example of pass statement
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")

                total_sum += num

            print(f"Sum of all numbers from {start} to {end} is: {total_sum}")

        except ValueError:
            print("Invalid input! Please enter valid integers.")
            continue


    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.\n")