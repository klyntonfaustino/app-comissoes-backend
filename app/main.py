#main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as app_router
from app.db import conectar
import os
import mysql.connector

# Define a lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Tentando conectar ao banco de dados...")
    conn = None
    cursor = None
    try:
        conn = conectar()
        if conn:
            print("Conexão com o banco de dados estabelecida com sucesso!")
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM cargas LIMIT 1;")
            print("Tabela 'cargas' verificada com sucesso.")
        else:
            print("Falha ao conectar ao banco de dados.")
    except mysql.connector.Error as err:
        print(f"Erro MySQL na inicialização (verificar 'cargas'): {err}")
        print("Certifique-se de que a tabela 'caegas' existe no banco de dados 'comissoes'.")
        raise
    except Exception as e:
        print(f"Erro inesperado na inicialização: {e}")
        raise
    yield
    print("Desligando a aplicação FastAPI.")

app = FastAPI(lifespan=lifespan)

# Configuração do CORS
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8000",   
    "http://10.0.2.2",
    "http://10.0.3.2",
    "http://localhost:*",
    "http://127.0.0.1:*",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#inclui as rotas que vamos definir no arquivo app/routes.py
app.include_router(app_router, prefix="/api")

@app.get("/")
def read_root():
    return {"mensagem": "API de comissões online!"}