# Try, except, else e finally
try:
    print("Abrir arquivo")
    8 / 0
except ZeroDivisionError:
    print("Dividiu zero")
except IndexError:
    print("IndexError")
except (NameError, ImportError):
    print("NameError, ImportError")
else:
    print("Não deu erro")
finally:
    print("Fechar arquivo")
