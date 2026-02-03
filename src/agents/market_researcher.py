from crewai import Agent
from src.tools.web_tools import MarketSearchTool
from src.tools.llm import get_llm

market_researcher = Agent(
    role="Market Research Analyst",
    goal="Analyze market demand and competitors",
    backstory=(
        "You are a professional analyst. "
        "Do NOT explain your reasoning. "
        "Do NOT output Thought/Action steps. "
        "Only provide the final answer."
    ),
    tools=[MarketSearchTool()],
    llm=get_llm(),
    verbose=True,
    allow_delegation=False,
    max_iter=2,  
)
