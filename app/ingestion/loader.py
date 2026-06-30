from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class DocumentLoader:
    """
    Loads all PDF documents from a directory.
    """

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_documents(self) -> list[Document]:
        documents = []

        pdf_files = self.data_path.glob("*.pdf")

        for pdf_file in pdf_files:
            print(f"Loading: {pdf_file.name}")

            loader = PyPDFLoader(str(pdf_file))
            docs = loader.load()

            documents.extend(docs)

        return documents