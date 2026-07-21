from flask import Flask, render_template, request

from rag.indexer import RAGIndexer
from services.assistant import AssistantService

app = Flask(__name__)

print("Cargando índice FAISS...")

indexer = RAGIndexer()
vectorstore = indexer.get_vectorstore()

assistant = AssistantService(vectorstore)

print("Asistente listo.\n")

chat = []


@app.route("/", methods=["GET", "POST"])
def home():

    global chat

    if request.method == "POST":

        pregunta = request.form["pregunta"]

        resultado = assistant.ask(pregunta)

        if resultado["tipo"] == "RESPUESTA":

            respuesta = resultado["respuesta"]["respuesta"]

            fuentes = []

            for doc in resultado["respuesta"]["citaciones"]:

                fuentes.append({
                    "archivo": doc.metadata.get("source").split("\\")[-1],
                    "pagina": doc.metadata.get("page", 0) + 1
                })

        else:

            respuesta = resultado["mensaje"]

            fuentes = []

        chat.append(
            {
                "pregunta": pregunta,
                "respuesta": respuesta,
                "fuentes": fuentes
            }
        )

    return render_template(
        "index.html",
        chat=chat
    )


if __name__ == "__main__":
    app.run(debug=True)