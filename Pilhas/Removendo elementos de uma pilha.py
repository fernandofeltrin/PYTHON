sequencia = [11, 22, 33, 444, 555]

pilha = []

for elemento in sequencia:
    pilha.append(elemento)

print(pilha)

pilha.pop()
# Mesmo sem parâmetros, removerá o último elemento da pilha

print(pilha)
