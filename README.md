# 🚀 Production RAG System

A production-ready **Retrieval-Augmented Generation (RAG)** application that enables users to ask questions about PDF documents using **semantic search** and a **local Large Language Model (LLM)**.

The system extracts content from PDF documents, splits them into meaningful chunks, generates vector embeddings, stores them in **ChromaDB**, retrieves the most relevant information based on the user's query, and generates accurate answers using **Ollama**.

---

## 📌 Features

- 📄 PDF Document Ingestion
- ✂️ Intelligent Text Chunking
- 🧠 Sentence Transformer Embeddings
- 🔍 Semantic Search using ChromaDB
- 🤖 Local LLM Integration (Ollama)
- 📝 Prompt Engineering
- 📊 Structured Logging
- ⚠️ Custom Exception Handling
- 🏗️ Modular & Scalable Architecture
- 🔄 Easy to Extend for APIs and UI

---

# 🏛️ System Architecture

```
                    PDF Documents
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
                   Ollama (LLM)
                          │
                          ▼
                    Generated Answer
```

---

# 📂 Project Structure

```
RAG_2
│
├── app
│   ├── config
│   ├── core
│   ├── embedding
│   ├── ingestion
│   ├── llm
│   ├── prompt
│   ├── query
│   ├── retriever
│   └── vectorstore
│
├── data
│   ├── raw
│   └── vector_db
│
├── logs
│
├── scripts
│   ├── ingest.py
│   └── query.py
│
├── tests
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embedding Model | all-MiniLM-L6-v2 |
| LLM | Ollama (Qwen3:4B) |
| PDF Loader | PyPDFLoader |
| Logging | Python Logging |
| Exception Handling | Custom Exceptions |

---

# 🔄 RAG Workflow

### Document Ingestion

```
PDF

↓

Load Documents

↓

Split into Chunks

↓

Generate Embeddings

↓

Store in ChromaDB
```

---

### Question Answering

```
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

Answer
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Yaswanth-5ai/RAG_chatbot.git

cd RAG_chatbot
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

https://ollama.com

Download the model

```bash
ollama pull qwen3:4b
```

Start Ollama

```bash
ollama serve
```

---

# 📄 Index Documents

Place PDF files inside

```
data/raw/
```

Run

```bash
python -m scripts.ingest
```

---

# 💬 Ask Questions

```bash
python -m scripts.query
```

Example

```
Ask a question:

What is Machine Learning?
```

Output

```
Machine learning is a field of study that enables computers
to learn from data without being explicitly programmed.
```

---

# 📊 Logging

Application logs are stored inside

```
logs/
```

Logs include

- Document Loading
- Chunk Generation
- Embedding Generation
- Vector Search
- Prompt Building
- LLM Response Time
- Errors & Exceptions

---

# ⚠️ Exception Handling

Custom exceptions are implemented for

- Document Loading
- Document Splitting
- Embedding Generation
- Vector Database
- Retrieval
- Prompt Builder
- LLM
- Pipeline

---

# 🎯 Current Features

- ✅ Local LLM (Ollama)
- ✅ Semantic Search
- ✅ Modular Architecture
- ✅ Logging
- ✅ Exception Handling
- ✅ Configuration Management
- ✅ ChromaDB Persistence

---

# 🚀 Roadmap

## Version 1.0 ✅

- PDF Loader
- Chunking
- Embeddings
- ChromaDB
- Semantic Search
- Ollama Integration
- Logging
- Exception Handling

---

## Version 2.0 (In Progress)

- FastAPI Backend
- REST APIs
- Swagger Documentation
- Streamlit Frontend
- File Upload
- Multiple PDF Support

---

## Version 3.0

- Hybrid Search
- Reranking
- Query Rewriting
- Conversation Memory
- Authentication
- Docker
- Deployment

---

# 👨‍💻 Author

**Yaswanth Sai**

GitHub

https://github.com/Yaswanth-5ai

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.