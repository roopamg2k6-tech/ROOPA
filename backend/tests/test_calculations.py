import pytest
from backend.app.routes import get_solar

import asyncio

@pytest.mark.asyncio
async def test_get_solar_values():
    metrics = await get_solar()
    assert metrics.expected_kw > 0
    assert metrics.actual_kw > 0
    assert isinstance(metrics.energy_cost_usd, float)
    assert metrics.carbon_kg >= 0
