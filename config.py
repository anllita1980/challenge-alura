from pathlib import Path

from dotenv import load_dotenv

import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHAT_MODEL = os.getenv("CHAT_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "No se encontró GEMINI_API_KEY en el archivo .env"
    )

DOCUMENTS_DIR = BASE_DIR / "documentos"

VECTORSTORE_DIR = BASE_DIR / "vectorstore"

LOG_DIR = BASE_DIR / "logs"