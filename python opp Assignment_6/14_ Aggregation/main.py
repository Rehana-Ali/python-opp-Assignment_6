class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self , employee):
        self.employee = employee

    def show_employee(self):
        print(f"Employee Name: {self.employee.name}")

emp = Employee("Ali")
dep = Department(emp)
dep.show_employee()

del dep

print(emp)
