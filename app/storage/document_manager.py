from pathlib import Path

from app.config.settings import settings
from app.core.exceptions import DocumentManagerError
from app.core.logger import get_logger

logger = get_logger(__name__)

class DocumentManager:

    def __init__(self):
        self.data_path = Path(settings.DATA_PATH)

    def save_document(self):
        pass

  

    def delete_document(
        self,
        filename: str,
    ) -> bool:
        """
        Delete a document from storage.
        """

        try:

            file_path = self.data_path / filename

            if not file_path.exists():

                logger.warning(
                    f"Document not found: {filename}"
                )

                return False

            file_path.unlink()

            logger.info(
                f"Deleted document: {filename}"
            )

            return True

        except Exception as e:

            logger.exception(
                "Failed to delete document."
            )

            raise DocumentManagerError(str(e)) from e
    def replace_document(self):
        pass

    def document_exists(self):
        pass

    def list_documents(self):
        pass