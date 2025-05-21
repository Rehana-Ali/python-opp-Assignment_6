class Counter:
    count = 0
    
    def __init__(self):
        Counter.count +=1

    @classmethod
    def show_count(cls):
        print(f"total object created {cls.count}")
         
obj1 = Counter()
obj1 = Counter()
obj1 = Counter()
obj1 = Counter()
obj1 = Counter()

Counter.show_count()













        