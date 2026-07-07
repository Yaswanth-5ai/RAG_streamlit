from app.vectorstore.chroma_store import ChromaStore
from app.storage.document_manager import DocumentManager
from app.core.logger import get_logger

logger = get_logger(__name__)


class DocumentService:

    def __init__(
        self,
        vector_store: ChromaStore,
        document_manager: DocumentManager,
    ):
        self.vector_store = vector_store
        self.document_manager = document_manager

        logger.info("Document Service initialized.")

    def list_documents(self):
        return self.vector_store.list_documents()

    def document_exists(self, filename: str):
        return self.document_manager.document_exists(filename)

    def delete_document(  self,filename: str, ):

        logger.info(
            f"Deleting document: {filename}"
        )

        deleted = self.document_manager.delete_document(
            filename
        )

        if not deleted:
            return False

        self.vector_store.delete_document(
            filename
        )

        return True

    def replace_document(self, filename: str):
        pass