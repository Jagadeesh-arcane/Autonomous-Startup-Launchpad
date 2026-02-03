from crewai import Agent
from src.tools.llm import get_llm

content_marketer = Agent(
    role="Content & Growth Marketer",
    goal="Create a compelling go-to-market strategy",
    backstory="Former Head of Marketing at a YC startup.",
    llm=get_llm(),
    verbose=True,
    allow_delegation=False
)
