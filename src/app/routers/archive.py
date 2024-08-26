from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.archivesBase import ArchivesBase

router = APIRouter()

@router.get("/list/archives")
def list_categories(db: Session = Depends(get_db)):
    return db.query(ArchivesBase).all()