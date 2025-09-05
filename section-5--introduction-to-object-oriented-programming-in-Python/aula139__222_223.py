# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class MinhaString(str):
#     def upper(self):
#         print("Chamou upper")
#         # return super().upper()
#         return super(MinhaString, self).upper()


# string = MinhaString("Luiz")
# print(string.upper())


class A:
    atributo_a = "valor a"

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print("A")


class B(A):
    atributo_b = "valor b"

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print("B")


class C(B):
    atributo_c = "valor c"

    def __init__(self, *args, **kwargs):
        print("EI, burlei o sistema")
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()  # supper é B
        super(B, self).metodo()  # supper é A
        # super(A, self).metodo()  # supper é object
        A.metodo(self)  # igual que super(B, self).metodo() mas nnao é recomendavel
        print("C")


c = C("Atributo", "Qualquer")
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print(c.atributo)
c.metodo()

print("Method Resolution Order: ", C.mro())
