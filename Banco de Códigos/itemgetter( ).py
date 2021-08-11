from operator import itemgetter

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
