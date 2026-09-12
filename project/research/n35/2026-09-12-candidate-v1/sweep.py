#!/usr/bin/env python3
"""N35 proposals and exact acceptance, with all failed proposals retained."""
from collections import Counter
import json
import time
import envelopes as env
from frontier import HERE,expand


def refined_reason(s,rho):
    for h in range(1,max(s)+1):
        W=sum(v for v in s if v>=h)
        caps=[min(15-r,sum(h<=v<=r for v in s)) for r in rho if r>=h]
        z=len(caps);L=sum(min(h,c) for c in caps)
        high=sorted((c for c in caps if c>h),reverse=True)
        limits=[L-j*h+min(sum(high[:j]),j*z-j*(j+1)//2) for j in range(len(high)+1)]
        if W>max(limits):
            return dict(method='source_capped_threshold',h=h,W=W,z=z,capacities=caps,upper_bounds=limits)


def compact(cert):
    keep=[i for i,n in enumerate(cert['names']) if not
          (isinstance(n,tuple) and n[0]=='weight' and cert['numerators'][i]==0)]
    return dict(cert,names=[cert['names'][i] for i in keep],numerators=[cert['numerators'][i] for i in keep])


def main():
    start=time.monotonic()
    for t in (3,2):
        env.T=t;states,stats=expand(t);path=HERE/f't{t}.jsonl'
        saved=[json.loads(x) for x in path.read_text().splitlines()] if path.exists() else []
        assert len(saved)<=len(states)
        for i,rec in enumerate(saved):
            assert rec['state_id']==i and (tuple(rec['s']),tuple(rec['rho']))==states[i]
        counts=Counter(r['method'] for r in saved)
        with path.open('a') as out:
            for i,(s,rho) in enumerate(states):
                if i<len(saved):continue
                rec=dict(state_id=i,t=t,s=s,rho=rho)
                reason=(dict(method='positive_degree_mass',S=sum(s),r=sum(rho))
                        if min(s)>0 and sum(s)!=sum(rho)+2*t else
                        env.subset_reason(s,rho) or refined_reason(s,rho))
                if reason:rec.update(reason)
                else:
                    rec['proposals']=[]
                    for mode in ('fixed9','fixed13','adaptive'):
                        model=env.build(s,rho,mode);cert=env.integer_certificate(model)
                        rec['proposals'].append(dict(mode=mode,solver_status=int(model[-1].status),integer_accepted=cert is not None))
                        if cert:rec.update(compact(cert));rec['method']=mode;break
                    else:rec['method']='unresolved'
                counts[rec['method']]+=1
                out.write(json.dumps(rec,separators=(',',':'))+'\n');out.flush()
                if (i+1)%50==0 or i+1==len(states):
                    print('PROGRESS',t,i+1,len(states),dict(counts),round(time.monotonic()-start,2),flush=True)
        summary=dict(t=t,frontier=stats,counts=dict(counts),external_review='OPEN')
        (HERE/f't{t}_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
        print('COMPLETE',json.dumps(summary),flush=True)


if __name__=='__main__':main()
