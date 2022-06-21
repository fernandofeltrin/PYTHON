# Crie duas imagens ruído de tamanho 300x300 pixels em 3 canais de cor, adicione uma dimensão para cada imagem transformando-a em uma matriz de voxels. Crie uma nova imagem ruído a partir das duas geradas anteriormente
imagem1 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
imagem2 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
 
imagem1 = np.expand_dims(imagem1, axis=0)
imagem2 = np.expand_dims(imagem2, axis=0)
 
imagem3 = np.append(imagem1, imagem2, axis=0)

print(imagem3)
print(imagem3.shape)
