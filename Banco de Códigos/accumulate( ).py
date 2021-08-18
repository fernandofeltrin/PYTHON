# Como acumulação entenda-se a soma dos elementos subsequentes

from itertools import accumulate

acumula = accumulate([1,2,3,4])

print(list(acumula))
# Retornará o equivalente a (1) no índice 0, (1 + 2) no índice 1, (1 + 2 + 3)
# no índice 2 e (1 + 2 + 3 + 4) no índice 3 da lista retornada.
