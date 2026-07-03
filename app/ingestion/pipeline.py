from app.config.settings import settings
from app.core.exceptions import RAGException
from app.core.logger import get_logger

from app.embedding.embedder import Embedder
from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter
from app.vectorstore.chroma_store import ChromaStore

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

    def run(self) -> None:
        """
        Execute the complete ingestion pipeline.
        """

        try:

            logger.info("Starting ingestion pipeline.")

            documents = self.loader.load_documents()

            logger.info(
                f"Loaded {len(documents)} pages."
            )

            chunks = self.splitter.split_documents(
                documents
            )

            logger.info(
                f"Generated {len(chunks)} chunks."
            )

            self.vector_store.reset_collection()

            self.vector_store.index_documents(
                chunks
            )

            count = self.vector_store.count()

            logger.info(
                f"Stored Chunks: {count}"
            )

            logger.info(
                "Ingestion completed successfully."
            )

        except RAGException:

            logger.exception(
                "Ingestion pipeline failed."
            )

            raise

        except Exception as e:

            logger.exception(
                "Unexpected error in ingestion pipeline."
            )

            raise