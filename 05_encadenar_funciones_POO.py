import asyncio

class Encadenar:
    async def proceso1(self):
        await self.tiempo()
        print("Proceso 1 completado")

    async def tiempo(self):
        await asyncio.sleep(1)

    async def proceso2(self):
        await self.proceso1()
        print("Proceso 2 complicado")

encadenar=Encadenar()
asyncio.run(encadenar.proceso2())   