estoque = [
    {'Item01': 'Camisa Nike', 'Preco':39.90},
    {'Item02': 'Camisa Adidas', 'Preco':37.90},
    {'Item03': 'Moletom 00', 'Preco':79.90},
    {'Item04': 'Calca Jeans', 'Preco': 69.90},
    {'Item05': 'Tenis AllStar', 'Preco': 59.90}
]

precos04 = list(filter(lambda p: p['Preco'] >= 60, estoque))
# Precisa especificar um parâmetro a ser filtrado, nesse caso, "filtrando"
# apenas os valores da chave 'Preco' cujo valor seja igual ou maior que 60

print(f'Preços de estoque (Filter) {precos04}')
