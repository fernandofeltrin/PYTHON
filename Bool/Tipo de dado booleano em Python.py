# Quase todo tipo de dado/valor válido será True quando verificado

# Qualquer string é True, exceto strings vazias

print(bool('Fernando'))

print(bool(''))

# Qualquer número é True, com exceção do 0

print(bool(1987))

print(bool(0))

# Qualquer lista, tupla, set ou dicionário é True, exceto quando vazios

nomes = ['Ana', 'Carolina', 'Jéssica']

print(bool(nomes))

lista = []

print(bool(lista))
