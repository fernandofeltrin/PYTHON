import pandas as pd
import sqlite3
from calendar import monthrange
from datetime import date
from operator import getitem
import streamlit as st
import datetime
from st_on_hover_tabs import on_hover_tabs

from app import Clinica

st.set_page_config(layout="wide")

sistema = Clinica()

atualiza_exibe_agenda = sqlite3.connect('c:/Users/Fernando/Projeto_Clinica/base_agenda.db')
exibe_agenda = pd.read_sql_query("SELECT * FROM agenda", atualiza_exibe_agenda)
exibe_agenda = exibe_agenda.rename({'consulta_num':'Id',
                                    'nome_pac':'Paciente',
                                    'consulta_com':'Médico(a)',
                                    'dia':'Dia',
                                    'hora':'Hora'}, axis = 1)
exibe_agenda = exibe_agenda.set_index('Id')

st.sidebar.title('Menu Principal')

menu = st.sidebar.selectbox('Selecione a Opção', ['Página Principal',
                                                  'Agendar Consulta',
                                                  'Cadastrar Paciente',
                                                  'Cadastrar Médico(a)',
                                                  'Exibe Prontuários'])

if menu == 'Página Principal':
    st.title('Sistema Clínica')
    st.text('Agenda')

    st.dataframe(exibe_agenda)

    tab1, tab2 = st.tabs(["Pacientes", "Médicos"])

    with tab1:
        st.markdown("Relação de Pacientes")
        st.write(sistema.nomes_pacientes)

    with tab2:
        st.markdown("Relação de Médicos")
        st.write(sistema.nomes_medicos)
        
elif menu == 'Cadastrar Paciente':
    st.title('Cadastro de Paciente')

    with st.expander("Instruções"):
        st.write("""
        - Preencha todos os campos,
        - Por fim, clique em Enviar para concluir o cadastro
        """)

    with st.form(key = 'cadastro_paciente'):
        nome = st.text_input('Digite o nome completo do paciente: ').upper()
        identidade = st.text_input('Digite o nº do documento de Identidade: ')
        data_nasc = st.text_input('Digite a data de nascimento: ')
        fone = st.text_input('Digite um telefone para contato: ')
        email = st.text_input('Digite o endereço de e-mail: ').upper()
        endereco = st.text_input('Digite o endereço residencial: ').upper()
        profissao = st.text_input('Digite a atividade profissional: ').upper()
        outros = st.text_input('Digite as observações (caso houver): ').upper()
        botao_enviar = st.form_submit_button('Enviar')
        
    if botao_enviar:
        sistema.nome_pac = nome
        sistema.identidade = identidade
        sistema.data_nasc = data_nasc
        sistema.fone = fone
        sistema.email = email
        sistema.endereco = endereco
        sistema.profissao = profissao
        sistema.outros = outros
        conexao = sqlite3.connect('c:/Users/Fernando/Projeto_Clinica/base_pacientes.db')
        cursor_base = conexao.cursor()
        cursor_base.execute("REPLACE INTO pacientes (nome_pac, identidade, fone, email, endereco, data_nasc, profissao, observacoes) VALUES (:nome_pac, :identidade, :fone, :email, :endereco, :data_nasc, :profissao, :observacoes)", {
                        'nome_pac': sistema.nome_pac,
                        'identidade': sistema.identidade,
                        'fone': sistema.fone,
                        'email': sistema.email,
                        'endereco': sistema.endereco,
                        'data_nasc': sistema.data_nasc,
                        'profissao': sistema.profissao,
                        'observacoes': sistema.outros})
        conexao.commit()
        conexao.close()

        sistema.nomes_pacientes.append(sistema.nome_pac)
        
        sistema.prontuario.update({
            sistema.nome_pac:{'Nome: ': sistema.nome_pac,
                           'Data de Nascimento: ': sistema.data_nasc,
                           'Telefone para Contato: ': sistema.fone,
                           'Endereco Residencial: ': sistema.endereco,
                           'Observacoes: ': sistema.outros,
                           'Numero de Consultas: ': sistema.num_consultas,
                           'Prontuario: ': sistema.rel_agendamento}})
            
        st.text('Cadastro realizado / alterado com sucesso')

elif menu == 'Cadastrar Médico(a)':
    st.title('Cadastro de Médico')

    with st.expander("Instruções"):
        st.write("""
        - Preencha todos os campos,
        - Por fim, clique em Enviar para concluir o cadastro
        """)

    with st.form(key = 'cadastro_medico'):
        nome = st.text_input('Digite o nome completo do médico: ').upper()
        crm = st.text_input('Digite o número da credencial CRM: ')
        especialidade = st.text_input('Digite a especialidade: ').upper()
        botao_enviar = st.form_submit_button('Enviar')

    if botao_enviar:
        sistema.nome_med = nome
        sistema.crm = crm
        sistema.especialidade = especialidade
                    
        conexao = sqlite3.connect('c:/Users/Fernando/Projeto_Clinica/base_medicos.db')
        cursor_base = conexao.cursor()
        cursor_base.execute("REPLACE INTO medicos (nome_med, crm, especialidade) VALUES (:nome_med, :crm, :especialidade)", {
                'nome_med': sistema.nome_med,
                'crm': sistema.crm,
                'especialidade': sistema.especialidade})
        conexao.commit()
        conexao.close()

        sistema.nomes_medicos.append(sistema.nome_med)
        sistema.base_medicos.update({f'{sistema.nome_med}': f'{sistema.especialidade}'})

        st.text('Cadastro realizado / alterado com sucesso')

