try:
    age=int(input("enter the age:"))
    if age<18:
        raise ValueError("Age must be 18 or above")
    print("You are Eligible.")
except ValueError as e:
    print("Error:",e)