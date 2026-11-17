import multiprocessing

def child_process(conn):
    n1, n2, n3 = conn.recv()

    print("Child received:", n1, n2, n3)

    result = n1 * n2 * n3

    conn.send(result)
    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=child_process,
        args=(child_conn,)
    )

    process.start()

    parent_conn.send((500, 100, 150))

    print("Parent sent: 500, 100, 150")

    result = parent_conn.recv()

    print("Parent received multiplication:", result)

    parent_conn.close()
    child_conn.close()

    process.join()