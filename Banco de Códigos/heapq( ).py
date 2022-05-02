import heapq

numeros = [1, 54, 32, 101, 8, 21, 117, 99, 10, 87]

print(heapq.nlargest(5, numeros)) # retornará os 5 maiores números, do maior para o menor destes

print(heapq.nsmallest(5, numeros)) # retornará os 5 menores números, do menor para o maior destes

heapq.heapify(numeros) # retorna como primeiro elemento o menor deles, deixando o resto aleatório

heapq.heappop(numeros) # remove o menor elemento

heapq.heappush(numeros, 33) # insere o elemento 33 em uma posição aleatória

print(numeros)












