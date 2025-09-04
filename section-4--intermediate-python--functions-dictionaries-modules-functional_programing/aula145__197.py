# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)


# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
def soma(x, y, /, c):
    print(x + y + c)


# soma(1, y=2, c=3)  # errado; não pode nomear nem "x" nem "y"
soma(1, 2, c=3)  # certo
soma(1, 2, 3)  # certo
print()


# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def soma(a, b, *, c):
    print(a + b + c)


# soma(1, 2, 3)  # errado; só "a" e "b" podem ser argumentos posicionais, "c" tem que ser nomeado
soma(1, 2, c=3)  # certo
soma(1, b=2, c=3)  # certo
print()


# Combinando "/" e "*"
def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome="teste")
