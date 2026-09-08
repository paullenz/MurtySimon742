# Demand-tail stability v10

8 September 2026. **Candidate mathematics; independent mathematical review and novelty assessment OPEN.**

This checkpoint sharpens the v9 threshold-capacity continuation using the same general demand-tail theorem but a tighter one-threshold stability argument. It does not depend on the n=25/n=27/n=28 finite computations.

## Candidate result

For a=n-1-Delta and t=m-Delta(n-Delta), the new hand argument gives

```text
a >= 25  ==>  t < ((3-2*sqrt(2))/2 - 1/750) a^2.
```

Combining this with the original charging bound for 1<=a<=24 gives the conservative all-order implication

```text
n >= 4 and Delta(G) >= 0.6126 n
    ==> e(G) < floor(n^2/4).
```

The previous continuation gave 0.6129. The improvement is small numerically but the proof is shorter and has explicit rational margins. No best-known or priority claim is made pending specialist literature review.

Read [PROOF.md](PROOF.md). Run `python3 -I -B check_v10.py` to verify every displayed rational comparison and the small-a inequalities. That script checks arithmetic only; it does not prove the graph-to-selected-system lemmas.

[EXPLORATORY_MULTI_THRESHOLD.md](EXPLORATORY_MULTI_THRESHOLD.md) records a deliberately non-rigorous discretised relaxation suggesting that simultaneous thresholds may permit a materially larger quadratic loss. It is a research lead, not evidence for a stronger theorem.

Frozen finite-order papers, original archives and the governed theorem ledger are unchanged.
