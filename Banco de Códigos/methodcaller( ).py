from operator import methodcaller

nomes = ['Ana', 'Claudia', 'Camila', 'Débora', 'Caroline', 'Fernanda', 'Marta']

nomes_a = list(filter(methodcaller('startswith','C'), nomes)) # Methodcaller recebe como parâmetros em justaposição o nome da função, seguido de seu(s) parâmetro(s). Nesse caso, reduzimos ainda mais o código substituindo a função lambda pelo methodcaller( )

print(nomes_a)
