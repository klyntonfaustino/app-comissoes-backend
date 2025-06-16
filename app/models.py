#app/models.py

from pydantic import BaseModel, Field

class ComissaoRequest(BaseModel):
    valor_carga: float = Field(..., gt=0, description="valor total da carga")
    percentual_comissao: float = Field(..., gt=0, description="percentual da comissao")

class ComissaoResponse(BaseModel):
    valor_carga: float
    percentual_comissao: float
    valor_comissao: float   