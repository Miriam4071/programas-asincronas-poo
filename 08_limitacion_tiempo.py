import asyncio


async def tarea():
    print("Comienza tarea")
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(tarea(),timeout=3)
    except asyncio.TimeoutError:
        print("Tarea excedió el tiempo de espera")

asyncio.run(main())    