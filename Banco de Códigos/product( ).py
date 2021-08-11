import itertools

lista1 = [1, 2, 3, 4]
lista2 = ['x', 'y']

for num in itertools.product(lista1, lista2):
  print(num)
