import time

final = 0

total = 10

print('Contagem iniciada...')

while final <= 10:
    print(total)
    time.sleep(2)
    total -= 1
    final = total
    if total == -1:
        print('Contagem encerrada!!!')
        break

