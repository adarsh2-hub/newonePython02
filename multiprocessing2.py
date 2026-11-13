import multiprocessing
def print_message():
    print("Hello! I am learning in a seperate process.")
if __name__=="__main__":
    p=multiprocessing.Process(target=print_message)
    p.start()
    p.join()