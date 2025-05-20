from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.database import engine, Base
from api.routes import router as api_router

# Cria as tabelas no banco (caso não existam ainda)
Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Code Milionário API",
        description="API do jogo em Python com login e ranking",
        version="1.0.0"
    )

    # CORS (caso precise acessar a API de outro domínio/aplicação)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Em produção, especifique os domínios
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Inclui as rotas definidas no arquivo routes.py
    app.include_router(api_router)

    return app

app = create_app()