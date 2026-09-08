#!/usr/bin/env python3
"""Exact early-kernel replay for n=30, Delta=17.

Scopes:
  m=226 -> (a,b,t)=(12,17,5)
  m=225 -> (a,b,t)=(12,17,4)

Mathematical inputs only:
  * residual activity for t>0;
  * charging inequality;
  * exact threshold-capacity inequality;
  * exact source-capacity Hall dual.

No residual-row enumeration, projected screen, joint propagator, endpoint LP,
or cumulative-threshold LP is used.
"""
from fractions import Fraction
from math import comb, lcm
from pathlib import Path
from collections import Counter
import argparse, hashlib, json, math
from scipy.optimize import linprog

A=12
B=17

def demand_profiles(t):
    need=Fraction(B+2*t)
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
            cur.append(s)
            yield from rec(left-1,s,score+vals[s])
            cur.pop()
    yield from rec(A,0,Fraction())

def residual_bounds(s,t):
    charge=sum((Fraction(x*(x-1),A-x) for x in s),Fraction())
    rmin=B+math.ceil(charge)
    rmax=min(sum(s)-2*t,comb(A,2)-t)
    return rmin,rmax

def threshold_cut(s,rmax):
    for h in range(2,A):
        high=[x for x in s if x>=h]
        if not high:
            continue
        # residual activity: r >= B + z_h(h-1)
        zmax=min(B,(rmax-B)//(h-1))
        H=max(high); W=sum(high)
        if H>zmax:
            return {
                "kind":"source_count","h":h,"H":H,"zmax":zmax,
                "rmax":rmax
            }
        rhs=zmax*zmax-zmax+h*(h+1)
        lhs=2*W
        if lhs>rhs:
            return {
                "kind":"threshold","h":h,"W":W,"zmax":zmax,
                "lhs":lhs,"rhs":rhs,"margin":lhs-rhs,"rmax":rmax
            }
    return None

def exact_dual(s,rmax):
    """Return an exactly verified source-capacity Hall dual, if found.

    n_j = number of sources of residual degree j, j=1..A.
    For each largest-demand prefix k, D_k is required selected incidence.
    A[k,j] is an upper bound on what one residual-j source can supply.

      D_k <= sum_j A[k,j] n_j,
      sum_j n_j = B,
      sum_j (j-1)n_j <= rmax-B.

    Floating point proposes dual weights only. Acceptance is exact integer
    arithmetic in the assertions below.
    """
    ss=sorted(s,reverse=True)
    D=[sum(ss[:k]) for k in range(1,A+1)]
    cap=[
        [min(A-j,sum(x<=j for x in ss[:k])) for j in range(1,A+1)]
        for k in range(1,A+1)
    ]

    res=linprog(
        [-x for x in D+[B]],
        A_ub=[[cap[k][j] for k in range(A)]+[1] for j in range(A)],
        b_ub=list(range(A)),
        bounds=[(0,None)]*A+[(None,None)],
        method="highs"
    )
    if not res.success:
        return None

    y=[
        max(Fraction(),Fraction(float(x)).limit_denominator(10000))
        for x in res.x[:A]
    ]
    mu=min(
        Fraction(j)-sum(y[k]*cap[k][j] for k in range(A))
        for j in range(A)
    )
    score=sum(y[k]*D[k] for k in range(A))+B*mu
    if score<=rmax-B:
        return None

    scale=lcm(mu.denominator,*(x.denominator for x in y))
    weights=[int(x*scale) for x in y]
    mui=int(mu*scale)

    # Exact proof event.
    for j in range(A):
        assert mui+sum(weights[k]*cap[k][j] for k in range(A)) <= scale*j
    lhs=sum(weights[k]*D[k] for k in range(A))+B*mui
    rhs=scale*(rmax-B)
    assert lhs>rhs

    return {
        "kind":"dual","scale":scale,"weights":weights,"mu":mui,
        "lhs":lhs,"rhs":rhs,"margin":lhs-rhs,"rmax":rmax
    }

def run_scope(t):
    counts=Counter()
    duals=[]
    domain=0
    threshold_margins=[]
    opens=[]
    for s in demand_profiles(t):
        domain+=1
        rmin,rmax=residual_bounds(s,t)
        if rmin>rmax:
            cert={"kind":"bounds"}
        else:
            cert=threshold_cut(s,rmax)
            if cert is None:
                cert=exact_dual(s,rmax)
            if cert is None:
                cert={"kind":"OPEN"}
        counts[cert["kind"]]+=1
        if cert["kind"]=="threshold":
            threshold_margins.append(cert["margin"])
        elif cert["kind"]=="dual":
            rec={"s":s,"rmin":rmin,"rmax":rmax}
            rec.update(cert)
            duals.append(rec)
        elif cert["kind"]=="OPEN":
            opens.append({"s":s,"rmin":rmin,"rmax":rmax})
    return {
        "t":t,
        "charging_feasible_profiles":domain,
        "counts":dict(counts),
        "final_survivors":len(opens),
        "minimum_threshold_margin":min(threshold_margins) if threshold_margins else None,
        "minimum_dual_margin":min((x["margin"] for x in duals),default=None),
        "duals":duals,
        "opens":opens,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,required=True)
    z=ap.parse_args()
    z.output.mkdir(parents=True,exist_ok=True)

    scopes={"226":run_scope(5),"225":run_scope(4)}
    assert scopes["226"]["charging_feasible_profiles"]==250
    assert scopes["226"]["counts"]=={"threshold":250}
    assert scopes["226"]["final_survivors"]==0
    assert scopes["225"]["charging_feasible_profiles"]==1155
    assert scopes["225"]["counts"]=={"threshold":1070,"source_count":67,"dual":18}
    assert scopes["225"]["final_survivors"]==0
    assert len(scopes["225"]["duals"])==18

    dual_doc={
        "schema":"n30-d17-source-capacity-duals-v1",
        "date":"2026-09-09",
        "scope":{"n":30,"Delta":17,"m":225,"a":A,"b":B,"t":4},
        "certificates":scopes["225"]["duals"],
    }
    dual_text=json.dumps(dual_doc,indent=2,sort_keys=True)+"\n"
    dual_path=z.output/"D17_EXACT_DUAL_CERTIFICATES.json"
    dual_path.write_text(dual_text)

    report={
        "schema":"n30-d17-early-kernel-v1",
        "date":"2026-09-09",
        "scope":"n=30, Delta=17 at m=226 and m=225",
        "results":{},
        "uses_residual_row_enumeration":False,
        "uses_lp_endpoint_model":False,
        "uses_exact_source_capacity_dual":True,
        "all_duals_exact_integer_verified":True,
        "mathematical_status":"CANDIDATE; independent expert review remains OPEN",
    }
    for m,rec in scopes.items():
        report["results"][m]={
            k:v for k,v in rec.items() if k not in ("duals","opens")
        }
    report["dual_certificate_sha256"]=hashlib.sha256(dual_text.encode()).hexdigest()
    (z.output/"D17_KERNEL_REPORT.json").write_text(
        json.dumps(report,indent=2,sort_keys=True)+"\n"
    )
    print(json.dumps(report,sort_keys=True))

if __name__=="__main__":
    main()
