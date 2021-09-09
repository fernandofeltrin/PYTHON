from fnmatch import fnmatchcase

nome = 'fernando'

fnmatchcase(nome, 'Fernando') # Retornará False pois fnmatchcase usa da regra Case Sensitive
