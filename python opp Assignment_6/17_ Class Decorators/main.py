# Class Decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # greet method ko class mein jor dia
    return cls

# Decorated Class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def  introduce(self):
        return f"Hi, I am {self.name}"
    
person = Person("Ali")
print(person.greet())
        

