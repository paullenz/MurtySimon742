#!/usr/bin/env python3
"""Reconstruct saved input keys and attach archived costs; do not recalculate them."""
from __future__ import annotations
import base64, collections, gzip, hashlib, itertools, json, math
from pathlib import Path


def main() -> None:
    root=Path(__file__).resolve().parent
    obj=json.loads((root/'EXACT_ROWS.indexed.json').read_text())
    if obj['format']!='domain-indexed-d5-endpoint-row-costs-v1':
        raise ValueError('Unknown evidence format')
    costs=gzip.decompress(base64.b64decode(obj['cost_bytes_gzip_base64'],validate=True))
    domain=[]
    for h in range(7):
        kappa=9+h
        for L in range(5*h//4+1):
            for u in itertools.combinations_with_replacement(range(L+1),5):
                if sum(u)!=L or any(h-L+x<0 for x in u):
                    continue
                capacity=5*h-4*L
                weight=math.factorial(5)
                for count in collections.Counter(u).values():
                    weight//=math.factorial(count)
                for n0 in range(kappa+1):
                    for N in range(kappa-n0+1):
                        n2=kappa-n0-N
                        if N+2*n2<=capacity and N<=capacity:
                            domain.append(([h,L,*u,n0,N,n2],weight))
    domain.sort()
    if len(domain)!=obj['rows'] or len(costs)!=len(domain):
        raise ValueError('Archived cost/domain length mismatch')
    rows=[key+[cost,weight] for (key,weight),cost in zip(domain,costs)]
    data=(json.dumps(rows,separators=(',',':'))+'\n').encode()
    if hashlib.sha256(data).hexdigest()!=obj['complete_table_sha256']:
        raise ValueError('Reconstructed table checksum mismatch')
    (root/'SAVED_ROW_COSTS.json').write_bytes(data)
    print(f'PASS: reconstructed {len(rows)} saved rows; costs not recomputed')


if __name__=='__main__':
    main()
