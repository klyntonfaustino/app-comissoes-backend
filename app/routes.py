#app/routes.py

from fastapi import APIRouter, Query, HTTPException
from app.services import calcular_comissao

router = APIRouter()

@router.get("/comissao")
def calcular_comissao(
    valor_carga: float = Query(..., gt=0, description="valor total da carga"),
    percentual_comissao: float = Query(..., gt=0, description="percentual da comissão")
):
    try:
        valor_comissao = calcular_comissao(valor_carga, percentual_comissao)
        return {
            "valor_carga": valor_carga,
            "percentual_comissao": percentual_comissao,
            "valor_comissao": round(valor_comissao,2)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro no cálculo: {str(e)}")