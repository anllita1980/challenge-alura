from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from llm import LLMService

from rag.prompts import RAG_PROMPT
from rag.retriever import RAGRetriever


class RAGService:

    def __init__(self, vectorstore):

        self.retriever = RAGRetriever(vectorstore)

        self.llm = LLMService()

        self.document_chain = create_stuff_documents_chain(
            self.llm.model,
            RAG_PROMPT
        )

    def ask(self, question: str):

        documents = self.retriever.search(question)
        
        print("\n========== DEBUG RETRIEVER ==========")
        print(f"Pregunta: {question}")
        print(f"Documentos encontrados: {len(documents)}")

        for i, doc in enumerate(documents, start=1):
            print(f"\nDocumento {i}")
            print(f"Fuente: {doc.metadata.get('source')}")
            print(f"Página: {doc.metadata.get('page')}")
            print(doc.page_content[:300])
        print("====================================\n")
        
        if not documents:

            return {
                "respuesta": "No lo sé.",
                "citaciones": [],
                "documentos_encontrados": False
            }

        answer = self.document_chain.invoke(
            {
                "input": question,
                "context": documents
            }
        )

        if answer.strip().lower().startswith("no lo sé"):

            return {
                "respuesta": "No lo sé.",
                "citaciones": [],
                "documentos_encontrados": False
            }

        return {
            "respuesta": answer,
            "citaciones": documents,
            "documentos_encontrados": True
        }