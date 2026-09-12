#!/usr/bin/env python3
"""Deterministic sample after reapplying every existing hand filter."""
from collections import Counter,defaultdict
from pathlib import Path
import hashlib,json,sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(HERE.parent/'2026-09-12-heavy-load-family-v1'))
from evidence_io import read_bytes


def old_hand(rec):
    a,s,rho,t=rec['a'],rec['s'],rec['rho'],rec['t']
    if min(s)>0 and sum(s)!=sum(rho)+2*t:return dict(method='positive_degree_mass')
    for h in range(1,max(s)+1):
        W=sum(v for v in s if v>=h)
        Z=[v for v in rho if v>=h];z=len(Z)
        if h>=2 and z>=h and 2*W==z*(z-1)+h*(h+1) and W-h*(h+1)>sum(v-1 for v in Z):
            return dict(method='tight_subset_threshold',h=h)
        caps=[min(a-v,sum(h<=sv<=v for sv in s)) for v in Z]
        low=sum(min(h,c) for c in caps);high=sorted((c for c in caps if c>h),reverse=True)
        bounds=[low-j*h+min(sum(high[:j]),j*z-j*(j+1)//2) for j in range(len(high)+1)]
        if W>max(bounds):return dict(method='source_capped_threshold',h=h,bounds=bounds,W=W)
    return None


def select():
    raw=read_bytes('remaining_states.json')
    records=[r for r in json.loads(raw) if r['original_method'] in ('fixed9','fixed13','adaptive')]
    eligible=[];removed=[]
    for r in records:
        why=old_hand(r)
        if why:removed.append(dict(layer=r['layer'],state_id=r['state_id'],reason=why))
        else:eligible.append(r)
    groups=defaultdict(list)
    for r in eligible:groups[r['layer'],r['original_method']].append(r)
    sample=[]
    # Up to three evenly spaced records per layer/method stratum, plus all
    # six small upper-layer cases and three evenly spaced zero-demand cases.
    for key,items in sorted(groups.items()):
        indices=range(len(items)) if key[0]=='n35-m307' else sorted({0,len(items)//2,len(items)-1})
        sample.extend(items[i] for i in indices)
    zeros=[r for r in eligible if min(r['s'])==0]
    sample.extend(zeros[i] for i in sorted({0,len(zeros)//2,len(zeros)-1}) if zeros)
    sample=list({(r['layer'],r['state_id']):r for r in sample}.values())
    sample.sort(key=lambda r:(r['layer'],r['state_id']))
    report=dict(schema='joint-routing-pilot-selection-v1',input_sha256=hashlib.sha256(raw).hexdigest(),
        historical_envelope_pool=len(records),removed_by_reapplied_hand_rules=removed,
        eligible_pool=len(eligible),eligible_counts={str(k):len(v) for k,v in sorted(groups.items())},
        selection='Per layer/method: first, middle, last; all N35 m307; first/middle/last zero-demand survivors; deduplicate; sort by layer/id.',
        selected=len(sample),sample=sample)
    return report

if __name__=='__main__':
    report=select();(HERE/'pilot_inputs.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('sample','removed_by_reapplied_hand_rules')},indent=2))
    print('REAPPLIED_HAND_REMOVALS',len(report['removed_by_reapplied_hand_rules']))
