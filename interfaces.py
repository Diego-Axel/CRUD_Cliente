''' Arquivo para as minhas 'interfaces' gráficas'''

import os

def dados_cliente():
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print("#######################################################################################################################################")
    print("#################################################         Relatório de Clientes           #############################################")
    print("#######################################################################################################################################")
    print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
    print("| Cod |               Nome Completo                 |                    E-mail                   |      Celular     |       CPF      |")
    print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")


def cadastrar_dados():
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print("############################################")
    print("#####        Cadastrar Cliente         #####")
    print("############################################")


def exibir_dados():
    os.system('clear || cls')  # use 'clear' no Linux e 'cls' no Windows
    print("#######################################")
    print("#####   EXIBIR DADOS DO CLIENTE   #####")
    print("#######################################")
    print("#####     0 - RETORNA AO MENU     #####")
    print("#######################################")


def alterar_dados():
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print("#############################################") 
    print("#####           Alterar Cliente         #####")
    print("#############################################")


def excluir_dados():
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print("############################################")
    print("#####          Excluir Cliente         #####")
    print("############################################")