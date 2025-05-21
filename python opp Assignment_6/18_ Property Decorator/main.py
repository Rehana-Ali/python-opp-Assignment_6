
class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        print("Setting the price...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price


p1 = Product(100)

print(p1.price)    

p1.price = 200     
print(p1.price)  

del p1.price      
