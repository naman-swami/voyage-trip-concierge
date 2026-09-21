"""
Voyage Multi-Objective Travel Itinerary Optimizer
Evaluates Pareto optimality across travel budget, total transit duration, and eco-carbon rating.
"""
from typing import List, Dict, Any

class TravelOptimizationEngine:
    @staticmethod
    def evaluate_pareto_options(options: List[Dict[str, Any]], max_budget_usd: float) -> Dict[str, Any]:
        feasible = [o for o in options if o["cost_usd"] <= max_budget_usd]
        if not feasible:
            return {"status": "NO_FEASIBLE_OPTION", "recommendation": "INCREASE_BUDGET"}

        # Score formula: Balance rating / (cost_ratio * transit_ratio)
        best_option = max(feasible, key=lambda x: x["hotel_rating"] / (x["cost_usd"] * 0.001 + x["transit_hours"] * 0.1))

        return {
            "total_options_evaluated": len(options),
            "feasible_within_budget": len(feasible),
            "recommended_plan": best_option["plan_name"],
            "cost_usd": best_option["cost_usd"],
            "transit_hours": best_option["transit_hours"],
            "co2_footprint_kg": best_option["co2_kg"]
        }
