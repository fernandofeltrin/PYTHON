# import datetime

from datetime import datetime, date, time

data = datetime(2020, 6, 12, 15, 24, 59)
# Por justaposição, os parâmetros estarão como:
# ano, mês, dia, hora, minuto, segundo

print(data.date())
print(data.time())

print(data.year)
print(data.month)
print(data.day)

print(data.hour)
print(data.minute)
print(data.second)
