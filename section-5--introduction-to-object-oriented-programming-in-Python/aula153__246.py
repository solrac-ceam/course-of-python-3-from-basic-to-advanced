# Método especial __call__
# callable  é a;go que pode ser executado com parênteses
# Em classes normais, __call__ faz a instancia de uma
# classe "callable".
class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, nome):
        print(nome, "está chamando,", self.phone)
        return 2134


call_me = CallMe("23945876545")
retorno = call_me("Luiz Otávio")
print(retorno)
