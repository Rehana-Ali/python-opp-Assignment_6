class Person:
    def __init__(self, name):
        self.name = name     #instance variable

class Teacher(Person):
    def __init__(self, name , subject):
        super().__init__(name)
        self.subject = subject   #instance variable

    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

teacher1 = Teacher("Ali" , "Math")  #instance of the class
teacher2 = Teacher("Ahmed" , "urdu")
teacher1.display()   #instance methpod
teacher2.display()

