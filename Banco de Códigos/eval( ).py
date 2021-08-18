# Avalia uma expressão fora de contexto, normalmente em formato de string,
# e caso essa expressão seja válida executa a expressão mesmo fora de contexto.

variavel = 'print(99)'
# Em forma de string existe uma função com parâmetro

print(variavel)

print(eval(variavel))
# Executará a função identificada na string de variavel
