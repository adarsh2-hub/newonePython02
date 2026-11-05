def Welcome_decorator():
    def wrapper():
        print("Welcome to Python!..")
        func()
        print("Have the nice day..")
    return wrapper
def study():
    print("I am learning Decorator!..")
study()