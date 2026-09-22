# Corporate Travel Policy & Duty of Care Standards

## 1. Governance & Regulatory Framework
Voyage Multi-Objective Itinerary Concierge operates under enterprise travel guidelines aligned with:
- **ISO 31030:2021 (Travel Risk Management — Guidance for Organizations)**
- **U.S. General Services Administration (GSA) Federal Travel Regulation (FTR)**
- **Corporate Sustainability Due Diligence Directive (CSDDD)**

---

## 2. Multi-Objective Pareto Frontier Optimization
The itinerary planning engine evaluates flight, rail, ground transit, and accommodation options across three competing objectives:

$$\min \mathbf{F}(\mathbf{x}) = \begin{bmatrix} \text{Cost}(\mathbf{x}) \\ \text{Duration}(\mathbf{x}) \\ \text{Carbon}(\mathbf{x}) \end{bmatrix}$$

### A. Non-Dominated Solution Set (Pareto Dominance)
An itinerary $\mathbf{x}^*$ belongs to the Pareto frontier $\mathcal{P}$ if and only if there does not exist any alternative itinerary $\mathbf{x}'$ such that:
$$\forall i \in \{\text{cost}, \text{time}, CO_2\}, \quad f_i(\mathbf{x}') \le f_i(\mathbf{x}^*) \quad \text{and} \quad \exists j, \quad f_j(\mathbf{x}') < f_j(\mathbf{x}^*)$$

### B. Enterprise Policy Guardrails:
1. **Budget Cap**: Maximum allowable round-trip spend per employee grade (e.g., $\$800.00$ domestic, $\$2,500.00$ international).
2. **Transit Time Window**: Total travel duration including layovers cannot exceed **12 consecutive hours** for single-day itineraries.
3. **Mandatory Rail Substitution**: If high-speed rail travel time is under **4 hours**, commercial air travel is blocked by policy to minimize Scope 3 carbon emissions.

---

## 3. Traveler Safety & Duty of Care Protocols
- **High-Risk Destination Geofencing**: Automatically screens itineraries against U.S. Department of State Level 3 and 4 travel advisories.
- **Flight Redundancy**: No more than 3 company executive officers may travel on the same scheduled aircraft flight.
- **24/7 Itinerary Monitoring**: In the event of flight cancellations or severe weather, the engine automatically re-routes travelers along the nearest Pareto-efficient alternative.
