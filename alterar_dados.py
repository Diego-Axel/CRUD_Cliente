'''Arquivo referente a Alteração dos Dados dos Clientes'''

'''Imports'''
import psycopg2
import banco.up_query as up_query #  Arquvio de consulta para a Alteração dos Dados do Cliente
import validarores as validar # arquivo dos meus validadores
import os


def alterar_dados(): # Manutenção Feita
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
        print("#############################################") # Pedindo os Dados do Cliente a ser Alterado
        print("#####           Alterar Cliente         #####")
        print("#############################################")
        print()
        cod_cliente = input("##### Digite o ID do cliente a ser alterado: ")
        print()
        nome_cliente = input("##### Nome: ")
        print()
        verficador = True
        while verficador:
            email = input("#### E-mail: ")
            if validar.validar_email(email):
                print("E-mail válido!")
                verficador = False
            else:
                print("O e-mail não é válido, veja se você não esquceu o '@'/domínio/'.com'. Por favor digite novamente.")
                print()
        print()
        celular = input("##### Digite seu Celular: ")
        print()
        cpf = input("##### CPF: ")
        up_query.update_query() # Definindo a query de atualização
        cursor.execute(up_query.update_query(), (nome_cliente, email, celular, cpf, cod_cliente))
        connection.commit()
        print(f"Cliente com ID {cod_cliente} atualizado com sucesso")
        print()
        input("tecle <ENTER> para prosseguir ")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ou operar no PostgreSQL", error)
    finally:
        # Fechar Conexão
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Conexão com PostgreSQL fechada")