#main.py
from fastapi import FastAPI
from app.routes import router as app_router
from app.db import conectar

app = FastAPI()

#inclui as rotas que vamos definir no arquivo app/routes.py
app.include_router(app_router, prefix="/api")

@app.get("/")
def read_root():
    return {"mensagem": "API de comissões online!"}

@app.on_event("startup")    
def startup_event():
    conexao = conectar()
    if conexao:
        print("Conexão com o banco de dados estabelecida com sucesso!")
        conexao.close()
    else:
        print("Falha ao conectar ao banco de dados.")