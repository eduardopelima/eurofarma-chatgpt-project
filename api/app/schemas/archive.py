from pydantic import BaseModel
from typing import Optional

class ArchiveSchema(BaseModel):
    id: Optional[int] = None
    categoria: str
    nome: str
    descricao: str
    conteudo: str

    class Config:
        from_attributes = True
