'''
Arquivo para as minhas querys referentes a SELECT(s).
'''
def select_query():
    select_query = "SELECT cod_cliente, nome, email, celular, cpf FROM clientes WHERE cod_cliente = %s"
    return select_query


def select_full_query():
    select_full_query = "SELECT * FROM clientes;"
    return select_full_query


def where_query():
    select_where_query = "SELECT * FROM clientes WHERE cod_cliente = %d"
    return select_where_query