def my_decorator(func):
    def wrapper():
        print("Welcome to Python!..")
        func()
        print("I am learning Python!..")
    return wrapper
@my_decorator
def greet():
    print("Thank You!..")
greet()