'''Arquivo referente a exibição dos dados dos clientes'''

'''imports'''
import psycopg2
import sel_query #  Arquvio de consulta para dar SELECT(s) na Tabela
import os

def exibir_cliente():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            user="postgres",
            password="palmeiras123",
            host="localhost",
            port="5432",
            database="clientes"
        )
        cursor = connection.cursor()
        
        os.system('clear || cls')  # use 'clear' no Linux e 'cls' no Windows
        print("#######################################")
        print("#####   EXIBIR DADOS DO CLIENTE   #####")
        print("#######################################")
        print("#####   0 - RETORNA AO MENU       #####")
        print("#######################################")
        print()
        cod_cliente = input("##### Digite o código do Cliente: ")
        
        if cod_cliente == '0':
            return
        
        # Definindo a query de seleção
        sel_query.select_query()
        
        cursor.execute(sel_query.select_query(), (cod_cliente,))
        records = cursor.fetchall()
        
        if records:
            print()
            print("#######################################################################################################################################")
            print("#################################################         Relatório de Clientes           #############################################")
            print("#######################################################################################################################################")
            print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
            print("| Cod |               Nome Completo                 |                    E-mail                   |      Celular     |       CPF      |")
            print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
            for row in records:
                print("| %-3s "%(row[0]), end="")
                print("| %-43s "%(row[1]), end="")
                print("| %-43s "%(row[2]), end="")
                print("| %-16s "%(row[3]), end="")
                print("| %-14s "%(row[4]))
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print()
        else:
            print("Código Inexistente")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)
    finally:
        # Fechar Conexão
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Conexão com PostgreSQL fechada")
    
    print()
    input("tecle <ENTER> para prosseguir ")