import multiprocessing

def child_process(conn):
    num = conn.recv()

    print("Child received:", num)

    if num % 2 == 0:
        result = f"{num} is Even"
    else:
        result = f"{num} is Odd"

    conn.send(result)
    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=child_process,
        args=(child_conn,)
    )

    process.start()

    parent_conn.send(45)

    print("Parent sent: 45")

    result = parent_conn.recv()

    print("Parent received:", result)

    parent_conn.close()
    child_conn.close()

    process.join()