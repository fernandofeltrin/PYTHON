# Útil para iterar isoladamente desmembrando elementos de uma tupla/lista/dicionário

cidades = iter(['Curitiba', 'Brasília', 'Florianópolis'])

cidade1 = next(cidades)
# Retornará o primeiro elemento isoladamente
print(cidade1)

cidade2 = next(cidades)
# next() retornará o segundo elemento, e assim por diante, até o número total de elementos
print(cidade2)

cidade3 = next(cidades)
print(cidade3)
