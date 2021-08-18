from timeit import timeit as t
from collections import namedtuple

Pessoa = namedtuple('Pessoa', 'nome email fone casado filhos nacionalidade')

pessoa1 = Pessoa('Pessoa',
                 'fernando2rad@gmail.com',
                 '55991357259',
                 'não',
                 'não',
                 'brasileiro')

print(t(pessoa1.nome, globals=globals()))
# Irá retornar o tempo em segundos que o núcleo Python levou para abrir
# e processar todo o conteúdo desse código.
