# Uma vez que temos em mãos uma array Numpy (2x3) composta por elementos de valores próprios, adicione uma nova dimensão a essa array, alterando seu formato para (1,2,3)
array = np.array([[4, 2, 1],
                  [6, 4, 2]])
print(array)

array = np.expand_dims(array, axis=0)
print(array)
