# 🚀 Enterprise RAG Assistant

A production-grade **Retrieval-Augmented Generation (RAG)** system that enables users to upload documents and interact with them using natural language through semantic search and local Large Language Models.

The system extracts content from documents, intelligently chunks the text, generates embeddings using Sentence Transformers, stores vectors in **ChromaDB**, retrieves relevant context using semantic similarity, and generates accurate responses using **Ollama-powered LLMs**.

---

# 📌 Features

## Backend Features

* 📄 PDF Document Ingestion
* 🗑️ Document Deletion Support
* 📋 Document Metadata Tracking
* ✂️ Intelligent Text Chunking
* 🧠 Sentence Transformer Embeddings
* 🔍 Semantic Search with ChromaDB
* 🤖 Local LLM Integration using Ollama
* 📝 Prompt Engineering
* 📊 Structured Logging
* ⚠️ Custom Exception Handling
* 📈 Health and Statistics APIs
* 📚 Swagger Documentation
* 🏗️ Dependency Injection Ready
* 🔄 Modular Architecture

---

## Frontend Features

* 💬 ChatGPT-style Conversation Interface
* 📂 Sidebar Document Management
* 📤 File Upload Support
* 📊 Real-time Statistics Dashboard
* 📑 Document Metadata Visualization
* 🧹 Chat History Management
* 🗑️ One-click Document Removal

---

## DevOps Features

* 🐳 Dockerized Backend
* 🐳 Dockerized Frontend
* 📦 Docker Compose Support
* 🔄 Persistent Storage Volumes
* 🚀 Deployment Ready

---

# 🏛️ System Architecture

```text
                     Upload Document
                            │
                            ▼
                    FastAPI Backend
                            │
                            ▼
                    Document Loader
                            │
                            ▼
                   Document Splitter
                            │
                            ▼
             SentenceTransformer Embeddings
                            │
                            ▼
                        ChromaDB
                            │
                            ▼
                        Retriever
                            │
                            ▼
                    Prompt Builder
                            │
                            ▼
                     Ollama LLM
                            │
                            ▼
                     Generated Answer
                            │
                            ▼
                    Streamlit Frontend
```

---

# 📂 Project Structure

```text
RAG_2
│
├── app
│   ├── api
│   ├── config
│   ├── container
│   ├── core
│   ├── embedding
│   ├── ingestion
│   ├── llm
│   ├── prompt
│   ├── query
│   ├── retrieval
│   ├── storage
│   └── vectorstore
│
├── frontend
│   ├── api
│   ├── components
│   └── app.py
│
├── data
│   └── raw
│
├── chroma_db
│
├── logs
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# ⚙️ Technology Stack

| Category          | Technology       |
| ----------------- | ---------------- |
| Language          | Python 3.13      |
| Backend           | FastAPI          |
| Frontend          | Streamlit        |
| Framework         | LangChain        |
| Vector Database   | ChromaDB         |
| Embedding Model   | all-MiniLM-L6-v2 |
| LLM               | Ollama           |
| Default Model     | Qwen3:4B         |
| Package Manager   | uv               |
| Containerization  | Docker           |
| Orchestration     | Docker Compose   |
| Logging           | Python Logging   |
| API Documentation | Swagger/OpenAPI  |

---

# 🔄 RAG Workflow

## Document Ingestion

```text
Upload Document
        ↓
Load Document
        ↓
Split into Chunks
        ↓
Generate Embeddings
        ↓
Store in ChromaDB
        ↓
Store Metadata
```

---

## Question Answering

```text
User Question
      ↓
Generate Query Embedding
      ↓
Semantic Search
      ↓
Retrieve Top K Chunks
      ↓
Build Prompt
      ↓
Ollama
      ↓
Generated Answer
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Yaswanth-5ai/RAG_chatbot.git
cd RAG_chatbot
```

---

## Install Dependencies

```bash
uv sync
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

# 🤖 Install Ollama

Install:

```text
https://ollama.com/download
```

Download model:

```bash
ollama pull qwen3:4b
```

Start Ollama:

```bash
ollama serve
```

---

# 🔧 Configuration

Configuration file:

```text
app/config/settings.py
```

Example:

```python
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_MODEL = "qwen3:4b"

OLLAMA_HOST = "http://localhost:11434"

TOP_K = 5

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200
```

---

# 🔄 Supported LLM Models

To switch models, change:

```python
LLM_MODEL = "qwen3:4b"
```

Examples:

### Fast Models

```text
phi3:mini
qwen2.5:3b
```

### Balanced Models

```text
qwen3:4b
gemma3:4b
```

### Large Models

```text
llama3:8b
qwen2.5:7b
```

---

# 🚀 Run Application Locally

## Backend

```bash
uv run uvicorn app.api.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Frontend

```bash
uv run streamlit run frontend/app.py
```

Frontend:

```text
http://localhost:8501
```

---

# 🐳 Docker Deployment

Build backend image:

```bash
docker build -t rag-backend -f Dockerfile.backend .
```

Build frontend image:

```bash
docker build -t rag-frontend -f Dockerfile.frontend .
```

Start all services:

```bash
docker compose up
```

Access:

Frontend:

```text
http://localhost:8501
```

Backend:

```text
http://localhost:8000/docs
```

---

# 📚 Available API Endpoints

| Method | Endpoint                | Description            |
| ------ | ----------------------- | ---------------------- |
| GET    | `/health`               | Health Check           |
| GET    | `/stats`                | Application Statistics |
| POST   | `/ingest`               | Upload Document        |
| GET    | `/documents`            | List Documents         |
| DELETE | `/documents/{filename}` | Delete Document        |
| POST   | `/query`                | Ask Questions          |

---

# 📊 Logging

Logs include:

* Document Loading
* Chunk Generation
* Embedding Generation
* Vector Search
* Prompt Building
* LLM Inference
* API Requests
* Error Handling

---

# 🚀 Roadmap

## Version 1.0 ✅

* PDF Loader
* Chunking
* Embeddings
* ChromaDB
* Ollama Integration
* Logging
* Exception Handling

---

## Version 2.0 ✅

* FastAPI Backend
* REST APIs
* Swagger Documentation
* Streamlit Frontend
* File Upload
* Multiple Document Support
* Metadata Management
* Docker Support

---

## Version 3.0

* Source Citations
* DOCX Support
* Hybrid Search
* Reranking
* Authentication
* Cloud Deployment
* CI/CD Pipeline

---

# 👨‍💻 Author

## Yaswanth Sai

GitHub:

[Yaswanth Sai GitHub Profile](https://github.com/Yaswanth-5ai/RAG_streamlit.git)

LinkedIn:

[yaswanth linkedin](https://www.linkedin.com/in/yaswanth-sai-7a599b1a9)

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.
  