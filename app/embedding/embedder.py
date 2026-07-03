from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings

from app.config.settings import settings
from app.core.logger import get_logger
from app.core.exceptions import EmbeddingError

logger = get_logger(__name__)


class Embedder(Embeddings):

    def __init__(self, model_name: str = settings.EMBEDDING_MODEL):

        try:

            logger.info(
                f"Loading embedding model: {model_name}"
            )

            self.model = SentenceTransformer(model_name)

            logger.info(
                "Embedding model loaded successfully."
            )

        except Exception as e:

            logger.exception(
                "Failed to load embedding model."
            )

            raise EmbeddingError(str(e)) from e

    def embed_documents(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        try:

            logger.info(
                f"Generating embeddings for {len(texts)} chunks."
            )

            embeddings = self.model.encode(
                texts,
                convert_to_numpy=True
            )

            logger.info(
                "Document embeddings generated successfully."
            )

            return embeddings.tolist()

        except Exception as e:

            logger.exception(
                "Failed to generate document embeddings."
            )

            raise EmbeddingError(str(e)) from e

    def embed_query(
        self,
        text: str
    ) -> list[float]:

        try:

            logger.info(
                "Generating query embedding."
            )

            embedding = self.model.encode(
                text,
                convert_to_numpy=True
            )

            return embedding.tolist()

        except Exception as e:

            logger.exception(
                "Failed to generate query embedding."
            )

            raise EmbeddingError(str(e)) from e