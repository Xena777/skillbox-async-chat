"""
Пример программы для работы с асинхронностью

Данные
- пользователь вводит число X

Сделать
- асинхронную функцию, которая запустится X раз
- функция должна считать от 0 до числа X
- между выводом чисел должны быть паузы по 0,5 сек
"""
import asyncio


async def print_number(x: int):
    for number in range(x):
        print(number)
        await asyncio.sleep(1)


async def start(y: int):
    queue = []

    for counter in range(y):
        queue.append(
            asyncio.create_task(print_number(y))
        )

    await asyncio.wait(queue)

asyncio.run(start(5))