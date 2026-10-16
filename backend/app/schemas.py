from pydantic import BaseModel
from typing import List, Dict, Any

class SolarMetrics(BaseModel):
    expected_kw: float
    actual_kw: float
    inverter_kw: float
    demand_kw: float
    grid_import_kw: float
    grid_export_kw: float
    energy_cost_usd: float
    carbon_kg: float

class HeatmapPoint(BaseModel):
    zone: str
    temperature_c: float

class HeatmapResponse(BaseModel):
    zones: List[HeatmapPoint]

class Recommendation(BaseModel):
    title: str
    reason: str
    confidence: float
    actions: List[str]

class AIQuery(BaseModel):
    question: str
