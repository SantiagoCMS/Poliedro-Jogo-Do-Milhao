from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

# Import da Base declarada no arquivo database.py
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha = Column(String(100), nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    # Relacionamento com pontos
    pontos = relationship("Ponto", back_populates="usuario")

class Ponto(Base):
    __tablename__ = "pontos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    pontuacao = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relacionamento (reverso) com o usuário
    usuario = relationship("Usuario", back_populates="pontos")

# Fazer mais modelos/tabelas feitas no banco de dados

# class Questoes(Base):
#     __tablename__ = "questoes"

#     id = Column(Integer, primary_key=True)
#     question_text = Column(String(255), nullable=False)
#     opcao_a = Column(String(100), nullable=False)
#     opcao_b = Column(String(100), nullable=False)
#     opcao_c = Column(String(100), nullable=False)
#     opcao_d = Column(String(100), nullable=False)
#     opcao_correta = Column(String(1), nullable=False)