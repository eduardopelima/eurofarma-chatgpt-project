from pydantic import BaseModel
from typing import Optional

class ArchiveRequestCreateSchema(BaseModel):
    categoria: str
    nome: str
    descricao: str
    conteudo: str

    class Config:
        from_attributes = True
