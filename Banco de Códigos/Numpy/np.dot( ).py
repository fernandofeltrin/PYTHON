# Providas duas arrays Numpy A e B, compostas de elementos de valores próprios, calcule e exiba em tela o produto escalar de A sobre B.
A = np.array([[2, 3], [-4, 2], [5, 0]])
B = np.array([[4, 3, 2], [-1, 0, 2]])
 
print(np.dot(A, B))
# Mesmo que: A.dot(B)
