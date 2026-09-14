#!/usr/bin/env python3
"""Verify the global S/r/t ledger on the hash-pinned combined survivor stream."""
from pathlib import Path
import json
import sys

HERE=Path(__file__).resolve().parent
CAT=HERE.parent/'2026-09-12-compatible-routing-catalogue-v1'
sys.path.insert(0,str(CAT))
from evidence_io import read_bytes  # noqa: E402

OUT=HERE/'FROZEN_STATE_GLOBAL_LEDGER_VERIFICATION.json'


def main():
    rows=json.loads(read_bytes('survivors.json'))
    combined=[r for r in rows if r['combined_survives']]
    assert len(combined)==4584
    positive=zero=eq=strict=0
    layers={}
    slack_hist={}
    for rec in combined:
        a,b,t=rec['a'],rec['b'],rec['t']
        s=rec['s'];rho=rec['rho']
        S=sum(s);r=sum(rho);slack=S-r-2*t
        assert a==15
        assert b in (18,19)
        assert t>0
        assert len(s)==a and len(rho)==b
        assert min(rho)>=1
        assert slack>=0,(rec['layer'],rec['state_id'],S,r,t)
        if min(s)>0:
            positive+=1
            assert slack==0,(rec['layer'],rec['state_id'],S,r,t)
        else:
            zero+=1
        eq+=slack==0
        strict+=slack>0
        layers[rec['layer']]=layers.get(rec['layer'],0)+1
        slack_hist[str(slack)]=slack_hist.get(str(slack),0)+1
    result={
        'schema':'frozen-state-global-ledger-verification-v1',
        'combined_survivors':len(combined),
        'layers':layers,
        'positive_demand_states':positive,
        'zero_demand_states':zero,
        'ledger_equality_states':eq,
        'ledger_strict_slack_states':strict,
        'ledger_slack_histogram':dict(sorted(slack_hist.items(),key=lambda x:int(x[0]))),
        'checks':[
            'a=15',
            'b in {18,19}',
            't>0',
            'rho_u>=1',
            'sum(s)>=sum(rho)+2t',
            'min(s)>0 => sum(s)=sum(rho)+2t',
        ],
        'result':'PASS',
        'scope':'Frozen combined N34/N35 survivor stream only',
        'external_review':'OPEN',
    }
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
