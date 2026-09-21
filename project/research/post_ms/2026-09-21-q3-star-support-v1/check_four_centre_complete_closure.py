#!/usr/bin/env python3
"""Arithmetic and hostile-control audit for the four-centre density closure."""
import json
from math import floor
from pathlib import Path


def main():
    minimum_slack = None
    minimizer = None
    minimum_slack_w_ge_2 = None
    minimizer_w_ge_2 = None
    for t in range(5, 81):
        for r in range(1, 81):
            for q in range(0, 81):
                for s in range(4, 41):
                    w = r + q
                    u = t + w
                    D = floor((u + s) ** 2 / 4) - floor(u**2 / 4) - s - 3
                    excess_cap = max(0, floor(s * (w - 2) / 2))
                    slack = D - excess_cap
                    assert slack >= 0, (t, r, q, s, D, excess_cap)
                    if minimum_slack is None or slack < minimum_slack:
                        minimum_slack = slack
                        minimizer = [t, r, q, s]
                    if w >= 2 and (
                        minimum_slack_w_ge_2 is None or slack < minimum_slack_w_ge_2
                    ):
                        minimum_slack_w_ge_2 = slack
                        minimizer_w_ge_2 = [t, r, q, s]

    fixture_path = Path(__file__).with_name("RTS_BOWTIE_REALIZABILITY_RESULTS.json")
    controls = json.loads(fixture_path.read_text())
    checked = []
    for key in ("fourth_present_control", "fourth_missing_control"):
        row = controls[key]
        codes = row["codes"]
        edges = {tuple(sorted(e)) for e in row["A_edges"]}
        R = [i for i, c in enumerate(codes) if c == "P0"]
        T = [i for i, c in enumerate(codes) if c == "P1"]
        S = [i for i, c in enumerate(codes) if c.startswith("S")]

        def adjacent(a, b):
            return tuple(sorted((a, b))) in edges

        cross = sum(adjacent(r, t) for r in R for t in T)
        I = sum(
            adjacent(a, b)
            for side in (R, T)
            for i, a in enumerate(side)
            for b in side[i + 1 :]
        )
        M = len(R) * len(T) - cross
        U = M - I
        A = sum(adjacent(r, x) for r in R for x in S)
        TS = sum(adjacent(t, x) for t in T for x in S)
        SS = sum(
            adjacent(a, b)
            for i, a in enumerate(S)
            for b in S[i + 1 :]
        )
        B = cross + I + A + TS + SS
        epsilon = max(0, B - len(R) * len(T) - len(S))
        cap = max(0, floor(len(S) * (len(R) + len(T) - 2) / 2))
        assert epsilon <= U and epsilon <= cap
        checked.append({
            "fixture": key,
            "U": U,
            "B": B,
            "epsilon": epsilon,
            "symmetric_cap": cap,
        })

    out = {
        "parameter_scan": {
            "t": [5, 80],
            "r": [1, 80],
            "q": [0, 80],
            "s": [4, 40],
            "minimum_D_minus_symmetric_cap": minimum_slack,
            "first_minimizer_t_r_q_s": minimizer,
            "minimum_D_minus_symmetric_cap_for_w_at_least_2": minimum_slack_w_ge_2,
            "first_w_at_least_2_minimizer_t_r_q_s": minimizer_w_ge_2,
        },
        "actual_D2C_controls": checked,
        "status": "PASS",
    }
    path = Path(__file__).with_name("FOUR_CENTRE_COMPLETE_CLOSURE_CHECK.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
