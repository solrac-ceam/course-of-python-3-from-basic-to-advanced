"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista.
"""
import os

lista_de_comprar = []

while True:
    opcao = input('Selecione uma opção\n[i]nserir, [a]pagar, [l]istar: ')
    opcao = opcao.lower()
    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista_de_comprar.append(valor)
    elif opcao == 'a':
        indice_str = input('escolha o indice para apagar: ')
        try:
            indice = int(indice_str)
            del lista_de_comprar[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista_de_comprar) == 0:
            print('Nada para listar')
        
        for i, item in enumerate(lista_de_comprar):
            print(i, item)
    else:
        print('Por favor, escolha i, a ou l.')
