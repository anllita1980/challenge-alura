from langchain_core.documents import Document


class RAGRetriever:

    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def search(self, question: str) -> list[Document]:
        """
        Busca los documentos más relevantes para la pregunta.
        """
        resultados = self.vectorstore.similarity_search_with_score(
            question,
            k=8
        )

        return [doc for doc, _ in resultados]