from pydantic import BaseModel
from typing import Optional

class ArchiveMetadataResponseSchema(BaseModel):
    id: int
    categoria: str
    nome: str
    descricao: str

    class Config:
        from_attributes = True