elif menu == 'Agendar Consulta':
    with st.form(key = 'escolha_paciente'):
        st.write('Agendamento')
        nome_pac = st.text_input('Digite o nome do paciente: ').upper()
        botao_verificar1 = st.form_submit_button(label = 'Verificar')
        if botao_verificar1:
            if nome_pac in sistema.nomes_pacientes:
                st.write('Paciente já cadastrado')
            else:
                st.write('Paciente não cadastrado')
                st.write('Favor cadastrar para continuar o agendamento')

    with st.form(key = 'escolha_medico'):
        nome_med = st.text_input('Digite o nome do médico(a): ').upper()
        botao_verificar2 = st.form_submit_button('Verificar')
        if botao_verificar2:
            if nome_med in sistema.nomes_medicos:
                st.write('Médico(a) já cadastrado')
            else:
                st.write('Médico(a) não cadastrado')
                st.write('Favor cadastrar para continuar o agendamento')

    with st.form(key = 'escolha_plano'):
        nome_plano = st.radio('Escolha um Plano de Saúde', ('SUS', 'CAUZZO', 'UNIMED'))
        if nome_plano == 'SUS':
            sistema.valor_consulta = 0
            st.write('Aplicado o desconto de 100%')
        if nome_plano == 'CAUZZO':
            sistema.valor_consulta = sistema.valor_consulta - sistema.valor_consulta * 0.40
            st.write('Aplicado o desconto de 40%')
        if nome_plano == 'UNIMED':
            sistema.valor_consulta = sistema.valor_consulta / 2
            st.write('Aplicado o desconto de 50%')
        botao_verificar3 = st.form_submit_button('Escolher')

    with st.form(key = 'escolha_dia'):
        dia_consulta_ = st.date_input('Escolha o dia: ', datetime.date(2022, 1, 1))
        dia_consulta = dia_consulta_.day
        botao_verificar4 = st.form_submit_button('Definir')
        st.write(f'Dia: {dia_consulta}')

    with st.form(key = 'escolha_hora'):
        hora_consulta = st.slider('Escolha um horário: ',
                                  min_value = 8,
                                  max_value = 18,
                                  step = 1)
        botao_verificar5 = st.form_submit_button('Definir')
        st.write(f'Hora: {hora_consulta} horas')

    with st.form(key = 'conclui_agendamento'):
        if ((botao_verificar1 == True) and (botao_verificar2 == True) and (botao_verificar3 == True) and (botao_verificar4 == True) and (botao_verificar5 == True)):
            st.write('Agendamento realizado com sucesso')
        botao_concluir = st.form_submit_button('Finalizar Agendamento')

    if botao_concluir:
        sistema.nome_pac = nome_pac
        sistema.nome_med = nome_med
        sistema.data = dia_consulta
        sistema.hora = hora_consulta

        sistema.agenda.update({f'{sistema.consulta_num}': f'Dia: {sistema.data}, às {sistema.hora} horas. Paciente: {sistema.nome_pac}, Dr.(a): {sistema.nome_med}'})
        
        sistema.num_consultas = len(sistema.agenda.items())
        sistema.consulta_num = sistema.num_consultas
        sistema.receita_consultas += sistema.valor_consulta

        sistema.rel_agendamento.append(f'{sistema.nome_pac} - Consulta com {sistema.nome_med}, dia {sistema.data} às {sistema.hora} horas')

        sistema.prontuario.update({
            sistema.nome_pac:{'Nome: ': sistema.nome_pac,
                           'Data de Nascimento: ': sistema.data_nasc,
                           'Telefone para Contato: ': sistema.fone,
                           'Endereco Residencial: ': sistema.endereco,
                           'Observacoes: ': sistema.outros,
                           'Numero de Consultas: ': sistema.num_consultas,
                           'Prontuario: ': sistema.rel_agendamento}
        })
        
        conexao = sqlite3.connect('c:/Users/Fernando/Projeto_Clinica/base_agenda.db')
        cursor_base = conexao.cursor()
        cursor_base.execute("INSERT INTO agenda (consulta_num, nome_pac, consulta_com, dia, hora) VALUES (:consulta_num, :nome_pac, :consulta_com, :dia, :hora)", {
                'consulta_num': sistema.consulta_num,
                'nome_pac': sistema.nome_pac,
                'consulta_com': sistema.nome_med,
                'dia': sistema.data,
                'hora': sistema.hora})
        conexao.commit()
        conexao.close()

        st.write(f'Consulta agendada para o dia {sistema.data} às {sistema.hora} horas com o(a) Dr.(a) {sistema.nome_med}')
        st.write(f'Valor da consulta: R${sistema.valor_consulta}')

elif menu == 'Exibe Prontuários':
    st.title('Prontuários')
    prontuarios = []
    for i in sistema.prontuario.values():
        prontuarios.append(i)
    df = pd.DataFrame(prontuarios)
    st.dataframe(df)

    st.warning('Os prontuários dos pacientes são atualizados a cada novo agendamento de consulta', icon="⚠️")
