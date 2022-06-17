# Data uma array composta por seus próprios elementos, exiba em terminal cada um dos elementos da array separadamente, respeitando sua ordem
array = np.array([[1, 4, 3, 7],
                  [5, 2, 6, 8]])
 
for i in np.nditer(array):
    print(i)
