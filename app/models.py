#app/models.py

from pydantic import BaseModel, Field

class ComissaoRequest(BaseModel):
    valor_carga: float = Field(..., gt=0, description="valor total da carga, deve ser maior que zero")
    percentual_comissao: float = Field(..., gt=0, le=100, description="percentual da comissao, entre 0 e 100")

class ComissaoResponse(BaseModel):
    valor_carga: float
    percentual_comissao: float
    valor_comissao: float   

class CargaModel(BaseModel):
    descricao: str
    valor: float = Field(..., gt=0, description="valor total da carga, deve ser maior que zero")
    percentual_comissao: float = Field(..., gt=0, le=100, description="percentual da comissao, entre 0 e 100")