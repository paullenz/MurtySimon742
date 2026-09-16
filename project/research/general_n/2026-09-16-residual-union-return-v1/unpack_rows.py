#!/usr/bin/env python3
"""Expand STORED symmetry records; never solve a receiver minimization."""
import base64,gzip,hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
record=json.loads(gzip.decompress(base64.b64decode((root/'SYMMETRY_ROWS.json.gz.b64').read_bytes(),validate=False)))
lookup={tuple(row[:6]):row[6:] for row in record['rows']}
rows=[]
for p in range(1,5):
 for a in range(2,7):
  for lam in (1,a,a+1):
   for flags in range(1<<(2*p)):
    states=[(flags>>(2*t))&3 for t in range(p)]
    key=(p,a,lam,states.count(0),states.count(3),sum(x in (1,2) for x in states))
    rows.append([p,a,lam,flags]+lookup[key])
raw=json.dumps(rows,separators=(',',':')).encode()
if hashlib.sha256(raw).hexdigest()!=record['full_domain_sha256']:
 raise ValueError('Stored row expansion hash mismatch')
(root/'DECODED_EXACT_ROWS.json').write_bytes(raw)
print('Decoded',len(rows),'stored rows; SHA256',hashlib.sha256(raw).hexdigest())
