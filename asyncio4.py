import asyncio
async def download():
    await asyncio.sleep(3)
    print("Download started.")
    print("Download completed.")
async def main():
    task=asyncio.create_task(download())
    print("Main function is running.")
    await task
asyncio.run(download())