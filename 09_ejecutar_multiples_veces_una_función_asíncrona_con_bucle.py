import asyncio

async def contar(numero):
    await asyncio.sleep(1)
    print(f"Tarea {numero} completada")
    
async def main():
    for i in range(5):
        await contar(i)

asyncio.run(main())         