#app/routes.py

from fastapi import APIRouter, Query, HTTPException, Body
from app.services import calcular_comissao
from app.models import ComissaoRequest, ComissaoResponse, CargaModel
from app.db import conectar
import mysql.connector

router = APIRouter()

#Endpoint GET - recebe os dados via query parameters
@router.get("/comissao", response_model=ComissaoResponse)
def calcular_comissao_endpoint(valor_carga: float, percentual_comissao: float):
    try:
        valor_comissao = calcular_comissao(valor_carga, percentual_comissao)
        return ComissaoResponse(
            valor_carga=valor_carga,
            percentual_comissao=percentual_comissao,
            valor_comissao=valor_comissao
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro no cálculo: {str(e)}")
    
#Endpoint POST - recebe os dados via corpo da requisição (JSON) 
@router.post("/comissao", response_model=ComissaoResponse)
def calcular_comissao_post(request: ComissaoRequest):
    try:
        valor_comissao = calcular_comissao(request.valor_carga, request.percentual_comissao)
        return ComissaoResponse(
            valor_carga=request.valor_carga,
            percentual_comissao=request.percentual_comissao,
            valor_comissao=valor_comissao
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"erro no cálculo:{str(e)}")
    
# GET - lista todas as cargas salvas no banco de dados
@router.get("/cargas")
def listar_cargas():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT descricao, valor, percentual,(valor * percentual /100) AS Comissao from cargas")
        cargas = cursor.fetchall()
        cursor.close()
        conn.close()
        return cargas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar cargas: {str(e)}")
    
# POST - adicionar nova carga no banco de dados
@router.post("/cargas", status_code=201)
def adicionar_carga(carga: CargaModel = Body(...)):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cargas (descricao, valor, percentual) VALUES (%s, %s, %s)",
            (carga.descricao, carga.valor, carga.percentual_comissao)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return {
            "descricao": carga.descricao,
            "valor": carga.valor,
            "percentual": carga.percentual_comissao,
            "comissao": (carga.valor * carga.percentual_comissao) / 100
    }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar carga: {str(e)}")