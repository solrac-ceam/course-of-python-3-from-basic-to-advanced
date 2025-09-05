# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, asdict, astuple, field, fields

# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str

#     @property
#     def nome_completo(self) -> str:
#         return f"{self.nome} {self.sobrenome}"
    
#     @nome_completo.setter
#     def nome_completo(self, nome_completo: str) -> None:
#         nome, sobrenome = nome_completo.split(" ", 1)
#         self.nome = nome
#         self.sobrenome = sobrenome


# pessoa1 = Pessoa("Luiz", "Otávio")
# pessoa1.nome_completo = "Maria Helena Figueredo"
# print(pessoa1)
# print(pessoa1.nome_completo)




# @dataclass(init=False)
# class Pessoa:
#     nome: str
#     sobrenome: str

#     def __init__(self, nome: str, sobrenome: str) -> None:
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.nome_completo = f"{self.nome} {self.sobrenome}"

#     def __post_init__(self) -> None:
#         print("POST INIT")


# pessoa1 = Pessoa("Luiz", "Otávio")
# print(pessoa1)
# print(pessoa1.nome_completo)




# @dataclass(frozen=True)
# class Pessoa:
#     nome: str
#     sobrenome: str


# pessoa1 = Pessoa("Luiz", "Otávio")
# pessoa1.nome = "Maria"  # Isso vai gerar um erro, pois a classe é imutável
# print(pessoa1)




# @dataclass(order=True)
# class Pessoa:
#     nome: str
#     sobrenome: str

# pessoas = [
#     Pessoa("Luiz", "Otávio"),
#     Pessoa("Maria", "Helena"),
#     Pessoa("João", "Silva"),
# ]
# possoas_ordenadas = sorted(pessoas)
# print(possoas_ordenadas)




# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str


# pessoa1 = Pessoa("Luiz", "Otávio")
# print(asdict(pessoa1))  # Converte a dataclass em um dicionário
# print(astuple(pessoa1))  # Converte a dataclass em uma tupla




@dataclass
class Pessoa:
    nome: str = field(default="Missing", repr=False)
    sobrenome: str = "Not sent"
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


pessoa1 = Pessoa()
print(pessoa1)
print(fields(pessoa1))  # Mostra os campos da dataclass
