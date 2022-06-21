# Supondo que em uma estrutura de código temos uma array Numpy [[[1, 2, 3], [6, 3, 2]]], formato (1,2,3), reduza uma dimensão desta array tornando-a uma array formato (2,3)
array = np.array([[[1, 2, 3], [6, 3, 2]]])
print(array.shape)

array = np.squeeze(array)
print(array.shape)
