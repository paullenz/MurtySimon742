#!/usr/bin/env python3
"""Decode domain-indexed decisions and verify the recorded full-output hash.

The fixed domain reconstructs matrix shapes; only positive destination
masks are stored. This decoder does not recompute any routing decision.
"""
import hashlib
import itertools
import json
from pathlib import Path
root=Path(__file__).resolve().parent
obj=json.loads((root/'EXACT_DECISIONS.indexed.json').read_text())
if obj['format']!='indexed-two-hole-decisions-v1':
    raise SystemExit('Unknown evidence format')
pairs=list(itertools.combinations(range(5),2))
def domain(i,remaining,counts):
    if i==len(pairs):
        if not any(remaining):yield counts
        return
    s,t=pairs[i]
    for n in range(min(remaining[s],remaining[t])+1):
        r=remaining.copy();r[s]-=n;r[t]-=n
        if any(r[v] and not any(v in e for e in pairs[i+1:]) for v in range(5)):
            continue
        yield from domain(i+1,r,counts+[n])
rows=[]
for counts in sorted(domain(0,[6]*5,[])):
    holes=[pair for pair,n in zip(pairs,counts) for _ in range(n)]
    if len(holes)!=15:raise SystemExit('Malformed domain')
    rows.append(counts+[0 if t in pair else -1 for t in range(5) for pair in holes])
if len(rows)!=654:raise SystemExit('Domain size mismatch')
for packed in obj['nonzero_packed']:
    index,mask=divmod(packed,32)
    row,col=divmod(index,75)
    if not 0<=row<len(rows) or not mask or rows[row][10+col]!=0:
        raise SystemExit('Malformed nonzero decision')
    rows[row][10+col]=mask
full={'interfaces':rows,'scalar':obj['scalar']}
raw=json.dumps(full,sort_keys=True,separators=(',',':')).encode()+b'\n'
expected=json.loads((root/'CHECK_RESULTS.json').read_text())['exact_decisions_sha256']
if hashlib.sha256(raw).hexdigest()!=expected:raise SystemExit('Decision SHA256 mismatch')
(root/'EXACT_DECISIONS.json').write_bytes(raw)
print(f'Verified and decoded {len(raw)} bytes')
