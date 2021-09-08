import timeit
from threading import Thread

class Contador:
  __slots__ = ['num']
  def __init__(self):
    self.num = 100000000
    while self.num > 0:
        self.num -= 1

contagem_regressiva = Contador()

tempo3 = Thread(target = Contador)

print(f'Tempo de execução: {tempo3} segundos')

print(timeit.timeit())
