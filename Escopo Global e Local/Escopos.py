variavel1 = 'Paulo'
# Escopo global / no corpo geral do código, iterável por qualquer objeto

def funcao1():
    print(f'Print da variável do escopo global: {variavel1}')
  
funcao1()


def funcao2():
  variavel2 = 'Maria'
  # Escopo local / dentro do corpo da função, visível e iterável apenas de
  # dentro da função funcao2( )
  print(f'Print da variável do escopo local: {variavel2}')

funcao2()
