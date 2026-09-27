# Local canonical certificate and ordering separation

User-requested in-chat continuation, 27 September 2026. Base inspected: `0321ba26f56442f57eb09d0c8c1c29fddcf04921`; CURRENT_STATE.md was read first. All results are internal, without external review or novelty clearance. No general Murty–Simon bound, equality claim, schedule, deployment or paid computation is changed.

## Results

[PROOF.md](PROOF.md) gives a solver-free instance certificate for the greatest rearrangement-tight Hall minimum, with nonnegative real quotas and unit supported arcs. It needs no global WCD or demand-order assumptions. A neutral deletion may remove a source different from the high receiver. The local rule persists under restriction to exact minima; hence its deletions commute, giving one terminal regardless of order, even if that terminal is not tight. The explicit three-vertex boundary shows the rule is not complete for all instances with a greatest tight minimum.

[COMPARISON.md](COMPARISON.md) proves that all 120 nonincreasing column orders of the six-vertex padded example miss its obstruction. Exactly 144 of 5,040 transposed orders detect it, with an infinite-family counting formula. A feasible margin vector dominating an infeasible one rules out ANY single fixed prefix-dominance reference in the original orientation. Chen's full main condition remains uninspected; this is not a claim about an invented Chen premise.

## Exact checks

| Regime | Instances | Certificates accepted | WCD/RD instances | Nonempty certificates | Greatest tight exists but no certificate |
|---|---:|---:|---:|---:|---:|
| n=3, P,d in {0,1,2} | 46,656 | 33,309 | 9,252 | 5,190 | 852 |
| n=3, P,d in {0,1/2,1} | 46,656 | 32,292 | 8,334 | 6,501 | 264 |

Each regime includes all 64 labelled loopless supports, one block and all quota vectors. They overlap in 4,096 instances; counts are not additive distinct coverage. Each compares all eight source subsets using an independently written scaled-integer oracle. Every accepted terminal equals the oracle's greatest tight minimum. Every reachable local deletion choice is explored; each instance has exactly one terminal. All WCD/RD cases succeed. Zero discrepancies were found. Acceptance outside WCD/RD includes zero-deletion cases; do not call all such acceptances nontrivial extensions.

Additional checks cover six explicit examples, all 256 states/1,024 transitions of an eight-deletion construction, 16 rejected corrupt certificates, all 5,160 matrix orders and the incomplete three-vertex system. The eight-deletion example uses its hand-proved optimum, not a 2^17 exhaustive subset oracle. The 40,320 full deletion orders are represented by the explored state graph, not separately enumerated.

The original endpoint-only development stage was superseded and is retained in the downloadable bundle, not added to these counts. One hostile test initially doubled an EMPTY terminal list, creating no corruption; its expected rejection correctly failed. The fixture was repaired to use a nonempty terminal. No verifier soundness defect was observed in that failure. A numerical value in the draft prose was checked against its certificate and corrected before publication.

## Reproduce

Python 3.10+ standard library only. `verify_local.py` is the small verifier; `test_local.py` supplies an independent maximum-flow producer and brute-force quantity oracle. It uses the verifier's local predicate to enumerate the rule's moves, so that part is not a separately implemented predicate audit.

Frozen individual evidence files are losslessly packed as filename-to-UTF-8-content strings in EVIDENCE.json.gz. Extract them first:

```sh
python - <<'PY'
import gzip,json
from pathlib import Path
for name,text in json.loads(gzip.decompress(Path('EVIDENCE.json.gz').read_bytes())).items():
    if Path(name).name != name:
        raise ValueError('unexpected evidence path')
    Path(name).write_text(text,encoding='utf-8')
PY
python verify_local.py DEMO_CERTIFICATE.json
mkdir -p replay
for mode in integer rational hostile orders limits; do
    python test_local.py replay "$mode"
done
python - <<'PY'
from pathlib import Path
for name in ('INTEGER_RESULTS.json','RATIONAL_RESULTS.json','HOSTILE_RESULTS.json',
             'ORDER_RESULTS.json','INCOMPLETENESS.json','DEMO_CERTIFICATE.json'):
    assert Path(name).read_bytes() == (Path('replay')/name).read_bytes(), name
print('six outputs match byte-for-byte')
PY
```

The final source was replayed before packaging and all six outputs matched byte-for-byte. SOURCE_HASHES.json records both stored-source and extracted-evidence SHA-256 hashes. This is same-programme testing, not external specialist review or formal verification.

## Exact next step

Implement a verified residual implication from the neutrally deleted source to a different source supplying the strict incoming-row difference. First repair the frozen P=(0,2,1), d=(1,1,0), R={0->1,0->2,1->2} example, then test the generalized rule and whether all-or-none residual blocks remain necessary. The enhanced rule is not implemented or included in current totals. Do not repeat an abstract-only Chen search as though its main condition had been read.
