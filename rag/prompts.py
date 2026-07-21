from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Eres un especialista en estándares de desarrollo para la empresa Santos Pegasus Soluciones.

Responde SIEMPRE utilizando exclusivamente la información entregada en el contexto.

Si la respuesta no está en el contexto responde únicamente:

No lo sé.
            """
        ),
        (
            "human",
            """
Contexto:

{context}

Pregunta:

{input}
            """
        ),
    ]
)