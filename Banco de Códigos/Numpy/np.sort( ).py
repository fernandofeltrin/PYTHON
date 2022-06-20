# Uma vez que temos uma array Numpy composta por [[4.99, 3.49, 9.99], [1.99, 9.99, 4.99], [14.99, 2.39, 7.29]], exiba em tela de modo crescente cada elemento de cada segmento e também cada segmento do menor para o maior de acordo com seus valores
A = np.array([[4.99, 3.49, 9.99], [1.99, 9.99, 4.99], [14.99, 2.39, 7.29]])
 
print(np.sort(A)) # ordena os elementos dentro de cada segmento
print(np.sort(A, axis=0)) # ordena os segmentos do menor para o maior de acordo com seus valores
