'''
Arquivo para as minhas querys referentes para Alterar os dados do Cliente, UPDATE
'''

def update_query():
    update_query = """
        UPDATE clientes
        SET nome = %s, email = %s, celular = %s, cpf = %s
        WHERE cod_cliente = %s
        """
    return update_query


def update_query_nome():
    update_query_nome = '''
        UPDATE clientes
        SET nome = %s
        WHERE cod_cliente = %d
        '''
    return update_query_nome


def update_query_email():
    update_query_email = '''
        UPDATE clientes
        SET email = %s
        WHERE cod_cliente = %d
        '''
    return update_query_email


def update_query_celular():
    update_query_celular = '''
        UPDATE clientes
        SET celular = %s
        WHERE cod_cliente = %d
        '''
    return update_query_celular


def update_query_cpf():
    update_query_cpf = '''
        UPDATE clientes
        SET cpf = %s
        WHERE cod_cliente = %d
        '''
    return update_query_cpf