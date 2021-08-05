import itertools

lista1 = [2,4,6,8,10]
lista2 = [1,3,5,7,9]

lista3 = itertools.chain(lista1, lista2)

print(lista3)
print(list(lista3))


########################################

lista1 = [2,4,6,8,10]
lista2 = [1,3,5,7,9]
listax = ['a', 'b', 'c', 'd', 'e']

listas = itertools.chain(listax, lista1, lista2)

print(list(listas))
