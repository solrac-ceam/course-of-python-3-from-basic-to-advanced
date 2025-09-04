# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import aula97_m__155_156
from aula97_m__155_156 import variavel_module, soma

# print("Este módulo se chama", __name__)
print(aula97_m__155_156.variavel_module)
print(variavel_module)
print(soma(2, 3))
print(aula97_m__155_156.soma(2, 3))
