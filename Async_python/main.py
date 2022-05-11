import asyncio
async def main():

    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    # await other_function()

    print("B")
    await task


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("1")
asyncio.run(main())