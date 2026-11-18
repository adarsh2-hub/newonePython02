import asyncio
async def task():
    print("My name is Adarsh..")
async def task2():
    print("I am learning Python Language..")
    await asyncio.sleep(5)
async def main():
    await asyncio.gather(task(),task2())
    print("All the tasks are completed")
asyncio.run(main())