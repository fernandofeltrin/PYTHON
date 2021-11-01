texto = input('Digite um texto: ')

maiusculas = 0
minusculas = 0

for letra in texto:
    if (letra .islower()):
        minusculas += 1
    elif (letra.isupper()):
        maiusculas += 1

print(f'No texto {texto} foram encontradas {maiusculas} letras maiúsculas')

print(f'No texto {texto} foram encontradas {minusculas} letras minúsculas')

