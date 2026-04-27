'''Arquivo referente ao Relatório de todos os meus clientes - Usando ORM'''

'''imports'''
import interfaces as face
from banco.config import SessionLocal
from banco.models import Cliente

def relatorio_clientes(): # Manutenção Feita com ORM. Em funcionamento.
    db = SessionLocal()
    try:
        face.dados_cliente()
        
        # Consultar todos os clientes com ORM
        clientes = db.query(Cliente).order_by(Cliente.cod_cliente).all()
        
        if clientes:
            for cliente in clientes:
                print("| %-3s "%(cliente.cod_cliente), end="")
                print("| %-43s "%(cliente.nome), end="")
                print("| %-43s "%(cliente.email), end="")
                print("| %-16s "%(cliente.celular), end="")
                print("| %-14s "%(cliente.cpf))
            print("---------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("Nenhum cliente cadastrado")
        
        print()
        input("tecle <ENTER> para prosseguir ")
    except Exception as error:
        print("Erro ao consultar clientes:", error)
    finally:
        db.close()
        print("Conexão com PostgreSQL fechada")