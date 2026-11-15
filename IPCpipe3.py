import multiprocessing
def child_process(conn):
    message=conn.recv()
    print("Received Message:",message)
    conn.send("Hello from Child Process")
    conn.close()
if __name__=="__main__":
    parent_conn,child_conn=multiprocessing.Pipe()
    process=multiprocessing.Process(target=child_process,args=(child_conn,))
    process.start()
    parent_conn.send("Hello from Parent Process")
    message=parent_conn.recv()
    print("Reply:",message)
    process.join()