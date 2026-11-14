import multiprocessing
def send_message(q):
    q.put("Hello from Child Process")
if __name__=="__main__":
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=send_message,args=(q,))
    p.start()
    print("Received Message:",q.get())
    p.join()