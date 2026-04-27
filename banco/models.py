'''
Modelo de dados para Cliente usando SQLAlchemy ORM
'''

from sqlalchemy import Column, Integer, String, Boolean
from banco.config import Base

class Cliente(Base):
    """Modelo ORM para a tabela clientes"""
    
    __tablename__ = "clientes"
    
    cod_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)
    email = Column(String(40), nullable=False)
    celular = Column(String(25), nullable=False)
    cpf = Column(String(20), nullable=False)
    ativo = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Cliente(cod_cliente={self.cod_cliente}, nome={self.nome}, email={self.email})>"
