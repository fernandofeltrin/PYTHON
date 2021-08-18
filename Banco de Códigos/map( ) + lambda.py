# map( ) permite aplicar uma função individualmente sobre cada elemento de um
# contêiner de dados.

estoque = [
    {'Item01': 'Camisa Nike', 'Preco':39.90},
    {'Item02': 'Camisa Adidas', 'Preco':37.90},
    {'Item03': 'Moletom 00', 'Preco':79.90},
    {'Item04': 'Calca Jeans', 'Preco': 69.90},
    {'Item05': 'Tenis AllStar', 'Preco': 59.90}
]

precos02 = list(map(lambda p: p['Preco'], estoque))
# map( ) percorrendo cada elemento de estoque, retornando a cada laço
# especificamente o valor de 'Preco', retornando esses valores em forma
# de lista

print(f'Preços de estoque (Map + Lambda) {precos02}')
