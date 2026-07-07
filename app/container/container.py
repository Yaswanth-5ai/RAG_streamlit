from app.embedding.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore
from app.retriever.retriever import Retriever
from app.prompt.builder import PromptBuilder
from app.llm.ollama_client import OllamaClient
from app.query.query_pipeline import QueryPipeline
from app.storage.document_manager import DocumentManager
from app.services.document_service import DocumentService

from app.core.logger import get_logger

logger = get_logger(__name__)


class ApplicationContainer:
    """
    Creates and stores shared application components.
    """

    def __init__(self):

        logger.info("Initializing Application Container.")

        self.embedder = Embedder()

        self.vector_store = ChromaStore(
            embedder=self.embedder
        )
        self.document_manager = DocumentManager()

        self.document_service = DocumentService(
            vector_store=self.vector_store,
            document_manager=self.document_manager,
        )


        self.retriever = Retriever(
            self.vector_store
        )

        self.prompt_builder = PromptBuilder()

        self.llm = OllamaClient()

        self.query_pipeline = QueryPipeline(
            retriever=self.retriever,
            prompt_builder=self.prompt_builder,
            llm=self.llm,
        )

        logger.info("Application Container initialized successfully.")