# dir, hasattr e getattr em Pythom
string = "Luiz"
metodo = "upper"

if hasattr(string, metodo):
    print("Existe", metodo)
    # print(string.upper())
    print(getattr(string, metodo)())
else:
    print("Não existe o método", metodo)
