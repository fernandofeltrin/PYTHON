# Crie uma array Numpy de 3 linhas e 4 colunas, com números sequenciais até 12. Salve tal array em um arquivo de texto nomeado array.txt. Carregue a array contida no arquivo array.txt, atribuindo a mesma para uma nova variável. Exiba em tela o conteúdo da array.
A = np.arange(12, dtype = 'int').reshape(-1, 4)
np.savetxt(fname = 'array.txt',
           X = A,
           fmt = '%0.2f')
 
B = np.loadtxt('array.txt')
print(B)
