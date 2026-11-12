import threading
def student():
    print("Adarsh is learning Python")
t=threading.Thread(target=student)
t.start()
t.join()