import multiprocessing

def child_process(conn):

    for i in range(3):
        message = conn.recv()
        print("Child received:", message)

    conn.send("All messages received successfully!")
    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=child_process,
        args=(child_conn,)
    )

    process.start()

    messages = [
        "Hello",
        "Welcome to Python",
        "Multiprocessing is interesting"
    ]

    for message in messages:
        parent_conn.send(message)
        print("Parent sent:", message)

    confirmation = parent_conn.recv()

    print("\nParent received:", confirmation)

    parent_conn.close()
    child_conn.close()

    process.join()