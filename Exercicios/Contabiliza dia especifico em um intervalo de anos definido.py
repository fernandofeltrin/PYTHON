from datetime import datetime

segundas = 0
meses = range(1, 13)

for ano in range(2010, 2021):
    for mes in meses:
        if datetime(ano, mes, 1).weekday() == 0:
            segundas +=1

print(f'Entre 2010 e 2020 existem {segundas} segundas-feiras no primeiro dia do mês.')

