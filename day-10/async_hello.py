import asyncio
import time

async def say_after(delay, what):
    print(f"Sleeping for {delay} seconds...")
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())