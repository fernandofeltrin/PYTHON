# Mesmas funcionalidades de um dicionário padrão, porém caso o usuário tente
# consultar uma entrada inexistente, ao invés de um erro é retornado um valor padrão

from collections import defaultdict

dicionario = defaultdict(int)
dicionario['Ano'] = 2021
dicionario['Mês'] = 5

print(dicionario.items())
print(dicionario['Dia'])
# Retornará 0 no lugar de uma exceção
