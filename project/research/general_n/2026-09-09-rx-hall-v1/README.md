# General-N RX-Hall / Hall-core programme

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite evidence plus candidate structural reduction. Not an unrestricted theorem. Independent mathematical review remains OPEN.**

## 1. Current position

Mining the exact n=29 and n=30 Delta=16 certificates exposed a much smaller endpoint mechanism than the original cumulative-threshold LP.

In the positive-demand zero-slack sector,

```text
S=sum_i s_i=r+2t.
```

The stripped RX-Hall system keeps source/supplement compatibility and endpoint Hall structure while deleting the old cumulative-tail variables and unordered-pair aggregate capacity.

The n=29 hard frontiers are now **exact**, not merely numerical:

```text
(a,b,t,dmax)=(12,16,3,10): 94/94 exact integer Farkas rejections;
(a,b,t,dmax)=(12,16,2,10): 902/902 exact integer Farkas rejections.
```

All 996 certificates were checked by a separate standard-library verifier which imports neither SciPy nor the certificate generator. The preserved aggregate is `RX_HALL_N29_EXACT_REPLAY.json` (clean run `34326568879`). Numerical LP is proposal-only; exact integer arithmetic is the acceptance layer.

The early red sharded numerical run is therefore **not** evidence of a graph survivor. It was superseded by regenerated-input hardened replays and exact proof-producing checks. Historical failures remain preserved rather than rewritten.

## 2. RX inequalities

For a selected incidence from B-source `u` to A-label `i`, write

- `rho_u` for source residual degree;
- `q_u` for selected outdegree;
- `p_u` for supplement indegree;
- `s_i>0` for label demand;
- `R_i` for residual column degree;
- `x_i` for selected label degree.

The existing bridge gives

```text
s_i <= rho_u,                                      (RX1)
R_i+s_i <= rho_u+q_u-1,                           (RX2)
R_i+x_i >= q_u+p_u.                               (RX3)
```

The full stripped RX-Hall model uses source/supplement transportation, label distributions, residual budget and selected incidence, but no cumulative tails and no unordered-pair aggregate capacity.

## 3. Exact n=29 RX-Hall replay

The preserved exact aggregate records:

```text
t=3: 94 hard rows, 94 exact Farkas contradictions, 0 unresolved;
t=2: 902 hard rows, 902 exact Farkas contradictions, 0 unresolved;
total: 996 exact contradictions, 996 independently rechecked.
```

The exact model has explicit unit-density bounds because its W/P/L/Z variables are normalized fractions. Floating point only proposes multipliers; every accepted contradiction is verified against integer coefficient dictionaries.

This result remains conditional on the universal graph-to-demand/RX-Hall bridge and on the earlier exact frontier preparation.

## 4. Further collapse: the t=3 Hall core

The n=29 `t=3` frontier has now been reduced to an even weaker exact model which deletes

- all P transport variables;
- all R residual variables and the residual budget;
- all Z incidence variables;
- RX2;
- grouped source-label caps;
- cumulative tails;
- unordered-pair aggregate capacity.

It retains only

```text
RX1 pointwise source-degree capacity
+ source/supplement threshold transport
+ RX3 extra-load consequence
+ total selected-incidence balance
+ Hall inequalities for unions of at most two compatibility rectangles.
```

All **94/94** hard t=3 rows still receive exact integer Farkas contradictions. Clean workflow `General RX-Hall t3 Hall core`, run `34329608225`, independently verifies all 94 certificates with a standard-library-only checker. The Hall-domain family has only 6 to 40 candidate domains per row.

The graph-level version of this reduction is recorded in [`HALL_CORE_SYMBOLIC_LEMMAS.md`](HALL_CORE_SYMBOLIC_LEMMAS.md).

## 5. Symbolic Hall-core formulation

Put

```text
y_i=x_i-s_i,
h_u=max(0,q_u+p_u-dmax).
```

RX1 and RX3 imply that every selected incidence `u -> i` obeys

```text
s_i <= rho_u,
y_i >= h_u.
```

Thus each source has a rectangular compatibility neighborhood

```text
N(u)={(s,y):s<=rho_u, y>=h_u}.
```

Direct counting then yields pointwise source caps, nested source/supplement transport inequalities, and ordinary Hall-capacity inequalities for threshold rectangles and their unions. These are graph-level necessary conditions, not LP artefacts.

The next target is to combine those inequalities with charging/demand bounds and eliminate the `y` profile symbolically.

## 6. Cross-order falsification

The strongest immediate test of the proposed simplification is **not** another fixed-order proof. It is whether the same two-rectangle Hall core survives unchanged on the n=30 Delta=16 hard frontiers and then on n=31.

A clean n=30 falsification workflow has been added at `.github/workflows/general-rx-hall-n30-hall-core.yml`. It regenerates the n=30 frontiers from committed source, preserves any unresolved Hall-core rows as artifacts, and tests

```text
n=30, m=226: (a,b,t,dmax)=(13,16,2,11), expected 8 hard rows;
n=30, m=225: (a,b,t,dmax)=(13,16,1,11), expected 207 hard rows.
```

A survivor here would narrow or falsify the two-rectangle sufficiency conjecture without affecting the already assembled n=30 candidate proof.

## 7. Highest-priority next steps

1. finish the n=30 Hall-core falsification and inspect any preserved survivors;
2. if the same tiny core survives, independently exact-check the n=30 Hall-core certificates;
3. mine exact Hall weights to seek a one- or two-threshold symbolic inequality;
4. test whether every relevant Hall staircase can be compressed to at most two rectangles;
5. apply the proposed inequality parametrically across the unresolved `Delta/n < 293/500` band;
6. use n=31 primarily as a falsification laboratory rather than as a brute-force trophy;
7. continue external review of the universal graph-to-demand bridge, which remains the principal mathematical trust boundary.

No complete order above 30, unrestricted solution, novelty determination, full formal verification or external endorsement is claimed here.
