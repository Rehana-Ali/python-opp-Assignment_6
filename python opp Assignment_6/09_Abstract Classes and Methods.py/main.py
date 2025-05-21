from abc import ABC, abstractmethod 
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(shape):
    def __init__(self, weight, height):
            self.weight = weight
            self.height = height

    def area(self):
        return self.weight * self.height
    
result = Circle(5, 10)
print("Area of circle :", result.area())
        

            
