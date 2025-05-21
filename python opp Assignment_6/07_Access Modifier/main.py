


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    # Getter method to access private variable
    def get_ssn(self):
        return self.__ssn
    
    def get_salary(self):
        return self._salary

# Create object
emp = Employee("Ali", 50000, "123-45-6789")

# Accessing variables
print("Public variable:", emp.name)
print("Protected variable using method:", emp.get_salary())

# Accessing private variable safely
print("Private variable using method:", emp.get_ssn())

# Trying to access private variable directly
try:
    print("Private variable directly:", emp.__ssn)
except AttributeError:
    print("Cannot access private variable directly")


