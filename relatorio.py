'''Arquivo referente ao Relatório de todos os meus clientes'''

'''imports'''
import psycopg2
import banco.sel_query as sel_query #  Arquvio de consulta para dar SELECT(s) na Tabela
import os


def relatorio_clientes(): # Manutenção Feita. Em funcionamento.
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="palmeiras123",
            host="localhost",
            port="5432",
            database="clientes"
        )
        cursor = connection.cursor()
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("#######################################################################################################################################")
        print("#################################################         Relatório de Clientes           #############################################")
        print("#######################################################################################################################################")
        print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
        print("| Cod |               Nome Completo                 |                    E-mail                   |      Celular     |       CPF      |")
        print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
        # Consultar os dados inseridos
        sel_query.select_full_query()
        cursor.execute(sel_query.select_full_query())
        records = cursor.fetchall()
        for row in records:
            # print(f"ID: {row[0]}, Cliente: {row[1]}, E-mail: {row[2]}, Celular: {row[3]}, CPF: {row[4]}")
            print("| %-3s "%(row[0]), end="")
            print("| %-43s "%(row[1]), end="")
            print("| %-43s "%(row[2]), end="")
            print("| %-16s "%(row[3]), end="")
            print("| %-14s "%(row[4]))
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        print()
        input("tecle <ENTER> para prosseguir ")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgrSQL", error)
    finally:
        # Fechar Conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgrSQL fechada")