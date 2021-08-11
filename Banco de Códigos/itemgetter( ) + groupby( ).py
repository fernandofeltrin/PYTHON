from operator import itemgetter
from itertools import groupby

usuarios = [('Ana', 16),
            ('Carlos', 26),
            ('Pedro', 4),
            ('Maria', 10),
            ('Ana', 30),
            ('Eder', 44),
            ('Tania', 45)]

print(usuarios)

usuarios.sort(key = itemgetter(0))

print(usuarios)

print({key: sorted(map(itemgetter(1), value)) for key,
       value in groupby(usuarios, key = itemgetter(0))})
