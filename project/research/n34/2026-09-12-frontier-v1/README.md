# N34: partial upper bound and explicit remaining frontier

> Historical upper-layer checkpoint. The [current N34 bound package](../2026-09-12-m290-v1/README.md) closes the 290-edge branch and gives the candidate bound 289; equality classification remains OPEN. The result and state counts below record this earlier checkpoint.

12 September 2026. Research direction: Paul Lenz. Development, computation and
internal checking: ChatGPT/Geeps.

**Partial candidate result: e(G)<=290. The Murty-Simon target is 289.**
There is no complete N34 candidate proof or equality classification here.
Independent mathematical review, novelty assessment and external reproduction
remain OPEN.

## 1. Reduction to one maximum degree

Let G be a simple diameter-two edge-critical graph on 34 vertices, and target
`m=e(G)>=289`. The bipartite case is complete bipartite and obeys the conjecture.
The dense non-bipartite dominating-edge case is excluded by the Dailly–Foucaud–Hansberg
theorem; see the [source/dependency audit](../../../reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md).

Average degree forces `Delta>=17`.

- `Delta=17`: handshaking gives m<=289. The
  [balanced-degree theorem](../../general_n/2026-09-12-balanced-degree-v1/BALANCED_DEGREE_THEOREM.md)
  forces equality to be K(17,17).
- `Delta=19`: a=14, benchmark 19*15=285. At m>=289, t>=4, so the bridge
  requires Q>=19+8=27, contradicting the fourteen-label bound Q<=23.
- `Delta=20`: a=13, benchmark 20*14=280. At m>=289, t>=9, giving Q>=38
  against the thirteen-label bound Q<=21.
- `21<=Delta<=32`: a<=12. The source-independent twelve-label result forbids
  positive surplus over Delta*(34-Delta), which is at most 273 in this range.
- `Delta=33`: a universal-vertex D2C graph is a star.

Thus only `Delta=18` remains in the target range. Its bridge parameters are

`(a,b)=(15,18)`, `t=m-288`.

The fifteen-label theorem gives `18+2t<=Q<=26`, so t<=4 and m<=292.
The isolated-C lemma gives `d_i<=13` because `b>a-1-t` throughout this range.

The higher-degree inputs are indexed in the
[general step-back package](../../../../releases/general-stepback-v1/README.md)
and the [fixed-order reviewer index](../../../../releases/REVIEW_READY_INDEX.md).
This reduction does not use the general 7/12 profile-integral theorem.

## 2. Complete finite frontier

`enumerate_frontier.cpp` scans all 77,558,760 nondecreasing 15-tuples in
`{0,...,14}`. It accumulates Q through descending demand multiplicities.
At Q>=20 the counts are:

| Q | profiles |
|---:|---:|
| 20 | 588 |
| 21 | 379 |
| 22 | 193 |
| 23 | 88 |
| 24 | 43 |
| 25 | 11 |
| 26 | 2 |

Residual tails z_h must be nonincreasing. Taking the backward maximum of
their gamma lower bounds removes eight Q=20 profiles. The d_i<=13 bound
removes no further profiles in this frontier. The remaining union has
exactly 1,296 profiles, preserved in `FRONTIER.csv`.

For each profile, let rho_min be the sorted positive residual degrees
corresponding to these closed tail lower bounds. Every actual sorted rho is
coordinatewise at least rho_min. The budget `sum rho<=S-2t` therefore permits
only the enumerated unit increments above rho_min, capped at rho<=a.
`check_frontier.py` enumerates every such increment multiset and removes
duplicates; it also applies `r<=binomial(a,2)-t-ceil(a/2)`.

| m | t | demand profiles after tail closure | residual states | current disposition |
|---:|---:|---:|---:|---|
| 289 | 1 | 1,296 | 13,546 | OPEN: 12,926 positive-demand and 620 zero-demand states |
| 290 | 2 | 337 | 1,614 | OPEN: 1,585 positive-demand and 29 zero-demand states |
| 291 | 3 | 56 | 110 | 109 exact envelope exclusions + 1 hand contradiction |
| 292 | 4 | 2 | 2 | 2 exact envelope exclusions |

These are conservative necessary-condition states, not actual graphs.

## 3. Exact upper-layer certificates

The N32/N33 nine-rectangle potential is retained unchanged in graph-level
coordinates `(d,h)`:

`4[d>=2]+2[d>=2,h<=11]+[d>=2,h<=9]+[d>=2,h<=7]`

`+[d>=2,h<=4]+[d>=2,h<=3]+[d>=3,h<=8]+[d>=3,h<=6]+[d>=3,h<=5]`.

The discovery program uses `(a,b,dmax)=(15,18,13)` and the existing envelope
construction. SciPy proposes scalar coefficients, which are rounded,
one-sided-repaired and accepted only after every inequality and strict gap
passes integer arithmetic. Full coefficients are saved in
`upper_layer_certificates.json`; a numerical infeasibility return is never
used to exclude a graph.

`verify_upper_layers.py` does not import the numerical model builder. It
checks all label and source options directly, the balance/transport signs,
40,239 local integer inequalities, and complete state coverage. The worst
strict gap numerators are -9,897 for t=3 and -9,967 for t=4.
The [potential lemma](../../general_n/2026-09-09-rx-hall-v1/POTENTIAL_CERTIFICATE_LEMMA.md)
allows a free real balance coefficient, since its balance sum is exactly zero.

## 4. The one hand state at 291 edges

The unchanged potential does not supply an envelope for

`s=(5^9,6^6)`, `rho=(1^5,4,5^6,6^6)`.

Here S=81, r=75, and thirteen residual sources have degree at least two.
Thus `S=C_2(13)=81` is exact. Every demand is at least two. The
[tight total-demand threshold lemma](../../general_n/2026-09-12-joint-clipping-v1/TIGHT_THRESHOLD_LEMMA.md)
requires `b+2t<=2*3=6`, contradicting `18+6=24`.
Explicitly, at least 75 incoming exceptions are forced into the high sources,
while endpoint forcing permits at most 57.

This closes all 110 states at t=3. Together with the two t=4 certificates
and scalar exclusion of t>=5, it gives the partial candidate bound m<=290.

## 5. Replay

Solver-free certificate and state checks:

```sh
python project/research/n34/2026-09-12-frontier-v1/check_frontier.py
python project/research/n34/2026-09-12-frontier-v1/verify_upper_layers.py
```

To independently regenerate the complete demand frontier, compile
`enumerate_frontier.cpp` with C++17 and pass an output CSV path. The resulting
CSV must match the committed `FRONTIER.csv` byte for byte. The full domain,
counts and maximum-score assertions are checked by that program.

`certify_upper_layers.py` reproduces discovery and requires NumPy/SciPy;
neither dependency is needed by the acceptance verifier. Solver versions,
artifact hashes and exact replay commands are recorded in the release manifest.

## 6. Next obligations

Exclude the 290-edge branch to reach the conjectured upper bound. Then settle
the 289-edge Delta=18 equality branch to obtain the unique equality graph.
The 23-label scalar extension is separate structural progress and does not
automatically discharge either obligation. No N34 complete theorem is promoted.
