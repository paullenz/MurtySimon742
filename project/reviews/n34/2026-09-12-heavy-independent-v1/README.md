# N34 normalization audit and hand simplification

12 September 2026. Internally audited candidate mathematics. External review OPEN.

The [new hand proof](HAND_PROOF.md) replaces the last 12,570-column Farkas
certificate with the parameterized bound `6k<=r+6z` when all high-residual
sources have p<=4. In the exceptional N34 state this would say `78<=74`.
The current [reviewer-v2 package](../../../../releases/n34-reviewer-v2/README.md)
therefore retains 6,837 exact envelope exclusions and has 6,709 hand/accounting
exclusions; the candidate conclusion remains `e(G)<=289`, equality `K(17,17)`.

## Independent model construction

`count_model.py` reconstructs the graph image using whole object counts and
semantic tuple keys. It does not import the historical model. Source states
are enumerated from Cartesian products and filtered by canonical inequalities;
label states, oriented selected pairs, and selected incidences are constructed
separately. Every row counts actual objects.

| Historical variable | New whole-count variable | Scale multiplying the old variable |
|---|---|---|
| W(k,q,p,H) | Source count | n_k |
| L(g,R,x) | Label count | m_g |
| P(k,l,q,q') | Oriented selected-pair count | n_k(n_l-[k=l]) |
| Z(k,g,q,p,H,R,x) | Selected-incidence count | n_k m_g |

The group sizes are n_1=10,n_2=8 and m_1=2,m_2=13. The source and label
normalizations become counts n_k,m_g, and the total residual equation becomes
`sum R*label_count=26`. Pair outflow is q times the appropriate source count;
pair inflow is p times the supplement count. Incidence balances count q, H,
and x from their respective endpoints. For a source state and label group,
its incidence count is at most m_g times its source count. Variable upper
bounds become the corresponding whole-count scales. The heavy-routing row
uses `H[H>2]-p[rho>=2]` with no group factor because source counts already
include group size.

`compare_models.py` substitutes each old variable by count/scale and compares
the **complete exact row multisets**, including duplicate multiplicities,
normalization right sides and all upper bounds. It uses rational arithmetic,
positive rescaling of inequalities, and arbitrary nonzero rescaling of
equalities. Every one of 12,570 variables, 12,985 inequalities and 690
equalities matches. It then translates the saved Farkas multipliers, whose
exact whole-count right side is -103,847,120.

`verify_count_certificate.py` verifies that translated certificate using only
the new count model. It imports no original model and no numerical package.
This specifically addresses the shared-normalization trust gap identified
after reviewer v1. It is a separate internal implementation, **not external
independent review**. Matching two models alone would not prove their graph
image; the whole-count explanation above and the canonical incidence argument
remain the mathematical obligations.

## Preserved discovery and current replay

`compact_heavy.py` records the intermediate class-specific potential searches.
The two exact coefficient records reduce 23 nonzero coefficients to 14.
`search_small_potential.py` records the subsequent 3,200 small-integer trials,
including every successful tuple and the chosen four-step proof. Failed
numerical proposals and the earlier feasible relaxation remain preserved in
the historical equality package.

From the repository root:

```sh
python project/reviews/n34/2026-09-12-heavy-independent-v1/compare_models.py
python project/reviews/n34/2026-09-12-heavy-independent-v1/verify_count_certificate.py
python project/reviews/n34/2026-09-12-heavy-independent-v1/verify_hand.py
python project/reviews/n34/2026-09-12-heavy-independent-v1/verify_v2.py
```

All four checks use Python's standard library. The v2 replay keeps disjoint
coverage of the original 13,546 states, checks the unchanged 3,018,781 local
envelope inequalities, and applies the hand theorem to the unique remaining
state. It neither constructs the heavy model nor reads a Farkas certificate.
The old formula-check module's incidental model import is inert in this replay.
The original normalized certificate and its new whole-count translation are
corroborating evidence rather than proof-critical dependencies of v2.

## Focused hostile internal audit

- The hand theorem uses actual selected heavy degree H, not total q, in
  the routing implication. Only q>=H is used to compare loads.
- Incoming routing is summed over all Z, including sources with H=0; their
  negative correction is included. No incoming capacity is lost.
- The p<=4 condition is checked from p<=rho+b-a-1 in the N34 state. It is
  not silently transferred to N35, where rho=2 would only imply p<=5.
- The label proof works for every R>=0 and x>=2. It neither asserts R=0
  on light labels nor needs the exact positive-demand identity.
- The source cases cover arbitrary H, not merely the finite N34 range.
- The final contradiction is strict, 78>74. The other 6,837 envelopes remain
  required; this is not a hand proof of the full N34 candidate.
- Original certificate files, historical replay outputs and frozen proof
  statements have not been rewritten. New replay outputs carry new provenance.

No blocking flaw was found in this focused internal audit. Specialist review,
novelty checking and external computational reproduction remain OPEN.
