import asyncio

async def tarea(numero):
    await asyncio.sleep(2)
    print(f"Tarea {numero} completada")

async def main():
    tareas=[]
    for i in range(3):
        
        tareas.append(asyncio.create_task(tarea(i)))

    await asyncio.gather(*tareas)
asyncio.run(main())