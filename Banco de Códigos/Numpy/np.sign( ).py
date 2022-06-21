# Dada uma array Numpy [[-4, 3, 0, 1, -5], [6, -4, -2, 1, 3]], retorne o "sinal" de cada elemento, exibindo em tela tais valores.
array = np.array([[-4, 3, 0, 1, -5], [6, -4, -2, 1, 3]])
 
print(np.sign(array)) # Função sign() retornará -1 quando for um elemento negativo, 0 quando for 0 e 1 quando for um elemento positivo
