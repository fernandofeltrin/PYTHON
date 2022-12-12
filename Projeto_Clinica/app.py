# -*- coding: utf-8 -*-

import pandas as pd
import sqlite3
from calendar import monthrange
from datetime import date
from operator import getitem
import streamlit as st

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

        self.valor_consulta = 250
        self.num_consultas = 0
        self.consulta_num = 1
        self.base_consultas = {}
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
                                 'Numero de Consultas: ': '',
                                 'Prontuario: ': ''}
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
