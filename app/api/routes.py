from fastapi import APIRouter, Request
from fastapi import UploadFile, File

from pathlib import Path
import shutil

from fastapi import UploadFile, File, HTTPException

from app.api.schemas import IngestResponse
from app.ingestion.pipeline import IngestionPipeline

from app.api.schemas import (
    QueryRequest,
    QueryResponse,
)

router = APIRouter()



@router.get("/")
def root():
    return {
        "message": "Welcome to Production RAG API!"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "Production RAG API",
        "version": "2.0.0"
    }





@router.post(
    "/query",
    response_model=QueryResponse
)
def query(
    request: Request,
    body: QueryRequest,
):

    container = request.app.state.container

    answer = container.query_pipeline.run(
        body.question
    )

    return QueryResponse(
        answer=answer
    )


@router.post(
    "/ingest",
    response_model=IngestResponse
)
def ingest(
    file: UploadFile = File(...)
):

    upload_dir = Path("data/raw")
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / file.filename

    # Reject duplicate uploads
    if file_path.exists():
        raise HTTPException(
            status_code=409,
            detail=f"'{file.filename}' already exists."
        )

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Index only this file
    pipeline = IngestionPipeline()

    pipeline.ingest_file(str(file_path))

    return IngestResponse(
        message="PDF indexed successfully.",
        filename=file.filename
    )


@router.get("/documents")
def list_documents(request: Request):

    container = request.app.state.container

    return container.document_service.list_documents()


@router.delete("/documents/{filename}")
def delete_document(
    filename: str,
    request: Request,
):

    container = request.app.state.container

    deleted = container.document_service.delete_document(
        filename
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    return {
        "message": "Document deleted successfully."
    }