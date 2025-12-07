# SwarajDesk Multilingual RAG-Powered Conversational Support System

An AI-powered multilingual citizen support system that delivers accurate, hallucination-free responses using Retrieval-Augmented Generation (RAG). The system supports both text and voice interactions, answering queries strictly from verified SwarajDesk documents and policies.

## Features

### Core Capabilities

- **Multilingual Support**: English, Hindi, Hinglish, and Odia (easily scalable)
- **Zero Hallucinations**: Answers derived exclusively from authenticated knowledge base
- **Voice Input**: Speech-to-text conversion for natural voice queries
- **Voice Output**: Text-to-speech responses in selected language
- **Text Chat**: Full-featured text-based conversation interface
- **Context-Aware**: Vector similarity search with semantic understanding
- **Smart Escalation**: Automatic redirection to support/admin when needed

---

## System Architecture

```
User Input (Text/Voice)
        ↓
[Speech-to-Text] ← Google STT (if voice)
        ↓
┌─────────────────────────────┐
│      RAG Pipeline           │
│  • Sentence Transformers    │
│  • ChromaDB Vector Store    │
│  • Groq LLM (gpt-oss-120b)  │
└─────────────────────────────┘
        ↓
Bot Response (Text)
        ↓
[Text-to-Speech] ← gTTS (if voice)
        ↓
Final Output (Text/Audio)
```

---

## Project Structure

```
SIH-SWARJ_AI_RAG_BOT_(DEPLOYED_FINAL)/
│
├── main.py                      # FastAPI app entry point
├── app.py                       # RAG pipeline & LLM logic
├── speech_to_text.py            # Voice input processing
├── text_to_speech.py            # Voice output generation
├── voice_routes.py              # Voice chat API endpoints
├── SwarajDesk_vectorDB.json     # Knowledge base documents
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not in git)
│
├── chroma_store/                # Vector database persistence
└── static/
    └── voice/                   # Generated audio files
```

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI + Uvicorn |
| **Vector Store** | ChromaDB |
| **Embeddings** | HuggingFace Sentence-Transformers (multilingual) |
| **LLM** | Groq API (openai/gpt-oss-120b) |
| **Speech-to-Text** | Google SpeechRecognition |
| **Text-to-Speech** | gTTS |
| **Deployment** | AWS EC2, Gunicorn + Nginx |

---

## Project Setup

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/swarajdesk-rag-bot.git
   cd swarajdesk-rag-bot
   ```

2. **Create and activate virtual environment**
   ```bash
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
   LANGCHAIN_API_KEY=your_langchain_key_here  # Optional
   ```

5. **Create required directories**
   ```bash
   mkdir -p static/voice
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`

---

## API Endpoints

### Health Check
```http
GET /health
```

### Welcome
```http
GET /
```

### Text Chat
```http
POST /chat_swaraj
Content-Type: application/json

{
  "user_query": "How do I reset my password?",
  "language": "english"
}
```

**Response:**
```json
{
  "reply": "To reset your password, navigate to...",
  "sources": ["document_id_1", "document_id_2"]
}
```

### Voice Chat
```http
POST /voice-chat
Content-Type: multipart/form-data

Form Data:
- file: audio file (.wav or .mp3)
- language: english | hindi | hinglish | odia
```

**Response:**
```json
{
  "reply": "Your answer in text format",
  "audio_url": "/static/voice/82f3b0a5e4b.mp3"
}
```

---

## Safety & Hallucination Prevention

The system ensures accuracy through:

- **Source-grounded responses**: Answers derived only from retrieved context
- **No fabrication**: System never generates information not in the knowledge base
- **Query validation**: Non-SwarajDesk queries redirected to support
- **Escalation protocol**: Complex cases forwarded to admin
- **Citation tracking**: All responses linked to source documents

---

## Supported Languages

| Language | Code | Status |
|----------|------|--------|
| English | `english` | Full Support |
| Hindi | `hindi` | Full Support |
| Hinglish | `hinglish` | Full Support |
| Odia | `odia` | Full Support |

*Additional languages can be added by extending the language configuration.*


