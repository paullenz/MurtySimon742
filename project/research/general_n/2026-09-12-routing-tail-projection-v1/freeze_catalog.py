#!/usr/bin/env python3
"""Freeze pilot ratios and their zero-penalty ablations before full replay."""
from pathlib import Path
from fractions import Fraction
import json,math,hashlib
HERE=Path(__file__).resolve().parent

def main():
    raw=(HERE/'pilot_results.jsonl').read_bytes();found=set()
    for line in raw.splitlines():
        rec=json.loads(line)
        for mode,result in rec['modes'].items():
            for threshold in result.get('thresholds',[]):
                h=threshold['h']
                for test in threshold['tests']:
                    for c in test.get('cases',[]):
                        if not c.get('capacity_exclusion'):
                            found.add(tuple(Fraction(c[k],c['denominator']*h) for k in ('lam','mu','eta','kappa')))
    source_count=len(found)
    found.update(t[:3]+(Fraction(0),) for t in list(found))
    # Retain the preceding frozen routing catalogue too; all have kappa=0.
    old=json.loads((HERE.parent/'2026-09-12-joint-routing-pilot-v1/multiplier_catalog.json').read_text())
    found.update(tuple(Fraction(t[k],t['denominator']) for k in ('lam','mu','eta'))+(Fraction(0),) for t in old['templates'])
    entries=[]
    for t in sorted(found):
        den=math.lcm(*(x.denominator for x in t))
        entries.append(dict(denominator=den,**{k:int(v*den) for k,v in zip(('lam','mu','eta','kappa'),t)}))
    report=dict(schema='routing-tail-projection-catalog-v1',source_sha256=hashlib.sha256(raw).hexdigest(),pilot_distinct_ratios=source_count,
                rule='Successful pilot local certificates, their kappa=0 versions, and the preceding 20 routing templates; scale all numerators by h.',templates=entries)
    (HERE/'multiplier_catalog.json').write_text(json.dumps(report,indent=2)+'\n');print('FROZEN',len(entries),'templates from',source_count,'pilot ratios')

if __name__=='__main__':main()
