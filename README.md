# Voyage Multi-Criteria Travel Concierge

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Travel](https://img.shields.io/badge/Domain-Travel_Hospitality_Pareto-orange.svg)](docs/travel_optimization_theory.md)
[![Algorithm](https://img.shields.io/badge/Model-Pareto_Frontier-blue.svg)](docs/travel_optimization_theory.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An intelligent travel and hospitality concierge engine performing multi-objective Pareto optimization across travel expenditure, transit latency, and carbon footprints.

```
                    ┌─────────────────────────┐
                    │ Multi-Modal Trip Options│
                    │ (Air, Rail, Hotel, CO2) │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ itinerary/pareto_engine │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │ Budget Filter       │         │ Pareto Tradeoff     │
      │ Cost <= Max Budget  │         │ Rating vs Duration  │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Optimal Itinerary Plan  │
                    │ (Recommended Package)   │
                    └─────────────────────────┘
```

## Features

- **Multi-Objective Travel Tradeoffs**: Balances budget constraints against transit fatigue and hotel comfort.
- **Carbon-Aware Travel Guidance**: Compares high-speed rail vs domestic flights on emissions.
- **Benchmark Destination Packages**: Includes multi-modal European and transcontinental travel options.

## Directory Structure

```
voyage-trip-concierge/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint travel provenance
├── itinerary/
│   └── pareto_itinerary_engine.py   # Multi-objective Pareto optimizer
├── fixtures/
│   └── destinations/
│       └── sample_travel_options.json # Benchmark travel packages
├── docs/
│   └── travel_optimization_theory.md # Optimization formulation
├── tests/
│   └── test_agent.py                # Travel concierge test suite
├── concierge.py                          # Voyage CLI
└── requirements.txt
```

## Quick Start

```bash
# Run travel optimization tests
pytest tests/ -v

# Optimize sample itinerary options
python concierge.py --demo
```
