from pydantic import BaseModel

class ArchiveSchema(BaseModel):
    id: int
    categoria: str
    nome: str
    descricao: str
    conteudo: str

    class Config:
        from_attributes = True
