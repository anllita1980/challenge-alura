# Asistente documental con RAG y agente de decisión

Este proyecto implementa un asistente conversacional que responde preguntas sobre documentos internos utilizando un flujo de Recuperación Aumentada por Generación (RAG). Además, incluye un agente de clasificación que decide si una solicitud puede resolverse automáticamente, necesita más información o debe abrir un ticket.

## Arquitectura

La solución está organizada en cuatro capas principales:

1. **Interfaz web**
   - Una aplicación Flask expone una interfaz simple en la ruta principal.
   - El usuario envía una pregunta desde la UI y recibe una respuesta con referencias a los documentos utilizados.

2. **Orquestación del asistente**
   - El servicio principal en [services/assistant.py](services/assistant.py) recibe la pregunta y delega la decisión a un agente especializado.
   - El agente determina si la solicitud debe:
     - resolverse automáticamente con RAG,
     - pedir más información,
     - o derivarse a un ticket.

3. **Motor RAG**
   - El módulo en [rag/service.py](rag/service.py) busca documentos relevantes en un índice vectorial FAISS.
   - El retriever recupera fragmentos semánticamente relacionados y el modelo de lenguaje genera una respuesta basada en ellos.

4. **Almacenamiento y modelos**
   - Los documentos fuente se encuentran en la carpeta [documentos](documentos).
   - El índice vectorial se almacena en [vectorstore](vectorstore).
   - La integración con Gemini se realiza a través de [llm/chat.py](llm/chat.py) y [llm/embeddings.py](llm/embeddings.py).

## Ejemplos de preguntas y respuestas

El agente puede responder consultas como estas, siempre que la información necesaria esté indexada en los documentos:

- Pregunta: "¿Cuáles son las políticas para desplegar un servicio nuevo?"
  - Respuesta: El asistente recupera la política relevante y responde con un resumen acompañado de las fuentes consultadas.

- Pregunta: "¿Qué debo hacer si necesito una excepción para una regla de seguridad?"
  - Respuesta: El agente puede identificar que la solicitud requiere una acción especial y responder con la indicación de abrir un ticket.

- Pregunta: "Necesito más contexto para evaluar esta solicitud."
  - Respuesta: El sistema puede pedir información adicional si la pregunta no es lo suficientemente clara.

## Requisitos

- Python 3.10 o superior
- Acceso a una API de Gemini configurada en la variable de entorno `GEMINI_API_KEY`

## Instrucciones de ejecución

1. Crear y activar un entorno virtual:

   En Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

   ```env
   GEMINI_API_KEY=tu_api_key
   CHAT_MODEL=gemini-3.5-flash
   EMBEDDING_MODEL=models/text-embedding-001
   ```

4. Colocar los documentos fuente en la carpeta [documentos](documentos).

5. Ejecutar la aplicación:

   ```bash
   python web.py
   ```

6. Abrir el navegador en:

   ```text
   http://127.0.0.1:5000
   ```

## Notas importantes

- Si aún no existe un índice FAISS, la primera ejecución lo creará automáticamente a partir de los documentos de [documentos](documentos).
- Los logs de ejecución se almacenan en la carpeta [logs](logs).
- La interfaz está construida con Flask y los templates se encuentran en [templates](templates).
