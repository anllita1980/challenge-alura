from pathlib import Path

from langchain_community.vectorstores import FAISS

from config import VECTORSTORE_DIR


class VectorStore:

    def exists(self):

        faiss_file = VECTORSTORE_DIR / "index.faiss"
        pkl_file = VECTORSTORE_DIR / "index.pkl"

        return faiss_file.exists() and pkl_file.exists()

    def load(self, embeddings):

        print("Cargando índice FAISS...\n")

        return FAISS.load_local(
            str(VECTORSTORE_DIR),
            embeddings.model,
            allow_dangerous_deserialization=True
        )

    def save(self, vectorstore):

        VECTORSTORE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        vectorstore.save_local(
            str(VECTORSTORE_DIR)
        )

        print("Índice guardado.\n")