# Supondo que temos uma array Numpy 3x3 composta de alguns valores numéricos quaisquer, "filtre" a array, modificando seus campos de valores maiores que 10 para o valor fixo 10.1
A = np.array(
    [[4.99, 3.49, 9.99],
    [1.99, 9.99, 14.99],
    [14.99, 2.39, 7.29]])
 
print(A)
print(np.where(A > 10.0, 10.1, A))
