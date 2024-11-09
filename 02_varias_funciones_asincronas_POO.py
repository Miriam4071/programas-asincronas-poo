import asyncio

class Tareas:

  async def tarea1(self):
      print("Tarea 1 completada")

  async def tarea2(self):
      print("Tarea 2 completada")
  
  async def tiempo1(self):
      await asyncio.sleep(2)

  async def tiempo2(self):
      await asyncio.sleep(1)

  async def ejecutar(self):
      await self.tiempo1()
      await self.tarea1()
      await self.tiempo2()
      await self.tarea2()


tareas=Tareas()

asyncio.run(tareas.ejecutar())    
