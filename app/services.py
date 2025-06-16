# app/services.py

def calcular_comissao(valor_carga: float, percentual_comissao: float) -> float:
    return round(valor_carga * percentual_comissao / 100,2)