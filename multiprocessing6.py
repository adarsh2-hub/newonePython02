import multiprocessing
def show_process():
    process=multiprocessing.current_process()
    print("Process Name:",process.name)
if __name__=="__main__":
    p1=multiprocessing.Process(target=show_process)
    p2=multiprocessing.Process(target=show_process)
    p1.start()
    p2.start()
    p1.join()
    p2.join()