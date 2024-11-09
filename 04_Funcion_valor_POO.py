import asyncio

class Valor:

    async def obtener_dato(self):
        await self.tiempo()
        return "Dato recibido"
    
    async def tiempo(self):
        await asyncio.sleep(2)
    
    async def main(self):
        dato = await self.obtener_dato()
        print(dato)
    

valor=Valor()

asyncio.run(valor.main())   




     