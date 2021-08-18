from dataclasses import dataclass

@dataclass # Irá auto gerar os métodos construtores e repr, associando seus respectivos objetos de classe
class Pessoa2:
    nome: str
    idade: int

pessoa2 = Pessoa2('Fernando', 34)

print(pessoa2)
