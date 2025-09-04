"""
Operação ternaria (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
condicao = 10 == 11
varaivel = 'valor' if condicao else 'Outro valor'
print(varaivel)

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('valor' if False else 'Outro valor' if False else 'Fim')
