"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com signal de igual 
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição
def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y)


soma(1, 2, 3)
soma(2, 1, 3)
soma(y=2, z=3, x=1)
soma(1, 2, z=5)

