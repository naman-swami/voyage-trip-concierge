import argparse
import json
import os
from itinerary.pareto_itinerary_engine import TravelOptimizationEngine

def main():
    parser = argparse.ArgumentParser(description="Voyage Trip Concierge CLI")
    parser.add_argument("--demo", action="store_true", help="Evaluate sample travel itineraries")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "destinations", "sample_travel_options.json")

    if args.demo:
        with open(data_file, "r") as f:
            options = json.load(f)
        res = TravelOptimizationEngine.evaluate_pareto_options(options, max_budget_usd=1000.0)
        print("=== VOYAGE MULTI-OBJECTIVE TRAVEL ITINERARY REPORT ===\n")
        print(f"Options Evaluated: {res['total_options_evaluated']} | Feasible under $1,000 budget: {res['feasible_within_budget']}")
        print(f"Recommended Plan: {res['recommended_plan']}")
        print(f"  Cost: ${res['cost_usd']} | Transit Duration: {res['transit_hours']} hrs")
        print(f"  Carbon Footprint: {res['co2_footprint_kg']} kg CO2\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
