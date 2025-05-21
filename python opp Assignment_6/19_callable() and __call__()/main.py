class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # multiply karne wala factor

    def __call__(self, value):
        return self.factor * value

times3 = Multiplier(3)

result = times3(10)  
print(result)         

print(callable(times3))  # ➜ True
