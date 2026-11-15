import multiprocessing

def send_numbers(conn):

    numbers = conn.recv()

    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    results = {
        "sum": total,
        "maximum": maximum,
        "minimum": minimum
    }

    conn.send(results)
    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=send_numbers,
        args=(child_conn,)
    )

    process.start()

    numbers = [10, 20, 30, 40, 50]

    parent_conn.send(numbers)

    results = parent_conn.recv()

    print("Sum:", results["sum"])
    print("Maximum:", results["maximum"])
    print("Minimum:", results["minimum"])

    parent_conn.close()

    process.join()