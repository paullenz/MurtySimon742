#!/usr/bin/env python3
"""Replay all difficult profiles, retaining every threshold's budget terms."""
import collections, hashlib, json
from pathlib import Path
from explore_thresholds import profiles
from verify_interval_budget import check, target_caps
ROOT=Path(__file__).parent
counts=collections.Counter();first=collections.Counter();best=collections.Counter();details=[];nrows=0
for p in profiles:
    assert target_caps(p['a'],p['q'],p['rho'],p['Esel'],p['s'].count(0))==p['P']
    result=check(p['q'],p['rho'],p['P'],p['a'],p['t'],p['D0'],p['Esel'])
    assert all(row['Xi']==0 for row in result['rows'])
    assert max(row['interval_lower'] for row in result['rows'])>0
    counts['profiles']+=1;counts['interval_detected']+=1
    counts['uniform_weight_detected']+=sum(row['deficiency'] for row in result['rows'])>0
    first[next(row['tau'] for row in result['rows'] if row['deficiency']>0)]+=1
    best[max(result['rows'],key=lambda row:row['deficiency'])['tau']]+=1
    nrows+=len(result['rows'])
    details.append(dict(index=p['index'],state=p['state'],a=p['a'],b=p['b'],delta=p['b']-p['a'],D0=p['D0'],Esel=p['Esel'],t=p['t'],r=p['r'],Q=p['Q'],G=p['G'],q_hist=dict(collections.Counter(p['q'])),rho_hist=dict(collections.Counter(p['rho'])),thresholds=result['rows']))
summary=dict(status='PASS',counts=dict(counts),first_threshold=dict(first),maximum_deficiency_threshold=dict(best),threshold_rows_checked=nrows,source_sha256=hashlib.sha256((ROOT/'LAYER_EXCEPTION_DIAGNOSTIC.tsv').read_bytes()).hexdigest(),scope='Independent integer checks, frozen difficult profiles only')
assert dict(counts)==dict(profiles=812,interval_detected=812,uniform_weight_detected=476)
assert nrows==6667 and dict(first)=={2:426,3:191,4:195} and dict(best)=={2:220,3:170,4:422}
(ROOT/'INTERVAL_812_CORRELATIONS.json').write_text(json.dumps(details,indent=2,sort_keys=True)+'\n')
(ROOT/'INTERVAL_812_VERIFICATION.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,indent=2,sort_keys=True))
