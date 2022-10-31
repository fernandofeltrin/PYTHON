class Clinica:
    def __init__(self):
        self.nome_pac = ''
        self.fone = ''
        self.endereco = ''
        self.data_nasc = ''
        self.convenio = ''
        self.outros = ''

        self.prontuario = {}
        self.agenda = {}
        self.dias_agendamento = ['SEGUNDA', 'TERÇA', 'QUINTA']
        self.horarios = [8, 9, 10, 11, 14, 15, 16, 17]

        self.rel_pacientes = []
        self.rel_medicos = {}

        self.valor_consulta = 250
        self.num_consultas = 0

    def cadastra_paciente(self):
        self.nome_pac = input('Digite o nome completo do paciente: ').upper()
        self.data_nasc = input('Digite a data de nascimento: ')
        self.fone = input('Digite um telefone para contato: ')
        self.endereco = input('Digite o endereço residencial: ').upper()
        self.outros = input('Digite as observações (caso houver): ').upper()
        
        print(f'Paciente cadastrado com sucesso \n')

        self.rel_pacientes.append(self.nome_pac)
        self.prontuario.update({self.nome_pac:[f'Nome: {self.nome_pac}',
                                               f'Data de Nascimento: {self.data_nasc}',
                                               f'Telefone para Contato: {self.fone}',
                                               f'Endereço Residencial: {self.endereco}',
                                               f'Observações: {self.outros}',
                                               f'Número de Consultas: {self.num_consultas}']})

        return self.rel_pacientes

    def cadastra_medico(self,
                        nome_med = '',
                        crm = '',
                        especialidade = ''):
        
        self.nome_med = input('Digite o nome completo do médico: ').upper()
        self.crm = input('Digite o número da CRM: ').upper()
        self.especialidade = input('Digite a especialidade: ').upper()

        self.rel_medicos.update({f'Nome: {self.nome_med} - CRM Nº {self.crm}': f'Especialidade: {self.especialidade}'})
        print(f'Médico cadastrado com sucesso. \n')

        return self.rel_medicos

    def agenda_consulta(self):
        self.nome_pac = input('Digite o nome completo: ').upper()
        self.nome_med = ''
        self.plano = ''
        self.data = ''
        self.hora = ''

        if self.nome_pac not in self.rel_pacientes:
            print(f'Paciente novo, é necessário o cadastrar para pode realizar o agendamento. \n')
            self.cadastra_paciente()

        else:
            self.nome_med = input('Com qual médico(a) gostaria de consultar? ').upper()
            if self.nome_med not in self.rel_medicos:
                print(f'Médico novo, é necessário o cadastrar para poder realizar agendamento. \n')
                self.cadastra_medico()

                print(f'Prosseguindo com o agendamento para o Dr. {self.nome_med}\n')
                self.plano = input('Qual o plano de saúde? ').upper()

                if self.plano == 'UNIMED':
                    self.valor_consulta = self.valor_consulta / 2

                self.data = input('Qual dia deseja consultar? ').upper()

                if self.data not in self.dias_agendamento:
                    print(f'Agendamento apenas segundas, terças e quintas \n')
                else:
                    self.hora = int(input('Em qual horário? '))

                    if self.hora not in self.horarios:
                        print(f'Atendimento apenas em horário comercial \n')
                    else:
                        self.agenda.update({f'Dia: {self.data}, às {self.hora}':[f'Paciente: {self.nome_pac}', f'Dr.(a): {self.nome_med}']})
                        self.num_consultas += 1
                        print(f'Consulta agendada com sucesso para o dia {self.data} às {self.hora} horas com o(a) Dr.(a) {self.nome_med}')
                        print(f'Valor da consulta: R${self.valor_consulta} \n')
                        self.prontuario.update({self.nome_pac:[f'Nome: {self.nome_pac}',
                                                f'Data de Nascimento: {self.data_nasc}',
                                                f'Telefone para Contato: {self.fone}',
                                                f'Endereço Residencial: {self.endereco}',
                                                f'Observações: {self.outros}',
                                                f'Número de Consultas: {self.num_consultas}']})

        return self.agenda

    def exibe_prontuario(self):
        for i in self.prontuario.items():
            print(i)

    def exibe_agenda(self):
        if len(self.agenda.keys()) == 0:
            print(f'Agenda atualmente vazia \n')

        for i in self.agenda.items():
            print(i)
    
    def relacao_medicos(self):
        if len(self.rel_medicos.keys()) == 0:
            print(f'Não existem médicos cadastrados \n')

        for i in self.rel_medicos.items():
            print(i)

def main():
    sistema = Clinica()

    while True:
        print('1 - Agendar Consulta')
        print('----------------------')
        print('2 - Cadastrar Paciente')
        print('3 - Cadastrar Médico')
        print('----------------------')
        print('4 - Exibir Agenda')
        print('5 - Relação Prontuários de Pacientes')
        print('6 - Relação de Médicos Cadastrados')
        print('------------------------------------')
        print(f'9 - SAIR \n')

        try:
            opcao = int(input('Escolha uma opção: '))

            match opcao:
                case 1:
                    sistema.agenda_consulta()
                case 2:
                    sistema.cadastra_paciente()
                case 3:
                    sistema.cadastra_medico()
                case 4:
                    sistema.exibe_agenda()
                case 5:
                    sistema.exibe_prontuario()
                case 6:
                    sistema.relacao_medicos()
                case 9:
                    break

        except:
            print(f'Escolha uma opção: \n')
            pass

main()
