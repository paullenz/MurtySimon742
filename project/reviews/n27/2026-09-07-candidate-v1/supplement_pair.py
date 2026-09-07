#!/usr/bin/env python3
"""Forced-label and supplement-neighbourhood pair-budget certificates.

If a label needs D_i selected sources and only D_i sources are eligible, every
eligible source must select it. Let f_b count these forced labels. A selected
bi has q_b >= max(f_b, d_i-rho_b+1, 1). Its supplement w must have at least
q_b-1 A-neighbours, but has at most rho_w+c_w. Count unordered pairs admitting
at least one label and orientation meeting these necessary conditions.
"""
import argparse,gzip,hashlib,json
from pathlib import Path

def certificate(row):
    state,k,r,d,rho,R,c=row;a=len(d);b=len(rho)
    demand=[max(0,d[i]-R[i]) for i in range(a)]
    eligible=[[v for v in range(b) if d[i]<=rho[v]+c[v]-1 and d[i]<=rho[v]+R[i]] for i in range(a)]
    forced=[0]*b
    for i in range(a):
        if demand[i]>len(eligible[i]):
            return {'kind':'single_label','label':i,'required':demand[i],'available':len(eligible[i])}
        if demand[i]==len(eligible[i]) and demand[i]>0:
            for v in eligible[i]:forced[v]+=1
    allowed=[]
    for v in range(b):
        for w in range(v):
            possible=False
            for source,supp in ((v,w),(w,v)):
                for i in range(a):
                    if source not in eligible[i] or d[i]>rho[source]+rho[supp]:continue
                    q_lower=max(1,forced[source],d[i]-rho[source]+1)
                    if q_lower<=c[source] and rho[supp]+c[supp]>=q_lower-1:
                        possible=True;break
                if possible:break
            if possible:allowed.append([w,v])
    if sum(demand)>len(allowed):
        return {'kind':'supplement_pair_budget','demand_by_label':demand,'eligible_sources':eligible,
                'forced_by_source':forced,'allowed_pairs':allowed,
                'required':sum(demand),'available':len(allowed)}
    return None

def run(source,prefix):
    rows=[json.loads(s) for s in gzip.open(source,'rt')];certs=[];survivors=[]
    for row in rows:
        witness=certificate(row)
        (certs if witness else survivors).append({'row':row,'witness':witness} if witness else row)
    data={'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checked':len(rows),
          'eliminated':len(certs),'surviving_columns':len(survivors),
          'status':'ALL_REJECTED' if not survivors else 'SURVIVORS_RETAINED','external_review':False,
          'certificates':certs,'survivors':survivors}
    Path(str(prefix)+'_supplement_certificates.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ('certificates','survivors')}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('prefix',type=Path)
    a=p.parse_args();run(a.input,a.prefix)
