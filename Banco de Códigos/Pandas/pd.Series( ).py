# Fornecida uma lista composta de 5 nomes/elementos em forma de string, crie uma Série a partir desta lista, exibindo em tela seu tipo de dado e conteúdo:
nomes = ['Anna', 'Fernando', 'Maria', 'Paulo', 'Tânia']

pdnomes = pd.Series(data = nomes)

print(pdnomes)
print(type(pdnomes))
