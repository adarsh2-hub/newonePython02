import multiprocessing,time
def task():
    print("Process is running.....")
    time.sleep(3)
if __name__=="__main__":
    p=multiprocessing.Process(target=task)
    p.start()
    print("Process status:",p.is_alive())
    p.join()
    print("Process status:",p.is_alive())
    print("This Process Is Completed..")