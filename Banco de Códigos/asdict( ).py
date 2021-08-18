# Convertendo uma dataclass para dicionário por questões de compatibilidade

from dataclasses import dataclass, asdict

@dataclass
class Pessoa4:
    nome: str
    idade: int

pessoa4 = Pessoa4('Fernando', 34)
print(pessoa4)
print(asdict(pessoa4))
