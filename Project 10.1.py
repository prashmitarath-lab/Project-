
class Employee:
    # Method Overloading style: default values allow multiple ways to create objects
    def __init__(self, name=None, age=None, employee_id=None, salary=None):
        self.name = name
        self.age = age
        self.__employee_id = employee_id   # Encapsulated
        self.__salary = salary             # Encapsulated

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, new_id):
        self.__employee_id = new_id

    # Encapsulation: Getter & Setter for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def display(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${self.__salary}")

    def __del__(self):
        # Destructor
        print(f"Resources freed for Employee: {self.name}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        print("\nDeveloper Details:")
        super().display()
        print(f"Programming Language: {self.programming_language}")


person_list = []
employee_list = []
manager_list = []
developer_list = []

def create_person():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    person_list.append({"name": name, "age": age})
    print(f"\nPerson created with name: {name} and age: {age}.")


def create_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    emp = Employee(name, age, emp_id, salary)
    employee_list.append(emp)
    print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")


def create_manager():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    dept = input("Enter Department: ")
    mgr = Manager(name, age, emp_id, salary, dept)
    manager_list.append(mgr)
    print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")


def create_developer():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    lang = input("Enter Programming Language: ")
    dev = Developer(name, age, emp_id, salary, lang)
    developer_list.append(dev)
    print(f"\nDeveloper created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and language: {lang}.")


def show_details():
    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for p in person_list:
            print(f"\nName: {p['name']}, Age: {p['age']}")
    elif choice == 2:
        for e in employee_list:
            e.display()
    elif choice == 3:
        for m in manager_list:
            m.display()
    elif choice == 4:
        for d in developer_list:
            d.display()
    else:
        print("Invalid choice.")

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_person()
    elif choice == 2:
        create_employee()
    elif choice == 3:
        create_manager()
    elif choice == 4:
        create_developer()
    elif choice == 5:
        show_details()
    elif choice == 6:
        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")