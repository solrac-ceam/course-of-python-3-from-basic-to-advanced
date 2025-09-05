# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # attributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def methodo_de_classe(cls):
        print("Hey")

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônima", idade)


print(Pessoa.ano)

p1 = Pessoa("João", 34)
p2 = Pessoa.criar_com_50_anos("Helena")
p3 = Pessoa.criar_sem_nome(25)

p1.methodo_de_classe()
Pessoa.methodo_de_classe()
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
