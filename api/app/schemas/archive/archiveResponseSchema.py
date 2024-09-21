from pydantic import BaseModel
from typing import Optional

class ArchiveResponseSchema(BaseModel):
    id: int
    categoria: str
    nome: str
    descricao: str
    conteudo: str

    class Config:
        from_attributes = True
