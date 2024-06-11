'''imports'''
import psycopg2
import Cr_querys #  Arquvio de consulta para a Criação da Tabela
import Insr_query
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

        # Consultar os dados inseridos
        select_query = "SELECT * FROM clientes;"
        cursor.execute(select_query)
        records = cursor.fetchall()

        print("Dados na Tabela 'clientes': ")
        for row in records:
            print(f"ID: {row[0]}, Cliente: {row[1]}, E-mail: {row[2]}, Celular: {row[3]}, CPF: {row[4]}")
            print("Carregando...")
        
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