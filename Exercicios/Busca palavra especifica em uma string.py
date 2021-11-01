texto = 'Python é uma excelente linguagem de programação!!!'

pesquisa = input('Digite uma palavra a ser pesquisada: ')

if (texto.find(pesquisa) == -1):
    print(f'Palavra "{pesquisa}" não encontrada no texto de origem.')
else:
    print(f'Palavra "{pesquisa}" é uma das palavras do texto de origem')
