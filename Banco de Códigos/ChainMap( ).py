from collections import ChainMap
     
cozinha = {'Fogão': 470,
           'Geladeira': 1100,
           'Forno Microondas': 399}
sala = {'Sofá': 799,
        'Estante': 499}
quarto = {'Cama': 1049,
          'Roupeiro': 899,
          'Criado Mudo': 224}
banheiro = {'Pia': 459,
            'Vaso': 499,
            'Lixeira': 49}
     
x = ChainMap(cozinha, sala, quarto, banheiro)
y = input('Digite o item a ser buscado: ')

if y in cozinha.keys():
  print(f'Informação extraída a partir do dicionário "cozinha"')
  print(f'O valor de {y} é R${x[y]},00')
elif y in sala.keys():
  print(f'Informação extraída a partir do dicionário "sala"')
  print(f'O valor de {y} é R${x[y]},00')
elif y in quarto.keys():
  print(f'Informação extraída a partir do dicionário "quarto"')
  print(f'O valor de {y} é R${x[y]},00')
elif y in banheiro.keys():
  print(f'Informação extraída a partir do dicionário "banheiro"')
  print(f'O valor de {y} é R${x[y]},00')
else:
  print(f'O dado solicitado não consta em nenhum dicionário')
