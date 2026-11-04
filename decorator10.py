def my_decorator(func):
    def wrapper():
        print("Welcome!..")
        func()
        print("Thank You!..")
    return wrapper
@my_decorator
def greet():
    print("Hello Python!..")
greet()