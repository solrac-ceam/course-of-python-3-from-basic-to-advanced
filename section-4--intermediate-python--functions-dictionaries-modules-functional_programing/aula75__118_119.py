# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebidp como parâmetro.


def criar_multiplicador(multiplicador):
    def multiplicar(x):
        return x * multiplicador

    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))
