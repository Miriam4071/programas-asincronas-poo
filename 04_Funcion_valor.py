import asyncio


async def obtener_dato():
    await asyncio.sleep(2)
    return "Dato recibido"


async def main():
    dato = await obtener_dato()
    print(dato)


asyncio.run(main())        