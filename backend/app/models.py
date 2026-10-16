from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .db import Base

class SensorReading(Base):
    __tablename__ = "sensor_readings"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)  # e.g., 'solar', 'inverter', 'warehouse_zone_1'
    metric = Column(String, index=True)  # e.g., 'power_kw', 'temperature_c'
    value = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
