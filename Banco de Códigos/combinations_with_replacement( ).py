# Forma alternativa de combinations, permitindo a repetição de elementos

from itertools import combinations_with_replacement

combina = combinations_with_replacement([1, 2, 3, 4], 2)

print(list(combina))
