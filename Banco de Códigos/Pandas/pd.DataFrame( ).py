# Uma vez fornecido um dicionário composto de seus itens próprios, converta tal contêiner de dados em um DataFrame, em seguida adicionando uma coluna nomeada 'Preço'. Exiba em tela o conteúdo do DataFrame assim como seu tipo de dado:
estoque = {'Cel Xiaomi Redmi Note 11': 1699,
           'Cel Samsung Galaxy s22': 3999,
           'Cel Motorola Moto G200': 2999,
           'Cel LG V60 ThinQ': 1999}

pdestoque = pd.Series(data = estoque)
pdestoque = pd.DataFrame(pdestoque, columns = ['Preço'])

print(pdestoque)
print(type(pdestoque))
