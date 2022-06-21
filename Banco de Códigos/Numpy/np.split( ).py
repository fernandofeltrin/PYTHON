# Fornecida uma array Numpy estruturada em 5 linhas e 8 colunas, composta de elementos de valores próprios, crie a partir da mesma 3 novas arrays, sendo a primeira composta dos elementos das primeiras duas colunas, a segunda array composta dos elementos das próximas 4 colunas, por fim a última array composta dos elementos das duas últimas colunas da array de origem
A = np.random.randint(low=0, high=7, size=(5, 8))
print(A)
 
A1, A2, A3 = np.split(A, [2, 6], axis=1)

print(A1)
print(A2)
print(A3)
