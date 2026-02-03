import os

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Hard-disable OpenAI everywhere
os.environ["CREWAI_TELEMETRY"] = "false"
os.environ["OPENAI_API_KEY"] = "dummy"

from src.crew import build_crew

def run(idea: str) -> str:
    crew = build_crew(idea)
    result = crew.kickoff()

    # CrewAI returns CrewOutput, extract text safely
    if hasattr(result, "raw"):
        return result.raw

    return str(result)

if __name__ == "__main__":
    print(run("AI-powered hiring platform"))
