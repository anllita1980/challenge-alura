from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader

from config import DOCUMENTS_DIR


class DocumentLoader:

    def load(self):

        documentos = []

        pdfs = sorted(Path(DOCUMENTS_DIR).glob("*.pdf"))

        if not pdfs:
            raise FileNotFoundError(
                f"No existen documentos PDF en {DOCUMENTS_DIR}"
            )

        for pdf in pdfs:
            print(f"Cargando {pdf.name}...")

            loader = PyMuPDFLoader(str(pdf))

            documentos.extend(loader.load())

        print(f"Se cargaron {len(documentos)} páginas.\n")

        return documentos