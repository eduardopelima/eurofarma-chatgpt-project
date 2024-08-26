from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.archive import ArchiveBase
from ..schemas.archive import ArchiveSchema

router = APIRouter()

@router.get("/list/archive", response_model=List[ArchiveSchema])
def list_archives(db: Session = Depends(get_db)):
    return db.query(ArchiveBase).all()

@router.post("/add/archive", response_model=ArchiveSchema)
def add_archive(archive: ArchiveSchema, db: Session = Depends(get_db)):
    db_archive = ArchiveBase(**archive.model_dump())
    db.add(db_archive)
    db.commit()
    db.refresh(db_archive)
    return db_archive

