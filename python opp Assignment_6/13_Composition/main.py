class Engine:
    def start(self):
        print("Engine has started")

class Car:
    def __init__(self):
      self.engine = Engine()

    def start_car(self):
      self.engine.start()


my_car = Car()
my_car.start_car()


