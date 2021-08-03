from collections import OrderedDict

dicionario = OrderedDict()
dicionario['a'] = 1
dicionario['b'] = 2
dicionario['c'] = 3
dicionario['d'] = 4
dicionario['e'] = 5
print(dicionario)

for k, v in dicionario.items():
    print(k, v)

# Internamente é gerado um mapeamento da ordem aos quais os itens foram inseridos
# Caso uma nova entrada tente atualizar uma chave:valor do dicionário, a posição
# original é mantida, esse log de alterações pode ser visualizado via MyPy.
