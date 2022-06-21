# Supondo que temos uma lista convertida para uma array, onde em sua estrutura temos pares de elementos representando um identificador de um produto e um preço, exiba em tela tal array, porém apenas com os pares de elementos referentes aos produtos aleatoriamente distribuídos. O resultado deve ser replicável.
np.random.seed(42)
array = np.array([['ID', 'preço'],
                  ['001', 14.99],
                  ['002', 4.99],
                  ['003', 7.99],
                  ['004', 2.49],
                  ['005', 1.49]])
 
np.random.shuffle(array[1:])

print(array)
