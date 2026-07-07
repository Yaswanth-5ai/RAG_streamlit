from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.embedding.embedder import Embedder
from app.config.settings import settings
from app.core.logger import get_logger
from app.core.exceptions import VectorStoreError

logger = get_logger(__name__)


class ChromaStore:

    def __init__(
        self,
        embedder: Embedder,
        persist_directory: str = settings.CHROMA_PATH,
        collection_name: str = settings.COLLECTION_NAME,
    ):

        self.embedder = embedder
        self.collection_name = collection_name
        self.persist_directory = persist_directory

        self.vector_store = self._create_vector_store()

    def _create_vector_store(self) -> Chroma:
        """
        Create and return a Chroma vector store.
        """

        try:

            vector_store = Chroma(
                collection_name=self.collection_name,
                persist_directory=self.persist_directory,
                embedding_function=self.embedder,
            )

            logger.info(
                f"Connected to collection: {self.collection_name}"
            )

            return vector_store

        except Exception as e:

            logger.exception(
                "Failed to initialize ChromaDB."
            )

            raise VectorStoreError(str(e)) from e

    def index_documents(
        self,
        documents: list[Document]
    ) -> None:
        """
        Store document chunks in ChromaDB.
        """

        try:

            logger.info(
                f"Indexing {len(documents)} chunks..."
            )

            self.vector_store.add_documents(documents)

            logger.info(
                "Document indexing completed successfully."
            )

        except Exception as e:

            logger.exception(
                "Failed to index documents."
            )

            raise VectorStoreError(str(e)) from e

    def similarity_search(
        self,
        query: str,
        k: int = settings.TOP_K
    ) -> list[Document]:
        """
        Retrieve the most relevant documents.
        """

        try:

            logger.info(
                f"Searching for query: {query}"
            )

            results = self.vector_store.similarity_search(
                query=query,
                k=k
            )

            logger.info(
                f"Retrieved {len(results)} document(s)."
            )

            return results

        except Exception as e:

            logger.exception(
                "Similarity search failed."
            )

            raise VectorStoreError(str(e)) from e

    def count(self) -> int:
        """
        Return the number of indexed chunks.
        """

        try:

            count = self.vector_store._collection.count()

            logger.info(
                f"Current indexed chunks: {count}"
            )

            return count

        except Exception as e:

            logger.exception(
                "Failed to count indexed documents."
            )

            raise VectorStoreError(str(e)) from e

    def reset_collection(self) -> None:
        """
        Delete the current collection and recreate it.
        """

        try:

            logger.warning(
                "Resetting Chroma collection..."
            )

            self.vector_store.delete_collection()

            self.vector_store = self._create_vector_store()

            logger.info(
                "Collection reset successfully."
            )

        except Exception as e:

            logger.exception(
                "Failed to reset collection."
            )

            raise VectorStoreError(str(e)) from e
        
    def list_documents(self) -> list[dict]:
        """
        Return unique indexed documents.
        """

        logger.info("Fetching indexed documents.")

        try:

            result = self.vector_store.get(
                include=["metadatas"]
            )

            metadatas = result.get("metadatas", [])

            documents = {}

            for metadata in metadatas:

                document_name = metadata.get("document_name")

                if not document_name:
                    continue

                if document_name not in documents:

                    documents[document_name] = {
                        "document_name": document_name,
                        "document_id": metadata.get("document_id"),
                        "file_type": metadata.get("file_type"),
                        "ingested_at": metadata.get("ingested_at"),
                        "total_chunks": metadata.get("total_chunks"),
                    }

            logger.info(
                f"Found {len(documents)} document(s)."
            )

            return sorted(
                documents.values(),
                key=lambda x: x["document_name"].lower()
            )

        except Exception:

            logger.exception(
                "Failed to fetch documents."
            )

            raise


    def delete_document( self, document_name: str,) -> bool:
        """
        Delete all chunks belonging to a document.
        """

        logger.info(
            f"Deleting embeddings for: {document_name}"
        )

        try:

            self.vector_store._collection.delete(
                where={
                    "document_name": document_name
                }
            )

            logger.info(
                "Embeddings deleted successfully."
            )

            return True

        except Exception as e:

            logger.exception(
                "Failed to delete embeddings."
            )

            raise VectorStoreError(str(e)) from e