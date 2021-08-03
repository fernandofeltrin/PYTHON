from collections import defaultdict

dicionario2 = defaultdict(list) # Define que o retorno deste dicionário sempre será em forma de lista

print(dicionario2) # Retornará <class 'list'>, {} pois o objeto gerado (mesmo que vazio) é uma lista dentro de um dicionário
print(type(dicionario2)) # Retornará <class 'collections.defaultdict'>

dicionario2['Nomes'].append('Ana')
dicionario2['Nomes'].append('Gabriella')
dicionario2['Nomes'].append('Pedro')
dicionario2['Nomes'].append('Gabriella')
dicionario2['Nomes'].append('Maria')
dicionario2['Nomes'].append('Rafael')
dicionario2['Nomes'].append('Gabriella')

print(dicionario2)

dicionario3 = defaultdict(set) # Criando um dicionário padrão especificando que seus elementos estarão no formato set, ao tentar inserir elementos de mesmo valor os mesmos serão ignorados
dicionario3['Nomes'].add('Ana')
dicionario3['Nomes'].add('Gabriella')
dicionario3['Nomes'].add('Pedro')
dicionario3['Nomes'].add('Gabriella')
dicionario3['Nomes'].add('Maria')
dicionario3['Nomes'].add('Rafael')
dicionario3['Nomes'].add('Gabriella')

print(dicionario3)
