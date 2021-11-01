lista1 = [-1, 6, -9, -8, 4, 0, -3, 2, 7, 1, 8, -2]

print(f'Lista original: {lista1}')

lista2 = [x for x in lista1 if x < 0] + [x for x in lista1 if x >= 0]

print(f'Lista rearranjada: {lista2}')
