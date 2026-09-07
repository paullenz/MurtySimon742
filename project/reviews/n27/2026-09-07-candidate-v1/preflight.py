#!/usr/bin/env python3
"""Exact numerical reductions and aggregate consistency for the n=27 candidate."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def main():
    n=27;bound=Fraction(n*n,4)+(n*n-Fraction(81,5)*n+56)/320
    assert bound==Fraction(146669,800) and (bound.numerator-1)//bound.denominator==183
    witness={e:[comb(h,2)+h*(n-h)+(378-2*e-2*h)*(377-2*e-2*h) for h in range((378-2*e)//2+1)] for e in (183,182)}
    assert max(witness[183])==141 and witness[182][0]==182 and max(witness[182][1:])==161
    scopes=[]
    for e in (183,182):
        for delta in (15,16,17):
            a=26-delta;L=351-e-a-comb(delta,2);t=comb(a,2)-L
            assert t==e-delta*(27-delta)>0
            bands=[]
            for k in range(a):
                if k==0 and delta>L-comb(a-1,2):continue
                if k==1 and delta>L-1-comb(a-2,2):continue
                bands.extend((k,r) for r in range(delta,L-(a*k+1)//2+1))
            if delta==17:assert not bands
            else:
                if delta==16:
                    data=json.loads((ROOT/f'd16_{e}/primary_summary.json').read_text())
                    other=json.loads((ROOT/f'd16_{e}/independent_summary.json').read_text())
                    assert set(bands)=={(v['k'],v['r']) for v in data['rows']}
                    for key in ('scope','state_count','state_key_sha256','rows','survivors','column_vectors'):assert data[key]==other[key]
                    assert data['survivors']==data['column_vectors']==0
                    assert all(set(row['dispositions'])<= {'pair_threshold'} for row in data['rows'])
                else:
                    rows=[json.loads(s) for s in (ROOT/f'd15_{e}_summary.jsonl').read_text().splitlines()]
                    assert set(bands)=={(v['k'],v['r']) for v in rows}
                    check=json.loads((ROOT/f'd15_{e}_outer_check.json').read_text())
                    assert check['status']=='PASS' and check['counts']==[sum(v['counts'][i] for v in rows) for i in range(5)]
                    scan=json.loads((ROOT/f'd15_{e}_column_summary.json').read_text())
                    replay=json.loads((ROOT/f'd15_{e}_check_column_summary.json').read_text())
                    for key in scan:
                        if key!='checking':assert scan[key]==replay[key]
                    assert check['counts'][4]==scan['states']
                    assert (ROOT/f'd15_{e}_columns.jsonl').read_bytes()==(ROOT/f'd15_{e}_check_columns.jsonl').read_bytes()
            scopes.append({'edges':e,'delta':delta,'a':a,'L':L,'t':t,'bands':bands})
    return {'status':'PASS','Fan_strict_bound':str(bound),'witness_tables':witness,'domains':scopes,'external_review':False}

if __name__=='__main__':
    result=main();(ROOT/'PREFLIGHT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
