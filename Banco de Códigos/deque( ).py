from collections import deque

fila1 = deque(maxlen = 5) # Parâmetro maxlen define um tamanho máximo para a fila

fila1.append(1)
fila1.append(2)
fila1.append(3)
fila1.append(4)
fila1.append(5)

print(fila1)
print(type(fila1))
