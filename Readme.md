# 🎬 ClipMind

> **"Tired of watching lengthy news segments or complex tutorials? Just input the YouTube URL, and let LLMs assist you."**

**ClipMind** is an AI-powered tool that simplifies video content consumption. It summarizes YouTube videos, answers your questions, and provides multiple perspectives on topics using advanced language models.

---

## 🧩 Project Structure

```
ClipMind/
├── clipmind-backend/     # FastAPI backend
└── clipmind-frontend/    # React frontend
```

---

## 🚀 Features

### ✅ Part 1: YouTube Video Summarizer

* Input a YouTube URL.
* Fetches and transcribes the video.
* Summarizes content using LLaMA 2 or OpenAI models.

### 🧠 Part 2: Q\&A Box *(In Progress)*

* Pose questions about the video.
* Receive context-aware answers derived from the video's content.

### ⚖️ Part 3: BlindSpot – "What am I missing?" *(In Progress)*

* Presents multiple viewpoints on a topic.
* Aims to provide a balanced understanding by highlighting differing perspectives.

---

## 🛠️ Tech Stack

* **Frontend:** React, TypeScript, Tailwind CSS
* **Backend:** FastAPI (Python)
* **LLMs:** LLaMA 2, OpenAI GPT
* **Transcription:** `youtube-transcript-api`, Whisper
* **Vector Store (Planned):** FAISS / Supabase
* **Embeddings (Planned):** OpenAI / HuggingFace

---

## 🖥️ Installation & Running Guide

### Prerequisites

* **Node.js** (v14 or higher)
* **Python** (v3.8 or higher)
* **pip** (Python package installer)
* **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/sivani-tutika/ClipMind.git
cd ClipMind
```

### 2. Backend Setup

```bash
cd clipmind-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Environment Variables

Create a `.env` file in the `clipmind-backend` directory and add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key
```

### 3. Frontend Setup

```bash
cd ../clipmind-frontend
npm install
npm run dev
```

### 4. Running the Application

#### Start the Backend

```bash
cd ../clipmind-backend
uvicorn main:app --reload
```

#### Start the Frontend

```bash
cd ../clipmind-frontend
npm start
```

Access the application at `http://localhost:3000`.

---

## 📌 Future Enhancements

* Implement vector-based Q\&A using embeddings.
* Support for uploading custom video files.
* Browser extension for on-the-go summarization.
* Misinformation detection and content validation.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
