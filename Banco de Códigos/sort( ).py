def f(crit):
  return crit['ano']

carros = [
  {'carro': 'Celta', 'ano': 2005},
  {'carro': 'Gol', 'ano': 2000},
  {'carro': 'Palio', 'ano': 2019},
  {'carro': 'Corsa', 'ano': 2011},
  {'carro': 'Fiesta', 'ano': 2009}
]

carros.sort(key=f)

print(carros)
