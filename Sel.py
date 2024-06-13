'''
Arquivo para as minhas querys referentes a SELECT(s).
'''

def select_query():
    select_query = "SELECT * FROM clientes;"
    return select_query


def where_query():
    select_where_query = "SELECT * FROM clientes WHERE cod_cliente = %s"
    return select_where_query