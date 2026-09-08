# Jensen-tail stability v11

8 September 2026. **Candidate mathematics; independent mathematical review and novelty assessment OPEN.**

This checkpoint adds a second stability centre to the demand-tail programme. The v9/v10 charging defect controls dispersion around alpha=1-1/sqrt(2). The new exact Jensen identity controls dispersion around the *actual mean demand* y. Combining that identity with the same demand-tail source-supplement capacity theorem gives a materially larger explicit quadratic loss.

## Candidate result

For a=n-1-Delta, t=m-Delta(n-Delta), and c=(3-2*sqrt(2))/2:

```text
a >= 50  ==>  t < (c-1/300) a^2.
```

Together with the original charging bound for 2<=a<=49 and a direct a=1 observation, this gives the conservative all-order candidate implication

```text
n >= 4 and Delta(G) >= 0.6116 n
    ==> e(G) < floor(n^2/4).
```

This improves the v10 0.6126 coefficient. The numerical change is not the main point: the new Jensen-defect identity is a reusable structural statement that explains why simultaneous demand-tail constraints are stronger than a single alpha-centred stability estimate.

Read [PROOF.md](PROOF.md). `check_v11.py` verifies the rational endpoint comparisons, exact degree-ratio inequalities, the 2<=a<=49 reduction, and a standard-library exact Sturm certificate proving positivity of the remaining degree-seven polynomial. The corrected checker passed in a clean Ubuntu 24.04 GitHub runner; see [REMOTE_EXACT_CHECK.json](evidence/REMOTE_EXACT_CHECK.json). The first runner attempt failed only because the checker compared two equal rational envelope values with `<` instead of using the already verified strict sqrt(2) bracket; the record preserves that correction. No theorem constant or proof inequality changed.

The exact check verifies algebra only. The graph-to-selected-system and demand-tail lemmas remain hand proofs. No finite-order certificate enumeration, Fan bound, weak-core reduction or positive-surplus residual-activity lemma is used. No best-known or priority claim is made pending specialist review.
