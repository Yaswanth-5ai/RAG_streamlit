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