# Usando elif a partir da segunda proposição, uma proposição sendo verdadeira
# já encerra o processo naquele ponto.

num1 = float(input('Digite um número: '))

if num1 <= 49:
    print('Menor que 50')
elif num1 == 50:
    print('Igual a 50')
elif num1 >= 51 and num1 < 100:
    print('Maior que 50')
else:
    print('Número Inválido')
