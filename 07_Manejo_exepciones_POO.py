import asyncio

class Manejo:
    
  async def tarea(self):
      try:

          await self.imprimir()
          await self.tiempo()
          raise ValueError("Ocurrio un error")
      except ValueError as e:
          print(f"Exception capture: {e}")

  async def imprimir(self):
      print("Ejecutar tarea")
  
  async def tiempo(self):
      await asyncio.sleep(1)
      
manejo=Manejo()
asyncio.run(manejo.tarea())