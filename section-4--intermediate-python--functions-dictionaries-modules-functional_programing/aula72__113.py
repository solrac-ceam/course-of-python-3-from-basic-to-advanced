# Exercícios com funções


# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)


# Crie uma função fala se um número é par ou impar.
# Retorne se o número é par ou ímpar.
def par_ou_impar(x):
    return "par" if x % 2 == 0 else "ímpar"


print(par_ou_impar(3))
print(par_ou_impar(6))
