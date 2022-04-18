endereco = ''

while ((endereco.startswith('www.') and endereco.endswith('.com.br'))) != True:
    endereco = input('Digite o endereço do site: ')

print(f'{endereco} é um endereço válido.')
