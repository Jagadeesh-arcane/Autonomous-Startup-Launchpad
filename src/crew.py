from crewai import Crew, Task

from src.agents.market_researcher import market_researcher
from src.agents.financial_strategist import financial_strategist
from src.agents.content_marketer import content_marketer


def build_crew(idea: str):

    research = Task(
        description=(
            f"Research the market for the following startup idea:\n\n"
            f"{idea}\n\n"
            "Use web search ONLY if helpful. "
            "If tools fail, proceed with best-known industry knowledge."
        ),
        expected_output=(
            "Market research summary including target customer, problem, competitors, "
            "and approximate market size."
        ),
        agent=market_researcher,
    )

    finance = Task(
        description=(
            "Based on the market research, create realistic financial projections "
            "for a startup in its first year."
        ),
        expected_output=(
            "A financial plan including:\n"
            "- Revenue model\n"
            "- Pricing strategy\n"
            "- Estimated year-1 revenue\n"
            "- Estimated year-1 costs\n"
            "- Break-even timeline"
        ),
        agent=financial_strategist,
    )

    marketing = Task(
        description=(
            "Create a go-to-market and content marketing strategy "
            "for launching this startup."
        ),
        expected_output=(
            "A marketing strategy including:\n"
            "- Positioning statement\n"
            "- Primary acquisition channels\n"
            "- Messaging themes\n"
            "- Early traction plan"
        ),
        agent=content_marketer,
    )

    return Crew(
        agents=[
            market_researcher,
            financial_strategist,
            content_marketer,
        ],
        tasks=[
            research,
            finance,
            marketing,
        ],
        verbose=True,
    )
