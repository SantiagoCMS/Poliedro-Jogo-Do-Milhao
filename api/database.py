from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexão com o banco de dados propriamente dita a partir da URL
DATABASE_URL = "mysql+pymysql://USUÁRIO:SENHA@HOST:PORTA/NOME_DO_BANCO"

# "Engine" gerencia conexões com o banco de dados
engine = create_engine(DATABASE_URL)

# "SessionLocal" é uma classe que cria sessões locais e temporarias para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# "Base" é a classe base para os modelos do banco de dados
Base = declarative_base()