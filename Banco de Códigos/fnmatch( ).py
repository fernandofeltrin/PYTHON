# Usado para verificar certas correspondências em strings

from fnmatch import fnmatch

arquivo = 'c:/Users/Fernando/Documentos/arquivo.txt'

fnmatch(arquivo, '*.txt') # Verifica se existe qualquer coisa na string que termine em .txt
