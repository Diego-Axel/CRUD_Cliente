

'''imports'''
import os


def menu_cliente():
    os.system('clear || cls')
    print()
    print("############################################")
    print("#####   Você está no Módulo Clientes   #####")
    print("############################################")
    print("##### 1 - Cadastrar Cliente            #####")
    print("##### 2 - Exibir Dados do Cliente      #####")
    print("##### 3 - Alterar Dados do Cliente     #####")
    print("##### 4 - Excluir Cliente              #####")
    print("##### 0 - Encerrar Programa            #####")
    print("############################################")
    print()
    op_cliente = input("##### Escolha sua opção: ")
    return op_cliente