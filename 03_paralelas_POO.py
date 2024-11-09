import asyncio

class Paralela:

    async def tarea1(self):
        print("Tarea 1 completada")

    async def tarea2(self):
        print("Tarea 2 completada")

    async def tiempo1(self):
        await asyncio.sleep(2)
    
    async def tiempo2(self):
        await asyncio.sleep(1)

    async def ejecutar(self):
        await asyncio.gather(self.tiempo1(),self.tarea1()) 
        await asyncio.gather(self.tiempo2(), self.tarea2()) 

paralela=Paralela()
asyncio.run(paralela.ejecutar())
