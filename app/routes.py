from fastapi import APIRouter

router = APIRouter()

@router.get("/comissao")
def calcular_comissao(valor_carga: float, percentual_comissao: float):
    comissao = (valor_carga * percentual_comissao) / 100
    return {
        "valor_carga": valor_carga,
        "percentual_comissao": percentual_comissao,
        "comissao": comissao
        }