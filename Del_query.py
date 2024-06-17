'''
Arquivo para as minhas querys referentes para deletar um cliente, DELETE FROM.
'''

def delete_query(cod_cliente):
    delete_query = f"DELETE FROM clientes WHERE id = {cod_cliente};"
    return delete_query