from crewai import Agent
from src.tools.llm import get_llm

financial_strategist = Agent(
    role="Startup Financial Strategist",
    goal="Build realistic financial projections",
    backstory="CFO who scaled multiple SaaS startups.",
    llm=get_llm(),
    verbose=True,
    allow_delegation=False
)
