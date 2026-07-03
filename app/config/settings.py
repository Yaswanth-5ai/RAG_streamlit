from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:

    # ==========================
    # Embedding
    # ==========================

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    # ==========================
    # Chroma
    # ==========================

    CHROMA_PATH = "data/vector_db"

    COLLECTION_NAME = "rag_documents"

    # ==========================
    # Data

    DATA_PATH = "data/raw"

    # ==========================
    # LLM

    LLM_MODEL = "qwen3:4b"

    OLLAMA_HOST = "http://localhost:11434"

    # ==========================
    # Retrieval

    TOP_K = 3


settings = Settings()