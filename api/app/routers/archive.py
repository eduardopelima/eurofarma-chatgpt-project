from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.archive import ArchiveBase
from ..schemas.archive.archiveResponseSchema import ArchiveResponseSchema
from ..schemas.archive.archiveRequestCreateSchema import ArchiveRequestCreateSchema

router = APIRouter()

@router.get("/list/archive", response_model=List[ArchiveResponseSchema])
def list_archives(db: Session = Depends(get_db)):
    return db.query(ArchiveBase).all()

@router.post("/add/archive", response_model=ArchiveResponseSchema)
def add_archive(archive: ArchiveRequestCreateSchema, db: Session = Depends(get_db)):
    db_archive = ArchiveBase(
        categoria=archive.categoria,
        nome=archive.nome,
        descricao=archive.descricao,
        conteudo=archive.conteudo
    )
    db.add(db_archive)
    db.commit()
    db.refresh(db_archive)
    return db_archive

