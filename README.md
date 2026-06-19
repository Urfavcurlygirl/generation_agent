# Generation Agent Projects

Welcome to the **Generation Agent** repository! This project serves as an exploration and demonstration of building intelligent applications using Large Language Models (LLMs), LangChain, LangGraph, and Streamlit. 

The repository is divided into two main parts:
1. Core LLM scripts and LangGraph Agent demonstrations.
2. A Streamlit-based YouTube Assistant that leverages Retrieval-Augmented Generation (RAG) to answer questions based on video transcripts.

## 🚀 Features

### 1. LangChain & LangGraph Basics (Root Directory)
- **Pet Name Generator (`main.py`)**: A simple implementation using LangChain and Groq's API (`llama-3.3-70b-versatile`) to generate creative names for pets based on user input.
- **React Agent (`test_langchain.py`)**: Demonstrates the modern approach to building agents using `langgraph`. The agent is equipped with:
  - A custom Python-based calculator tool.
  - The Wikipedia tool for knowledge retrieval.
  - Thinking process visualization through streaming messages.

### 2. YouTube Assistant (`Ytb assistant/`)
A fully functional Streamlit application that allows you to query any YouTube video.
- **Transcript Extraction**: Automatically pulls transcripts from YouTube videos using `YoutubeLoader`.
- **Vector Database**: Chunks the transcript and stores it in a FAISS vector database using `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`).
- **Interactive Chat UI**: Uses Streamlit to provide an intuitive interface where users can paste a YouTube URL and ask questions.
- **Powered by Groq**: Uses Groq's high-speed inference for answering questions based on the retrieved video context.

## 🛠️ Technology Stack

- **Frameworks**: [LangChain](https://python.langchain.com/), [LangGraph](https://langchain-ai.github.io/langgraph/), [Streamlit](https://streamlit.io/)
- **LLM Provider**: [Groq](https://groq.com/) (`llama-3.3-70b-versatile`)
- **Embeddings**: [HuggingFace](https://huggingface.co/) (`all-MiniLM-L6-v2`)
- **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Urfavcurlygirl/generation_agent.git
   cd generation_agent
   ```

2. **Set up a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   Make sure you have all the required libraries installed. You can install the major requirements using pip:
   ```bash
   pip install langchain langchain-groq langchain-openai langchain-community langgraph streamlit python-dotenv faiss-cpu youtube-transcript-api sentence-transformers wikipedia
   ```

4. **Environment Variables:**
   Create a `.env` file in the root of the project and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 💻 Usage

### Running Core Agent Examples
To run the basic generation script:
```bash
python main.py
```

To run the LangGraph React Agent (Calculator + Wikipedia):
```bash
python test_langchain.py
```

### Running the YouTube Assistant
Navigate to the YouTube Assistant folder and run the Streamlit app:
```bash
cd "Ytb assistant"
streamlit run main.py
```
This will open a new tab in your default web browser where you can interact with the app.

## 📁 Repository Structure
```
generation_agent/
│
├── main.py                  # Basic LangChain pet name generator
├── test_langchain.py        # LangGraph ReAct agent implementation
├── check_executor.py        # Environment check script
├── check_imports.py         # Import validation script
├── inspect_agents.py        # Agent inspection utility
├── .env                     # Environment variables (Create this!)
│
└── Ytb assistant/           # YouTube RAG Application
    ├── main.py              # Streamlit UI
    └── youtube_helper.py    # Logic for YouTube transcript processing & FAISS
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.