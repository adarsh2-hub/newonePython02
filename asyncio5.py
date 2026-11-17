import asyncio

async def long_task():
    print("Task started")
    await asyncio.sleep(5)
    print("Task completed")

async def main():
    try:
        await asyncio.wait_for(long_task(), timeout=2)

    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(main())