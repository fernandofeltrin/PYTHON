# Todos dados possuem um identificador interno, caso seja necessário,
# é possível descobrir o número identificador desse objeto

carros = ['Astra', 'Golf', 'Vectra']

ids = id(carros)

print(ids)
