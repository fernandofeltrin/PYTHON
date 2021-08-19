# Delegando métodos de classe em classes associadas

class Mensagens:
  def mensagem_1(self):
    print('Inicializando o sistema')
  
  def mensagem_2(self):
    print('Encerrando o sistema')

class Gatilhos:
  def __init__(self):
    self.msg = Mensagens() # Recebe a classe Mensagem como atributo, para que possamos usar de métodos de classe internos a eata classe
  
  def msg1(self):
    return self.msg.mensagem_1() # Instancia e inicializa o método de classe mensagem_1( ) da classe Mensagem
  
  def msg2(self):
    return self.msg.mensagem_2()

  def __getattr__(self, mensagem):
    return getattr(self.msg, mensagem)


operacao1 = Gatilhos()
operacao1.msg1() # Retornará normalmente a funcionalidade de msg1( ), método de classe de Gatilhos
operacao1.mensagem_2() # Graças ao getattr( ), como o método mensagem_2( ) não existe na classe Gatilhos, o interpretador delega essa função para o método mensagem_2( ) existente na classe Mensagem
