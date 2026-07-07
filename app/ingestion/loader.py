from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from app.core.logger import get_logger
from app.core.exceptions import DocumentLoadError


logger = get_logger(__name__)


class DocumentLoader:
    """
    Loads PDF documents either from a directory or a single file.
    """

    def __init__(self, data_path: str | None = None):
        self.data_path = Path(data_path) if data_path else None

    def load_directory(self) -> list[Document]:

        try:

            if self.data_path is None:
                raise DocumentLoadError("Data path is not configured.")

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

                logger.info(f"Loading PDF: {pdf_file.name}")

                loader = PyPDFLoader(str(pdf_file))

                documents.extend(loader.load())

            logger.info(
                f"Loaded {len(documents)} pages successfully."
            )

            return documents

        except Exception as e:

            logger.exception("Failed to load PDF documents.")

            raise DocumentLoadError(str(e)) from e

    def load_file(self, file_path: str) -> list[Document]:

        try:

            pdf_path = Path(file_path)

            if not pdf_path.exists():
                raise DocumentLoadError(
                    f"File does not exist: {pdf_path}"
                )

            logger.info(f"Loading PDF: {pdf_path.name}")

            loader = PyPDFLoader(str(pdf_path))

            documents = loader.load()

            logger.info(
                f"Loaded {len(documents)} pages successfully."
            )

            return documents

        except Exception as e:

            logger.exception("Failed to load PDF.")

            raise DocumentLoadError(str(e)) from e