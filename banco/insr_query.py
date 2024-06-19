'''
Arquivo para as minhas querys referentes a inserção de valores nas tabelas, INSERT INTO.
'''
def insert_into():
    insert_query = '''
        INSERT INTO clientes (nome, email, celular, cpf, ativo)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING cod_cliente;
        '''
    return insert_query