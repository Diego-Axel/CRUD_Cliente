'''Arquivo referente ao cadastro de clientes - Usando ORM'''

'''Imports'''
import interfaces as face
import validarores as validar # arquivo dos meus validadores
from banco.config import SessionLocal, Base, engine
from banco.models import Cliente

def criar_tabelas():
    """Criar todas as tabelas se não existirem"""
    Base.metadata.create_all(bind=engine)

def cadastro(): # Manutenção Feita. Em funcionamento com ORM.
    db = SessionLocal()
    try:
        # Criar tabela se não existir
        criar_tabelas()
        
        # Pedindo os Dados:
        face.cadastrar_dados()
        print()
        nome_cliente = input("##### Nome: ")
        print()
        verificador = True
        while verificador:   
            email = input("#### E-mail: ")
            if validar.validar_email(email):
                print("E-mail válido!")
                verificador = False
            else:
                print("O e-mail não é válido, veja se você não esquceu o '@'/domínio/'.com'. Por favor digite novamente.")
                print()
        print()
        verificador = True
        while verificador:
            print("##### Digite o Celular com DDD e o 9 adicional seguinddo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
            celular = input("##### Digite seu Celular: ")
            if validar.validar_numero(celular):
                print("Número válido!")
                verificador = False
            else:
                print("Número não válido. Por favor, verifique se você colocou o número de acordo com o padrão e tente novamente")
                print()
        print()
        cpf = input("##### CPF: ")
        print()
        
        # Criar novo cliente com ORM
        novo_cliente = Cliente(
            nome=nome_cliente,
            email=email,
            celular=celular,
            cpf=cpf,
            ativo=True
        )
        
        db.add(novo_cliente)
        db.commit()
        db.refresh(novo_cliente)
        
        print(f"Dado Salvo com sucesso, inserido com o ID: {novo_cliente.cod_cliente}")
        print()
        input("tecle <ENTER> para prosseguir ")    
    except Exception as error:
        db.rollback()
        print("Erro ao cadastrar cliente:", error)
    finally:
        db.close()
        print("Conexão com PostgreSQL fechada")