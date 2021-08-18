# Abre um arquivo, possibilitando manipular o mesmo diretamente via código

arquivo1 = open('pareceres.txt', 'r')

print(arquivo1.read())

##########################################################################

# Modos de leitura de arquivo:

'r' - apenas leitura
'w' - leitura e escrita
't' - abre um arquivo em formato apenas texto
'b' - abre um arquivo em seu modo binário
'x' - cria no diretório um arquivo
