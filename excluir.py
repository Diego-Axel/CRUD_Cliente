'''Arquivo referente a exclusão dos Dados dos Clientes - Usando ORM'''

'''Imports'''
import interfaces as face
from banco.config import SessionLocal
from banco.models import Cliente

def excluir_cliente():
    db = SessionLocal()
    try:
        face.excluir_dados()
        print()
        cod_cliente = input("##### Digite o ID do cliente a ser excluído: ") # Pedindo o ID do cliente a ser excluído
        
        # Buscar e deletar cliente com ORM
        cliente = db.query(Cliente).filter(Cliente.cod_cliente == int(cod_cliente)).first()
        
        if cliente:
            db.delete(cliente)
            db.commit()
            print(f"Cliente com ID {cod_cliente} excluído com sucesso")
        else:
            print(f"Cliente com ID {cod_cliente} não encontrado")
        
        print()
        input("tecle <ENTER> para prosseguir ")
    except Exception as error:
        db.rollback()
        print("Erro ao excluir cliente:", error)
        input("tecle <ENTER> para prosseguir ")
    finally:
        db.close()
        print("Conexão com PostgreSQL fechada")