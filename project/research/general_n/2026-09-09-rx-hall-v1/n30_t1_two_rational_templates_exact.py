#!/usr/bin/env python3
"""Exact two-template replay for the seven hard n=30,t=1 RX-Hall profiles.

Standard library only. No LP/MIP solver and no floating point.

The script evaluates the explicit 13-term primitive monotone 3D potential and
two fixed rational scalar templates. For each profile it computes the optimal
label/source envelope constants by exhaustive finite minimisation and verifies
a strictly positive certificate gap.

Mathematical status: exact certificate for the RX-Hall necessary-condition
profile system, conditional on POTENTIAL_CERTIFICATE_LEMMA_3D.md and the
surrounding graph-to-profile bridge. It is not an unrestricted Murty-Simon
proof and is not needed by the existing fixed n=30 candidate package.
"""
from collections import Counter
from fractions import Fraction
import json

A=13
B=16
DMAX=11

PROFILES=[
 {"hard_position":0,"demand_id":2094,
  "s":[1,1,2,2,3,3,3,3,3,3,3,3,3],
  "rho":[1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3]},
 {"hard_position":1,"demand_id":2309,
  "s":[1,1,3,3,3,3,3,3,3,3,3,3,3],
  "rho":[1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,3]},
 {"hard_position":2,"demand_id":2596,
  "s":[1,2,2,2,2,2,3,3,3,3,3,3,3],
  "rho":[1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3]},
 {"hard_position":3,"demand_id":2701,
  "s":[1,2,2,2,3,3,3,3,3,3,3,3,3],
  "rho":[1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,3]},
 {"hard_position":4,"demand_id":2812,
  "s":[1,2,2,3,3,3,3,3,3,3,3,3,3],
  "rho":[1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,3]},
 {"hard_position":5,"demand_id":2984,
  "s":[1,2,3,3,3,3,3,3,3,3,3,3,3],
  "rho":[1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3]},
 {"hard_position":6,"demand_id":2984,
  "s":[1,2,3,3,3,3,3,3,3,3,3,3,3],
  "rho":[1,1,1,1,1,1,2,2,3,3,3,3,3,3,3,3]},
]

# Primitive global potential:
#   Phi = sum w_{D,V} 1[d>=D,v>=V]
#       + 17 1[d+v>=15] + 8 1[d+v>=16]
#       + 39 1[s>=2].
BC={
 (1,7):7,(1,10):11,(1,12):5,(1,13):21,(1,14):29,(1,15):39,
 (2,12):6,
 (3,8):5,(3,9):8,(3,11):11,
}
J={15:17,16:8}
SH={(2,0):39}

def F(x): return Fraction(x)

TEMPLATE_A={
 "lambda":F(33),"c":F(91)/6,"mu":F(143)/3,
 "tau":{2:F(1),3:F(27)/4,6:F(1)/10,9:F(11)/5},
}
TEMPLATE_B={
 "lambda":F(33),"c":F(76)/5,"mu":F(89)/2,
 "tau":{2:F(17)/8,3:F(41)/5,6:F(1)/10,8:F(9)/10,9:F(3)/2},
}

ASSIGN={0:"A",1:"A",2:"B",3:"B",4:"B",5:"B",6:"B"}
TEMPLATES={"A":TEMPLATE_A,"B":TEMPLATE_B}
EXPECTED_GAPS={
 0:F(27)/5,
 1:F(1)/2,
 2:F(333)/20,
 3:F(7)/10,
 4:F(1369)/20,
 5:F(674)/5,
 6:F(11)/20,
}

def tterm(rho,q,p,j):
    return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

def phi(d,h,scoord):
    v=B-h
    ans=0
    for (D,V),w in BC.items():
        if d>=D and v>=V: ans+=w
    for K,w in J.items():
        if d+v>=K: ans+=w
    for (S,V),w in SH.items():
        if scoord>=S and v>=V: ans+=w
    return F(ans)

def certificate_gap(pf,th):
    sc=Counter(pf["s"])
    rc=Counter(pf["rho"])

    # ell_s <= lambda R + c x + x Phi(s,R+s,b-R-x)
    ell={}
    for s in sc:
        vals=[]
        for R in range(DMAX-s+1):
            for x in range(s,B-R+1):
                vals.append(th["lambda"]*R + th["c"]*x
                            + x*phi(R+s,R+x,s))
        ell[s]=min(vals)

    # sigma_rho <= mu(q-p)-cq+sum tau_j*T_j-q Phi(source)
    sig={}
    for rho in rc:
        vals=[]
        qmax=min(A-rho,sum(si<=rho for si in pf["s"]))
        for q in range(qmax+1):
            pmax=min(rho+B-A-1,B-1-q)
            for p in range(pmax+1):
                z=th["mu"]*(q-p)-th["c"]*q
                for j,tau in th["tau"].items():
                    z += tau*tterm(rho,q,p,j)
                z -= q*phi(rho+q-1,q+p,rho)
                vals.append(z)
        sig[rho]=min(vals)

    gap=(sum(sc[s]*ell[s] for s in sc)
         +sum(rc[r]*sig[r] for r in rc)
         -th["lambda"]*sum(pf["rho"]))
    return gap,ell,sig

def main():
    assert len(BC)+len(J)+len(SH)==13
    weights=list(BC.values())+list(J.values())+list(SH.values())
    from math import gcd
    g=0
    for w in weights:g=gcd(g,w)
    assert g==1
    assert sum(weights)==206

    results=[]
    for pf in PROFILES:
        i=pf["hard_position"]
        name=ASSIGN[i]
        gap,ell,sig=certificate_gap(pf,TEMPLATES[name])
        assert gap==EXPECTED_GAPS[i],(i,gap,EXPECTED_GAPS[i])
        assert gap>0,(i,gap)
        results.append({
          "hard_position":i,
          "demand_id":pf["demand_id"],
          "template":name,
          "gap":str(gap),
          "positive":True,
        })

    print(json.dumps({
      "schema":"n30-t1-two-rational-templates-exact-replay-v1",
      "status":"PASS",
      "solver_used":False,
      "floating_point_used":False,
      "arithmetic":"fractions.Fraction exact rational",
      "profiles":len(PROFILES),
      "global_potential_terms":13,
      "primitive_weight_sum":206,
      "template_count":2,
      "results":results,
      "minimum_gap":str(min(EXPECTED_GAPS.values())),
      "interpretation":"Exact finite certificate for the seven hard n=30,t=1 RX-Hall profiles, conditional on the 3D symbolic potential-certificate lemma and graph-to-profile bridge."
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
