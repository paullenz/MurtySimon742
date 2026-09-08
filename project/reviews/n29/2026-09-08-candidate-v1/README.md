# n=29 Murty–Simon candidate — 8 September 2026

**Candidate theorem:** every 29-vertex diameter-two edge-critical graph has at most **210** edges, with equality exactly for **K(14,15)**.

**Status:** complete candidate hand proof with the new Delta=16 finite arithmetic reproduced on a clean GitHub runner. Independent mathematical review, independent computational reproduction, novelty assessment and full formal verification remain **OPEN**. This checkpoint is not a theorem-ledger promotion.

Read [PROOF.md](PROOF.md) first. The proof is self-contained at the fixed-order level and deliberately does **not** use the later general `293/500` candidate theorem.

## Degree partition

- `Delta<=14`: degree sum gives at most 203 edges.
- `Delta=15`: a witness-deficit count excludes 211 edges; at 210 it forces the graph to be `K(14,15)`.
- `Delta=16`: fresh direct finite calculation excludes both 211 and 210 edges.
- `Delta=17`: the pointwise charging score is at most `176/7`, below the required 29 or 31.
- `18<=Delta<=27`: residual h-index inequality excludes every case.
- `Delta=28`: a universal vertex forces a star.

Fan's strict bound as reported by Wang reduces the upper-bound problem to excluding 211 edges. The non-bipartite dominating-edge theorem of Dailly–Foucaud–Hansberg removes that separate structural case.

## Delta=16 exact replay

The Delta=16 route has `(a,b)=(12,16)` and treats `t=3` (211 edges) and `t=2` (210 edges). It adapts the hash-pinned n=28 direct197 implementation, but generates fresh n=29 domains.

The successful clean-runner aggregate is [evidence/N29_D16_REPLAY.json](evidence/N29_D16_REPLAY.json):

| Scope | Demand tuples | Residual rows | Projected survivors | Joint survivors | Exact final split | Final |
|---|---:|---:|---:|---:|---:|---:|
| m=211 | 4,867 | 1,848,957 | 118 | 36 | 13 shared + 23 typed | 0 |
| m=210 | 9,251 | 5,765,218 | 1,225 | 593 | 213 shared + 378 typed + 2 endpoint | 0 |

Two independent C++ row scanners agree. Joint states are independently reconstructed. A floating-point solver proposes only candidate Farkas multipliers; every counted LP exclusion is checked as an exact integer contradiction against a separately rebuilt named constraint system.

## Reproduce the non-Delta16 arithmetic

Standard library only:

```sh
python3 -I -B check_all_degrees.py > /tmp/n29-all-degrees.json
cmp /tmp/n29-all-degrees.json ALL_DEGREES_CHECK.json
```

This checks the Fan substitution, both Delta=15 witness tables, the exact Delta=17 factorisation, every Delta=18..27 h-index arithmetic case, the degree-sum bound, and an explicit graph check that `K(14,15)` is diameter-two edge-critical.

The full Delta=16 rerun is `.github/workflows/n29-d16.yml`; it uses the source in `project/research/n29/2026-09-08-delta16-direct-v1/` and the archived n=28 implementation antecedent. SciPy is used only for discovery/proposal; exact certificate verification is the proof-producing step.

## Audit trail

[FAILURE_HISTORY.json](FAILURE_HISTORY.json) records three failed hosted Delta=16 attempts before the successful run. They were environment/setup failures (missing SciPy, isolated Python hiding a user-site install, missing Boost headers); none is reported as a mathematical pass or counterexample.

[AUDIT.md](AUDIT.md) records the same-assistant adversarial review and remaining trust boundaries. [PROVENANCE.json](PROVENANCE.json) identifies source commits and preserved ancestors. [MANIFEST.json](MANIFEST.json) hashes the point-in-time review payload.

Frozen n=25/n=27/n=28 proofs, their archives, and the governed theorem ledger are unchanged.
