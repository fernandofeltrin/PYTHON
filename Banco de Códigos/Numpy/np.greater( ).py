# Verifique se os valores dos elementos de A são maiores do que os valores dos elementos de B
A = np.array([0.4, 0.5])
B = np.array([0.39999999, 0.5000001])

print(A > B)
print(np.greater(A, B))
