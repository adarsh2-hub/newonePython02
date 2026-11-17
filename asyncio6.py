import asyncio

async def task1():
    print("Downloading file...")
    await asyncio.sleep(2)
    print("File downloaded!")

async def task2():
    print("Processing data...")
    await asyncio.sleep(3)
    print("Data processing completed!")

async def main():
    await asyncio.gather(task1(), task2())
    print("All tasks completed!")

asyncio.run(main())