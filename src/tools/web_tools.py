from crewai.tools import BaseTool
from duckduckgo_search import DDGS
from pydantic import BaseModel, Field
from typing import Union, Type, Any


# --- Tool Input Schema (RELAXED ON PURPOSE) ---
class MarketSearchInput(BaseModel):
    query: Union[str, dict] = Field(
        ...,
        description="Plain text search query about market, competitors, or industry"
    )


class MarketSearchTool(BaseTool):
    name: str = "market_search"
    description: str = (
        "Search the web for real-world market demand, competitors, and industry context "
        "using DuckDuckGo. Input must be a simple search query."
    )

    args_schema: Type[BaseModel] = MarketSearchInput

    def _run(self, query: Any) -> str:
        # --- HARD NORMALIZATION (CRITICAL) ---
        if isinstance(query, dict):
            # Extract meaningful text from bad tool calls
            query = " ".join(str(v) for v in query.values())
        else:
            query = str(query)

        query = query.strip()
        if not query:
            return "No valid query provided."

        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(r["body"])

        return "\n".join(results) if results else "No relevant results found."
