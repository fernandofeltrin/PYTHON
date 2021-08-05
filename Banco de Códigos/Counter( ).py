from collections import Counter

multiset1 = Counter(X = 3, Y = 1, Z = 5)
# Mesmo que dizer que X tem multiplicidade de instância igual a 3, Y 1 e Z 5

print(list(multiset1.elements()))

print(multiset1.elements()) # Será retornado apenas a referência do objeto alocado em memória, assim como o tipo de dado itertools.chain, uma vez que os elementos de um Multiset são encadeados sequencialmente.

print(multiset1.most_common()) # Retornará cada elemento com seu valor de multiplicidade

print(multiset1.most_common(2)) # Retornará os dois elementos com maior valor de multiplicidade
