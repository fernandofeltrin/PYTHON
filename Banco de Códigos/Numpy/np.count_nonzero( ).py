# Gere uma array formato 6 linhas, 10 colunas com valores aleatórios distribuídos entre 0 e 1. Contabilize o número de elementos de valor 0 e exiba em tela o resultado. A array deve ser reproduzível.
np.random.seed(42)
array = np.random.randint(low=0, high=2, size=(10, 6))

print(array)
print(f'Número de ZEROS encontrados: {np.count_nonzero(array)}')
