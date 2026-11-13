import threading,time
def student():
    print("Student marks is running..")
    time.sleep(5)
    print("student marks is in percentage form:98.")
t=threading.Thread(target=student)
t.start()
t.join()