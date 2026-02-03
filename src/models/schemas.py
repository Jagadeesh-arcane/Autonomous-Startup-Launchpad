from pydantic import BaseModel
from typing import List

class MarketResearch(BaseModel):
    target_customer: str
    problem: str
    competitors: List[str]
    market_size_usd: float

class FinancialPlan(BaseModel):
    revenue_model: str
    pricing: str
    year_1_revenue: float
    year_1_costs: float
    break_even_month: int

class BusinessPlan(BaseModel):
    idea: str
    market: MarketResearch
    finance: FinancialPlan
    marketing_strategy: str
