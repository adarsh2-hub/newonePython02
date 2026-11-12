import threading,time
name=input("Enter the name:")
age=int(input("Enter the age:"))
def display_info():
    time.sleep(2)
    print("student name:",name)
    time.sleep(3)
    print("student age:",age)
t=threading.Thread(target=display_info)
t.start()
t.join()