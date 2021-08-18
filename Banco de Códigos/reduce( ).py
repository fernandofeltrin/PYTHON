estoque = [
    {'Item01': 'Camisa Nike', 'Preco':39.90},
    {'Item02': 'Camisa Adidas', 'Preco':37.90},
    {'Item03': 'Moletom 00', 'Preco':79.90},
    {'Item04': 'Calca Jeans', 'Preco': 69.90},
    {'Item05': 'Tenis AllStar', 'Preco': 59.90}
]

from functools import reduce

def func_reduce(soma, valores):
    return soma + valores['Preco']

precos_total = reduce(func_reduce, estoque, 0)
# reduce( ) recebe como parâmetros uma função, um objeto origem e um valor inicial

print(f'Soma dos Preços (Reduce) {precos_total}')
