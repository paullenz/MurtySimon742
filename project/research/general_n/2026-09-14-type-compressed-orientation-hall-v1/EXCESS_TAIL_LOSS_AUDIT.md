# Selected-excess tail-loss audit

14 September 2026. Local exact audit only; external review OPEN.

## Reproduction

Run `python3 verify_excess_tail_loss.py` from this directory. Output must equal `EXCESS_TAIL_LOSS_VERIFICATION.json` as parsed JSON values. Only the Python standard library is used.

## What was checked

- 179,375 pointwise identities: k=0..6, q=0..24, E=0..40, z=0..24. This deliberately includes z>E, E=0, q=0, absent-cap and zero-floor cases.
- 6,381 complete small cap profiles from (a,b)=(2,3),(2,4),(3,4),(3,5), all multisets of allowed (q,rho), every E=0..Q and z=0..a. All 171,504 source subsets were tested; 7,135 were deficient.
- 10,000 deterministic random profiles, seed 74220260914, a=2..12 and b-a=1..5. The nonnegative-cap branches numbered 9,301, with 93,010 source-set checks. Negative caps were not silently clipped to zero.
- Exact equality of direct cap and tail-loss/potential-loss decomposition; exact global slack equality; exact direct Hall margin versus source-cut vacancy budget.
- Archived a=4,b=7 non-tail counterexample retained: singleton margin -1, nonempty high-q-tail margins 2,3,3; empty-tail margin 0. Its Q-r-E=-7 explicitly violates the nonnegative two-defect bridge ledger.

No cases are described as graph-realizable. The random and small-profile universes test algebra on a larger domain than the graph bridge. They are not a run over the frozen 812-profile artifact or the 3,607-state frontier.

## Harness correction retained

The first local run reached its final archived-example assertion and failed because the newly typed expected tail margins were [1,0,0,0]. Direct recomputation and hand counting give [2,3,3,0]: total target capacity is 21, full demand is 19, and the six high-q sources have demand 18. The expected values were corrected; no formula or existing repository evidence was changed. The complete audit was then rerun successfully. This was a local regression-fixture mistake, not a counterexample to the new loss identity.

## Trust boundary

The new necessary budget is an exact reformulation of the existing sum-P screen, not an additional exclusion beyond it. The all-source-cut identity is an exact reformulation of labelled Hall margins. Their value is structural access to bridge defects, selected-excess tail counts, pair loss and cut vacancy in one formula. Neither q-tail sufficiency nor an all-order contradiction is inferred. Independent external review and the separate relational promotion gate remain open.
