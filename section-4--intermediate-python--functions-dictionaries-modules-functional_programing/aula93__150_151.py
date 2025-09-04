# Try, except, else e finally
try:
    a = 18
    a[3]
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Dividiu por zero")
except NameError:
    print("Nome b não definido")
except (TypeError, IndexError) as error:
    print("TypeError + IndexError")
    print("MSG", error)
    print("Nome", error.__class__.__name__)
except Exception as e:
    print("Erro desconhecido")

print("CONTINUAR")
