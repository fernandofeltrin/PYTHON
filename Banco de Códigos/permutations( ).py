import itertools

for combinacao in itertools.permutations([1, 2, 3, 4]):
  print(''.join(str(x) for x in combinacao))
