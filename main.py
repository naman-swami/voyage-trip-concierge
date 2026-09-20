import json
import argparse
from src.trip_engine import TripDisruptionEngine

def main():
    parser = argparse.ArgumentParser(description="Voyage Trip Concierge CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated EU261 statutory claim audit")
    args = parser.parse_args()

    engine = TripDisruptionEngine()
    report = engine.compute_eu261_compensation(flight_distance_km=5800, delay_arrival_hours=4.5, carrier_fault=True)
    print("="*60)
    print(" VOYAGE TRIP DISRUPTION & STATUTORY AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
