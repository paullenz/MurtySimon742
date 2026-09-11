# N30 m225 continuation: seven scalar Hall certificates

11 September 2026. Recovered baseline: `paullenz/MurtySimon742`, main at `b104846d222f09cb0d8bbf25ff9f51f6d1165bdf`.

**Candidate analytic reduction; exact arithmetic REPRODUCED. Independent mathematical review remains OPEN. No fixed-order theorem status or governed ledger entry is promoted.**

The new [scalar excess/Hall lemma](SCALAR_EXCESS_HALL_LEMMA.md) excludes **57 of the 207 positive ledger-tight rows** at `n=30,Delta=16,m=225` using seven fixed integer-weight formulas. Each formula reduces to small pointwise source minima, with only three possible supplement-degree endpoints. The [full appendix](EXACT_APPENDIX.md) displays all 57 contradictions.

| Stage | Rows | Dependency |
|---|---:|---|
| Saved exact Q>=18 demand frontier | 100 profiles | Exact completeness remains a finite input |
| Reconstructed demand/residual rows | 272 | At most three units of threshold/ledger slack |
| Positive ledger slack | 61 excluded | Earlier ledger-equality argument |
| Tight rows containing a zero demand | 4 excluded | Earlier exact Hall/Farkas certificates |
| Positive tight rows | 207 | Starting point for this continuation |
| New scalar exclusions | 57 | Seven explicit formulas; minimum assigned gap 1/12 |
| Positive rows still requiring stronger methods | 150 | Preserved residual-budget / joint-profile methods |

The 150 rows are **not survivors of the full existing N30 proof**. They survive this new, deliberately weaker scalar test. The older complete candidate remains available and still has finite certificate dependencies.

**Later successor:** the [four joint-envelope certificates](../2026-09-11-m225-resource-envelope-v1/README.md) now cover all 211 tight rows, including these 150 and the four zero-demand rows. This checkpoint and its remainder list are historical intermediate evidence. The complete 100-profile demand classification remains the principal next hand-reduction target for Delta=16; no fully hand-derived N30 proof is claimed.

## Files and replay

- [Lemma and seven-template table](SCALAR_EXCESS_HALL_LEMMA.md).
- [Integer certificates](SCALAR_CERTIFICATES.json) and [all 57 explicit rows](EXACT_APPENDIX.md).
- [Standalone exact checker](verify_scalar_certificates.py) and [audit output](EXACT_AUDIT.json).
- [Remaining 150 positive rows](REMAINING_150_POSITIVE_ROWS.json).
- [Recovery, validation and next-step record](HANDOVER.md).
- [Source-degree erratum](../../../reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md).

From the repository root:

```sh
python -I -B project/research/n30/2026-09-11-m225-hall-continuation-v1/verify_scalar_certificates.py
```

This uses only Python's standard library. It independently reconstructs the tail-slack rows, checks all seven templates on all 211 tight rows, and verifies pointwise source minima by both full integer-domain evaluation and the three-endpoint formula. The saved run checks 200,043 source cases and 143 label-algebra cases. It imports neither the discovery programs nor historical row generators.

The optional discovery programs `mine_scalar_excess.py` and `compress_scalar_excess.py` use SciPy 1.17.0. Their float optimization results and failed denominator attempts are retained in `SCALAR_EXCESS_DISCOVERY.json`, `SCALAR_EXCESS_COVER.json` and `SMALL_SCALAR_TEMPLATES.json`. They are not acceptance dependencies or proofs of optimality. The certificate file can be checked without reproducing discovery.

The proof-critical classification of the 100 demand profiles is **not** established by this checker. No full N30 hand proof, unrestricted theorem, minimal-template theorem or new external review is claimed.
