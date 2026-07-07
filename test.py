from langchain_chroma import Chroma

from app.embedding.embedder import Embedder
from langchain_core.documents import Document
from app.config.settings import settings
from app.core.logger import get_logger
from app.core.exceptions import VectorStoreError
from app.vectorstore.chroma_store import ChromaStore

embedder = Embedder()

store = ChromaStore(embedder)

store.delete_document("A13 batch.pdf")

print(store.list_documents())