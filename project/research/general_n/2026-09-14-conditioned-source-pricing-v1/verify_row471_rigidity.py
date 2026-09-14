#!/usr/bin/env python3
"""Exact hand-arithmetic verifier for row 471 e_L=39,40 rigidity closures."""
from __future__ import annotations
import json
from pathlib import Path

Q=[5,3,4,1,1,6,4,4,5,2,6,7,7,4,2,3,5,3,2,5,2,3,7,3,2]
RHO=[1,1,2,1,1,3,2,1,1,3,3,3,3,3,1,2,3,1,1,3,1,1,2,3,1]
S=[1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3]
BRANCHES={
 39:{'A':[4,4,5,4,4,3,5,4,4,6,3,3,3,4,4,5,4,4,4,4,4,4,5,6,4],
     'charge_upper':225,'charge_lower':224,'forced':{9:4,23:4,13:2},'high_excess':8},
 40:{'A':[4,4,5,4,4,3,5,4,4,6,3,3,3,5,4,5,4,4,4,4,4,4,5,6,4],
     'charge_upper':225,'charge_lower':223,'forced':{9:4,23:3,13:2},'high_excess':7},
}

def min_cost(cap,required):
    inf=10**12;dp=[inf]*(required+1);dp[0]=0
    for qq,cc in zip(Q,cap):
        nd=[inf]*(required+1)
        for have,cost in enumerate(dp):
            if cost>=inf:continue
            for d in range(cc+1):
                h=min(required,have+d)
                nd[h]=min(nd[h],cost+qq*d)
        dp=nd
    return dp[required]

def nested_excess(high_counts,pressures):
    m=max(high_counts,default=0)
    return sum(max([d for h,d in zip(high_counts,pressures) if h>=j]+[0]) for j in range(1,m+1))

def min_required_high_excess(low_slots,pressures):
    qs=[2,3,4] # sources 9,23,13
    best=None;arg=[]
    for k9 in range(qs[0]+1):
      for k23 in range(qs[1]+1):
       for k13 in range(qs[2]+1):
        ks=[k9,k23,k13]
        if sum(ks)>low_slots:continue
        hs=[qq-k for qq,k in zip(qs,ks)]
        val=nested_excess(hs,pressures)
        if best is None or val<best:best=val;arg=[dict(low=ks,high=hs)]
        elif val==best:arg.append(dict(low=ks,high=hs))
    return best,arg

def main():
    assert sum(Q)==96 and sum(S)==49 and sum(RHO)==47
    high_sources=[u for u,r in enumerate(RHO) if r>=3]
    assert high_sources==[5,9,10,11,12,13,16,19,23]
    assert sum(Q[u] for u in high_sources)==45
    report={}
    for eL,b in BRANCHES.items():
        A=b['A'];free=[min(a,r-1) for a,r in zip(A,RHO)];cap=[a-f for a,f in zip(A,free)]
        required=sum(Q)-sum(free)
        assert required==74
        base=min_cost(cap,required)
        assert base==b['charge_lower']
        forced_checks={}
        for u,need in b['forced'].items():
            weakened=cap.copy();weakened[u]=need-1
            bound=min_cost(weakened,required)
            assert bound>b['charge_upper']
            forced_checks[str(u)]=dict(required_pressure=need,contrary_min_charge=bound)
        # Twelve high labels all have demand 3. Their total selected incidence is 36+E_high.
        low_slots=sum(Q[u] for u in high_sources)-(36+b['high_excess'])
        assert low_slots==eL-38
        pressures=[b['forced'][9],b['forced'][23],b['forced'][13]]
        min_high,args=min_required_high_excess(low_slots,pressures)
        assert min_high>b['high_excess']
        report[str(eL)]=dict(receiver_min_charge=base,source_price_upper=b['charge_upper'],
                            forced_pressure=forced_checks,high_source_low_slots=low_slots,
                            available_high_excess=b['high_excess'],minimum_required_high_excess=min_high,
                            minimizing_low_allocations=args,contradiction=f'{min_high}>{b["high_excess"]}')
    out=dict(schema='row471-conditioned-rigidity-v1',row=471,closed_e_low=[39,40],reports=report,
             scope='hand arithmetic from conditioned caps, receiver pressure cost, source-price upper and positive-label forcing; profile not fully excluded')
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
