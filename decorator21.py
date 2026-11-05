def My_decorator(func):
    def wrapper(a,b):
        print("Calculation is starting..")
        result=func(a,b)
        print(result)
        print("calculation is completed..")
    return wrapper
@My_decorator
def add(a,b):
    return a+b
add(10,20)