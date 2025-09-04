# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = "nome"
pessoa[chave] = "Luiz Otávio"
pessoa["sobrenome"] = "Miranda"

print(pessoa[chave])

pessoa[chave] = "Maria"

del pessoa["sobrenome"]
print(pessoa)

valor = pessoa.get("sobrenome")
if valor is None:
    print(" Não existe")
else:
    print(valor)

