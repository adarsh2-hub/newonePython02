import threading 
def task1():
    print("Learning Python")
def task2():
    print("Practicing Coding")
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()