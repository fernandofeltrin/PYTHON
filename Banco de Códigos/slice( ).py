lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ultimos2 = slice(-2, None) 

print(ultimos2)
print(lista1[ultimos2])

########################################

# slice( ) pode receber em justaposição três parâmetros, start, end e step
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

corte1 = slice(3, 6, None) 

print(lista1[corte1])

########################################
lista1 = [1,2,3,4,5,6,7,8,9,10]

print(lista1[:5])

fatia1 = slice(0, 5, None)

print(lista1[fatia1])

########################################
lista1 = [1,2,3,4,5,6,7,8,9,10]

comp3 = [lista1[i:i + n] for i in range(0, len(lista1), 10)]

print(comp3)

########################################
exame = 'histerossalpingografia'

print(exame[2:10])

fatia1 = slice(2, 10)

print(exame[fatia1])
