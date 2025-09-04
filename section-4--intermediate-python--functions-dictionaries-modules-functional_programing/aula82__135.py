def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


print(executa(lambda x, y: x + y, 2, 3))
print(executa(soma, 2, 3))
print(soma(2, 3))

print()

duplica1 = cria_multiplicador(2)
duplica2 = executa(lambda multiplicador: lambda numero: numero * multiplicador, 2)

print(duplica1(4))
print(duplica2(4))
