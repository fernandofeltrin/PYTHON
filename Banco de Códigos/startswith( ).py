nomes = ['Ana', 'Claudia', 'Camila', 'Débora', 'Caroline', 'Fernanda', 'Marta']

nomes_a = list(filter(lambda x: x.startswith('C'), nomes)) # Após percorrer cada elemento da lista, retornará apenas os que começarem com 'C'

print(nomes_a)
