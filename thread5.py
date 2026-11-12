import threading,time
def download_file():
    print("Download file...")
    time.sleep(5)
    print("Download completed!")
t=threading.Thread(target=download_file)
t.start()
t.join()