import multiprocessing
def send_message(conn):
    conn.send("Hello from Child Process")
    conn.close()
if __name__=="__main__":
    parent_conn,child_conn=multiprocessing.Pipe()
    process=multiprocessing.Process(target=send_message,args=(child_conn,))
    process.start()
    child_conn.close()
    message=parent_conn.recv()
    print("Received Message:",message)
    parent_conn.close()
    process.join()