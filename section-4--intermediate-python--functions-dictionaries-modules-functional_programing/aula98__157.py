import importlib

import aula98_m__157

print(aula98_m__157.variavel)

for i in range(10):
    importlib.reload(aula98_m__157)
    print(i)

print("Fim")
