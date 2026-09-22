# Voyage Multi-Objective Itinerary Concierge

> **Autonomous Pareto Frontier Optimization for Corporate & Leisure Travel**  
> Balancing Financial Budget, Transit Duration, and Carbon Footprint ($CO_2e$) Trade-Offs.

---

### Multi-Objective Pareto Optimization

Rather than prescribing a single rigid route, Voyage constructs the non-dominated Pareto frontier across three competing objective dimensions:

$$\min \mathbf{F}(\mathbf{x}) = \left[ \text{Cost}(\mathbf{x}), \text{Duration}(\mathbf{x}), \text{Carbon}(\mathbf{x}) \right]^T$$

A travel option $\mathbf{x}_1$ dominates $\mathbf{x}_2$ if and only if $\mathbf{x}_1$ is strictly better in at least one dimension without being worse in any other.

---

### Sample Itinerary Trade-Off Matrix

Evaluated for benchmark transcontinental route (`fixtures/destinations/sample_travel_options.json`):

| Itinerary Persona | Selected Modality | Total Cost (USD) | Transit Time | Carbon ($kg CO_2e$) | Pareto Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Eco-Conscious Traveler** | High-Speed Rail + Hotel | **$340.00** | 6h 30m | **18.4 kg** | Non-Dominated |
| **Executive Express** | Direct Flight + Premium Transfer | $680.00 | **2h 45m** | 142.0 kg | Non-Dominated |
| **Budget Explorer** | Regional Bus + Economy Stay | **$160.00** | 10h 15m | 32.1 kg | Non-Dominated |
| *Sub-Optimal Route* | Multi-Layover Flight | $720.00 | 7h 10m | 185.0 kg | *Dominated (Pruned)* |

---

### Travel Concierge CLI

```bash
# Evaluate benchmark travel options along Pareto frontier
python concierge.py --demo

# Run multi-objective optimization unit tests
pytest tests/ -v
```

Traveler policy allowances, per-diem caps, and carbon offsets are governed by [TRAVEL_POLICY.md](TRAVEL_POLICY.md).
