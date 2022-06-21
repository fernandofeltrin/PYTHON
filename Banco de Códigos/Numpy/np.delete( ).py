# Uma vez que temos em mãos uma array Numpy inicialmente estruturada em 8 linhas, 4 colunas, compostas de elementos de valores próprios, atualize a array, removendo a terceira coluna da mesma.
array = np.random.randn(8, 4)
print(array)

array = np.delete(array, [2], axis=1)
print(array)
