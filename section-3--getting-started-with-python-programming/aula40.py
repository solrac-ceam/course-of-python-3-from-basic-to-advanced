""" Calculadora com while """

while True:
    numero_1_str = input('Digite um número: ')
    numero_2_str = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    try:
        numero_1 = float(numero_1_str)
        numero_2 = float(numero_2_str)
        resultado = None
        
        if operador == '+':
            resultado = numero_1 + numero_2
        elif operador == '-':
            resultado = numero_1 - numero_2
        elif operador == '*':
            resultado = numero_1 * numero_2
        elif operador == '/':
            resultado = numero_1 / numero_2
        else:
            print(f'Operador {operador} não é valido')
        
        print(f'O resultado é: {resultado}')
    except:
        print('Um ou ambos os neumeros não são válidos')
    
    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    if sair:
        break

