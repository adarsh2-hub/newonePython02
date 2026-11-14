import multiprocessing
def calculate_square(q):
    list=[2,4,6,8,10]
    for num in list:
        q.put(num*num)
if __name__=="__main__":
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=calculate_square,args=(q,))
    p.start()
    for i in range(5):
        print(q.get())
    p.join()