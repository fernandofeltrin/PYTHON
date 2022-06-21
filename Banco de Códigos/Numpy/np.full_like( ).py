# Fornecida uma array Numpy de formato 3x3, composta por elementos de valores próprios, atualize os valores de todos os elementos para 5.55
array = np.array([[4.99, 3.49, 9.99],
                  [1.99, 9.99, 14.99],
                  [14.99, 2.39, 7.29]])
 
print(np.full_like(array, 5.55))
