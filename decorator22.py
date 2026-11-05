def time_decorator(func):
    def wrapper():
        print("Function Started..")
        func()
        print("Function is finished..")
    return wrapper
@time_decorator
def hello():
    print("Python is awesome!..")
hello()