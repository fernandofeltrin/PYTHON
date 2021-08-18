from itertools import combinations

lista10 = ['Ana', 'Bianca', 'Carla', 'Daniela', 'Franciele', 'Maria']

for combinacoes in combinations(lista10, 2):
  # possíveis combinações em grupos de 2
  print(combinacoes)

# A ordem não importa e não haverão combinações repetidas entre os elementos
