# Problema de parøametros mutáveis em funções Python
def adiciona_clientes(nome, lista=None): # Não colocar valor padrão em parámetros mutáveis: lista=[] (não fazer porque a lista vai ser criada uma vez só na definição da função)
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


clientes1 = adiciona_clientes("luiz")
adiciona_clientes("Joana", clientes1)
adiciona_clientes("Fernanado", clientes1)
clientes1.append("Edu")
print(clientes1)

clientes2 = adiciona_clientes("Helena")
adiciona_clientes("Maria", clientes2)
print(clientes2)
