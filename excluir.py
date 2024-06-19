'''Arquivo referente a exclusão dos Dados dos Clientes'''

'''Imports'''
import psycopg2
import banco.del_query as del_query #  Arquvio de consulta para a Deletação de Cliente
import os


def excluir_cliente():
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
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####          Excluir Cliente         #####")
        print("############################################")
        print()
        cod_cliente = input("##### Digite o ID do cliente a ser excluído: ") # Pedindo o ID do cliente a ser excluído
        del_query.delete_query() # Definindo a query de exclusão
        cursor.execute(del_query.delete_query(), (cod_cliente,)) # Executando a query de exclusão
        connection.commit()
        print(f"Cliente com ID {cod_cliente} excluído com sucesso")
        print()
        input("tecle <ENTER> para prosseguir ")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)
        input("tecle <ENTER> para prosseguir ")
    finally:
        # Fechar Conexão
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Conexão com PostgreSQL fechada")