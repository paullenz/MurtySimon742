#!/usr/bin/env python3
"""Exact profile-level weighted RX2 necessary-condition screen.

For positive-demand zero-slack rows, selected-incidence RX2 gives
  sum_i x_i d_i <= sum_u q_u(rho_u+q_u-1).
Using x_i>=s_i and the exact degree-mass identity sum d_i=2(r+t), this
script computes the exact minimum possible left side and compares it to a
safe independent-source upper bound on the right side.

This is deliberately a weak scalar screen: it drops p/transport coupling and
source-label Hall coupling. Rejection is therefore sound inside the RX-Hall
bridge; survival has no graph meaning.
"""
from pathlib import Path
import argparse,json


def lower_envelope(s,r,dmax):
    # sum s_i d_i = sum s_i^2 + sum s_i R_i; allocate r units of R to
    # cheapest s_i subject to 0<=R_i<=dmax-s_i.
    rem=r; val=sum(x*x for x in s)
    for x in sorted(s):
        take=min(rem,dmax-x)
        val += x*take
        rem -= take
        if rem==0: break
    if rem:
        return None
    return val


def source_upper(s,rho,a):
    # Drop all coupling between sources. q(rho+q-1) is nondecreasing for
    # rho>=1,q>=0, so each source is maximized at its safe local q cap.
    total=0
    qs=[]
    for rh in rho:
        qmax=min(a-rh,sum(1 for x in s if x<=rh))
        total += qmax*(rh+qmax-1)
        qs.append(qmax)
    return total,qs


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--demands-json',type=Path,required=True)
    p.add_argument('--rows',type=Path,required=True)
    p.add_argument('--a',type=int,required=True)
    p.add_argument('--dmax',type=int,required=True)
    p.add_argument('--t',type=int,required=True)
    p.add_argument('--output',type=Path,required=True)
    z=p.parse_args()
    D=json.loads(z.demands_json.read_text())
    hard=[]; rejected=[]; survivors=[]
    hp=0
    for pos,line in enumerate(z.rows.read_text().splitlines()):
        if not line.strip(): continue
        v=list(map(int,line.split())); did,total,rho=v[0],v[1],v[2:]; s=D[did]['s']
        if min(s)<=0 or sum(s)!=sum(rho)+2*z.t: continue
        r=sum(rho); L=lower_envelope(s,r,z.dmax); U,qs=source_upper(s,rho,z.a)
        rec={'hard_position':hp,'position':pos,'demand_id':did,'s':s,'rho':rho,'r':r,'lower':L,'source_upper':U,'gap':L-U if L is not None else None,'qmax':qs}
        hard.append(rec)
        if L is not None and L>U: rejected.append(rec)
        else: survivors.append(rec)
        hp+=1
    out={'schema':'weighted-rx2-profile-screen-v1','scope':{'a':z.a,'dmax':z.dmax,'t':z.t},'hard_rows':len(hard),'rejected':len(rejected),'survivors':len(survivors),'rejected_rows':rejected,'survivor_rows':survivors,'soundness':'RHS independently maximizes every source after dropping p/transport/Hall coupling; rejection only is meaningful.'}
    z.output.parent.mkdir(parents=True,exist_ok=True); z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('rejected_rows','survivor_rows')},sort_keys=True))

if __name__=='__main__': main()
