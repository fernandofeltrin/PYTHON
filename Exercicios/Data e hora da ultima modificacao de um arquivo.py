import os
import time

def ultima_modificacao(arquivo):
    status = os.stat(arquivo)
    data = time.localtime((status.st_mtime))
    ano = data[0]
    mes = data[1]
    dia = data[2]
    hora = data[3]
    minuto = data[4]
    segundo = data[5]

    str_ano = str(ano)[0:]

    if (mes <= 9):
        str_mes = '0' + str(mes)
    else:
        str_mes = str(mes)

    if (dia <= 9):
        str_dia = '0' + str(dia)
    else:
        str_dia = str(dia)
    
    return (str_dia + '-' + str_mes + '-' + str_ano + ' / ' + str(hora) + ':' + str(minuto) + ':' + str(segundo))
    
print('Ultima modificação realizada em: ', ultima_modificacao('testes.txt'))
