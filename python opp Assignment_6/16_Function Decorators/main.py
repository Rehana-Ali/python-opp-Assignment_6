def log_function_call(add):
    def wrapper():
        print("Function is being called")
        return add()
    return wrapper

@log_function_call
def say_hello():
    print(5 +10)

say_hello()

        