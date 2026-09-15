#!/usr/bin/env python3
"""Exact necessary inequalities for a simultaneous family of forced cores."""
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path

def cores(p):
    a,b,s,q,rho=p['a'],p['b'],p['s'],p['q'],p['rho']
    out=[]
    for r in sorted(set(rho)):
        h=sum(d<=r for d in s)
        U=[v for v in range(b) if rho[v]==r and q[v]==h]
        if not h or not U: continue
        eligible=[v for v in range(b) if v not in U and q[v]<=h+r-1 and q[v]+rho[v]>=h-1 and rho[v]+b-a-1>0]
        out.append({'r':r,'h':h,'m':len(U),'U':U,'eligible':eligible})
    return out

def joint_cuts(p):
    cc=cores(p); s=p['s'];b=p['b'];caps=[max(0,r+b-p['a']-1) for r in p['rho']]
    checks=0; failures=[]
    # A receiver has ONE incoming capacity shared by the distinct source cores.
    # Restrict to any set of cores and any demand-label tail.
    for bits in range(1,1<<len(cc)):
        J=[c for j,c in enumerate(cc) if bits>>j&1]
        for tau in sorted(set(s)):
            need=sum(c['m']*sum(tau<=d<=c['r'] for d in s) for c in J)
            if not need:continue
            by_receiver=[min(caps[v],sum(c['m'] for c in J if c['r']>=tau and v in c['eligible'])) for v in range(b)]
            available=sum(by_receiver);checks+=1
            if available<need:
                failures.append({'cores':[c['r'] for c in J],'label_tail':tau,'demand':need,'capacity':available,'receiver_caps':by_receiver})
    return checks,failures

def labelled_joint_cuts(p):
    cc=cores(p);s=p['s'];b=p['b'];q=p['q'];rho=p['rho']
    caps=[max(0,r+b-p['a']-1) for r in rho]
    saturated=[q[v]==sum(d<=rho[v] for d in s) for v in range(b)]
    values=sorted({d for d in s if any(d<=c['r'] for c in cc)})
    checks=0;failures=[]
    for cbits in range(1,1<<len(cc)):
        J=[c for j,c in enumerate(cc) if cbits>>j&1]
        for dbits in range(1,1<<len(values)):
            ds=[d for j,d in enumerate(values) if dbits>>j&1]
            need=sum(c['m']*sum(d<=c['r'] and d in ds for d in s) for c in J)
            if not need:continue
            available=[]
            for v in range(b):
                cap=0
                for d in ds:
                    if saturated[v] and d<=rho[v]:continue
                    mass=sum(c['m'] for c in J if d<=c['r'] and v in c['eligible'])
                    cap=max(cap,min(caps[v],mass))
                available.append(cap)
            checks+=1
            if sum(available)<need:
                failures.append({'cores':[c['r'] for c in J],'demand_values':ds,'demand':need,'capacity':sum(available),'receiver_caps':available,'saturated_receivers':[v for v in range(b) if saturated[v]]})
    return checks,failures

def fractional_cost(caps,loss,need):
    if sum(caps)<need:return None
    cost=Fraction(0);left=need
    for i in sorted(range(len(caps)),key=lambda i:Fraction(loss[i],caps[i])):
        amount=min(left,caps[i]);cost+=Fraction(amount*loss[i],caps[i]);left-=amount
        if not left:break
    return cost

def weighted_threshold_cuts(p):
    checks=0;failures=[]
    for core in cores(p):
        r,h,m=core['r'],core['h'],core['m'];V=core['eligible']
        caps=[min(m,p['rho'][v]+p['b']-p['a']-1) for v in V]
        taus=sorted({s for s in p['s'] if s>r})
        if len(taus)<2:continue
        budget=[sum(q for q,rho in zip(p['q'],p['rho']) if rho>=tau)-sum(s for s in p['s'] if s>=tau) for tau in taus]
        loss=[[max(0,p['q'][v]-r) if p['rho'][v]>=tau else 0 for v in V] for tau in taus]
        # A bounded discovery family; each accepted contradiction is exact.
        weights=[tuple(1 for _ in taus)]
        for i,j in combinations(range(len(taus)),2):
            for x,y in product(range(1,5),repeat=2):
                w=[0]*len(taus);w[i]=x;w[j]=y;weights.append(tuple(w))
        for w in sorted(set(weights)):
            combined=[sum(w[j]*loss[j][i] for j in range(len(taus))) for i in range(len(V))]
            B=sum(x*y for x,y in zip(w,budget));lower=fractional_cost(caps,combined,h*m);checks+=1
            if lower is None or lower>B:
                failures.append({'core':r,'thresholds':taus,'weights':w,'budget':B,'minimum_fractional_loss':None if lower is None else [lower.numerator,lower.denominator]})
    return checks,failures

def main():
    profiles=json.loads((Path(__file__).parent/'RESCUE_PROFILES.json').read_text())
    output=[];joint_checks=weighted_checks=labelled_checks=0
    for p in profiles:
        jc,jf=joint_cuts(p);wc,wf=weighted_threshold_cuts(p);lc,lf=labelled_joint_cuts(p)
        joint_checks+=jc;weighted_checks+=wc
        labelled_checks+=lc
        output.append({'layer':p['layer'],'state_id':p['state_id'],'cores':cores(p),'joint_failures':jf,'weighted_failures':wf,'labelled_joint_failures':lf})
    result={'scope':'124 preserved fixed-q rescue witnesses; not a whole-state enumeration','profiles':len(profiles),'joint_checks':joint_checks,'weighted_checks':weighted_checks,'labelled_checks':labelled_checks,'joint_rejected':[r['state_id'] for r in output if r['joint_failures']],'weighted_rejected':[r['state_id'] for r in output if r['weighted_failures']],'labelled_joint_rejected':[r['state_id'] for r in output if r['labelled_joint_failures']],'results':output}
    (Path(__file__).parent/'JOINT_CORE_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2))

if __name__=='__main__':main()
