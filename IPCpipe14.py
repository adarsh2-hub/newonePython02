import multiprocessing

def child_process(conn):
    student = conn.recv()

    print("\nChild received student details:")
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])

    conn.send("Student details received successfully!")
    conn.close()


if __name__ == "__main__":

    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(
        target=child_process,
        args=(child_conn,)
    )

    process.start()

    student = {
        "name": "Adarsh",
        "age": 21,
        "course": "BCA"
    }

    parent_conn.send(student)

    print("Parent sent student details.")

    message = parent_conn.recv()

    print("\nParent received:", message)

    parent_conn.close()
    child_conn.close()

    process.join()