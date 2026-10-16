from .db import AsyncSessionLocal
from .models import SensorReading
import asyncio

async def seed_sample_data():
    # Lightweight seeding — no duplicates on repeated runs for MVP simplicity
    async with AsyncSessionLocal() as session:
        # We intentionally don't populate a large dataset; endpoints return simulated values.
        await asyncio.sleep(0.01)
