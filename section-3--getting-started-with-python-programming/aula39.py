"""
Iterando strings com while
"""

nome = 'Luiz Otávio'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    novo_nome += f'*{nome[indice]}'
    indice += 1

novo_nome += '*'
print(novo_nome)
