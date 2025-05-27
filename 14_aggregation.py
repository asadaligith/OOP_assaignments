# Employee class (independent class)
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")

# Department class using aggregation
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Reference to an existing Employee object

    def show_details(self):
        print(f"Department: {self.department_name}")
        self.employee.display()  # Accessing method of Employee

# Creating an independent Employee object
emp1 = Employee("Alice")

# Creating a Department object that refers to the Employee (aggregation)
dept1 = Department("HR", emp1)

# Displaying information
dept1.show_details()
