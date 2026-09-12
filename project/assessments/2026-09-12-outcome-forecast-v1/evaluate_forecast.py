#!/usr/bin/env python3
"""Expose the arithmetic of a subjective forecast; this is not a proof verifier."""
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    inputs = json.loads((HERE / "forecast.json").read_text())
    scenarios = {}
    for scenario in ("cautious", "central", "favourable"):
        probability = Fraction(1)
        rows = []
        for milestone in inputs["milestones"]:
            conditional = Fraction(milestone[f"{scenario}_conditional_percent"], 100)
            if not 0 <= conditional <= 1:
                raise ValueError("Probability outside [0,1]")
            probability *= conditional
            rows.append({"id": milestone["id"],
                         "conditional_percent": float(100 * conditional),
                         "cumulative_fraction": str(probability),
                         "cumulative_percent": float(100 * probability)})
        scenarios[scenario] = rows
    # Exclusive bins are an arithmetic cross-check, not the preferred presentation.
    cumulative = [Fraction(1)] + [Fraction(row["cumulative_fraction"])
                                  for row in scenarios["central"]] + [Fraction(0)]
    bins = [cumulative[i] - cumulative[i + 1] for i in range(len(cumulative) - 1)]
    assert sum(bins) == 1 and all(value >= 0 for value in bins)
    report = {"schema": "murty-simon-subjective-forecast-arithmetic-v1",
              "status": "Arithmetic consistency only; no empirical calibration",
              "scenarios": scenarios,
              "central_exclusive_percent_lowest_to_highest": [float(100 * p) for p in bins],
              "central_exclusive_sum": str(sum(bins)),
              "display_central_rounded_to_nearest_five_percent": {
                  row["id"]: 5 * round(row["cumulative_percent"] / 5)
                  for row in scenarios["central"]}}
    (HERE / "arithmetic.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
