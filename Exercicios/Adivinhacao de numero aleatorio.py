import random

num_gerado, num_adivinhado = random.randint(0, 11), 0

while num_adivinhado != num_gerado:
    num_adivinhado = int(input('Digite um número entre 0 e 10: '))

print('Parabéns, você adivinhou o número!!!')

print(f'Número gerado: {num_gerado}')

