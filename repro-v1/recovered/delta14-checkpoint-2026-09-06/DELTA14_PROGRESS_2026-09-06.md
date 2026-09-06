# Delta=14 progress — 6 September 2026

## New computational result

The regenerated necessary-condition search has no surviving core/partition in
either of the following ranges:

| Branch | Residual range | Catalogue records | Records in target branch | Full-stage traces replayed |
|---|---:|---:|---:|---:|
| k=5 | 12–17 | 58,517 | 58,496 | 304 |
| k=6 | 3–12 | 3,506 | 3,426 | 345 |

The remaining 101 catalogue records have lower maximum F-degree and are
explicitly classified outside the target branch. The k=5 r=12–17 result
extends the earlier incomplete search; the k=6 result reproduces the earlier
internal exclusion with saved executable code and complete ledgers.

The separate coverage audit accounts for every catalogue index and every
admissible residual partition. It recomputes 233,187 arithmetic rejection
records. There are 57,569 screening SAT calls; 649 of those yield a weakened
screen survivor subsequently excluded by the full necessary-condition CNF.

All 649 standalone full-stage traces have passed the independent project C++
RUP checker: 10,420,049 added clauses checked, including the empty-clause
conclusions. The current compressed and decompressed trace hashes also pass.
One k=5 and thirteen k=6 initial proof files failed byte-hash checks. Those
copies were quarantined, regenerated without changing the recorded formulas,
and independently replayed. Their originals and the repair records are saved.

`CHECKPOINT_STATUS.json` gives the final recorded CNF-hash regeneration count.
The archive packager requires every recorded screening/full CNF hash to match
before producing a release archive.

## Important limits

This does **not** yet constitute a complete certificate-backed proof of k=5
or k=6. The 649 replayed traces cover only the full-stage survivors, not all
screening UNSAT exclusions. The earlier k=5 r=4–11 exclusions were not rerun
in this checkpoint. The mathematical necessity of the imported lemmas and
every encoded clause family still needs independent review. Catalogue
generation and canonical checks both use the nauty codebase.

The historical k=7 source package and its audit reports are included as
provenance; its historical certificate archives were not recovered here.
There is no new exclusion for k<=4 and no claim to have finished Delta=14 or
the n=25 case of Erdős Problem #742.

## Next work

1. Close the screening certificate gap, using proof-producing runs or fully
   audited hand reductions for groups of cases.
2. Reproduce k=5 r=4–11 with the same complete catalogue/partition discipline.
3. Audit the entire graph-to-CNF argument and the catalogue completeness
   assumptions with an independent implementation and mathematical reviewer.
4. Continue the lower-k cases with saved checkpoints and explicit proof status.

`README_DELTA14.md` gives setup, rerun, replay, and continuation commands.
