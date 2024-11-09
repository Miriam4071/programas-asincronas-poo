import asyncio

async def tarea1():
    await asyncio.sleep(2)
    print("Tarea 1 completada")

async def tarea2():
    await asyncio.sleep(1)
    print("Tarea 2 completada")


async def ejecutar():
    await asyncio.gather(tarea1(), tarea2()) 


asyncio.run(ejecutar())




    