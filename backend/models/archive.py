from sqlalchemy import Column, Integer, String, Text
from ..database import Base

class ArchiveBase(Base):
    __tablename__ = 'archives'
    
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String(50))
    nome = Column(String(50))
    descricao = Column(String(50))
    conteudo = Column(Text)
