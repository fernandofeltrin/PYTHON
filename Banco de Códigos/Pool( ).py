# Utiliza multi-processing ao invés de multi-threading

# Em outras palavras, cada processo ganha seu próprio interpretador
# Python e espaço dedicado em memória, como em computação paralela.

from multiprocessing import Pool
import time

contador = 100000000

def contagem_regressiva(num):
    while num > 0:
        num -= 1

if __name__ == '__main__':
  pool = Pool(processes = 4) # número de threads independentes
  inicio = time.time()
  tempo = pool.apply_async(contagem_regressiva, [contador//2])
  pool.close()
  pool.join()
  fim = time.time()
  print(f'Tempo de execução: {fim - inicio}')
