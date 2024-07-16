'''Arquivo referente a exibição dos dados dos clientes'''

'''imports'''
import interfaces as face
import psycopg2
import banco.sel_query as sel_query #  Arquvio de consulta para dar SELECT(s) na Tabela

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
        face.exibir_dados()
        print()
        cod_cliente = input("##### Digite o código do Cliente: ")
        if cod_cliente == '0':
            return
        sel_query.select_query() # Definindo a query de seleção
        cursor.execute(sel_query.select_query(), (cod_cliente,))
        records = cursor.fetchall()
        if records:
            print()
            face.dados_cliente()
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