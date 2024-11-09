import asyncio

class Limitacion:

    async def tarea(self):
        print("Comienza tarea")
        await self.tiempo()

    async def tiempo(self):
        await asyncio.sleep(5)

    async def main(self):
        try:
            await asyncio.wait_for(self.tarea(),timeout=3)
        except asyncio.TimeoutError:
            print("Tarea excedió el tiempo de espera")

limitacion=Limitacion()
asyncio.run(limitacion.main())    