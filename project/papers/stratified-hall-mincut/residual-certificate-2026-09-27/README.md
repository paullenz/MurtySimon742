# Residual path and all-or-none block Hall certificates

27 September 2026. User-requested in-chat continuation from
`b61a0b59d3960b6a48c2c0e869667a843ef6b18c`. CURRENT_STATE.md was read first;
main had not advanced. All results are internal. No external review, formal
verification, novelty clearance or general Murty–Simon proof is claimed.

## What is proved and implemented

[PROOF.md](PROOF.md) reconstructs the old rule, then proves a strict extension:
a neutrally deleted source may force a different strict incoming row along
a checked residual path. It proves persistence, commutation and a unique
terminal even on failed instances. Tight termination certifies the greatest
tight exact minimum and equality of the two minimum margins.

The next extension deletes full source projections of residual strongly
connected components. A block capped-loss argument proves the same results,
and a three-vertex fractional example proves that this adds capability beyond
singleton path deletions. Both rules are implemented in the standalone exact
rational verifier [verify_residual.py](verify_residual.py). The frozen supplied
example is accepted by [FROZEN_CERTIFICATE.json](FROZEN_CERTIFICATE.json), with
result [FROZEN_RESULT.json](FROZEN_RESULT.json).

Complete minimum cuts are distinguished from left/source projections. Paths
and SCCs use the unchanged FULL residual network; a source block is not the
full network SCC. Intermediate right vertices are not removed from that graph.

## What was tested, and what failed

[RESULTS.md](RESULTS.md) gives the exact counts. The two exhaustive regimes each
have all 46,656 labelled n=3 instances in their quota domain, all source
subsets and all complete cuts. They overlap in 4,096 instances. Old/path/block
acceptances are 33,309/33,609/33,609 for quotas {0,1,2}, and
32,292/32,292/32,430 for {0,1/2,1}. Zero oracle, persistence or terminal
uniqueness discrepancies were found. The independent predicate reproduces
the predecessor's old-rule counts. These are same-programme checks, not an
external independent audit.

All reachable source-removal choices and all receiver/strict-row witnesses
are explored; equivalent anchors within an SCC and equivalent residual paths
are represented by one canonical anchor and one shortest path per endpoint.
Each candidate move is checked on every exact-minimum restriction retaining
its removal block. Finite testing does not establish the theorems by itself.

Completeness is FALSE: the stronger block rule still misses 552/126 instances
with a greatest tight minimum in those domains. A three-vertex obstruction
isolates its cause: only a neutrally removable predecessor can be deleted
first, but that source misses the low receiver. An explicit second example
shows that removing this safeguard without replacement would lose a tight
minimum. There are also 500 seeded n=4..6 cases, competing path and genuine
multi-source block deletions, 27 rejected corrupt complete certificates, and
one rejected unsafe low-guard step. Their domains overlap the exhaustive
regimes where applicable; these counts are not additive distinct instances.

The archived JSON tables use **scaled integers** for H,U,F,G: divide by each
example's `scale`. Masks encode subsets by bit i for vertex i. In certificate
paths, nodes 0..n-1 are left vertices, n..2n-1 are right vertices, 2n is s and
2n+1 is t. Quotas and flow values in certificates are ordinary exact rationals.

## Reproduction and saved evidence

Python 3.10+ and the standard library only. No external solver, API, service,
network access, model execution or workflow is required. From this directory:

```sh
python verify_residual.py FROZEN_CERTIFICATE.json
python test_residual.py replay integer
python test_residual.py replay rational
python test_residual.py replay focused
python test_residual.py replay sample
python diagnose_residual.py replay
python - <<'PY'
import gzip,json,hashlib
from pathlib import Path
archive=json.loads(gzip.decompress(Path('EVIDENCE.json.gz').read_bytes()))
for name,text in archive.items():
    assert Path(name).name==name
    assert (Path('replay')/name).read_bytes()==text.encode(),name
hashes=json.loads(Path('SOURCE_HASHES.json').read_text())
for name,digest in hashes['files'].items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
for name,text in archive.items():
    assert hashlib.sha256(text.encode()).hexdigest()==hashes['extracted_evidence'][name],name
print('all five exact outputs match; source and evidence hashes pass')
PY
```

EVIDENCE.json.gz preserves the exact UTF-8 contents of five output files:
INTEGER_RESULTS.json, RATIONAL_RESULTS.json, FOCUSED_RESULTS.json,
SAMPLE_RESULTS.json and DIAGNOSIS_RESULTS.json. It includes full subset/cut
tables for representative examples, successful certificates, corruption
inputs/rejection reasons, counts and deterministic record hashes. Exhaustive
per-instance records are hashed, not all stored individually; the commands
regenerate their aggregate digest. SOURCE_HASHES.json records file and
extracted-evidence hashes. VERIFICATION.json records execution scope.

## Exact next step

Implement the sufficient residual forced-count alternative proved in PROOF.md
Section 9 as a NEW certificate version. At anchor a, count the sources
reachable from a_L that enter the low receiver x; allow that count > P_x as
an alternative to the current requirement that the deleted block enter x.
Keep every other condition, rerun the identical independent domains, and
save the first remaining obstruction. This alternative is hand-proved but
NOT implemented or included in the P/B acceptance counts here.

Chen's full 1992 main condition remains uninspected. All earlier X3,
audit34854911792, equality, certification and external-review controls remain
unchanged. No schedules, deployments, purchases, extra-charge execution,
financial/health alerts or human-hour credits were changed.
