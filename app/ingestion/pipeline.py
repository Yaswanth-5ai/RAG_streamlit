from app.ingestion.loader import DocumentLoader
from app.ingestion.splitter import DocumentSplitter


class IngestionPipeline:

    def __init__(self):
        self.loader = DocumentLoader("data/raw")
        self.splitter = DocumentSplitter()

    def run(self):

        documents = self.loader.load_documents()

        print(f"\nLoaded Pages : {len(documents)}")

        chunks = self.splitter.split_documents(documents)

        print(f"Generated Chunks : {len(chunks)}")

        print("\nFirst Chunk\n")
        print(chunks[0].page_content)

        print("\nMetadata\n")
        print(chunks[0].metadata)