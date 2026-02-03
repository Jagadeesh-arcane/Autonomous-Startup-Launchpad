import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "ollama/llama3")
OLLAMA_URL = "http://localhost:11434"
