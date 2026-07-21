from langchain_core.documents import Document


class RAGRetriever:

    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def search(self, question: str) -> list[Document]:

        resultados = self.vectorstore.similarity_search_with_score(
            question,
            k=8
        )

        print("\n========== SCORES ==========")

        documentos = []

        for doc, score in resultados:

            print(
                f"Score: {score:.4f} | "
                f"{doc.metadata.get('source')} "
                f"Página {doc.metadata.get('page')}"
            )

            documentos.append(doc)

        print("============================\n")

        return documentos