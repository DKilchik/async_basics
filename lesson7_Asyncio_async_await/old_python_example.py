import asyncio
from time import time


async def print_num():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


def main():
    task1 = asyncio.create_task(print_num())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
