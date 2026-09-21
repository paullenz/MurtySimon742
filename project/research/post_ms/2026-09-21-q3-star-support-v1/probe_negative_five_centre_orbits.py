#!/usr/bin/env python3
"""Bounded equal-multiplicity probe for the two one-copy-negative supports."""
import json
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
    out = {
        "scope": "equal multiplicities only; exact D2C SAT; diagnostic, not arbitrary-multiplicity proof",
        "case_count": len(rows),
        "feasible_count": len(feasible),
        "feasible": feasible,
        "rows": rows,
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_NEGATIVE_ORBIT_PROBE_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print(f"complete: {len(rows)} exact cases; {len(feasible)} feasible")


if __name__ == "__main__":
    main()
