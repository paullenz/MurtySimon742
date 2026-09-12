#!/usr/bin/env python3
"""Freeze scale-invariant multiplier templates from the completed pilot."""
from fractions import Fraction
from pathlib import Path
import json,math,hashlib
HERE=Path(__file__).resolve().parent

def main():
    raw=(HERE/'pilot_results.jsonl').read_bytes();ts=set()
    for line in raw.splitlines():
        r=json.loads(line)
        for mode in ('aggregate','joint'):
            w=r['modes'][mode]
            if not w:continue
            for c in w['cases']:
                if c.get('source_capacity_exclusion'):continue
                ts.add(tuple(Fraction(c[k],c['denominator']*w['h']) for k in ('lam','mu','eta')))
    entries=[]
    for tup in sorted(ts):
        den=math.lcm(*(x.denominator for x in tup))
        entries.append(dict(lam=int(tup[0]*den),mu=int(tup[1]*den),eta=int(tup[2]*den),denominator=den))
    report=dict(schema='joint-routing-multiplier-catalog-v1',source_sha256=hashlib.sha256(raw).hexdigest(),
        scale='Multiply each numerator by h, keeping the denominator.',
        scope='Templates frozen from the 27-case pilot before full-domain replay. No numerical optimization in replay.',templates=entries)
    (HERE/'multiplier_catalog.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FROZEN_TEMPLATES',len(entries))

if __name__=='__main__':main()
