inventario = {'Samgung J6':500,
              'Redmi Note9':1100,
              'iPhone 8':2200,
              'PocoPhone X3':1200}

menor_preco = min(zip(inventario.values(), inventario.keys()))
print(menor_preco)

maior_preco = max(zip(inventario.values(), inventario.keys()))
print(maior_preco)
