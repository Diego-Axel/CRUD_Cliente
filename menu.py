'''
Arquivo para a minha "interface" de clientes
'''

'''imports'''
import os

def menu_cliente():
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####   Você está no Módulo Clientes   #####")
    print("############################################")
    print("##### 1 - Cadastrar Cliente            #####")
    print("##### 2 - Exibir Dados do Cliente      #####")
    print("##### 3 - Alterar Dados do Cliente     #####")
    print("##### 4 - Excluir Cliente              #####")
    print("##### 5 - Relatório de Clientes        #####")
    print("##### 0 - Encerrar Programa            #####")
    print("############################################")
    print()
    op_cliente = input("##### Escolha sua opção: ")
    return op_cliente