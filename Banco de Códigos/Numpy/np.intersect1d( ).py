# Dadas duas arrays Numpy, uma composta de elementos válidos entre 0 a 8 distribuídos em uma matriz de 4 colunas e outra array de mesmo formato composta de números aleatórios, exiba em tela uma lista contendo os elementos que são comuns as duas arrays
A = np.arange(8).reshape(-1, 4)
B = np.array([[9, 10, 11, 3],
              [2, 8, 0, 9]])
print(A)
print(B)
print(np.intersect1d(A, B))
