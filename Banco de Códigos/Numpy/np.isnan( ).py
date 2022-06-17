# Dada uma array Numpy composta por alguns elementos próprios, verifique cada um dos elementos de sua composição, retornando True para cada elemento que não for de tipo numérico
     
A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])
     
print(np.isnan(A))
