# Com base na array Numpy [[5, 8, 16], [4, 1, 8], [-4, 4, -11]], calcule o "traço" de tal matriz (Soma dos elementos na diagonal principal).
A = np.array([[5, 8, 16], [4, 1, 8], [-4, 4, -11]])
print(A)
 
print(np.trace(A)) # 5 + 1 - 11
