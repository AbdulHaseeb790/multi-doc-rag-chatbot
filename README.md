# Multi-Document RAG Chatbot

A production-ready RAG (Retrieval Augmented Generation) pipeline that lets you chat with your own PDF documents using AI.

## What it doesU
- Upload any number of PDFs into the `docs/` folder
- Ask questions in natural language
- Get accurate answers strictly from your documents
- Refuses to answer anything outside your documents

## Tech Stack
- LangChain — RAG pipeline
- FAISS — vector database for semantic search
- Google Gemini — text embeddings
- Groq (LLaMA 3.3 70B) — answer generation
- Streamlit — web UI

## How to Run

### 1. Install dependencies
pip install langchain langchain-community langchain-groq langchain-google-genai faiss-cpu streamlit python-dotenv

### 2. Add your API keys in `.env`
GROQ_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here

### 3. Add your PDFs
Drop any PDF files into the `docs/` folder.

### 4. Index your documents
python indexing_v2.py

### 5. Run the app
streamlit run app.py

## Project Structure

- `docs/` — drop your PDFs here
- `faiss_index_v2/` — auto-generated vector store
- `indexing_v2.py` — indexes all PDFs into FAISS
- `rag_chain_v2.py` — RAG chain with ask_question()
- `app.py` — Streamlit web UI
