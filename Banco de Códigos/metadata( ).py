from importlib import metadata

versao_numpy = metadata.version('numpy')

print(versao_numpy)

metadados_numpy = metadata.metadata('numpy')

print(list(metadados_numpy))
print(metadados_numpy)

print(metadados_numpy['Maintainer-email'])
