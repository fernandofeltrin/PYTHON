from itertools import islice

def gerador(n):
  while True:
    yield n
    n += 1

num = gerador(0)
print(num) # Retornará apenas a instância do objeto alocado em memória

for n in islice(num, 5, 16): # num irá chamar a função gerador( ), iterando automaticamente dentro do intervalo definido, nesse caso, iniciando no número 5 até o número 15
  print(n)
