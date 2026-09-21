import os
import pytest
from itinerary.pareto_itinerary_engine import TravelOptimizationEngine

def test_travel_budget_filtering():
    options = [
        {"plan_name": "Luxury", "cost_usd": 2000.0, "transit_hours": 2.0, "hotel_rating": 5.0, "co2_kg": 300.0},
        {"plan_name": "Eco-Rail", "cost_usd": 500.0, "transit_hours": 4.0, "hotel_rating": 4.5, "co2_kg": 15.0}
    ]
    res = TravelOptimizationEngine.evaluate_pareto_options(options, max_budget_usd=1000.0)
    assert res["feasible_within_budget"] == 1
    assert res["recommended_plan"] == "Eco-Rail"
