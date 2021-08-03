sequencia = [11, 22, 33, 444]

pilha = []

for elemento in sequencia:
    pilha.append(elemento)

print(pilha)

pilha.append(555)
# Acrescenta como último elemento da pilha o valor 555

print(pilha)

pilha.append(1000)
pilha.append(2000)

print(pilha)

# Todos novos elementos sempre serão adicionados como último elemento da pilha
