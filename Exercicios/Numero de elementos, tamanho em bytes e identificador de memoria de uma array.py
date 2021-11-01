from array import *

lista1 = array('i', [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])

print(f'lista1 é composta de {len(lista1)} elementos')

print(f'lista1 possui um tamanho de {lista1.itemsize} bytes')

print(f'lista1 está alocada na memória no endereço: {lista1.buffer_info()[0]}')
