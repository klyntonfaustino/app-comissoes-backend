#app/routes.py

from fastapi import APIRouter, Query, HTTPException
from app.services import calcular_comissao
from app.models import ComissaoRequest, ComissaoResponse

router = APIRouter()

#Endpoint GET - recebe os dados via query parameters
@router.get("/comissao", response_model=ComissaoResponse)
def calcular_comissao_endpoint(request:ComissaoRequest):

    try:
        valor_comissao = calcular_comissao(request.valor_carga, request.percentual_comissao)
        return ComissaoResponse(
            valor_carga=request.valor_carga,
            percentual_comissao=request.percentual_comissao,
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