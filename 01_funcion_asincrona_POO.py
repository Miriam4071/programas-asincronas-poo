import asyncio

class Saludos:
    
    async def saludar(self):
      await self.tiempo()
      await self.imprimir()


    async def imprimir(self):
       print(f"Hola de forma asincrona")  
   
    async def tiempo(self):
      await asyncio.sleep(1)


saludos=Saludos()

asyncio.run(saludos.saludar())


