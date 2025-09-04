frase = 'O Python é uma linguiagem de programação ' \
    'multiparadigma. ' \
    'Python foi craido por Guido van Rossum.'

i = 0
letra_mais_frequente = ''
frequencia_da_letra_mais_frequente = 0
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual != ' ':
        frequencia_letra_atual = frase.count(letra_atual)

        if frequencia_letra_atual > frequencia_da_letra_mais_frequente:
            letra_mais_frequente = letra_atual
            frequencia_da_letra_mais_frequente = frequencia_letra_atual
    
    i += 1

print(f'A letra mais frequente é: {letra_mais_frequente}, '
      f'com {frequencia_da_letra_mais_frequente} aprições')
