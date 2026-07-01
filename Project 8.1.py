dataset_summary = {}

def built_in_summary(data):
    """Displays basic statistics using built-in functions."""
    print("\nData Summary:")
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")
    print(f"- Average value: {sum(data)/len(data):.2f}")

def find_duplicates(data):
    """Returns duplicate values from the dataset."""
    seen = set()
    duplicates = set()
    for num in data:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return duplicates

def show_args(*args):
    """Displays all values passed using *args."""
    print("\nValues received via *args:", args)


def show_kwargs(**kwargs):
    """Displays dataset characteristics using **kwargs."""
    print("\nDataset Characteristics:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

def factorial(n):
    """Recursive factorial function."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def filter_threshold(data, threshold):
    """Filters values >= threshold using lambda."""
    return list(filter(lambda x: x >= threshold, data))

def dataset_stats(data):
    """Returns min, max, sum, and average."""
    return min(data), max(data), sum(data), sum(data)/len(data)

def display_2d(data):
    """Displays 2D list in grid format."""
    print("\n2D List:")
    for row in data:
        print(" ".join(str(x) for x in row))


data_1d = []
data_2d = []

print("Welcome to the Data Analyzer and Transformer Program\n")

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        print("\nStep 1: Input Data")
        print("1. Enter 1D List")
        print("2. Enter 2D List")
        sub = input("Please enter your choice: ")

        if sub == "1":
            raw = input("\nEnter data for a 1D array (separated by spaces): ")
            data_1d = list(map(int, raw.split()))
            print("\nData has been stored successfully!")

            # Update global summary
            global dataset_summary
            dataset_summary = {
                "Total Elements": len(data_1d),
                "Mean": sum(data_1d)/len(data_1d)
            }

        elif sub == "2":
            rows = int(input("Enter number of rows: "))
            data_2d = []
            for i in range(rows):
                row = list(map(int, input(f"Enter row {i+1} values: ").split()))
                data_2d.append(row)
            print("\n2D Data stored successfully!")
            display_2d(data_2d)

    elif choice == "2":
        if not data_1d:
            print("No data available. Please input data first.")
        else:
            built_in_summary(data_1d)


    elif choice == "3":
        n = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial of {n} is: {factorial(n)}")

    elif choice == "4":
        if not data_1d:
            print("No data available. Please input data first.")
        else:
            threshold = int(input("Enter a threshold value: "))
            filtered = filter_threshold(data_1d, threshold)
            print("Filtered Data (values >= threshold):", filtered)


    elif choice == "5":
        if not data_1d:
            print("No data available. Please input data first.")
        else:
            print("Choose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            s = input("Enter your choice: ")

            if s == "1":
                data_1d.sort()
                print("Sorted Data in Ascending Order:", data_1d)
            else:
                data_1d.sort(reverse=True)
                print("Sorted Data in Descending Order:", data_1d)


    elif choice == "6":
        if not data_1d:
            print("No data available. Please input data first.")
        else:
            mn, mx, sm, avg = dataset_stats(data_1d)
            print("\nDataset Statistics:")
            print(f"- Minimum value: {mn}")
            print(f"- Maximum value: {mx}")
            print(f"- Sum of all values: {sm}")
            print(f"- Average value: {avg:.2f}")

    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again."