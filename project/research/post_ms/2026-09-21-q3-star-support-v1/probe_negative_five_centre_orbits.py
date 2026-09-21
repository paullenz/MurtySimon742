#!/usr/bin/env python3
"""Bounded equal-multiplicity probe for the two one-copy-negative supports."""
import json
import random
from pathlib import Path

from search_five_centre_support_orbits import solve


def main():
    supports = [(0, 1, 2, 3, 4), (0, 1, 2, 5, 6)]
    rows = []
    for support in supports:
        for coordinate_multiplicity in range(1, 4):
            for parity_multiplicity in range(0, 4):
                for star_multiplicity in range(1, 5):
                    codes = []
                    for i in range(3):
                        for e in range(2):
                            codes += [f"C{i}{e}"] * coordinate_multiplicity
                    codes += ["P0"] * parity_multiplicity
                    codes += ["P1"] * parity_multiplicity
                    for centre in support:
                        codes += [f"S{centre}"] * star_multiplicity
                    model = solve(codes)
                    rows.append({
                        "support": list(support),
                        "coordinate_multiplicity": coordinate_multiplicity,
                        "each_parity_multiplicity": parity_multiplicity,
                        "each_star_multiplicity": star_multiplicity,
                        "satisfiable": model is not None,
                        "model": model,
                    })
    feasible = [row for row in rows if row["satisfiable"]]
    random.seed(747)
    asymmetric = []
    halfcodes = ["C00", "C01", "C10", "C11", "C20", "C21", "P0", "P1"]
    for support in supports:
        for trial in range(100):
            half_mult = [random.randint(0, 4) for _ in halfcodes]
            star_mult = [random.randint(1, 4) for _ in support]
            codes = sum(([kind] * count for kind, count in zip(halfcodes, half_mult)), [])
            codes += sum(([f"S{centre}"] * count for centre, count in zip(support, star_mult)), [])
            model = solve(codes)
            asymmetric.append({
                "support": list(support), "trial": trial,
                "halfcode_multiplicities": half_mult,
                "star_multiplicities": star_mult,
                "satisfiable": model is not None,
            })
    asymmetric_feasible = [row for row in asymmetric if row["satisfiable"]]
    out = {
        "scope": "equal multiplicities only; exact D2C SAT; diagnostic, not arbitrary-multiplicity proof",
        "case_count": len(rows),
        "feasible_count": len(feasible),
        "feasible": feasible,
        "rows": rows,
        "seeded_asymmetric_case_count": len(asymmetric),
        "seeded_asymmetric_feasible_count": len(asymmetric_feasible),
        "seeded_asymmetric_rows": asymmetric,
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_NEGATIVE_ORBIT_PROBE_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print(f"complete: {len(rows)} equal and {len(asymmetric)} asymmetric cases; {len(feasible) + len(asymmetric_feasible)} feasible")


if __name__ == "__main__":
    main()
