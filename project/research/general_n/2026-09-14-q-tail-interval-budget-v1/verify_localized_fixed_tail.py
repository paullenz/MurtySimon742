#!/usr/bin/env python3
"""Independent reconstruction of the 812-case fixed tau=3 certificate.
This checks the stronger LOCALIZED cap model; the old-weight obstruction is not
silently deleted or transferred between models. No optimizer is needed.
"""
import collections,json
from pathlib import Path
from explore_thresholds import profiles
from verify_interval_budget import check,target_caps
ROOT=Path(__file__).parent

def localized(a,q,rho,s,E):
    P=target_caps(a,q,rho,E,s.count(0));trace=[]
    for eta in sorted({0,*rho}):
        low=[i for i,si in enumerate(s) if si<=eta]
        C=E+sum(s[i] for i in low)-sum(qu for qu,ru in zip(q,rho) if ru<=eta)
        if C<0:raise ValueError('Selected-incidence impossible')
        for u in range(len(q)):
            if rho[u]<=eta:continue
            k=min(len(low),q[u],C)
            if q[u]>k:
                cap=rho[u]-1+(C-k)//(q[u]-k)
                if cap<P[u]:trace.append([eta,u,P[u],cap,C]);P[u]=cap
    return P,trace

def main():
    counts=collections.Counter();first=collections.Counter();margins=[];details=[]
    for p in profiles:
        cap,trace=localized(p['a'],p['q'],p['rho'],p['s'],p['Esel'])
        checked=check(p['q'],p['rho'],cap,p['a'],p['t'],p['D0'],p['Esel'])
        row=next(r for r in checked['rows'] if r['tau']==3)
        assert row['interval_lower']==row['deficiency'] and row['deficiency']>0
        margins.append(row['deficiency'])
        counts['profiles']+=1;counts['changed']+=cap!=p['P']
        counts['uniform_detects']+=sum(r['deficiency'] for r in checked['rows'])>0
        first[next(r['tau'] for r in checked['rows'] if r['deficiency']>0)]+=1
        details.append(dict(index=p['index'],state=p['state'],P_local=cap,trace=trace,rows=checked['rows']))
    assert dict(counts)==dict(profiles=812,changed=748,uniform_detects=773)
    assert min(margins)==1 and max(margins)==15
    result=dict(status='PASS',scope='Existing 812 rows, localized caps, fixed tau=3; no optimizer or new generation',counts=dict(counts),first_threshold=dict(first),common_integer_weights=[0,0,1,0,0,0,0,0],minimum_integer_pressure=min(margins),maximum_integer_pressure=max(margins))
    (ROOT/'LOCALIZED_FIXED_TAIL_VERIFICATION.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    (ROOT/'LOCALIZED_812_RECONSTRUCTION.json').write_text(json.dumps(details,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
