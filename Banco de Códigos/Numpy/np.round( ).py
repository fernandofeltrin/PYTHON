# Gere uma array Numpy estruturada em 10 linhas, 8 colunas, composta por elementos de valores aleatórios. Com base da primeira array, crie uma segunda array baseada na primeira, porém com valores arredondados em duas casas decimais
A = np.random.randn(10, 8)
B = np.round(A, decimals=2)
 
print(A)
print(B)
