from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentSplitter:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

    def split(self, documentos):

        chunks = self.splitter.split_documents(documentos)

        print(f"Se generaron {len(chunks)} chunks.\n")

        return chunks