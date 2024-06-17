'''imports'''
import psycopg2
import Cr_querys #  Arquvio de consulta para a Criação da Tabela
import Del_query
import Insr_query #  Arquvio de consulta para a Inserção de Valores nas Tabelas
import Sel #  Arquvio de consulta para dar SELECT(s) na Tabela
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
        input("tecle <ENTER> para prosseguir ")

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


def exibir_cliente():
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
            print("Código Inexistente")

        
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgrSQL", error)
    finally:
        # Fechar Conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgrSQL fechada")
    
    print()
    input("tecle <ENTER> para prosseguir ")


def alterar_dados(): # Em desenvolvimento (está apresentado erros ainda. Estou fazendo a manutenção)
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="palmeiras123",
            host="localhost",
            port="5432",
            database="clientes"
        )
        cursor = connection.cursor()

        # Pedindo os Dados do Cliente a ser Alterado
        os.system('clear || cls')
        print()
        print("############################################")
        print("#####        Alterar Cliente            #####")
        print("############################################")
        print()
        cod_cliente = input("##### Digite o ID do cliente a ser alterado: ")
        print()
        nome_cliente = input("##### Nome: ")
        print()
        email = input("#### E-mail: ")
        print()
        celular = input("##### Digite seu Celular: ")
        print()
        cpf = input("##### CPF: ")

        # Atualizando Dados na Tabela:
        update_query = """
        UPDATE clientes 
        SET nome = %s, email = %s, celular = %s, cpf = %s 
        WHERE id = %s;
        """
        cursor.execute(update_query, (nome_cliente, email, celular, cpf, cod_cliente))
        connection.commit()
        print(f"Cliente com ID {cod_cliente} atualizado com sucesso")
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

def excluir_cliente(): # Em desenvolvimento (está apresentado erros ainda. Estou fazendo a manutenção)
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
        print("#####        Excluir Cliente            #####")
        print("############################################")
        print()
        cod_cliente = input("##### Digite o ID do cliente a ser excluído: ")

        # Excluindo Dados na Tabela:
        Del_query.delete_query(cod_cliente)
        cursor.execute(Del_query.delete_query())
        connection.commit()
        print(f"Cliente com ID {cod_cliente} excluído com sucesso")
        print()
        input("tecle <ENTER> para prosseguir ")


    finally:
        # Fechar Conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgreSQL fechada")


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
        input("tecle <ENTER> para prosseguir ")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgrSQL", error)
    finally:
        # Fechar Conexão
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com PostgrSQL fechada")