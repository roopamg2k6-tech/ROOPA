from fastapi import FastAPI
from .routes import router
from .db import init_models
from .sample_data import seed_sample_data

app = FastAPI(title="EcoTwin AI - Backend MVP")

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    # Initialize DB tables and seed sample data (simulated readings)
    await init_models()
    await seed_sample_data()
