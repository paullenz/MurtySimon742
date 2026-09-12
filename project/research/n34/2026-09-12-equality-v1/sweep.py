#!/usr/bin/env python3
"""Resumable equality sweep. Saved exact integers, not LP status, decide."""
from collections import Counter
import argparse
import json
import time
from envelopes import HERE, build, subset_reason, integer_certificate
from check_frontier import expand


def read_records(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def compact(cert):
    keep = [j for j,n in enumerate(cert['names'])
            if not (isinstance(n,tuple) and n[0]=='weight' and cert['numerators'][j]==0)]
    return dict(cert,names=[cert['names'][j] for j in keep],
                numerators=[cert['numerators'][j] for j in keep])


def refined_reason(s,rho):
    """Source-capped heavy-incidence capacity; proof is in SOURCE_CAPPED_THRESHOLD.md."""
    for h in range(1,max(s)+1):
        W=sum(v for v in s if v>=h)
        caps=[min(15-r,sum(h<=v<=r for v in s)) for r in rho if r>=h]
        z=len(caps)
        low=sum(min(h,c) for c in caps)
        high=sorted((c for c in caps if c>h),reverse=True)
        bounds=[low-j*h+min(sum(high[:j]),j*z-j*(j+1)//2)
                for j in range(len(high)+1)]
        if W>max(bounds):
            return dict(method='source_capped_threshold',h=h,W=W,z=z,
                        capacities=caps,upper_bounds=bounds)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stage',choices=['fixed','adaptive'])
    args = ap.parse_args()
    states,stats = expand(1)
    inputs = [dict(state_id=i,s=s,rho=rho) for i,(s,rho) in enumerate(states)]
    if args.stage == 'adaptive':
        prior = read_records(HERE/'fixed.jsonl')
        assert len(prior)==len(states)
        inputs = [{k:rec[k] for k in ('state_id','s','rho')}
                  for rec in prior if rec['method']=='unresolved']
    path = HERE/(args.stage+'.jsonl')
    saved = read_records(path)
    done = {rec['state_id'] for rec in saved}
    assert len(done)==len(saved) and done <= {r['state_id'] for r in inputs}
    counts = Counter(rec['method'] for rec in saved)
    start = time.monotonic()
    print('START',args.stage,'inputs',len(inputs),'resuming',len(saved),flush=True)
    with path.open('a') as out:
        for rec in inputs:
            if rec['state_id'] in done:
                continue
            s,rho = rec['s'],rec['rho']
            reason = None
            if args.stage=='fixed':
                if min(s)>0 and sum(s)!=sum(rho)+2:
                    reason = dict(method='positive_degree_mass',S=sum(s),r=sum(rho))
                else:
                    reason = subset_reason(s,rho)
            else:
                reason = refined_reason(s,rho)
            if reason:
                rec.update(reason)
            else:
                proposals=[]
                for mode in (['adaptive'] if args.stage=='adaptive' else ['fixed9','fixed13']):
                    model=build(s,rho,mode)
                    cert=integer_certificate(model)
                    proposals.append(dict(mode=mode,solver_status=int(model[-1].status),integer_accepted=cert is not None))
                    if cert:
                        rec.update(compact(cert));rec['method']=mode;break
                else:
                    rec['method']='unresolved'
                rec['proposals']=proposals
            counts[rec['method']]+=1
            out.write(json.dumps(rec,separators=(',',':'))+'\n');out.flush()
            done.add(rec['state_id'])
            if len(done)%200==0 or len(done)==len(inputs):
                print('PROGRESS',len(done),dict(counts),'seconds',round(time.monotonic()-start,2),flush=True)
    report=dict(schema='n34-equality-discovery-stage-v1',stage=args.stage,
                frontier=stats,inputs=len(inputs),processed=len(done),counts=dict(counts),
                discovery_complete=len(done)==len(inputs))
    (HERE/(args.stage+'_summary.json')).write_text(json.dumps(report,indent=2)+'\n')
    print('COMPLETE',json.dumps(report),flush=True)


if __name__=='__main__':
    main()
