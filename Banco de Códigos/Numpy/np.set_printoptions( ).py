# Gere uma array Numpy de 4 linhas, 10 colunas, composta de elementos de valores aleatórios. Defina o número de casas decimais como 5 para cada um dos elementos.
array = np.random.randn(10, 4)
np.set_printoptions(precision=5)

print(array)
