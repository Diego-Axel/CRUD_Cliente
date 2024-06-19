'''
Arquivo para as minhas querys referentes para deletar um cliente, DELETE FROM.
'''

def delete_query():
    delete_query = "DELETE FROM clientes WHERE cod_cliente = %s"
    return delete_query