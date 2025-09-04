"""
Escopo de funções em pythom
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O espoco global é o escopo onde todo o ceodigo é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra glocal faz uma variável do escopo externo
ser a mesma no escopo  interno.
"""

x = 1


def escopo():
    # global x
    x = 10

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
