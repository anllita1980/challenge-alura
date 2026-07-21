from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_API_KEY
from config import CHAT_MODEL


class LLMService:
    """
    Encapsula el acceso al modelo de lenguaje.
    """

    def __init__(self):

        self._llm = ChatGoogleGenerativeAI(
            model=CHAT_MODEL,
            temperature=0,
            google_api_key=GEMINI_API_KEY,
        )

    @property
    def model(self):
        return self._llm
    
   