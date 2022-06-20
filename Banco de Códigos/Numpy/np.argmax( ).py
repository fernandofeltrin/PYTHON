# Dada uma array numpy 3x3 composta por alguns valores decimais, retorne para cada linha a posição de índice a qual consta o elemento de maior valor
A = np.array([[0.4, 0.3, 0.1],
              [0.1, 0.1, 0.8],
              [0.2, 0.5, 0.3]])
 
print(np.argmax(A, axis=1))
