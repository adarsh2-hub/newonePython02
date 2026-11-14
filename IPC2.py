import multiprocessing
def send_data(q):
    q.put("Python")
    q.put("Java")
    q.put("C++")
if __name__=="__main__":
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=send_data,args=(q,))
    p.start()
    print("Received:",q.get())
    print("Received:",q.get())
    print("Received:",q.get())
    p.join()