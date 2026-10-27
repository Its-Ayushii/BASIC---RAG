# all setting for the app live here, in one place
import os
from dotenv import load_dotenv

load_dotenv()

## environment variable secret
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

## define data path
DATA_FILE_PATH = os.path.join("data", "hr_policy.txt")

## vector store
# vector storage is done in 3 ways
# 1. in memory 2. persistent memory 3. cloud memory
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")

## models
# LLM and Embedding models

LLM_MODEL_NAME = "openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"

## Chunk and text splitting config
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

## retrival results
TOP_K_RESULTS = 3

## system instructions
SYSTEM_PROMPT = (
    "You are a friendly HR assistant."
    "Always use the search_hr_policy tool to look up facts before answering."
    "If the answer isn't in the search result, say you don't know."
    "Do not guess."
    )

def check_api_keys() -> None:
    """ stop early with a clear message if a required API key is missing"""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Please add it to your .env file. ")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY. Please add it to your .env file. ")

