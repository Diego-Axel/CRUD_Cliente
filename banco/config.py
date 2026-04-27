'''
Configuração do SQLAlchemy ORM para conexão com PostgreSQL
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com o PostgreSQL
DATABASE_URL = "postgresql://postgres:palmeiras123@localhost:5432/clientes"

# Criar engine
engine = create_engine(DATABASE_URL)

# Criar Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

def get_db():
    """Função para obter uma sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
