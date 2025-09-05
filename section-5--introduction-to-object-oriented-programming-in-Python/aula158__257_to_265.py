"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: str, numero: str, saldo: float = 0.0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass

    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        self.detalhes(f"Depósito de {valor:.2f} realizado.")
        return self.saldo
    
    def detalhes(self, msg: str = "") -> None:
        print(f"Agência: {self.agencia}, Número: {self.numero},"
              f" Saldo: {self.saldo:.2f} - {msg}")

    def __repr__(self) -> str:
        return (f"Conta(agencia={self.agencia}, numero={self.numero},"
                f" saldo={self.saldo:.2f})")


class ContaCorrente(Conta):
    def __init__(
            self, 
            agencia: str, 
            numero: str, 
            saldo: float = 0.0, 
            limite: float = 0.0
        ):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        if valor > self.saldo + self.limite:
            self.detalhes(f"Saque não realizado. Saldo mais limit"
                          f" insuficiente. Valor solicitado: {valor:.2f};"
                          f" limite: {-self.limite:.2f}")
            return self.saldo
        
        self.saldo -= valor
        self.detalhes(f"Saque de {valor:.2f} realizado.")
        return self.saldo


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        if valor > self.saldo:
            self.detalhes(f"Saque não realizado. Saldo insuficiente."
                          f" Valor solicitado: {valor:.2f}")
            return self.saldo
            
        self.saldo -= valor
        self.detalhes(f"Saque de {valor:.2f} realizado.")
        return self.saldo
    

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome
    
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta

    def __repr__(self) -> str:
        return (f"Cliente(nome={self.nome}, idade={self.idade},"
                f" conta={self.conta!r})")


class Banco:
    def __init__(
            self, 
            nome: str, 
            agencias: list[str] | None = None,
        ):
        self.nome = nome
        self.agebcias = agencias or []
        self.clientes: list[Cliente] = []
        self.contas: list[Conta] = []
        self.conta_sequencial = 1
        
    def autenticar_cliente(self, cliente: Cliente) -> bool:
        if (cliente.conta.agencia not in self.agebcias 
            or cliente not in self.clientes 
            or cliente.conta not in self.contas
        ):
            return False
        return True
    
    def sacar(self, cliente: Cliente, valor: float) -> float:
        if not self.autenticar_cliente(cliente):
            print("Cliente não autenticado.")
            return 0.0
        return cliente.conta.sacar(valor)
    
    def depositar(self, cliente: Cliente, valor: float) -> float:
        if not self.autenticar_cliente(cliente):
            print("Cliente não autenticado.")
            return 0.0
        return cliente.conta.depositar(valor)
    
    def abrir_conta(
            self, 
            pessoa: Pessoa, 
            agencia: str, 
            tipo: str,
            limite: float = 0.0,
    ) -> Cliente:
        if agencia not in self.agebcias:
            raise ValueError(f"Agência {agencia} não pertence a este banco.")
        
        if tipo == "poupanca":
            conta = ContaPoupanca(agencia, f"{self.conta_sequencial:05d}-0")
        elif tipo == "corrente":
            conta = ContaCorrente(
                agencia, f"{self.conta_sequencial:05d}-0", limite=limite
            )
        else:
            raise ValueError("Tipo de conta inválido.")
        
        self.contas.append(conta)
        cliente = Cliente(pessoa.nome, pessoa.idade, conta)
        self.clientes.append(cliente)
        self.conta_sequencial += 1
        
        print(f"Conta {tipo} aberta com sucesso para {pessoa.nome}.")
        conta.detalhes()
        
        return cliente
   

# Exemplo de uso
print("criando bancos")
banco1 = Banco("Banco Exemplo", agencias=["001", "002"])
banco2 = Banco("Banco Exemplo 2", agencias=["003", "004"])

print("criando clientes e contas")
cliente1 = banco1.abrir_conta(Pessoa("Alice", 30), "001", "poupanca")
cliente2 = banco1.abrir_conta(Pessoa("Bob", 25), "002", "corrente", limite=200.0)
cliente3 = banco2.abrir_conta(Pessoa("Charlie", 40), "003", "corrente", limite=100.0)

print(f"realizando operações bancárias {cliente1}")
banco1.sacar(cliente1, 50.0)  # Deve falhar, saldo inicial é 0
banco1.depositar(cliente1, 100.0)  # Deposita 100 na conta poupança de Alice
banco1.sacar(cliente1, 50.0)  # Deve funcionar agora

print(f"realizando operações bancárias {cliente2}")
banco1.sacar(cliente2, 50.0)  # Deve funcionar, saldo inicial é 0, mas limite é 200
banco1.depositar(cliente2, 300.0)  # Deposita 300 na conta corrente de Bob
banco1.sacar(cliente2, 100.0)  # Deve funcionar, saldo agora é 250

print(f"realizando operações bancárias {cliente3}")
banco1.sacar(cliente3, 50.0)  # Deve falhar, cliente não pertence ao banco1
banco1.depositar(cliente3, 150.0)  # Deve falhar, cliente não pertence ao banco1
