# PDF Analyzer 📄🔍

PDF Analyzer is a tool that allows users to upload PDF files and ask questions about the content. It uses Google’s Generative AI to understand the document's context and provide answers.

## ✨ Features

* PDF uploads and stores them locally for processing.

* Uses RecursiveCharacterTextSplitter to break down large documents.

* Uses gemini-embedding-001 to convert text into vectors.

* Uses InMemoryVectorStore for temporary storage.

* Features a LangChain agent with a custom tool (pdf_search).

* A chat-based UI for user interaction.

## 🛠️ Tech Stack

* `Framework`: Streamlit

* `Orchestration`: LangChain

* `LLM`: Google Gemini (gemini-2.5-flash-lite)

* `Embeddings`: Google Generative AI Embeddings

* `Environment Management`: python-dotenv

## 🚀 Getting Started

### 1. Prerequisites

Python 3.9+.
A Google AI Studio API Key.

### 2. Installation

Clone the repository and install the dependencies:

    # bash
    pip install streamlit langchain-google-genai langchain-community langchain-text-splitters pypdf python-dotenv


### 3. Environment Setup

Create a .env file and add your Google API Key:

    # .env file
    GOOGLE_API_KEY=your_api_key_here

### 4. Running the App

Run this command in your terminal:

    bash
    streamlit run app.py

## 📖 How It Works

1. `Upload`: Upload a PDF.

2. `Process`: The app saves the file, loads it using PyPDFLoader, and splits the text.

3. `Embed`: The text is converted into embeddings and stored in an InMemoryVectorStore.

4. `Query`: When a user asks a question, the AI Agent uses the pdf_search tool.

5. `Respond`: The agent synthesizes the retrieved chunks into a natural language response.

## 🧹 Memory Management

The application has a "Clear Memory" button. Clicking this will delete the PDF from the local uploaded_files directory.

## ⚠️ Limitations

1. `Session Persistence`: The vector database is cleared if the Streamlit session restarts.

2. `File Types`: Supports .pdf files only.
