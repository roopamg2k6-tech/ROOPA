from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .schemas import SolarMetrics, HeatmapResponse, HeatmapPoint, Recommendation, AIQuery
import os
import shutil
from typing import List

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/api/solar", response_model=SolarMetrics)
async def get_solar():
    # Simulated values (explicitly simulated)
    expected = 120.0
    actual = 98.5
    inverter = 96.0
    demand = 150.0
    grid_import = max(0.0, demand - actual)
    grid_export = max(0.0, actual - demand)
    energy_cost = (grid_import * 0.15) - (grid_export * 0.05)
    carbon_intensity = 0.4  # kgCO2 per kWh (sample)
    carbon = (actual / 1.0) * carbon_intensity

    return SolarMetrics(
        expected_kw=expected,
        actual_kw=actual,
        inverter_kw=inverter,
        demand_kw=demand,
        grid_import_kw=grid_import,
        grid_export_kw=grid_export,
        energy_cost_usd=round(energy_cost, 3),
        carbon_kg=round(carbon, 3),
    )

@router.get("/api/warehouse/heatmap", response_model=HeatmapResponse)
async def warehouse_heatmap():
    # Simulated warehouse zones
    zones = [
        HeatmapPoint(zone="A1", temperature_c=2.5),
        HeatmapPoint(zone="A2", temperature_c=3.0),
        HeatmapPoint(zone="B1", temperature_c=4.2),
        HeatmapPoint(zone="B2", temperature_c=2.8),
    ]
    return HeatmapResponse(zones=zones)

@router.post("/api/ai-assistant")
async def ai_assistant(query: AIQuery):
    # Rule-based assistant (clearly labelled)
    q = query.question.lower()
    if "why" in q and "solar" in q:
        return JSONResponse({"answer": "Simulated solar underperformance can be caused by dust/soiling, shading, inverter issues, or incorrect array orientation. Recommend inspection and cleaning."})
    if "optimiz" in q or "schedule" in q:
        return JSONResponse({"answer": "This is a rule-based recommendation: shift flexible loads to periods with higher solar generation or lower grid carbon intensity. Integrate demand-response schedules with constraints."})
    return JSONResponse({"answer": "I am a rule-based assistant. I can explain simulated trends and offer non-binding recommendations. For detailed analysis, connect a generative AI service later."})

@router.post("/api/upload-image")
async def upload_image(file: UploadFile = File(...)):
    uploads_dir = os.getenv("UPLOADS_DIR", "uploads")
    os.makedirs(uploads_dir, exist_ok=True)
    file_path = os.path.join(uploads_dir, file.filename)
    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"filename": file.filename, "message": "File saved (simulated). No CV model is currently applied."}

@router.post("/api/optimize", response_model=List[Recommendation])
async def optimize():
    # Simple deterministic recommendations based on simulated heuristics
    recs = [
        Recommendation(title="Panel Cleaning", reason="Actual generation is below expected by >15%", confidence=0.8, actions=["Schedule cleaning", "Inspect for soiling"]),
        Recommendation(title="Shading Inspection", reason="Variance across array indicates potential shading", confidence=0.6, actions=["Inspect trees/nearby structures"]),
    ]
    return recs
