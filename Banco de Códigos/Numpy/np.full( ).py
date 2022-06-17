# Crie uma array Numpy de tamanho 10x10, preenchida com valores 128, sendo cada elemento de tipo float
array = np.full(shape = (10, 10),
                fill_value = 128,
                dtype='float')

print(array)
print(type(array[0,0]))
