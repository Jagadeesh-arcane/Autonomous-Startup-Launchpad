from crewai.llm import LLM
from src.config.settings import OLLAMA_MODEL

def get_llm():
    return LLM(
        model=OLLAMA_MODEL,
        provider="ollama",
        base_url="http://localhost:11434"
    )
