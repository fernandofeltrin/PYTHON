# Basicamente a mesma lógica implementada de list comprehension,
# mas quando temos chave:valor podemos transormar em dicionário.

lista = [('chave1','chave2'), ('chave2','valor2'),('chave3','valor3')]

dicionario = {x:y for x, y in lista}
# Mesmo que dicionario = dict(lista)

print(dicionario)
