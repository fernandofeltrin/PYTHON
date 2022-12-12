# -*- coding: utf-8 -*-

import pandas as pd
import sqlite3
from calendar import monthrange
from datetime import date
from operator import getitem

from bases import cria_bases

cria_bases()

class Clinica:
    def __init__(self):
        self.nome_pac = ''
        self.identidade = ''
        self.profissao = ''
        self.nome_med = ''
        self.nome_plano = ''
        self.crm = ''
        self.num_credencial = ''
        self.especialidade = ''
        self.fone = ''
        self.telefone = ''
        self.email = ''
        self.endereco = ''
        self.data_nasc = ''
        self.convenio = ''
        self.outros = ''
        self.plano = ''
        self.data = ''
        self.hora = ''

        self.prontuario = {}
        self.base_medicos = {}
        self.nomes_pacientes = []
        self.nomes_medicos = []
        self.nomes_planos = ['SUS', 'UNIMED', 'CAUZZO']

        self.agenda = {}
        self.dias_agendamento = ['SEGUNDA', 'QUARTA', 'SEXTA']
        self.horarios = [8, 9, 10, 11, 14, 15, 16, 17]

        self.valor_consulta = 250
        self.num_consultas = 0
        self.consulta_num = 1
        self.receita_consultas = 0

        self.rel_agendamento = []
        self.hist_receita_consultas = {}

        try:
            conexao1 = sqlite3.connect('base_pacientes.db')
            cursor_base = conexao1.cursor()
            for paciente in cursor_base.execute("SELECT nome_pac FROM pacientes"):
                for nome in paciente[0::]:
                    self.nomes_pacientes.append(nome)
            for paciente in cursor_base.execute("SELECT * FROM pacientes"):
                self.prontuario.update({
                    paciente[0]:{'Nome: ': paciente[0],
                                 'Data de Nascimento: ': paciente[5],
                                 'Telefone para Contato: ': paciente[2],
                                 'Endereco Residencial: ': paciente[4],
                                 'Observacoes: ': paciente[7],
                                 'Numero de Consultas: ': self.num_consultas,
                                 'Prontuario: ': self.rel_agendamento}
                })
            conexao1.commit()
            conexao1.close()

            conexao2 = sqlite3.connect('base_medicos.db')
            cursor_base = conexao2.cursor()
            for medico in cursor_base.execute("SELECT nome_med FROM medicos"):
                for nome in medico[0::]:
                    self.nomes_medicos.append(nome)
            for medico in cursor_base.execute("SELECT * FROM medicos"):
                self.base_medicos.update({medico[0]:medico[2]})
            conexao2.commit()
            conexao2.close()

            conexao3 = sqlite3.connect('base_agenda.db')
            cursor_base = conexao3.cursor()
            for consulta in cursor_base.execute("SELECT * FROM agenda"):
                self.agenda.update({
                    consulta[0]:{'Id: ': consulta[0],
                                 'Nome: ': consulta[1],
                                 'Médico(a): ': consulta[2],
                                 'Dia: ': consulta[3],
                                 'Hora: ': consulta[4]}
                })
            for num_consultas in cursor_base.execute("SELECT LAST_INSERT_ROWID() AS ID"):
                self.num_consultas = num_consultas + 1
            conexao3.commit()
            conexao3.close()
            
        except:
            return None
    
    def cadastra_paciente(self):
        self.nome_pac = input('Digite o nome completo do paciente: ').upper()
        if self.nome_pac in self.nomes_pacientes:
            print('Paciente já cadastrado, deseja alterar o cadastro?')
            print('1 - SIM')
            print('2 - NÃO')
            
            opcao = int(input('Digite uma opção: '))
            match opcao:
                case 1:
                    print(f'{self.nome_pac}')
                    self.identidade = input('Digite o nº do documento de Identidade: ').upper()
                    self.data_nasc = input('Digite a data de nascimento: ')
                    self.fone = input('Digite um telefone para contato: ')
                    self.email = input('Digite o endereço de e-mail: ').upper()
                    self.endereco = input('Digite o endereço residencial: ').upper()
                    self.profissao = input('Digite a atividade profissional: ').upper()
                    self.outros = input('Digite as observações (caso houver): ').upper()
        
                    conexao = sqlite3.connect('base_pacientes.db')
                    cursor_base = conexao.cursor()
                    cursor_base.execute("REPLACE INTO pacientes (nome_pac, identidade, fone, email, endereco, data_nasc, profissao, observacoes) VALUES (:nome_pac, :identidade, :fone, :email, :endereco, :data_nasc, :profissao, :observacoes)", {
                        'nome_pac': self.nome_pac,
                        'identidade': self.identidade,
                        'fone': self.fone,
                        'email': self.email,
                        'endereco': self.endereco,
                        'data_nasc': self.data_nasc,
                        'profissao': self.profissao,
                        'observacoes': self.outros})
                    conexao.commit()
                    conexao.close()
                    print('Cadastro alterado com sucesso \n')
                
                case 2:
                    pass

        if self.nome_pac not in self.nomes_pacientes:
            print(f'{self.nome_pac}')
            self.identidade = input('Digite o nº do documento de Identidade: ').upper()
            self.data_nasc = input('Digite a data de nascimento: ')
            self.fone = input('Digite um telefone para contato: ')
            self.email = input('Digite o endereço de e-mail: ').upper()
            self.endereco = input('Digite o endereço residencial: ').upper()
            self.profissao = input('Digite a atividade profissional: ').upper()
            self.outros = input('Digite as observações (caso houver): ').upper()
        
            conexao = sqlite3.connect('base_pacientes.db')
            cursor_base = conexao.cursor()
            cursor_base.execute("INSERT INTO pacientes (nome_pac, identidade, fone, email, endereco, data_nasc, profissao, observacoes) VALUES (:nome_pac, :identidade, :fone, :email, :endereco, :data_nasc, :profissao, :observacoes)", {
                'nome_pac': self.nome_pac,
                'identidade': self.identidade,
                'fone': self.fone,
                'email': self.email,
                'endereco': self.endereco,
                'data_nasc': self.data_nasc,
                'profissao': self.profissao,
                'observacoes': self.outros})
            conexao.commit()
            conexao.close()
            print('Cadastro realizado com sucesso \n')
            
            self.nomes_pacientes.append(self.nome_pac)
        
        self.prontuario.update({
            self.nome_pac:{'Nome: ': self.nome_pac,
                           'Data de Nascimento: ': self.data_nasc,
                           'Telefone para Contato: ': self.fone,
                           'Endereco Residencial: ': self.endereco,
                           'Observacoes: ': self.outros,
                           'Numero de Consultas: ': self.num_consultas,
                           'Prontuario: ': self.rel_agendamento}
        })

        return self.nomes_pacientes

    def cadastra_medico(self):
        self.nome_med = input('Digite o nome completo do médico: ').upper()
        if self.nome_med in self.nomes_medicos:
            print('Médico(a) já cadastrado, deseja alterar o cadastro?')
            print('1 - SIM')
            print('2 - NÃO')
            opcao = int(input('Digite uma opção: '))
            
            match opcao:
                case 1:
                    print(f'Dr(a) {self.nome_med}')
                    self.crm = input('Digite o número da CRM: ').upper()
                    self.especialidade = input('Digite a especialidade: ').upper()
                    
                    conexao = sqlite3.connect('base_medicos.db')
                    cursor_base = conexao.cursor()
                    cursor_base.execute("REPLACE INTO medicos (nome_med, crm, especialidade) VALUES (:nome_med, :crm, :especialidade)", {
                        'nome_med': self.nome_med,
                        'crm': self.crm,
                        'especialidade': self.especialidade})
                    conexao.commit()
                    conexao.close()
                    print('Cadastro alterado com sucesso \n')
                
                case 2:
                    pass

        if self.nome_med not in self.nomes_medicos:
            print(f'Dr(a) {self.nome_med}')
            self.crm = input('Digite o número da CRM: ').upper()
            self.especialidade = input('Digite a especialidade: ').upper()
                    
            conexao = sqlite3.connect('base_medicos.db')
            cursor_base = conexao.cursor()
            cursor_base.execute("INSERT INTO medicos (nome_med, crm, especialidade) VALUES (:nome_med, :crm, :especialidade)", {
                'nome_med': self.nome_med,
                'crm': self.crm,
                'especialidade': self.especialidade})
            conexao.commit()
            conexao.close()
            print('Cadastro realizado com sucesso \n')
            self.nomes_medicos.append(self.nome_med)

        self.base_medicos.update({f'{self.nome_med}': f'{self.especialidade}'})

        return self.base_medicos, self.nomes_medicos

    def agenda_consulta(self):
        self.nome_pac = input('Digite o nome completo: ').upper()
        if self.nome_pac not in self.nomes_pacientes:
            print('Paciente novo, é necessário o cadastrar para pode realizar o agendamento. \n')
            self.cadastra_paciente()
            print('Retomando o agendamento... \n')
        
        self.nome_med = input('Com qual médico(a) gostaria de consultar? ').upper()
        if self.nome_med not in self.nomes_medicos:
            print('Médico novo, é necessário o cadastrar para poder realizar agendamento. \n')
            self.cadastra_medico()
            print(f'Prosseguindo com o agendamento para o Dr. {self.nome_med} \n')
        
        print('SUS / UNIMED / CAUZZO')
        self.nome_plano = input('Qual o plano de saúde? Digite o nome caso houver ').upper()
        if self.nome_plano in self.nomes_planos:
            match self.nome_plano:
                case 'SUS':
                    self.valor_consulta = 0
                    print('Aplicado o desconto de 100% \n')
                    print(f'Valor da consulta: R${self.valor_consulta}')
                case 'UNIMED':
                    self.valor_consulta = self.valor_consulta / 2
                    print('Aplicado o desconto de 50% \n')
                    print(f'Valor da consulta: R${self.valor_consulta}')
                case 'CAUZZO':
                    self.valor_consulta = self.valor_consulta - self.valor_consulta * 0.40
                    print('Aplicado o desconto de 40% \n')
                    print(f'Valor da consulta: R${self.valor_consulta}')

        self.data = input('Qual dia da semana deseja consultar? ').upper()
        while self.data not in self.dias_agendamento:
            print('Agendamento apenas SEGUNDA, QUARTA e SEXTA \n')
            self.data = input('Qual dia da semana deseja consultar? ').upper()

        self.hora = int(input('Em qual horário? '))
        while self.hora not in self.horarios:
            print('Atendimento das 8 às 11h e das 14 às 17h \n')
            self.hora = int(input('Em qual horário? '))
            
        self.agenda.update({f'{self.consulta_num}': f'Dia: {self.data}, às {self.hora} horas. Paciente: {self.nome_pac}, Dr.(a): {self.nome_med}'})

        self.num_consultas += 1
        self.receita_consultas += self.valor_consulta

        conexao = sqlite3.connect('base_agenda.db')
        cursor_base = conexao.cursor()
        self.consulta_num += 1
        cursor_base.execute("INSERT INTO agenda (consulta_num, nome_pac, consulta_com, dia, hora) VALUES (:consulta_num, :nome_pac, :consulta_com, :dia, :hora)", {
                'consulta_num': self.consulta_num,
                'nome_pac': self.nome_pac,
                'consulta_com': self.nome_med,
                'dia': self.data,
                'hora': self.hora})
        conexao.commit()
        conexao.close()

        self.dia = date.today().strftime("%d/%m/%Y")
        self.rel_agendamento.append(f'Consulta com {self.nome_med}, {self.data}, {self.dia} às {self.hora} horas')

        print(f'Consulta agendada para {self.data} às {self.hora} horas com o(a) Dr.(a) {self.nome_med}')
        print(f'Valor da consulta: R${self.valor_consulta} \n')

        self.prontuario.update({
            self.nome_pac:{'Nome: ': self.nome_pac,
                           'Data de Nascimento: ': self.data_nasc,
                           'Telefone para Contato: ': self.fone,
                           'Endereco Residencial: ': self.endereco,
                           'Observacoes: ': self.outros,
                           'Numero de Consultas: ': self.num_consultas,
                           'Prontuario: ': self.rel_agendamento}
        })
        
        self.prontuario = sorted(self.prontuario.items(), key = lambda x: getitem(x[1], 'Nome: '))

        self.valor_consulta = 250

        return self.agenda, self.prontuario, self.receita_consultas, self.rel_agendamento, self.nomes_pacientes

    def exibe_prontuario(self):
        print('PRONTUÁRIOS')
        if len(self.prontuario.keys()) == 0:
            print('Não existem registros de pacientes \n')
        
        for i in self.prontuario.items():
            print(i)

    def exibe_agenda(self):
        print('AGENDA')
        print(type(self.agenda))
        if len(self.agenda.keys()) == 0:
            print('Agenda atualmente vazia \n')

        for i in self.agenda.items():
            print(i)
    
    def relacao_medicos(self):
        if len(self.nomes_medicos) == 0:
            print('Não existem médicos cadastrados \n')

        for i in self.base_medicos.items():
            print(i)

    def relatorio_gerencial(self):
        print(f'Número total de consultas: {self.num_consultas}')
        print(f'Receita gerada pelas consultas: R${self.receita_consultas}')
        print('---------------------------------')
        print(f'Número de pacientes cadastrados: {len(self.nomes_pacientes)}')
        print(f'Número de médicos conveniados: {len(self.nomes_medicos)} \n')
        print('---------------------------------')

        data_atual = date.today()
        ultimo_dia = data_atual.replace(day = monthrange(data_atual.year, data_atual.month)[1])
        if data_atual == ultimo_dia:
            print(self.receita_consultas)
            self.receita_consultas == 0
            self.hist_receita_consultas.update({f'MÊS {data_atual.month}':f'R$ {self.receita_consultas}'}) 
        if data_atual != ultimo_dia:
            print(f'Receita acumulada: R${self.receita_consultas}')
            self.hist_receita_consultas.update({f'MÊS {data_atual.month}':f'R$ {self.receita_consultas}'})
            print(self.hist_receita_consultas.items())
