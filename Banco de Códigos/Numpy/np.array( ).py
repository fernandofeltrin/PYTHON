# Dada uma matriz inicial 5x5 com elementos entre 20 e 45, gere uma nova matriz contendo apenas elementos a partir da terceira linha e segunda coluna
'''
[20, 21, 22, 23, 24],
[25, 26, 27, 28, 29],
[30, 31, 32, 33, 34],
[35, 36, 37, 38, 39],
[40, 41, 42, 43, 44]
'''
a = np.array([[20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29],
              [30, 31, 32, 33, 34],
              [35, 36, 37, 38, 39],
              [40, 41, 42, 43, 44]])

array = a[2:, 1:]

print(array)
