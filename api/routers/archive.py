from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.archive import ArchiveBase
from ..schemas.archive.archiveResponseSchema import ArchiveResponseSchema
from ..schemas.archive.archiveRequestCreateSchema import ArchiveRequestCreateSchema
from ..schemas.archive.archiveMetadataResponseSchema import ArchiveMetadataResponseSchema
from ..chatgpt.prompts import PromptFilterFileAndResponse

router = APIRouter()

@router.get("/list/archive", response_model=List[ArchiveResponseSchema])
def list_archives(db: Session = Depends(get_db)):
    return db.query(ArchiveBase).all() #alterar o return para o schema, não model

@router.get("/list/archive_metadata_only", response_model=List[ArchiveMetadataResponseSchema])
def list_archives_metadata_only(db: Session = Depends(get_db)):
    results = db.query(ArchiveBase.id, ArchiveBase.nome, ArchiveBase.categoria, ArchiveBase.descricao).all()
    return [ArchiveMetadataResponseSchema.model_validate(row) for row in results]

@router.get("/archive/{id}", response_model=ArchiveResponseSchema)
def get_archive_by_id(id: int, db: Session = Depends(get_db)):
    archive = db.query(ArchiveBase).filter(ArchiveBase.id == id).first()
    
    return ArchiveResponseSchema.model_validate(archive)


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

@router.post("/get/prompt_response")
def prompt_response(question: str, db: Session = Depends(get_db)):
    archives : List[ArchiveMetadataResponseSchema] = list_archives_metadata_only(db)
    archives = "[" + ", ".join([archive.model_dump_json() for archive in archives]) + "]"

    promptFilterFileAndResponse = PromptFilterFileAndResponse(archives, question)
    promptFilterFileAndResponse.search_file_id()

    if promptFilterFileAndResponse.get_file_id() == 0:
        return "Não sou capaz de responder a esta pergunta."
    
    selected_file_content : ArchiveResponseSchema = get_archive_by_id(promptFilterFileAndResponse.selected_file_id, db)
    promptFilterFileAndResponse.set_selected_file_content(selected_file_content)

    return promptFilterFileAndResponse.get_user_response()