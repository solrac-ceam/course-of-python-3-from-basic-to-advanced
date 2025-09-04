# Dictionary comprehension e Set Comprehension
produto = {
    "nome": "Caneta Azul",
    "preco": 2.5,
    "categoria": "Escritório",
}


dc = {chave: valor for chave, valor in produto.items()}
print(dc)


print()


dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}
print(dc)


print()


dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != "categoria"
}
print(dc)


print()


lista = [
    ("a", "valor a"),
    ("b", "valor a"),
    ("b", "valor a"),
]
dc = {chave: valor for chave, valor in lista}
print(dc)


print()


s1 = {2**i for i in range(10)}
print(s1)
