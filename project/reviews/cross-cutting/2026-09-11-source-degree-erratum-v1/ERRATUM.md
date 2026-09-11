# Erratum: source-degree identity in the frozen N29 bridge

11 September 2026. Found during the continuation/recovery audit of the N30 selected-excess work by ChatGPT/Geeps. **Non-blocking proof-text correction; independent mathematical review remains open.**

## Exact affected source

At repository baseline `b104846d222f09cb0d8bbf25ff9f51f6d1165bdf`, Section 5 of

```text
project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md
```

contains the display

```text
d_H(u)=rho_u+(b-1)-(q_u+p_u)>=a.
```

The source-file SHA-256 is

```text
4a2333802f011a51eca60041aeb412dc157bf8adf99807cb59581b4274152f42.
```

That expression omits the `q_u` selected cross-edges at source `u`. The bridge is also used as the frozen appendix to the current N29 reviewer-v4 manuscript. Historical source and PDF bytes are retained; reviewers should apply this erratum when reading them.

## Correct identity and proof

The source has `rho_u+q_u` neighbours in A, and `b-1-(q_u+p_u)` neighbours in B. It is nonadjacent to the root in H. Hence

```text
d_H(u)=(rho_u+q_u)+(b-1-q_u-p_u)
      =rho_u+b-1-p_u >= a.
```

Therefore

```text
p_u<=rho_u+b-a-1.
```

This is exactly the bound already stated as (5.2): `p_u<=rho_u+3` at N29 with `(a,b)=(12,16)`, and `p_u<=rho_u+2` at N30 with `(a,b)=(13,16)`.

The stronger constraint `q_u+p_u<=rho_u+b-a-1` does **not** follow from minimum degree and must not be introduced. The missing-degree identity `q_u+p_u=d_missing-B(u)` remains correct; it is the total-degree display that omitted the cross-edge contribution.

## Impact checked in this audit

- The stated supplement bound is correct, with the corrected derivation above.
- The inspected N29 corrected model `independent_threshold_model_v2.py` uses `p<=min(rho+3,15-q)`, the correct local domain.
- The inspected N30 `n30_threshold_model.py` uses `p<=min(rho+B-A-1,B-1-q)`, again the correct domain.
- The N30 hand endpoint, zero-demand exact checker and new scalar continuation use `p<=rho+2`.
- The N29 reviewer-v4 hand threshold-tail route does not depend on the old grouped LP. This correction does not change its stated tail inequality or numerical conclusion.

Thus the displayed typo does not invalidate the bound or the inspected computational models. This is a scoped dependency check, not a new exhaustive audit of every historical script. No fixed-order candidate status, theorem-ledger entry or external-review status is changed.

The [new scalar lemma](../../../research/n30/2026-09-11-m225-hall-continuation-v1/SCALAR_EXCESS_HALL_LEMMA.md) includes the corrected degree calculation explicitly.
