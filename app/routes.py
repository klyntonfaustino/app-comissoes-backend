#app/routes.py

from fastapi import APIRouter, Query, HTTPException, Body
from app.services import calcular_comissao
from app.models import ComissaoRequest, ComissaoResponse, CargaModel, DashbordSummary
from app.db import conectar, get_dashbord_summary
import mysql.connector
from datetime import date
from typing import Optional

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
def listar_cargas(
    data_inicio: Optional[date] = Query(None, description="Data de início para filtrar (YYYY-MM-DD)"),
    data_fim: Optional[date] = Query(None, description="Data de fim para filtrar (YYYY-MM-DD)") 
):
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        sql_query = "SELECT id, descricao, valor, percentual, data_carga, (valor * percentual /100) AS Comissao from cargas"
        params = []
        conditions = []

        if data_inicio:
            conditions.append("data_carga >= %s")
            params.append(data_inicio)
        if data_fim:
            conditions.append("data_carga <= %s")
            params.append(data_fim)

        if conditions:
            sql_query += " WHERE " + " AND ".join(conditions)

        cursor.execute(sql_query, params)
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
            "INSERT INTO cargas (descricao, valor, percentual, data_carga) VALUES (%s, %s, %s, %s)",
            (carga.descricao, carga.valor, carga.percentual_comissao, carga.data_carga)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return {
            "descricao": carga.descricao,
            "valor": carga.valor,
            "percentual": carga.percentual_comissao,
            "data_carga": carga.data_carga,
            "comissao": (carga.valor * carga.percentual_comissao) / 100
    }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar carga: {str(e)}")

# GET - Resumo do dashboard
@router.get("/dashboard/summary", response_model=DashbordSummary)
def get_dashboard_summary():
    summary = get_dashbord_summary()
    if summary is None:
        raise HTTPException(status_code=500, detail="Erro ao obter resumo do dashboard")
    return summary