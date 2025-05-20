from sqlalchemy.orm import Session
from sqlalchemy import func
from api import models, schemas
from typing import List, Optional
from datetime import datetime

class UserCRUD:
    def create_user(self, db: Session, user: schemas.CadastroUsuario) -> models.Usuario:
        db_user = models.Usuario(
            nome=user.nome,
            email=user.email,
            senha=user.senha,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def get_user_by_email(self, db: Session, email: str) -> Optional[models.Usuario]:
        return db.query(models.Usuario).filter(models.Usuario.email == email).first()
    
    def get_user_by_id(self, db: Session, user_id: int) -> Optional[models.Usuario]:
        return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    
class ScoreCRUD:
    def add_score(self, db: Session, score: schemas.NovaPontuacao) -> models.Pontuacao:
        db_score = models.Pontuacao(
            usuario_id=score.usuario_id,
            pontuacao=score.pontos
        )
        db.add(db_score)
        db.commit()
        db.refresh(db_score)
        return db_score
    
    def get_user_score(self, db: Session, user_id: int) -> List[models.Pontuacao]:
        return db.query(models.Pontuacao).filter(models.Pontuacao.usuario_id == user_id).all()
    
    def get_ranking(self, db: Session, limit: int = 10) -> List[schemas.RankingSaida]:
        result = (
            db.query(
                models.Usuario.nome,
                func.sum(models.Pontuacao.pontuacao).label("pontuacao")
            )
            .join(models.Pontuacao, models.Usuario.id == models.Pontuacao.usuario_id)
            .group_by(models.Usuario.id)
            .order_by(func.sum(models.Pontuacao.pontuacao).desc())
            .limit(limit)
            .all()
        )

        # Converte para lista de schemas.RankingOut
        return [schemas.RankingOut(username=row.username, total_points=row.total_points) for row in result]


# Instâncias dos CRUDs para importar facilmente
user_crud = UserCRUD()
score_crud = ScoreCRUD()