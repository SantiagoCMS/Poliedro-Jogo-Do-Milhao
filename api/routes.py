from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from api import crud, models, schemas
from api.database import get_db

router = APIRouter()

class UsuarioRoutes:

    def __init__(self):
        pass

    @router.post("/usuarios/", response_model=schemas.UsuarioOut)
    def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
        db_usuario = crud.UsuarioCRUD.criar(db, usuario)
        if not db_usuario:
            raise HTTPException(status_code=400, detail="Usuário já existe")
        return db_usuario

    @router.get("/usuarios/", response_model=list[schemas.UsuarioOut])
    def listar_usuarios(db: Session = Depends(get_db)):
        return crud.UsuarioCRUD.listar(db)

class PontuacaoRoutes:

    def __init__(self):
        pass

    @router.post("/pontuacoes/", response_model=schemas.PontuacaoOut)
    def criar_pontuacao(pontuacao: schemas.PontuacaoCreate, db: Session = Depends(get_db)):
        return crud.PontuacaoCRUD.criar(db, pontuacao)

    @router.get("/ranking/", response_model=list[schemas.PontuacaoOut])
    def listar_ranking(db: Session = Depends(get_db)):
        return crud.PontuacaoCRUD.listar_ranking(db)

# Instanciando as classes para registrar os endpoints
UsuarioRoutes()
PontuacaoRoutes()
