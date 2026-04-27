'''Arquivo referente a Alteração dos Dados dos Clientes - Usando ORM'''

'''Imports'''
import interfaces as face
import validarores as validar # arquivo dos meus validadores
from banco.config import SessionLocal
from banco.models import Cliente

def alterar_dados(): # Manutenção Feita com ORM
    db = SessionLocal()
    try:
        face.alterar_dados()
        print()
        cod_cliente = input("##### Digite o ID do cliente a ser alterado: ")
        print()
        nome_cliente = input("##### Nome: ")
        print()
        verficador = True
        while verficador:
            email = input("#### E-mail: ")
            if validar.validar_email(email):
                print("E-mail válido!")
                verficador = False
            else:
                print("O e-mail não é válido, veja se você não esquceu o '@'/domínio/'.com'. Por favor digite novamente.")
                print()
        print()
        verficador = True
        while verficador:
            print("##### Digite o Celular com DDD e o 9 adicional seguinddo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
            celular = input("##### Digite seu Celular: ")
            if validar.validar_numero(celular):
                print("Número válido!")
                verficador = False
            else:
                print("Número não válido. Por favor, verifique se você colocou o número de acordo com o padrão e tente novamente")
                print()
        print()
        cpf = input("##### CPF: ")
        
        # Buscar e atualizar cliente com ORM
        cliente = db.query(Cliente).filter(Cliente.cod_cliente == int(cod_cliente)).first()
        
        if cliente:
            cliente.nome = nome_cliente
            cliente.email = email
            cliente.celular = celular
            cliente.cpf = cpf
            
            db.commit()
            print(f"Cliente com ID {cod_cliente} atualizado com sucesso")
        else:
            print(f"Cliente com ID {cod_cliente} não encontrado")
        
        print()
        input("tecle <ENTER> para prosseguir ")
    except Exception as error:
        db.rollback()
        print("Erro ao atualizar cliente:", error)
    finally:
        db.close()
        print("Conexão com PostgreSQL fechada")