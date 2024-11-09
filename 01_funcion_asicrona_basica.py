import asyncio

async def saludo():
    await asyncio.sleep(1)
    print("Hola de forma asincrona!")


asyncio.run(saludo())
