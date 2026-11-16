import multiprocessing

def child_process(conn):
    num1, num2, num3 = conn.recv()

    print("Child received:", num1, num2, num3)

    result = num1 * num2 * num3

    conn.send(result)
    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=child_process,
        args=(child_conn,)
    )

    process.start()

    parent_conn.send((5, 10, 15))

    print("Parent sent: 5, 10, 15")

    result = parent_conn.recv()

    print("Parent received multiplication:", result)

    parent_conn.close()
    child_conn.close()

    process.join()