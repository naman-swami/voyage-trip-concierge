# Explainability — voyage-trip-concierge

## Decision Reasoning
Voyage manages travel logistics by tracking flight state vectors, comparing layover margins against airport connection thresholds, and activating contingency routing before passengers become stranded.

## Data Sources and Inputs Used
Global Distribution Systems (Amadeus/Sabre PNRs), FlightAware live ADS-B flight feeds, IATA Minimum Connect Time manuals, and DOT regulatory rulebooks.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, voyage-trip-concierge assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, voyage-trip-concierge will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, voyage-trip-concierge explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
voyage-trip-concierge actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Sovereign Border Control: Does not issue international travel visas or override passport immigration entry denials.
- Carrier Fleet Maintenance: Cannot physically fix aircraft mechanical engine defects.
- Air Traffic Control: Cannot override FAA or Eurocontrol ground delay programs.
- Travel Insurance: Does not directly underwrite or settle private travel insurance claims.

## Uncertainty Quantification Approach
When flight delays are categorized by airlines under ambiguous 'extraordinary circumstances' (e.g., weather versus technical fault), Voyage flags compensation claim ambiguity and requests technical airline maintenance logs for evidentiary verification.
