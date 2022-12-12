# -*- coding: utf-8 -*-

import sqlite3

def cria_bases():
    try:
        conexao1 = sqlite3.connect('Projeto_Clinica/base_pacientes.db')
        cursor_base = conexao1.cursor()
        cursor_base.execute('''
                    CREATE TABLE pacientes (
                        nome_pac text,
                        identidade text,
                        fone text,
                        email text,
                        endereco text,
                        data_nasc text,
                        profissao text,
                        observacoes text,
                        PRIMARY KEY(nome_pac)
                        )
                            ''')
        conexao1.commit()
        conexao1.close()

        conexao2 = sqlite3.connect('base_medicos.db')
        cursor_base = conexao2.cursor()
        cursor_base.execute('''
                    CREATE TABLE medicos (
                        nome_med text,
                        crm text,
                        especialidade text,
                        PRIMARY KEY(nome_med)
                        )
                            ''')
        conexao2.commit()
        conexao2.close()

        conexao3 = sqlite3.connect('base_agenda.db')
        cursor_base = conexao3.cursor()
        cursor_base.execute('''
                    CREATE TABLE agenda (
                        consulta_num integer,
                        nome_pac text,
                        consulta_com text,
                        dia text,
                        hora text
                        )
                            ''')
        conexao3.commit()
        conexao3.close()

    except:
        # print('Base de dados já existente')
        pass
