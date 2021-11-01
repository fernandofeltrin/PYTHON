def minha_funcao():
    x = 1
    y = 2
    nome = 'Tania'
    lista = []
    print(f'{x}, {y}')
    print(f'{nome}')
    print(f'{lista}')

print(minha_funcao())

var_locais = minha_funcao.__code__.co_nlocals

print(f'A função {minha_funcao} possui {var_locais} variáveis')
