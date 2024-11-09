import asyncio

class Usar:

    async def tarea(self,numero):
        await self.tiempo()
        print(f"Tarea {numero} completada")
    
    async def tiempo(self):
        await asyncio.sleep(2)

    async def main(self):
        tareas=[]
        for i in range(3):
            
            tareas.append(asyncio.create_task(self.tarea(i)))
            
            await asyncio.gather(*tareas)

usar=Usar()
asyncio.run(usar.main())