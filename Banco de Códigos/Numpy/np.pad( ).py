# Dada uma array inicial de tamanho 4x4, composta inteiramente por elementos de valor 1, insira uma camada de elementos de valor 0 acima, abaixo, à esquerda e à direita da array inicial, "encapsulando" a mesma.

A = np.ones(shape = (4, 4))

print(A)

print(np.pad(A, pad_width = 1,
             constant_values = 0))
