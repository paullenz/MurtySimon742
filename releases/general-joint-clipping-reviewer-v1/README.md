# Joint clipping and N34 follow-through: reviewer package v1

12 September 2026. **Source-first candidate mathematics. Independent review,
novelty assessment and independent reproduction remain OPEN.**

## Claims and limits

1. An exact parameterized recursion minimizes clipping loss over compatible
   lower tails. Its finite applications prove sharp scalar Q bounds
   `32,35,39,42,46,49,54` for `a=17,18,19,20,21,22,23`, respectively.
2. Clipping down to five is valid through a=22; at a=23 the terminal cap must
   be raised to six for this route. The original counterexample is preserved.
3. A hand tight-total-demand-threshold lemma gives `b+2t<=h(h+1)` whenever
   every demand is at least h and total threshold capacity is exact.
4. At n=34 the complete 291- and 292-edge layers are excluded, yielding
   **the partial candidate bound e(G)<=290**. The 289- and 290-edge layers
   remain OPEN at Delta=18. This is not a complete N34 Murty-Simon proof.

## Read in this order

- [Focused foundations audit and external review checklist](../../project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md)
- [Compatible-tail recurrence and scalar bounds](../../project/research/general_n/2026-09-12-joint-clipping-v1/JOINT_CLIPPING.md)
- [Tight threshold hand lemma](../../project/research/general_n/2026-09-12-joint-clipping-v1/TIGHT_THRESHOLD_LEMMA.md)
- [N34 partial proof and remaining frontier](../../project/research/n34/2026-09-12-frontier-v1/README.md)
- [Earlier balanced-degree and fixed-a results](../general-stepback-v1/README.md)

## Exact verification

From repository root:

```sh
python project/research/general_n/2026-09-12-joint-clipping-v1/verify_joint_clipping.py
python project/research/n34/2026-09-12-frontier-v1/check_frontier.py
python project/research/n34/2026-09-12-frontier-v1/verify_upper_layers.py
```

All three acceptance checks use only the Python standard library. The full
N34 demand enumeration additionally requires a C++17 compiler. SciPy is
needed only to reproduce numerical discovery of envelope coefficients.

The exact scope is recorded in [the artifact manifest](MANIFEST.json).
Separate implementations and this internal audit do not constitute external
independent mathematical validation. No proof beyond the stated fixed-a
ranges or complete fixed-order result above n=33 is claimed.
