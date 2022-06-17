# Dadas 4 arrays diferentes, cada uma composta de elementos próprios diversos, varifique se em cada array existe ao menos um elemento válido
# Também verifique a relação entre os elementos de mesma coluna em suas respectivas linhas, retornando caso algum dos elementos seja válido nesta comparação
A = np.array([[0, 0, 0],
              [0, 0, 0]])
 
B = np.array([[0, 0, 0],
              [0, 1, 0]])
 
C = np.array([[False, False, False],
              [True, False, False]])
 
D = np.array([[0.1, 0.0],
              [0.0, 0.2]])
 
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array)}')
    print(f'{name}: {np.any(array, axis=0)}') 
    
