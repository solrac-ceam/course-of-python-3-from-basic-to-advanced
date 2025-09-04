import sys

import aula99_package__158_to_160.modulo
from aula99_package__158_to_160.modulo import soma_do_modulo
from aula99_package__158_to_160 import modulo
from aula99_package__158_to_160.modulo import *

# print(*sys.path, sep="\n")
print(soma_do_modulo(1, 2))
print(aula99_package__158_to_160.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
# print(nova_variavel)  # Não é importada usando o * porque no modulo não esta dentro da lista __all__

from aula99_package__158_to_160.modulo_b import fala_oi

print(__name__)
fala_oi()

from aula99_package__158_to_160 import soma_do_modulo, fala_oi

print(soma_do_modulo(2, 3))
fala_oi()
