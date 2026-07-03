from ollama import Client
import time

from app.config.settings import settings
from app.core.logger import get_logger
from app.core.exceptions import LLMError

logger = get_logger(__name__)


class OllamaClient:

    def __init__(
        self,
        model: str = settings.LLM_MODEL,
        host: str = settings.OLLAMA_HOST,
    ):

        try:

            self.model = model

            self.client = Client(host=host)

            logger.info(
                f"Initialized Ollama client using model: {model}"
            )

        except Exception as e:

            logger.exception(
                "Failed to initialize Ollama client."
            )

            raise LLMError(str(e)) from e

    def generate(
        self,
        prompt: str
    ) -> str:
        """
        Generate an answer from the LLM.
        """

        try:

            logger.info("Sending prompt to Ollama.")

            start = time.perf_counter()

            response = self.client.generate(
                model=self.model,
                prompt=prompt,
                options={
                    "temperature": 0
                }
            )

            elapsed = time.perf_counter() - start

            logger.info(
                f"LLM response generated in {elapsed:.2f} sec."
            )

            return response["response"]

        except Exception as e:

            logger.exception(
                "LLM generation failed."
            )

            raise LLMError(str(e)) from e