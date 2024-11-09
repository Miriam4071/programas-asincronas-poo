import asyncio

async def tarea():
    print("Inicio de la tarea")
    await asyncio.sleep(3)
    print("Fin de la tarea")

asyncio.run(tarea())