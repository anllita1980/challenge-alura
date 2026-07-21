# Pegasus Assistant

Pegasus Assistant es un asistente conversacional basado en Retrieval-Augmented Generation (RAG) para responder preguntas sobre políticas, procedimientos y documentación interna de la empresa Santos Pegasus Soluciones.

El sistema combina:

- un agente de clasificación para decidir si una solicitud puede resolverse automáticamente, necesita más información o debe abrir un ticket;
- un motor RAG que busca en documentos locales y genera respuestas contextualizadas;
- modelos de lenguaje y embeddings de Google Gemini.

## 🧱 Arquitectura

1. `app.py`
   - Interfaz por consola.
   - Inicializa el indexador RAG y el servicio `AssistantService`.
   - Procesa preguntas y muestra respuestas o peticiones de información.

2. `web.py`
   - Interfaz web con Flask.
   - Usa el mismo `AssistantService` para responder desde una página HTML.

3. `services/assistant.py`
   - Orquesta dos componentes principales:
     - `PegasusAgent` para clasificar la solicitud.
     - `RAGService` para buscar en documentos y generar la respuesta cuando procede.

4. `agentes/pegasus.py`
   - Utiliza Google Gemini para decidir entre:
     - `AUTO_RESOLVER`
     - `PEDIR_INFO`
     - `ABRIR_TICKET`

5. `rag/`
   - `loader.py`: carga PDFs desde `documentos/`.
   - `splitter.py`: divide las páginas en chunks de texto.
   - `indexer.py`: genera o carga el índice FAISS.
   - `vectorstore.py`: guarda/carga el índice local en `vectorstore/`.
   - `retriever.py`: obtiene los documentos más relevantes.
   - `service.py`: genera una respuesta usando el modelo y el prompt de RAG.

6. `llm/`
   - `chat.py`: configura el modelo de lenguaje Gemini.
   - `embeddings.py`: configura el modelo de embeddings Gemini.

7. `config.py`
   - Define rutas y carga variables de entorno.

## 🔄 Flujo de operación

1. Se cargan documentos PDF desde `documentos/`.
2. Se generan chunks de texto y embeddings.
3. Se construye o se carga el índice FAISS en `vectorstore/`.
4. Al recibir una pregunta:
   - `PegasusAgent` decide si se puede responder automáticamente, si falta información o si debe abrirse un ticket.
   - Si es `AUTO_RESOLVER`, `RAGService` busca documentos relevantes y genera la respuesta con contexto.
   - Si es `PEDIR_INFO`, devuelve una solicitud de información adicional.
   - Si es `ABRIR_TICKET`, indica que la solicitud requiere ticket.

## 💬 Ejemplos de preguntas y respuestas

### Ejemplo 1: respuesta automática
Pregunta:
- `¿Dónde puedo encontrar la política de despliegue?`

Resultado esperado:
- Tipo: `RESPUESTA`
- Respuesta: texto generado desde el contexto relevante.
- Fuentes: lista de documentos/páginas relevantes.

### Ejemplo 2: pedir más información
Pregunta:
- `Necesito ayuda con el acceso a la base de datos.`

Resultado posible:
- Tipo: `PEDIR_INFO`
- Mensaje: `Necesito un poco más de información para ayudarte.`
- Campos faltantes: lista de datos adicionales requeridos.

### Ejemplo 3: abrir ticket
Pregunta:
- `Quiero una excepción para desplegar fuera de horario.`

Resultado posible:
- Tipo: `ABRIR_TICKET`
- Mensaje: `La solicitud requiere abrir un ticket.`
- Urgencia: `BAJA` / `MEDIANA` / `ALTA`

> Nota: las respuestas dependen del contenido de los documentos y de la interpretación del modelo.

## ⚙️ Requisitos

- Python 3.10 o superior
- Una clave de API de Google Gemini
- Acceso a internet para consumir los modelos de Gemini

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd challenge-alura
```

2. Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🔐 Configuración

Crea un archivo `.env` en la raíz del proyecto con:

```env
GEMINI_API_KEY=tu_clave_de_gemini
CHAT_MODEL=gemini-2.0-flash
EMBEDDING_MODEL=gemini-embedding-001
```

## ▶️ Ejecución

- Consola: `python app.py`
- Web: `python web.py`

Para salir en consola, escribe:

```text
salir
```

## 📁 Estructura del proyecto

```text
challenge-alura/
├── app.py
├── config.py
├── requirements.txt
├── agentes/
├── documentos/
├── llm/
├── logs/
├── rag/
├── services/
├── ui/
└── vectorstore/
```

## ✅ Puntos clave

- El asistente usa RAG para responder con contexto extraído de documentos.
- El agente clasifica la entrada en respuesta automática, solicitud de más información o apertura de ticket.
- El índice FAISS se guarda en `vectorstore/` y se reutiliza entre ejecuciones.

## 📄 Licencia

Este proyecto se proporciona como ejemplo educativo y de demostración.
