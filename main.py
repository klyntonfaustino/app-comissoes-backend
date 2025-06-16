from fastapi import FastAPI
from app.routes import router as app_router

app = FastAPI()

#inclui as rostar que vamos definir no arquivo app/routes.py
app.include_router(app_router)

@app.get("/")
def read_root():
    return {"mensagem": "API de comissões online!"}