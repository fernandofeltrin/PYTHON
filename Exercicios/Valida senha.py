import re

senha = input('Insira sua nova senha: ')
x = True

while x:
    if (len(senha) < 6 or len (senha) > 16):
        print('A senha deve conter entre 6 e 16 caracteres')
        break
    elif not re.search("[a-z]", senha):
        print('A senha deve ter ao menos uma letra minúscula')
        break
    elif not re.search("[0-9]", senha):
        print('A senha deve conter ao menos um número')
        break
    elif not re.search("[A-Z]", senha):
        print('A senha deve conter ao menos uma letra maiúscula')
        break
    elif not re.search("[$#@*!&]", senha):
        print('A senha deve conter ao menos um caractere especial')
        break
    elif re.search("\s", senha):
        break
    else:
        print('Senha cadastrada com sucesso!!!')
        x = False
        break

if x:
    print('Senha inválida!!!')

