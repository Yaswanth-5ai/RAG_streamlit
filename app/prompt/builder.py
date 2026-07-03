from langchain_core.documents import Document

from app.core.logger import get_logger
from app.core.exceptions import PromptBuildError

logger = get_logger(__name__)


class PromptBuilder:

    def build_prompt(
        self,
        question: str,
        documents: list[Document]
    ) -> str:
        """
        Build the prompt for the LLM using the retrieved documents.
        """

        try:

            if not documents:
                logger.warning(
                    "No documents available to build the prompt."
                )

                raise PromptBuildError(
                    "No documents were provided."
                )

            logger.info(
                f"Building prompt using {len(documents)} document(s)."
            )

            contexts = []

            for i, doc in enumerate(documents, start=1):

                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", "Unknown")

                contexts.append(
                    f"""
==================================================
DOCUMENT {i}

Source : {source}
Page   : {page}

Content:
{doc.page_content.strip()}
"""
                )

            context = "\n".join(contexts)

            prompt = f"""
You are a helpful AI assistant specialized in answering questions from the provided documents.

Instructions:
1. Answer ONLY using the provided context.
2. Do not use outside knowledge.
3. If the answer is not found, reply exactly:
   "I don't have enough information in the provided documents."
4. If multiple documents contain the answer, combine the information.
5. Mention the document source naturally when appropriate.
6. Keep the answer concise, accurate, and factual.

==================================================
CONTEXT

{context}

==================================================
QUESTION

{question}

==================================================
ANSWER
"""

            logger.info(
                f"Prompt built successfully. Length: {len(prompt)} characters."
            )

            return prompt.strip()

        except Exception as e:

            logger.exception(
                "Failed to build prompt."
            )

            raise PromptBuildError(str(e)) from e