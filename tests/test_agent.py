import pytest
from src.trip_engine import TripDisruptionEngine

def test_long_haul_payout():
    engine = TripDisruptionEngine()
    res = engine.compute_eu261_compensation(6000, 4.0, carrier_fault=True)
    assert res["compensation_due_eur"] == 600
    assert res["statutory_eligible"] is True

def test_weather_exemption():
    engine = TripDisruptionEngine()
    res = engine.compute_eu261_compensation(6000, 5.0, carrier_fault=False)
    assert res["compensation_due_eur"] == 0
