from app.config.settings import settings
from app.core.exceptions import RAGException
from app.core.logger import get_logger

from app.embedding.embedder import Embedder
from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter
from app.vectorstore.chroma_store import ChromaStore


from pathlib import Path
from uuid import uuid4
from datetime import datetime, UTC

logger = get_logger(__name__)


class IngestionPipeline:

    def __init__(self):

        logger.info("Initializing Ingestion Pipeline.")

        self.loader = DocumentLoader(settings.DATA_PATH)
        self.splitter = DocumentSplitter()
        self.embedder = Embedder()
        self.vector_store = ChromaStore(
            embedder=self.embedder
        )

    def run(self):

        logger.info("Starting ingestion pipeline.")
        self.vector_store.reset_collection()
        self.ingest_directory()
        logger.info("Ingestion completed successfully.")

    
    def _process_document(
        self,
        documents,
        document_name: str,
    ):
        """
        Complete processing of a document:
        Split -> Add Metadata -> Store in ChromaDB
        """

        logger.info(
            f"Processing document: {document_name}"
        )

        chunks = self.splitter.split_documents(documents)

        logger.info(
            f"Generated {len(chunks)} chunks."
        )

        chunks = self._add_metadata(
            chunks=chunks,
            document_name=document_name,
        )

        self.vector_store.index_documents(chunks)

        logger.info(
            f"Stored Chunks: {self.vector_store.count()}"
        )

    def ingest_directory(self):

        logger.info("Starting directory ingestion.")
        pdf_files = list(
            Path(settings.DATA_PATH).glob("*.pdf")
        )
        logger.info(
            f"Found {len(pdf_files)} PDF file(s)."
        )
        for pdf_file in pdf_files:

            documents = self.loader.load_file(
                str(pdf_file))

            self._process_document(
                documents,
                pdf_file.name,
            )

    def ingest_file(self,file_path: str):

        documents = self.loader.load_file(file_path)
        self._process_document(
        documents,
        Path(file_path).name)

    def _add_metadata(
        self,
        chunks,
        document_name: str,
    ):
        """
        Enrich every chunk with additional metadata.
        """

        logger.info(
            "Adding metadata to document chunks."
        )

        document_id = str(uuid4())

        total_chunks = len(chunks)

        ingested_at = datetime.utcnow().isoformat()

        for index, chunk in enumerate(chunks, start=1):

            chunk.metadata["document_id"] = document_id
            chunk.metadata["document_name"] = document_name
            chunk.metadata["chunk_id"] = index
            chunk.metadata["total_chunks"] = total_chunks
            chunk.metadata["ingested_at"] = ingested_at
            chunk.metadata["file_type"] = Path(document_name).suffix.lower()

        logger.info(
            f"Metadata added to {total_chunks} chunks."
        )

        return chunks