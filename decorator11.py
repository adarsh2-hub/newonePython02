def my_decorator(func):
    def wrapper():
        print("Starting Program!..")
        func()
        print("Learning Python!..")
    return wrapper
@my_decorator
def greet():
    print("Program Completed!..")
greet()