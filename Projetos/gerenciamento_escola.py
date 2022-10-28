import sys

class Escola:
  def __init__(self,
               nome_aluno = '',
               nome_pai = '',
               nome_mae = '',
               telefone = '',
               logradouro = '',
               outros = ''):
    
    self.nome_aluno = nome_aluno
    self.nome_pai = nome_pai
    self.nome_mae = nome_mae
    self.telefone = telefone
    self.logradouro = logradouro
    self.outros = outros

    self.curso = ''
    self.turma = []
    self.turma_num = 1
    self.materias = ['','','','','']
    self.notas = [0,0,0,0]
    self.conceito_final = ''

    self.n = 0
    self.base = {}
  
  def matricula(self):
    self.nome_aluno = input('Digite o nome completo do aluno: ').upper()
    self.nome_pai = input('Digite o nome do pai: ').upper()
    self.nome_mae = input('Digite o nome da mãe: ').upper()
    self.telefone = input('Digite um telefone para contato: ')
    self.logradouro = input('Digite o endereço residencial: ').upper()
    self.outros = input('Digite as observações (caso houver): ').upper()

    print(f'Aluno {self.nome_aluno} matriculado com sucesso \n')

    self.turma.append(self.nome_aluno)
    self.n += 1

  def cadastra_curso(self):
    print('Digite o curso: ')
    print('1 - Ensino Médio - 1º Ano')
    print('2 - Ensino Médio - 2º Ano')
    print('3 - Ensino Médio - 3º Ano \n')

    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
      self.curso = 'Ensino Médio - 1º Ano'
      print(f'{self.nome_aluno} matriculado no {self.curso} \n')
    if opcao == 2:
      self.curso = 'Ensino Médio - 2º Ano'
      print(f'{self.nome_aluno} matriculado no {self.curso} \n')
    if opcao == 3:
      self.curso = 'Ensino Médio - 3º Ano'
      print(f'{self.nome_aluno} matriculado no {self.curso} \n')
  
  def cadastra_materias(self):
    print(f'Escolha quais matérias deseja cadastrar: ')
    print(f'1 - Matemática')
    print(f'2 - Física')
    print(f'3 - Química')
    print(f'4 - História')
    print(f'5 - Português')
    print(f'6 - SAIR \n')

    while(1):
      opcao = int(input('Digite uma opção: '))
      if opcao == 1:
        self.materias[0] = 'Matemática (em curso)'
        print(f'Matemática adicionada à grade curricular \n')
      if opcao == 2:
        self.materias[1] = 'Física (em curso)'
        print(f'Física adicionada à grade curricular \n')
      if opcao == 3:
        self.materias[2] = 'Química (em curso)'
        print(f'Química adicionada à grade curricular \n')
      if opcao == 4:
        self.materias[3] = 'História (em curso)'
        print(f'História adicionada à grade curricular \n')
      if opcao == 5:
        self.materias[4] = 'Português (em curso)'
        print(f'Português adicionada à grade curricular \n')
      if opcao == 6:
        print(f'Grade curricular inserida com sucesso \n')
        break

  def cadastra_notas(self):
    print('Lançar notas de qual disciplina:')
    print('1 - Matemática')
    print('2 - Física')
    print('3 - Química')
    print('4 - História')
    print('5 - Português')
    print('6 - SAIR \n')

    def soma_notas(n1, n2, n3, n4):
      media_final =  (n1 + n2 + n3 + n4) / 4
      return media_final

    while(1):
      opcao = int(input('Escolha uma opção: '))
      if opcao == 1:
        n1 = int(input('Digite a nota do 1º bimestre: '))
        n2 = int(input('Digite a nota do 2º bimestre: '))
        n3 = int(input('Digite a nota do 3º bimestre: '))
        n4 = int(input('Digite a nota do 4º bimestre: '))
        n5 = soma_notas(n1, n2, n3, n4)
        if n5 >= 70:
          print(f'Média Final: {n5}')
          print('Aprovado(a) em Matemática \n')
          self.materias[0] = 'Matemática (aprovado(a))'
        else:
          print('Reprovado(a) em Matemática \n')
      if opcao == 2:
        n1 = int(input('Digite a nota do 1º bimestre: '))
        n2 = int(input('Digite a nota do 2º bimestre: '))
        n3 = int(input('Digite a nota do 3º bimestre: '))
        n4 = int(input('Digite a nota do 4º bimestre: '))
        n5 = soma_notas(n1, n2, n3, n4)
        if n5 >= 70:
          print(f'Média Final: {n5}')
          print('Aprovado(a) em Física \n')
          self.materias[1] = 'Física (aprovado(a))'
        else:
          print('Reprovado(a) em Física \n')
      if opcao == 3:
        n1 = int(input('Digite a nota do 1º bimestre: '))
        n2 = int(input('Digite a nota do 2º bimestre: '))
        n3 = int(input('Digite a nota do 3º bimestre: '))
        n4 = int(input('Digite a nota do 4º bimestre: '))
        n5 = soma_notas(n1, n2, n3, n4)
        if n5 >= 70:
          print(f'Média Final: {n5}')
          print('Aprovado(a) em Química \n')
          self.materias[2] = 'Química (aprovado(a))'
        else:
          print('Reprovado(a) em Química \n')
      if opcao == 4:
        n1 = int(input('Digite a nota do 1º bimestre: '))
        n2 = int(input('Digite a nota do 2º bimestre: '))
        n3 = int(input('Digite a nota do 3º bimestre: '))
        n4 = int(input('Digite a nota do 4º bimestre: '))
        n5 = soma_notas(n1, n2, n3, n4)
        if n5 >= 70:
          print(f'Média Final: {n5}')
          print('Aprovado(a) em História \n')
          self.materias[3] = 'História (aprovado(a))'
        else:
          print('Reprovado(a) em História \n')
      if opcao == 5:
        n1 = int(input('Digite a nota do 1º bimestre: '))
        n2 = int(input('Digite a nota do 2º bimestre: '))
        n3 = int(input('Digite a nota do 3º bimestre: '))
        n4 = int(input('Digite a nota do 4º bimestre: '))
        n5 = soma_notas(n1, n2, n3, n4)
        if n5 >= 70:
          print(f'Média Final: {n5}')
          print('Aprovado em Português \n')
          self.materias[4] = 'Português (aprovado(a))'
        else:
          print('Reprovado(a) em Português \n')
      if opcao == 6:
        break

  def relatorio_aluno(self):
    print(f'**********{self.nome_aluno}********** \n')
    print(f'BOLETIM: \n')
    print(f'Aluno(a): {self.nome_aluno}')
    print(f'Curso: {self.curso}')
    print('______________________________________')
    print(f'Matemática: {self.materias[0]}')
    print(f'Física: {self.materias[1]}')
    print(f'Química: {self.materias[2]}')
    print(f'História: {self.materias[3]}')
    print(f'Português: {self.materias[4]}')
    print('______________________________________ \n')

    self.base.update({f'Aluno(a) nº {self.n}':[self.nome_aluno,
                              f'Filiação: {self.nome_pai} e {self.nome_mae}',
                              f'Telefone: {self.telefone}',
                              f'Endereço: {self.logradouro}',
                              f'Curso: {self.curso}',
                              f'Turma: {self.turma_num}',
                              f'Disciplinas: {self.materias}',
                              f'Observações: {self.outros}']})
  
  def lista(self):
    print('Relação de Alunos Matriculados:')
    print(sorted(self.turma))
    print(f'Número total: {len(self.turma)} alunos')
    print('\n')
  
  def lista_base(self):
    print('Base de Dados Completa:')

    for aluno in self.base.items():
      print(aluno)
  
  def busca_aluno(self):
    nome = input('Digite o nome completo: ').upper()

    if nome in self.turma:
      print('Aluno(a) já matriculado')
      print('Deseja alterar alguma informação?')
      print('1 - SIM')
      print('2 - NÃO \n')
      o = int(input('Escolha uma opção: '))
      if o == 1:
        print('Qual dado cadastral deseja alterar?')
        print('1 - Telefone')
        print('2 - Endereço')
        print('3 - Curso \n')
        x = int(input('Escolha uma opção: '))
        if x == 1:
          self.telefone = int(input('Digite o novo número de telefone:'))
          print('Número de telefone atualizado com sucesso \n')
        if x == 2:
          self.logradouro = input('Digite o novo endereço residencial:').upper()
          print('Endereço atualizado com sucesso \n')
        if x == 3:
          self.cadastra_curso()
          print('Curso atualizado com sucesso \n')
      else:
        pass
    else:
      print(f'{nome} não consta na base de dados \n')
  
def main():
  sistema = Escola()
  
  while True:
    print('1 - Matrícular Aluno(a)')
    print('2 - Cadastrar Curso')
    print('3 - Cadastrar Disciplinas')
    print('4 - Cadastrar Notas')
    print('5 - Concluir Cadastro')
    print('-------------------------')
    print('6 - Listar Alunos')
    print('7 - Base de Dados')
    print('-------------------------')
    print('8 - Atualizar Cadastro')
    print('-------------------------')
    print('9 - SAIR')
    print('-------------------------')
    print('\n')

    op = int(input('Digite uma opção: '))
    if op == 1:
      sistema.matricula()
    if op == 2:
      sistema.cadastra_curso()
    if op == 3:
      sistema.cadastra_materias()
    if op == 4:
      sistema.cadastra_notas()
    if op == 5:
      sistema.relatorio_aluno()
    if op == 6:
      sistema.lista()
    if op == 7:
      sistema.lista_base()
    if op == 8:
      sistema.busca_aluno()
    if op == 9:
      break

main()
      
