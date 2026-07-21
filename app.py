from rag.indexer import RAGIndexer
from services import AssistantService


def main():

    print("=" * 60)
    print("Pegasus Assistant")
    print("=" * 60)

    indexer = RAGIndexer()

    vectorstore = indexer.get_vectorstore()

    assistant = AssistantService(vectorstore)

    while True:

        pregunta = input("\n👤 Tú: ")

        if pregunta.lower() == "salir":
            break

        resultado = assistant.ask(pregunta)

        print()

        if resultado["tipo"] == "RESPUESTA":

            print("🤖 Pegasus:\n")

            print(resultado["respuesta"]["respuesta"])

            if resultado["respuesta"]["documentos_encontrados"]:

                print("\nFuentes:")

                for doc in resultado["respuesta"]["citaciones"]:

                    print(
                        f"- {doc.metadata.get('source')} "
                        f"(Página {doc.metadata.get('page')})"
                    )

        elif resultado["tipo"] == "PEDIR_INFO":

            print("🤖 Pegasus:")

            print(resultado["mensaje"])

            faltantes = resultado["decision"]["campos_faltantes"]

            if faltantes:
                print("\nInformación faltante:")

                for campo in faltantes:
                    print(f"- {campo}")

        else:

            print("🤖 Pegasus:")

            print(resultado["mensaje"])

            print(f"Urgencia: {resultado['decision']['urgencia']}")

    print("\nHasta luego.")


if __name__ == "__main__":
    main()