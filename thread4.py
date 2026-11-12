import threading
def print_numbers():
    for i in range(1,6):
        print(i)
t=threading.Thread(target=print_numbers)
t.start()
t.join()
print("Task Completed!")    