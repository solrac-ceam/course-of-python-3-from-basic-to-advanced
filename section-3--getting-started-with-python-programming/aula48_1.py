"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE' # 5 carateres

# print(bool([])) # falsy

#         0    1     2              3    4
#        -5   -4    -3             -2   -1
lista = [123, True, 'Luiz Otávio', 1.2, []]
# print(lista, type(lista))
lista[-3] = 'Maria'
print(lista)
