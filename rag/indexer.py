from langchain_community.vectorstores import FAISS

from llm import EmbeddingService

from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter
from rag.vectorstore import VectorStore


class RAGIndexer:

    def __init__(self):

        self.loader = DocumentLoader()

        self.splitter = DocumentSplitter()

        self.vectorstore = VectorStore()

        self.embeddings = EmbeddingService()

    def get_vectorstore(self):

        if self.vectorstore.exists():

            return self.vectorstore.load(
                self.embeddings
            )

        print("Creando índice...\n")

        documentos = self.loader.load()

        chunks = self.splitter.split(documentos)

        print("Generando embeddings...")

        vectorstore = FAISS.from_documents(
            chunks,
            self.embeddings.model
        )

        self.vectorstore.save(vectorstore)

        return vectorstore