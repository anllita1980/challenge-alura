# Pegasus Assistant

Pegasus Assistant es un asistente conversacional basado en Retrieval-Augmented Generation (RAG) para responder preguntas sobre políticas, procedimientos y documentación interna de la empresa Santos Pegasus Soluciones.

El sistema combina:

- un agente de clasificación para decidir si una solicitud puede resolverse automáticamente, necesita más información o debe abrir un ticket;
- un motor RAG que busca en documentos locales y genera respuestas contextualizadas;
- modelos de lenguaje y embeddings de Google Gemini.

## 🚀 Características

- Respuesta automática a preguntas sobre políticas y documentación.
- Búsqueda semántica sobre documentos almacenados en la carpeta de documentos.
- Clasificación automática de solicitudes en tres categorías:
  - AUTO_RESOLVER
  - PEDIR_INFO
  - ABRIR_TICKET
- Interfaz por consola para interactuar con el asistente.

## 🧱 Requisitos

- Python 3.10 o superior
- Una clave de API de Google Gemini
- Acceso a internet para consumir los modelos de Gemini

## ⚙️ Instalación

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

Crea un archivo llamado .env en la raíz del proyecto con las siguientes variables:

```env
GEMINI_API_KEY=tu_clave_de_gemini
CHAT_MODEL=models/gemini-3.5-flash
EMBEDDING_MODEL=models/gemini-embedding-001
```

> Asegúrate de reemplazar los valores con tus credenciales reales.

## ▶️ Ejecución

Inicia la aplicación con:

```bash
python app.py
```

Una vez iniciada, puedes escribir preguntas en la consola. Por ejemplo:

```text
¿Dónde puedo encontrar la política de despliegue?
```

Para salir del asistente, escribe:

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

## 🧠 Cómo funciona

1. El sistema carga documentos desde la carpeta documentos.
2. Genera chunks y embeddings para construir un índice vectorial.
3. Cuando el usuario hace una pregunta, el agente decide la mejor acción.
4. Si la solicitud puede resolverse, el módulo RAG recupera contexto relevante y genera una respuesta.

## 📝 Notas

- Los documentos que quieras que el asistente consulte deben colocarse en la carpeta documentos.
- Si el índice vectorial no existe, se crea automáticamente la primera vez que ejecutas la aplicación.
- Los logs de ejecución se guardan en la carpeta logs.

## 📄 Licencia

Este proyecto se proporciona como ejemplo educativo y de demostración.
