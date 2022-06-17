# Crie uma array de formato 5x5, composta de números sequenciais a partir de 20. Salve a array para um arquivo nomeado array.npy. Carregue a array contida no arquivo array.npy, atribuindo a mesma para uma nova variável. Por fim, exiba em tela o conteúdo da array.
A = np.arange(20,45).reshape(5,5)
np.save('array.npy', A)
 
B = np.load('array.npy')
print(B)
