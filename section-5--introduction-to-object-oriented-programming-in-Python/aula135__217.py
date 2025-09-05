# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._productos = []

    def total(self):
        return sum([p.preco for p in self._productos])

    def inserir_produtos(self, *produtos):
        # self._productos.extend(produtos)
        # self._productos += produtos
        for produto in produtos:
            self._productos.append(produto)

    def listar_protutos(self):
        for produto in self._productos:
            print(produto.nome, produto.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()

p1, p2 = Produto("caneta", 1.20), Produto("Camiseta", 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_protutos()
print(carrinho.total())
