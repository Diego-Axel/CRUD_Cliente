'''Arquivo referente ao cadastro de clientes'''

'''Imports'''
import psycopg2
import banco.cr_querys as cr_querys #  Arquvio de consulta para a Criação da Tabela
import banco.insr_query as insr_query #  Arquvio de consulta para a Inserção de Valores nas Tabelas
import os

def cadastro(): # Manutenção Feita. Em funcionamento.
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
        cr_querys.create_table()

        cursor.execute(cr_querys.create_table())
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
        insr_query.insert_into()

        cursor.execute(insr_query.insert_into(), (nome_cliente, email, celular, cpf, ativo))
        cod_cliente_inserido = cursor.fetchone()[0]
        connection.commit()
        print(f"Dado Salvo com sucesso, inserido com o ID: {cod_cliente_inserido}")
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