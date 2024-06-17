'''
Arquivo para as minhas querys referentes para Alterar os dados do Cliente, UPDATE
'''

def update_query():
    update_query = """
        UPDATE clientes 
        SET nome = %s, email = %s, celular = %s, cpf = %s 
        WHERE id = %s;
        """
    return update_query