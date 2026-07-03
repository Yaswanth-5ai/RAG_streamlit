from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from app.core.logger import get_logger
from app.core.exceptions import DocumentSplitError

logger = get_logger(__name__)


class DocumentSplitter:
    """
    Splits documents into smaller chunks while preserving context.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        logger.info(
            f"Initializing DocumentSplitter "
            f"(chunk_size={chunk_size}, chunk_overlap={chunk_overlap})"
        )

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Split loaded documents into chunks.
        """

        try:

            if not documents:
                logger.warning(
                    "No documents received for splitting."
                )
                return []

            logger.info(
                f"Splitting {len(documents)} document(s)."
            )

            chunks = self.splitter.split_documents(documents)

            logger.info(
                f"Generated {len(chunks)} chunks."
            )

            return chunks

        except Exception as e:

            logger.exception(
                "Failed to split documents."
            )

            raise DocumentSplitError(str(e)) from e