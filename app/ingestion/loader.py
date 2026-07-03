from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from app.core.logger import get_logger
from app.core.exceptions import DocumentLoadError


logger = get_logger(__name__)


class DocumentLoader:
    """
    Loads all PDF documents from a directory.
    """

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_documents(self) -> list[Document]:

        try:

            if not self.data_path.exists():
                raise DocumentLoadError(
                    f"Directory does not exist: {self.data_path}"
                )

            documents = []

            pdf_files = list(self.data_path.glob("*.pdf"))

            if not pdf_files:
                logger.warning(
                    f"No PDF files found in {self.data_path}"
                )
                return []

            logger.info(
                f"Found {len(pdf_files)} PDF file(s)."
            )

            for pdf_file in pdf_files:

                logger.info(
                    f"Loading PDF: {pdf_file.name}"
                )

                loader = PyPDFLoader(str(pdf_file))

                docs = loader.load()

                documents.extend(docs)

            logger.info(
                f"Loaded {len(documents)} pages successfully."
            )

            return documents

        except Exception as e:

            logger.exception(
                "Failed to load PDF documents."
            )

            raise DocumentLoadError(str(e)) from e