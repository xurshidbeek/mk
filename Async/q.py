import asyncio
import time
import datetime

async def main():
    await asyncio.sleep(11)
    print("Hello World")

async def main2():
    await asyncio.sleep(21)
    print("Hello World 2 ")

async def main3():
    await asyncio.sleep(51)
    print("Hello World 3 ")
    await main2()



async def main4():
    await asyncio.sleep(6)
    print("Hello World 4 ")
    await main3()

async def main5():
    await asyncio.sleep(3)
    print("Hello World 5 ")
    await main()

async def main6():
    await asyncio.sleep(4)
    print("Hello World 6 ")

async def main7():
    await asyncio.sleep(5)
    print("Hello World 7 ")
    await main6()

async def main8():
    await asyncio.sleep(6)
    print("Hello World 8 ")
    await main4()


async def x():
    await asyncio.gather(main(), main2(), main3(), main4(), main5(), main6(), main7(), main8())
    print("Done")


if __name__ == "__main__":
    print(datetime.datetime.now())
    asyncio.run(x())
    print(datetime.datetime.now())
