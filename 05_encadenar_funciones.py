import asyncio


async def proceso1():
    await asyncio.sleep(1)
    print("Proceso 1 completado")

async def proceso2():
    await proceso1()
    print("Proceso 2 complicado")

asyncio.run(proceso2())        