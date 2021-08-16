def gerador():
  for i in range(100):
    yield i # Quando usado no lugar de return, irá ter comportamento de um gerador, retornando um dado/valor por iteração

numero = gerador()

print(numero) # Retornará um generator object

print(next(numero)) # Retornará o número gerado pela função, a contar desde 0 até 99, sequencialmente
