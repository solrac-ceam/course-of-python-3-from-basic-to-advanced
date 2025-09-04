import random

for _ in range(20):
    nove_primeiros_digitos = []
    for i in range(9):
        nove_primeiros_digitos.append(random.randint(0, 9))

    peso = 10
    soma_ponderada = 0
    for digito in nove_primeiros_digitos:
        soma_ponderada += digito * peso
        peso -= 1

    primeiro_digito_cru = (soma_ponderada * 10) % 11
    primeiro_digito = primeiro_digito_cru if primeiro_digito_cru <= 9 else 0

    # print('O primeiro dígito do CPF é', primeiro_digito)

    dez_primeiros_digitos = nove_primeiros_digitos + [primeiro_digito]
    peso = 11
    soma_ponderada = 0
    for digito in dez_primeiros_digitos:
        soma_ponderada += digito * peso
        peso -= 1

    segundo_digito_cru = (soma_ponderada * 10) % 11
    segundo_digito = segundo_digito_cru if segundo_digito_cru <= 9 else 0

    # print('O segundo dígito do CPF é', segundo_digito)

    digitos_cpf = dez_primeiros_digitos + [segundo_digito]

    cpf = ''
    for digito in digitos_cpf:
        cpf += str(digito)
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    print(cpf)
