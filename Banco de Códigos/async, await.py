import asyncio

async def minha_funcao():
  print('Hello')
  await asyncio.sleep(1)
  print('world')

  
# Rodar o programa com:
asyncio.run(minhafuncao())
