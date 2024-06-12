'''imports'''
import psycopg2
import Cr_querys #  Arquvio de consulta para a Criação da Tabela
import Insr_query
import Sel
import os


def cadastrar_cliente():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="palmeiras123",
            host="localhost",
            port="5432",
            database="clientes"
        )
        cursor = connection.cursor()

        # Criar Tabela
        Cr_querys.create_table()

        cursor.execute(Cr_querys.create_table())
        connection.commit()

        # Pedindo os Dados:
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####        Cadastrar Cliente         #####")
        print("############################################")
        print()
        nome_cliente = input("##### Nome: ")
        print()
        email = input("#### E-mail: ")
        print()
        celular = input("##### Digite seu Celular: ")
        print()
        cpf = input("##### CPF: ")
        print()
        ativo = True

        # Inserindo Dados na Tabela:
        Insr_query.insert_into()

        cursor.execute(Insr_query.insert_into(), (nome_cliente, email, celular, cpf, ativo))
        cod_cliente_inserido = cursor.fetchone()[0]
        connection.commit()
        print(f"Dado Salvo com sucesso, inserido com o ID: {cod_cliente_inserido}")
        print()
        input("tecle <ENTER> para prosseguir")

        # Consultar os dados inseridos
        # Sel.select_query()
        # cursor.execute(Sel.select_query())
        # records = cursor.fetchall()

        # print("Dados na Tabela 'clientes': ")
        # for row in records:
        #     print(f"ID: {row[0]}, Cliente: {row[1]}, E-mail: {row[2]}, Celular: {row[3]}, CPF: {row[4]}")
        # print()
        # input("tecle <ENTER> para prosseguir")
        
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgrSQL", error)
    finally:
        # Fechar Conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgrSQL fechada")


def exibit_cliente():
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
        print("#######################################")
        print("#####   EXIBIR DADOS DO CLIENTE   #####")
        print("#######################################")
        print("#####   0 - RETORNA AO MENU       #####")
        print("#######################################")
        print()
        cod_cliente = input("##### Digite o código do Cliente: ")
        Sel.where_query()
        cursor.execute(Sel.where_query(), (cod_cliente))
        records = cursor.fetchall()
        if (Sel.where_query() in records):
            print()
            print("#######################################################################################################################################")
            print("#################################################         Relatório de Clientes           #############################################")
            print("#######################################################################################################################################")
            print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
            print("| Cod |               Nome Completo                 |                    E-mail                   |      Celular     |       CPF      |")
            print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
            # print("| %-3s "%(Sel.where_query[0]), end="")
            # print("| %-43s "%(Sel.where_query[1]), end="")
            # print("| %-43s "%(Sel.where_query[2]), end="")
            # print("| %-16s "%(Sel.where_query[3]), end="")
            # print("| %-14s "%(Sel.where_query[4]))
            print("---------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("NAO")

        
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgrSQL", error)
    finally:
        # Fechar Conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgrSQL fechada")
    
    print()
    input("tecle <ENTER> para prosseguir")


def relatorio_clientes():
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
        Sel.select_query()
        cursor.execute(Sel.select_query())
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
        input("tecle <ENTER> para prosseguir")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgrSQL", error)
    finally:
        # Fechar Conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgrSQL fechada")

























# def cadastrar_cliente():
#     try:
#         connection = psycopg2.connect(
#             user="postgres",
#             password="palmeiras123",
#             host="localhost",
#             port="5432",
#             database="clientes"
#         )
#         cursor = connection.cursor()

#         # Criar Tabela
#         create_table_query = '''
#         CREATE TABLE IF NOT EXISTS clientes(
#             cod_cliente SERIAL PRIMARY KEY,
#             nome VARCHAR(60),
#             email VARCHAR(40),
#             celular VARCHAR(25),
#             cpf VARCHAR(20),
#             ativo BOOLEAN
#         );
#         '''
#         cursor.execute(create_table_query)
#         connection.commit()

#         # Pedindo os Dados:
#         os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
#         print()
#         print("############################################")
#         print("#####        Cadastrar Cliente         #####")
#         print("############################################")
#         print()
#         nome_cliente = input("##### Nome: ")
#         print()
#         email = input("#### E-mail: ")
#         print()
#         celular = input("##### Digite seu Celular: ")
#         print()
#         cpf = input("##### CPF: ")
#         print()
#         ativo = True

#         # Inserindo Dados na Tabela:
#         insert_query = '''
#         INSERT INTO clientes (nome, email, celular, cpf, ativo)
#         VALUES (%s, %s, %s, %s, %s)
#         RETURNING cod_cliente;
#         '''
#         cursor.execute(insert_query, (nome_cliente, email, celular, cpf, ativo))
#         cod_cliente_inserido = cursor.fetchone()[0]
#         connection.commit()
#         print(f"Dado Salvo com sucesso, inserido com o ID: {cod_cliente_inserido}")

#         # Consultar os dados inseridos
#         select_query = "SELECT * FROM clientes;"
#         cursor.execute(select_query)
#         records = cursor.fetchall()

#         print("Dados na Tabela 'clientes': ")
#         for row in records:
#             print(f"ID: {row[0]}, Cliente: {row[1]}, E-mail: {row[2]}, Celular: {row[3]}, CPF: {row[4]}")
#             print("Carregando...")
        
#     except (Exception, psycopg2.Error) as error:
#         print("Erro ao conectar ou operar no PostgrSQL", error)
#     finally:
#         # Fechar Conexão
#         if connection:
#             cursor.close()
#             connection.close()
#             print("Conexão com PostgrSQL fechada")