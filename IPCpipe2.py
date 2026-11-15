import multiprocessing
def receive_message(conn):
   message=conn.recv()
   print("Received Message:",message)
if __name__=="__main__":
   parent_conn,child_conn=multiprocessing.Pipe()
   process=multiprocessing.Process(target=receive_message,args=(child_conn,))
   process.start()
   parent_conn.send("Hello from Parent Process")
   parent_conn.close()
   child_conn.close()