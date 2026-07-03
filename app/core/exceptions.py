class RAGException(Exception):
    """Base exception for the RAG application."""


class DocumentLoadError(RAGException):
    """Raised when document loading fails."""


class DocumentSplitError(RAGException):
    """Raised when document splitting fails."""


class EmbeddingError(RAGException):
    """Raised when embedding generation fails."""


class VectorStoreError(RAGException):
    """Raised when vector database operations fail."""


class RetrievalError(RAGException):
    """Raised when retrieval fails."""


class PromptBuildError(RAGException):
    """Raised when prompt creation fails."""


class LLMError(RAGException):
    """Raised when the language model request fails."""