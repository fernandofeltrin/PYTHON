# Generalizando o exemplo anterior, apenas verifique se o conteúdo da variável A é igual ao de B
A = np.array([0.4, 0.5])
B = np.array([0.39999999, 0.5000001])

print(A == B)
print(np.equal(A, B))
