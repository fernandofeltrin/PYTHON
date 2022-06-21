# Fornecidas duas arrays Numpy, calcule a média aritmética entre as mesmas, atribuindo os valores retornados a uma nova array.
A = np.array([[3, 4, 9, 2], [5, 3, 2, 5]])
B = np.array([[4, 3, 2, 5], [6, 3, 1, 6]])

media = np.divide(np.add(A, B), 2)
# mesmo que: (A + B) / 2
print(media)
