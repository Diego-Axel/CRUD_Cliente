'''
Arquivo para as minhas querys referentes a criação de tabelas
'''
def create_table():
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS clientes(
        cod_cliente SERIAL PRIMARY KEY,
        nome VARCHAR(60),
        email VARCHAR(40),
        celular VARCHAR(25),
        cpf VARCHAR(20),
        ativo BOOLEAN
    );
    '''
    return create_table_query