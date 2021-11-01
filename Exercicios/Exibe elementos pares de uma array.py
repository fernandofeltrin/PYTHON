from array import *

numeros = array('i', [5, 10, 15, 20, 25])

for i in numeros:
    print(i)
    if i % 2 == 0:
        print(f'{i} é um número par')

