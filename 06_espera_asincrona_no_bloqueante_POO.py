import asyncio

class Espera:

    async def inicio_tarea(self):
        print("Inicio de la tarea")

    async def tiempo(self):
        await asyncio.sleep(3)
    
    async def fin_tarea(self):
        print("Fin de la tarea")

    async def main(self):
         await self.inicio_tarea()
         await self.tiempo()
         await self.fin_tarea()

espera=Espera()
asyncio.run(espera.main())