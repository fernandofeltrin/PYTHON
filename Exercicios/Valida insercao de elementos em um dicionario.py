clientes = {'Fernando' : '991357259',
            'Alberto' : '981120491'}

novo_cliente = input('Digite o nome do cliente: ')

if novo_cliente in clientes.keys():
    print(f'{novo_cliente} já existe na base de dados')
    novo_cliente = input('Digite o nome do cliente: ')
else:
    print(f'{novo_cliente} não está cadastrado.')
    print('Digite novamente o nome a ser cadastrado: ')
    nome = input('Digite o nome: ')
    telefone = str(input('Digite o telefone: '))
    clientes.__setitem__(nome, telefone)

print(clientes)
