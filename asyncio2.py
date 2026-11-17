import asyncio
async def student():
    print("Student started learning Python")
    await asyncio.sleep(3)
    print("Student completed learning Python")
asyncio.run(student())