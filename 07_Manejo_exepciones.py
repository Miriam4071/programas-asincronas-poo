import asyncio

async def tarea():
    try:

        print("Ejecutar tarea")
        await asyncio.sleep(1)
        raise ValueError("Ocurrio un error")
    except ValueError as e:
        print(f"Exception capture: {e}")


asyncio.run(tarea())