import asyncio

class Multiples:

    async def contar(self, numero):
        await self.tiempo()
        print(f"Tarea {numero} completada")

    async def tiempo(self):
        await asyncio.sleep(1)
        
    async def main(self):
        for i in range(5):
            await self.contar(i)

multiples=Multiples()
asyncio.run(multiples.main())         