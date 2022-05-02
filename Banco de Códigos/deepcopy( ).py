import copy

lista1 = [1,2,3,4,5,6,7,8,9,10]

lista2 = list(lista1)
print(lista2)

lista3 = copy.copy(lista1) # insere as referências dos elementos encontrados, pode gerar inconsistencias em listas muito grandes
print(lista3)

lista4 = copy.deepcopy(lista1) # insere cópias literais dos elementos encontrados da lista de origem.
print(lista4)
