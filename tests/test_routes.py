# tests/test_routes.py

import sys
import  os
from fastapi.testclient import TestClient

#Garante que o diretório raiz do projeto no sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)

def test_calcular_comissao_get():
    response = client.get("/comissao", params={"valor_carga": 1000, "percentual_comissao": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["valor_carga"] == 1000
    assert data["percentual_comissao"] == 10
    assert data["valor_comissao"] == 100

def test_calcular_comissao_post():
    payload ={
        "valor_carga": 2000,
        "percentual_comissao": 15
    }
    response = client.post("/comissao", json=payload)
    data = response.json()
    assert data["valor_carga"] == 2000
    assert data["percentual_comissao"] == 15
    assert data["valor_comissao"] == 300