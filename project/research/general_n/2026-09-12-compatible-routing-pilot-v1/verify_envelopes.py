#!/usr/bin/env python3
"""Independent source maxima and cardinality dynamic programming."""
from collections import Counter
from pathlib import Path
import json
from independent_verify import options,coefficient,rhs
HERE=Path(__file__).resolve().parent

def main():
    records={(r['layer'],r['state_id']):r for r in json.loads((HERE/'pilot_inputs.json').read_text())['sample']}
    envelopes=json.loads((HERE/'envelopes.json').read_text());checks=0;gaps=[]
    for env in envelopes:
        rec=records[env['layer'],env['state_id']];h,j,mode=env['h'],env['j'],env['mode']
        opts=options(rec,h,j,mode);best={};constant=0
        for kind,desc,w in env['weights']:
            assert type(w) is int and (kind=='eq' and desc==['selected_balance'] or kind=='ub' and w>=0)
            assert desc[0] not in ('source_count','high_sender_count','count_cap')
            constant+=w*rhs(desc,rec,h,j,opts)
        for i,opt in enumerate(opts):
            checks+=1;cost=-sum(w*coefficient(desc,opt,h,j,mode,i) for kind,desc,w in env['weights'])
            key=opt[0],int(opt[3]>h);best[key]=max(best.get(key,cost),cost)
        dp={0:0}
        for rho in rec['rho']:
            if mode=='catalogue_free' and rho<h:continue
            nxt={}
            for used,value in dp.items():
                for e in (0,1):
                    if (rho,e) not in best or used+e>j:continue
                    total=value+best[rho,e];nxt[used+e]=max(nxt.get(used+e,total),total)
            dp=nxt
        assert j in dp
        assert constant==env['constant'] and dp[j]==env['maximum_with_j_high']
        assert [[r,e,v] for (r,e),v in sorted(best.items())]==env['local_class_maxima']
        assert -constant-dp[j]==env['gap']>0;gaps.append(env['gap'])
    report=dict(status='PASS',envelopes=len(envelopes),source_options_checked=checks,minimum_integer_gap=min(gaps),
        cardinality_check='Per-source dynamic programming, independently of discovery sorting',external_review='OPEN')
    (HERE/'envelope_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
