import asyncio
async def my_task():
    print("Task started")
    await asyncio.sleep(2)
    print("Task completed")
asyncio.run(my_task())