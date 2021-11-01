import collections

c1 = (2, 4, 6, 8, 10)
dq1 = collections.deque(c1)

c2 = (2, 4, 6, 8, 10)
dq2 = collections.deque(c2)

dq3 = dq2

print(f'Conjunto 1: {dq1}')
print(f'Endereço de Conjunto 1: {id(dq1)}')

print(f'Conjunto 2: {dq2}')
print(f'Endereço de Conjunto 2: {id(dq2)}')

print(f'Conjunto 3: {dq3}')
print(f'Endereço de Conjunto 3: {id(dq3)}')

if (dq1 == dq2) and (id(dq1) == id(dq2)):
    print('Conjunto 1 e Conjunto 2 possuem os mesmos elementos e são o mesmo objeto alocado em memória')
if (dq1 == dq3) and (id(dq1) == id(dq3)):
    print('Conjunto 1 e Conjunto 3 possuem os mesmos elementos e são o mesmo objeto alocado em memória')
if (dq2 == dq3) and (id(dq2) == id(dq3)):
    print('Conjunto 2 e Conjunto 3 possuem os mesmos elementos e são o mesmo objeto alocado em memória')

if (dq1 == dq2) and (id(dq1) != id(dq2)):
    print('Conjunto 1 e Conjunto 2 possuem os mesmos elementos, porém são objetos diferentes alocados em memória')
if (dq1 == dq3) and (id(dq1) != id(dq3)):
    print('Conjunto 1 e Conjunto 3 possuem os mesmos elementos, porém são objetos diferentes alocados em memória')
if (dq2 == dq3) and (id(dq2) != id(dq3)):
    print('Conjunto 2 e Conjunto 3 possuem os mesmos elementos, porém são objetos diferentes alocados em memória')
