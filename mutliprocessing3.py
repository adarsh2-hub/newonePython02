import multiprocessing
def print_numbers():
    print("Process is Printing:")
    for i in range(1,6):
        print(i)
if __name__=="__main__":
    p1=multiprocessing.Process(target=print_numbers)
    p2=multiprocessing.Process(target=print_numbers)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Both processes completed!")