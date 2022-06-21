# Fornecidas 3 arrays Numpy unidimensionais compostas por elementos de valores próprios, crie uma nova array a partir do empilhamento das 3 arrays anteriores
a1 = np.array([1.6, 0.9, 2.2])
a2 = np.array([0.4, 1.3, 3.2])
a3 = np.array([1.4, 0.3, 1.2])

pilha = np.column_stack((a1, a2, a3))
 
print(pilha)
