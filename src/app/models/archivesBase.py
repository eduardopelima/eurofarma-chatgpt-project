from sqlalchemy import Column, Integer, String, Text
from ..database import Base

class ArchivesBase(Base):
    __tablename__ = 'archives_base'
    
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String(50))
    nome = Column(String(50))
    descricao = Column(String(500))
    conteudo = Column(Text)
