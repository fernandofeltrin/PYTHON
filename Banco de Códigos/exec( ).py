# Funcionalidade parecida com o eval( ), porém suportando duas ou mais expressões na mesma string

programa = 'n1 = 5\nn2 = 10\nprint("Resultado da soma:", n1 + n2)'
exec(programa)

# Cada linha demarcada por \n atua como separador para cada elemento e operação

# Seria o mesmo que:
# programa = 'n1 = 5,
#             n2 = 10,
#             print("Resultado da soma:", n1 + n2)'
# mas essa forma não é permitida.
