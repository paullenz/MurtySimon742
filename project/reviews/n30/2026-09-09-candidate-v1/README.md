# n=30 Murty–Simon candidate package

9 September 2026.

**Status: COMPLETE CANDIDATE. Independent mathematical review, independent computational reproduction and novelty assessment remain OPEN.**

Candidate statement:

```text
Every 30-vertex simple diameter-two edge-critical graph G satisfies
  e(G) <= 225,
with equality exactly K(15,15).
```

## Start here

- [`PROOF.md`](PROOF.md) — assembled candidate proof.
- [`ASSEMBLY_AUDIT.md`](ASSEMBLY_AUDIT.md) — fresh hostile end-to-end audit.
- [`check_outer.py`](check_outer.py) — standard-library exact checker for Fan arithmetic, degree-sum entry points, and the empty charging domains for `Delta=18,...,28`.

## Proof structure

Fan's strict bound leaves only 226 edges as an upper-bound counterexample.

At 225 edges:

- `Delta=15` is a hand equality case and forces `K(15,15)`;
- `Delta=16` is excluded by the parameterized trusted kernel;
- `Delta=17` is excluded by the early charging/threshold/Hall kernel;
- `Delta=18,...,28` have empty exact charging domains;
- `Delta=29` forces a star.

At 226 edges the same exclusions apply beginning at `Delta=16`.

## Delta=16 evidence

Parameterization / source:

- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/N30_PARAMETERIZATION_AUDIT.md`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/N30_PARAMETERIZATION_AUDIT.md)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/ISOLATED_C_PARAMETERIC_LEMMA.md`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/ISOLATED_C_PARAMETERIC_LEMMA.md)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_prepare.py`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_prepare.py)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_rows.cpp`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_rows.cpp)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_row_threshold.py`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_row_threshold.py)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_threshold_model.py`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_threshold_model.py)

Clean GitHub Actions:

```text
34286806474  strengthened prepare + complete residual-row scan
34287440190  exact row-level threshold-capacity screen
34287739057  final exact Farkas replay
```

Final exact frontier:

```text
m=226: 9 rows -> 9 exact contradictions -> 0 survivors
m=225: 272 rows -> 272 exact contradictions -> 0 survivors
```

## Delta=17 evidence

- [`project/research/n30/2026-09-09-delta17-v1/README.md`](../../../research/n30/2026-09-09-delta17-v1/README.md)
- [`project/research/n30/2026-09-09-delta17-v1/D17_EXACT_DUAL_CERTIFICATES.json`](../../../research/n30/2026-09-09-delta17-v1/D17_EXACT_DUAL_CERTIFICATES.json)
- [`project/research/n30/2026-09-09-delta17-v1/verify_committed.py`](../../../research/n30/2026-09-09-delta17-v1/verify_committed.py)
- [`project/research/n30/2026-09-09-delta17-v1/CI_PROVENANCE_NOTE.md`](../../../research/n30/2026-09-09-delta17-v1/CI_PROVENANCE_NOTE.md)

Clean replay:

```text
34292054922
```

Exact result:

```text
m=226: 250 charging-feasible profiles, all 250 threshold-rejected.
m=225: 1,155 profiles; 1,137 early rejects + 18 exact Hall-dual rejects.
final survivors: 0.
```

The earlier failed Delta=17 CI runs are intentionally retained in Actions history. They exposed replay-provenance and stale-metadata problems; the final committed certificates were regenerated and then passed the exact standard-library verifier.

## Universal bridge

The graph-to-demand lemmas used here were isolated and hostile-audited in the n=29 standalone package:

- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md`](../../n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md)
- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md`](../../n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md)
- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md`](../../n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md)

An external reviewer should attack these hand lemmas before spending time rerunning arithmetic.

## Review priorities

1. quasi-edge construction and injection;
2. residual activity;
3. source-demand and charging;
4. threshold-capacity lemma;
5. parameteric isolated-C lemma;
6. n=30 Delta=16 grouped-model normalization;
7. exact certificate semantics;
8. exact hypotheses of the cited published reductions.

Please report any suspected flaw through a GitHub Issue. A smallest counterexample or the first invalid implication is especially useful.