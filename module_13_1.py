import time
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    t = 1/power
    for i in range(1, 6):
        await asyncio.sleep(t)
        print(f'Силач {name} поднял шар № {i}')
    print(f'Силач {name} закончил соревнование')

async def start_tournament():
    uchast1 = asyncio.create_task(start_strongman('Pasha', 3))
    uchast2 = asyncio.create_task(start_strongman('Denis', 4))
    uchast3 = asyncio.create_task(start_strongman('Apollon', 5))
    await uchast1
    await uchast2
    await uchast3

asyncio.run(start_tournament())