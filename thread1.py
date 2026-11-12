import threading

def task():
    print("Hello from thread!")

t = threading.Thread(target=task)

t.start()
t.join()

print("Main program finished!")