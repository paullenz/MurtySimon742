# Forced-count and signed residual-closure Hall certificates

27 September 2026. User-authorized in-chat mathematics, starting from
`fc5d692113f62a55c91dacbca3a5b1a499f65cb1`, after reading CURRENT_STATE.md
first. The predecessor version-2 files are unchanged. No external review,
formal verification, novelty clearance or general Murty–Simon proof is claimed.

## Structural results

**Version 3:** [PROOF.md](PROOF.md) and [verify_forced.py](verify_forced.py)
implement the previously proposed forced-count alternative. A source/block
need not enter the low receiver if its residual implications force more than
that receiver's capacity into it. The source set is recomputed exactly. The
strict inequality, persistence, commutation and greatest-tight certificate
are proved and tested; the saved unsafe equality case remains rejected.

**Version 4:** [CLOSURE_PROOF.md](CLOSURE_PROOF.md) and
[verify_closure.py](verify_closure.py) make a further structural advance.
Mandatory sources are included in the least exact minimum containing an
anchor. An auxiliary flow certifies a positive signed incoming difference
over every exact minimum containing that anchor within the current state.
This replaces row containment. The actual deletion removes every source
that residually forces the excluded anchor, even across several SCCs.
The proofs establish same-flow persistence, confluence for overlapping
removals, and subsumption of every version-3 block move.

The checker needs only a feasible auxiliary flow with a sufficiently large
value, not an asserted auxiliary optimum. A separate producer computes
maxima and compares them with independent exhaustive source-subset minima.
The optimized criterion is exact for one pair crossing on every anchored
minimum; it is not complete for finding every greatest tight minimum.

## Executed comparison

| Domain | Instances | V2 block accepted | V3 block accepted | V4 accepted | Greatest tight exists but V4 fails |
|---|---:|---:|---:|---:|---:|
| n=3; P,d in {0,1,2} | 46,656 | 33,609 | 33,657 | 34,149 | 12 |
| n=3; P,d in {0,1/2,1} | 46,656 | 32,430 | 32,556 | 32,556 | 0 |
| Seeded n=4..6 mixed quotas | 500 | 199 | 200 | 206 | 0 |

The two exhaustive domains contain every labelled loopless support, one
receiver block, and every quota vector. They overlap in 4,096 instances;
version-3 and version-4 runs repeat these SAME instances. Do not add runs
as distinct coverage. The 500-instance domain is a deterministic sample,
not exhaustive. Every source subset is independently calculated in each run.
Version-3 runs additionally check all 2,985,984 complete original cuts per
exhaustive domain. Version-4 runs use independent subset minima to check
31,902 / 30,132 signed optimizations and 33,258 / 40,992 same-flow restriction
checks in the integer / half-integer domains. Complete cuts are not counted
again in those version-4 exhaustive runs.

Every reachable removal choice is explored, including overlapping cones.
All accepted terminals match the independently computed greatest tight
minimum; every choice graph has one terminal. Zero discrepancies. Version-3
runs reproduce version-2 counts, and version-4 runs reproduce version-3 block
counts. These are same-programme checks, not an external audit.

Focused checks include three independent two-step forced chains (27 states,
54 transitions), three independent compensation deletions (8 states,
12 transitions), SCC removals, overlapping predecessor removals, 24 rejected
corrupt complete certificates (15 V3 + 9 V4), and one rejected unsafe
nonstrict step. Counts include overlapping constructions; do not add them
as distinct instances. VERIFICATION.json records the executed scopes.

## Remaining obstruction and exact next step

Version 4 is still incomplete, with a sharp three-vertex example:
P=(2,1,0), d=(1,0,1), R={0->1,0->2,1->2,2->0}, one block. Every subset is
an exact minimum. The greatest tight minimum is {0,2}; source 1 must go.
Yet no single crossing pair excludes it across every anchored minimum.

A two-case proof works: if source 0 is absent, pair (2,1) crosses; if source
0 is present, pair (2,0) crosses. The branch assumptions are proof conditions,
not actual deletions of source 0. The exact tables and witnesses against every
fixed pair are in BRANCHING_OBSTRUCTION.json inside the evidence archive.

**Next:** implement this two-leaf branching certificate, with checked
conditional inclusion/exclusion constraints and auxiliary flows at its
leaves. Prove coverage, persistence and confluence, then replay the same
domains. The two-case example is hand/oracle checked; no branching verifier
or general completeness result is implemented here.

## Reproduction

Python 3.10+ standard library only; no solver service, network or paid/API
execution. The two verifiers are standalone. Tests also read the preserved
`../residual-certificate-2026-09-27/test_residual.py` and `verify_residual.py`.
Their hashes are included as dependencies. From this directory:

```sh
python test_forced.py replay integer
python test_forced.py replay rational
python test_forced.py replay sample
python test_forced.py replay focused
python test_closure.py replay integer
python test_closure.py replay rational
python test_closure.py replay sample
python test_closure.py replay focused
python diagnose_closure.py replay
python verify_forced.py replay/DEMO_CERTIFICATE.json
python verify_closure.py replay/CLOSURE_DEMO.json
python - <<'PY'
from pathlib import Path
import gzip,json,hashlib
saved=json.loads(gzip.decompress(Path('EVIDENCE.json.gz').read_bytes()))
for name,text in saved.items():
    assert Path(name).name==name
    assert (Path('replay')/name).read_bytes()==text.encode(),name
h=json.loads(Path('SOURCE_HASHES.json').read_text())
for category in ('files','dependencies'):
    for name,digest in h[category].items():
        assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
for name,text in saved.items():
    assert hashlib.sha256(text.encode()).hexdigest()==h['extracted_evidence'][name],name
print('13 exact outputs reproduced; all source and evidence hashes match')
PY
```

All nine generating modes were executed from the stored source. A separate
second full execution is not claimed. The archive preserves 13 exact JSON
output files, representative full subset/cut tables, certificates, corrupt
inputs/rejections, counts and hashes of deterministic ordered instance
records. Full exhaustive per-instance streams are hashed, not all stored.
Quota/flow certificate fields are ordinary exact rationals. H,U,F,G in
example oracle tables use integers scaled by the recorded `scale`. Masks
use bit i for source i. Certificate nodes 0..n-1 are sources, n..2n-1 receivers,
2n/2n+1 original s/t; V4's auxiliary terminals are 2n+2/2n+3.

X3, audit34854911792, equality and inherited certification controls are
unchanged. Chen's full main condition remains uninspected. Schedules remain
paused, alerts untouched, and no spending/deployment/research-hour credit
or background-work promise is made.
