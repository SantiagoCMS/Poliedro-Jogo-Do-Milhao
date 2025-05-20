from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# USUÁRIO

# Entrada de dados para cadastro de usuário
class CadastroUsuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str

# Retorno de dados: após cadastro ou busca
class UsuarioSaida(BaseModel):
    id: int
    nome: str
    email: EmailStr
    data_cadastro: datetime

    class Config:
        orm_mode = True # Permite que o Pydantic converta objetos ORM em dicionários

# PONTUAÇÃO

# Entrada: nova pontuação
class NovaPontuacao(BaseModel):
    usuario_id: int
    pontos: int

# Retorno: pontuação do usuário
class PontuacaoSaida(BaseModel):
    id: int
    usuario_id: int
    pontuacao: int
    timestamp: datetime

    class Config:
        orm_mode = True

# Ranking

# Saída combinada Usuário + Pontuação
class RankingSaida(BaseModel):
    nome: str
    pontuacao: int

    class Config:
        orm_mode = True