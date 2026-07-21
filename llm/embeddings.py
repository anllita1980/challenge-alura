from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_MODEL, GEMINI_API_KEY



class EmbeddingService:
    """
    Encapsula el modelo de embeddings.
    """

    def __init__(self):

        self._embeddings = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL,
            google_api_key=GEMINI_API_KEY
        )

    @property
    def model(self):
        return self._embeddings