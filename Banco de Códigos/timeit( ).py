from timeit import timeit as t

class Pessoa(object):
  nome = 'Pessoa'
  email = 'fernando2rad@gmail.com'
  fone = '55991357259'
  casado = 'não'
  filhos = 'não'
  nacionalidade = 'brasileiro'

print(t(Pessoa, globals=globals()))

# Irá retornar o tempo em segundos que o núcleo Python levou para abrir
# e processar todo o conteúdo desse código.
