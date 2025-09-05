# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value

    def descrever(self):
        print(self.nome, self._fabricante.nome, self._motor.nome)


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro("Fusca")
volkswagen = Fabricante("Volkswagen")
motor_1_0 = Motor("1.0")
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
fusca.descrever()

gol = Carro("Gol")
gol.fabricante = volkswagen
gol.motor = motor_1_0
gol.descrever()

fiat_uno = Carro("Uno")
fiat = Fabricante("Fiat")
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
fiat_uno.descrever()

focus = Carro("Focus Titanium")
ford = Fabricante("Ford")
motor_2_0 = Motor("2.0")
focus.fabricante = ford
focus.motor = motor_2_0
focus.descrever()
