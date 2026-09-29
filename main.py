from fastapi import FastAPI
from core.logging_config import logger

app = FastAPI(
    title="Acervo de Pesquisa Científica",
    description=(
        "Teste do cofre digital"
    ),
)

@app.get("/")
def teste():
    return {"status": "Cofre Digital de Pesquisa Científica ativo"}