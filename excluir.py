'''Arquivo referente a exclusão dos Dados dos Clientes'''

'''Imports'''
import psycopg2
import del_query #  Arquvio de consulta para a Deletação de Cliente
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

        # Pedindo o ID do cliente a ser excluído
        os.system('clear || cls')
        print()
        print("############################################")
        print("#####          Excluir Cliente         #####")
        print("############################################")
        print()
        cod_cliente = input("##### Digite o ID do cliente a ser excluído: ")

        # Definindo a query de exclusão
        del_query.delete_query()

        # Executando a query de exclusão
        cursor.execute(del_query.delete_query(), (cod_cliente,))
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