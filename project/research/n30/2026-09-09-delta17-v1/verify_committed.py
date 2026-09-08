#!/usr/bin/env python3
"""Standard-library verifier for committed n30 Delta17 exact duals."""
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib,json,math,sys

A=12
B=17
T=4

def profiles():
    need=Fraction(B+2*T)
    vals=[Fraction(s*(A+1-2*s),A-s) for s in range(A)]
    tail=[max(vals[i:]) for i in range(A)]
    cur=[]
    def rec(left,lo,score):
        if left==0:
            if score>=need:
                yield cur.copy()
            return
        if score+left*tail[lo] < need:
            return
        for s in range(lo,A):
            if score+vals[s]+(left-1)*tail[s] < need:
                continue
            cur.append(s); yield from rec(left-1,s,score+vals[s]); cur.pop()
    yield from rec(A,0,Fraction())

def residual_bounds(s):
    charge=sum((Fraction(x*(x-1),A-x) for x in s),Fraction())
    return B+math.ceil(charge), min(sum(s)-2*T,comb(A,2)-T)

def early_cut(s,rmax):
    for h in range(2,A):
        high=[x for x in s if x>=h]
        if not high: continue
        zmax=min(B,(rmax-B)//(h-1))
        H=max(high); W=sum(high)
        if H>zmax: return True
        if 2*W > zmax*zmax-zmax+h*(h+1): return True
    return False

def cap_matrix(s):
    ss=sorted(s,reverse=True)
    D=[sum(ss[:k]) for k in range(1,A+1)]
    cap=[
        [min(A-j,sum(x<=j for x in ss[:k])) for j in range(1,A+1)]
        for k in range(1,A+1)
    ]
    return D,cap

def verify(cert):
    s=cert["s"]; rmin,rmax=residual_bounds(s)
    assert cert["rmin"]==rmin and cert["rmax"]==rmax
    scale=cert["scale"]; weights=cert["weights"]; mu=cert["mu"]
    assert isinstance(scale,int) and scale>0
    assert len(weights)==A and all(isinstance(x,int) and x>=0 for x in weights)
    assert isinstance(mu,int)
    D,cap=cap_matrix(s)
    for j in range(A):
        assert mu+sum(weights[k]*cap[k][j] for k in range(A)) <= scale*j
    lhs=sum(weights[k]*D[k] for k in range(A))+B*mu
    rhs=scale*(rmax-B)
    assert lhs>rhs
    assert cert["lhs"]==lhs and cert["rhs"]==rhs
    assert cert["margin"]==lhs-rhs

def main():
    if len(sys.argv)!=3:
        raise SystemExit("verify_committed.py D17_EXACT_DUAL_CERTIFICATES.json D17_KERNEL_REPORT.json")
    cp=Path(sys.argv[1]); rp=Path(sys.argv[2])
    doc=json.loads(cp.read_text()); report=json.loads(rp.read_text())
    semantic=json.dumps(doc,sort_keys=True,separators=(",",":"))
    assert hashlib.sha256(semantic.encode()).hexdigest()==report["dual_certificate_semantic_sha256"]
    pending=[]
    domain=0
    for s in profiles():
        domain+=1
        rmin,rmax=residual_bounds(s)
        if rmin<=rmax and not early_cut(s,rmax):
            pending.append(tuple(s))
    assert domain==1155
    assert len(pending)==18
    certs=doc["certificates"]
    assert len(certs)==18
    assert sorted(tuple(c["s"]) for c in certs)==sorted(pending)
    for c in certs: verify(c)
    print(json.dumps({
        "status":"PASS",
        "charging_domain":domain,
        "pending_after_thresholds":len(pending),
        "exact_duals_verified":len(certs),
        "final_survivors":0
    },sort_keys=True))

if __name__=="__main__":
    main()
