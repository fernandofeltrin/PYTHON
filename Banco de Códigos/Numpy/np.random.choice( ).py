# Como em um resultado de loteria, sorteie 6 números aleatórios, de 1 a 50, sem que tais números se repitam e de forma que o resultado possa ser replicado
np.random.seed(42)
array = np.random.choice(range(1, 50),
                         size = 6,
                         replace = False)

print(array)
