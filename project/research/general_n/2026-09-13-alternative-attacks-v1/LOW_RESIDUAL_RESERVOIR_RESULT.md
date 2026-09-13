# Low-residual reservoir scan — current frontier result

13 September 2026. **Preserved negative/triage result. External mathematical review remains OPEN.**

[`LOW_RESIDUAL_RESERVOIR_BOUND.md`](LOW_RESIDUAL_RESERVOIR_BOUND.md) turns the low-c/high-q cross obstruction into a closed-form upper bound on `Q` whenever the scalar demand/residual data force a nonempty low-c reservoir.

The canonical ledger-current scan was run by [`scan_low_residual_reservoir.py`](scan_low_residual_reservoir.py) in GitHub Actions run `34789939044`, which completed successfully.

Input:

```text
3,623 current frozen scalar survivors
```

Result:

```text
bound applicable:     3,421
bound not applicable:   202
whole states excluded:    0
```

Thus the closed-form reservoir inequality is **not**, by itself, a further whole-state closure mechanism on the post-pair frontier.

The closest scalar survivors have only a two-unit margin:

```text
state 11228: S=73, Q_upper=75
state 11229: S=73, Q_upper=75
```

Several further states have margin `+3` or `+4`.

This negative result is informative. The 943-state potential-pair family cannot be explained merely by the coarse count of low-c versus high-q vertices; the exact two-dimensional potential-degree structure `d_KD(u)` and its interaction with individual incoming capacities contain materially more information.

The theorem remains useful as a symbolic all-order consequence and a cheap pre-screen, but the current finite residual frontier requires stronger relational information.

No timeout, solver failure or numerical infeasibility is treated as proof.
