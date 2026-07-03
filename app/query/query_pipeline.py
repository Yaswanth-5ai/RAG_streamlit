from app.embedding.embedder import Embedder
from app.vectorstore.chroma_store import ChromaStore
from app.prompt.builder import PromptBuilder
from app.llm.ollama_client import OllamaClient
from app.retriever.retriever import Retriever

from app.core.logger import get_logger
from app.core.exceptions import RAGException

logger = get_logger(__name__)


class QueryPipeline:

    def __init__(self):

        logger.info("Initializing Query Pipeline.")

        self.embedder = Embedder()

        self.vector_store = ChromaStore(
            embedder=self.embedder
        )

        self.retriever = Retriever(
            self.vector_store
        )

        self.prompt_builder = PromptBuilder()

        self.llm = OllamaClient()

    def run(
        self,
        query: str
    ) -> str:
        """
        Execute the complete RAG query pipeline.
        """

        try:

            logger.info(
                f"Processing query: {query}"
            )

            documents = self.retriever.retrieve(
                query=query
            )

            logger.info(
                f"Retrieved {len(documents)} documents."
            )

            prompt = self.prompt_builder.build_prompt(
                question=query,
                documents=documents
            )

            answer = self.llm.generate(
                prompt
            )

            logger.info(
                "Answer generated successfully."
            )

            return answer

        except RAGException:

            logger.exception(
                "Query pipeline failed."
            )

            raise

        except Exception:

            logger.exception(
                "Unexpected error occurred in Query Pipeline."
            )

            raise