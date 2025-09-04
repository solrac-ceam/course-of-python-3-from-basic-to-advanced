"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um neumero inteiro: ')
try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print('O neumero digitado é par')
    else:
        print('O neumero digitado é ímpar')
except:
    print('O numero digitado não é um inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora em números inteiros: ')
try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('A hora digitada não é correta')
except:
    print('O numero digitado não é um inteiro')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
hora = input('Digite seu primeiro nome: ')
largura_nome = len(hora)
if largura_nome >= 1:
    if largura_nome <= 4:
        print('Seu nome é curto')
    elif largura_nome >= 5 and largura_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite pelo menos uma letra')
