from langchain_core.documents import Document

from app.config.settings import settings
from app.vectorstore.chroma_store import ChromaStore
from app.core.logger import get_logger
from app.core.exceptions import RetrievalError

logger = get_logger(__name__)


class Retriever:

    def __init__(self, vector_store: ChromaStore):
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        k: int = settings.TOP_K
    ) -> list[Document]:

        try:

            logger.info(
                f"Retrieving top {k} documents."
            )

            documents = self.vector_store.similarity_search(
                query=query,
                k=k
            )

            logger.info(
                f"Retrieved {len(documents)} documents."
            )

            return documents

        except Exception as e:

            logger.exception(
                "Document retrieval failed."
            )

            raise RetrievalError(str(e)) from e