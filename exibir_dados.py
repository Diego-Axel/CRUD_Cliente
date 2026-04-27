'''Arquivo referente a exibição dos dados dos clientes - Usando ORM'''

'''imports'''
import interfaces as face
from banco.config import SessionLocal
from banco.models import Cliente

def exibir_cliente():
    db = SessionLocal()
    try:
        face.exibir_dados()
        print()
        cod_cliente = input("##### Digite o código do Cliente: ")
        if cod_cliente == '0':
            return
        
        # Buscar cliente com ORM
        cliente = db.query(Cliente).filter(Cliente.cod_cliente == int(cod_cliente)).first()
        
        if cliente:
            print()
            face.dados_cliente()
            print("| %-3s "%(cliente.cod_cliente), end="")
            print("| %-43s "%(cliente.nome), end="")
            print("| %-43s "%(cliente.email), end="")
            print("| %-16s "%(cliente.celular), end="")
            print("| %-14s "%(cliente.cpf))
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print()
        else:
            print("Código Inexistente")
    except Exception as error:
        print("Erro ao consultar cliente:", error)
    finally:
        db.close()
        print("Conexão com PostgreSQL fechada")
    print()
    input("tecle <ENTER> para prosseguir ")