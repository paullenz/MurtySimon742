#!/usr/bin/env python3
"""Strengthened exact demand preparation for n=30, Delta=16.

Uses only already-audited generic consequences:
- charging;
- residual activity;
- the k=0 / delta(C)>=1 contradiction;
- threshold source-supplement capacity;
- source-capacity Hall dual.

In addition to rejecting impossible profiles, exact feasible dual weights are
used as certified lower bounds on r.  Floating point proposes weights only;
all inequalities used to move r_min are checked with Fraction arithmetic.
"""
from fractions import Fraction
from math import comb,ceil
from pathlib import Path
import argparse,json
from scipy.optimize import linprog

N=30;A=13;B=16

def demands(t):
    need=Fraction(B+2*t)
    vals=[Fraction(x*(A+1-2*x),A-x) for x in range(A)]
    tail=[max(vals[i:]) for i in range(A)]
    cur=[]
    def rec(left,lo,score):
        if left==0:
            if score>=need:yield tuple(cur)
            return
        if score+left*tail[lo]<need:return
        for x in range(lo,A):
            if score+vals[x]+(left-1)*tail[x]<need:continue
            cur.append(x);yield from rec(left-1,x,score+vals[x]);cur.pop()
    yield from rec(A,0,Fraction())

def basic_bounds(s,t):
    charge=sum((Fraction(x*(x-1),A-x) for x in s),Fraction())
    lo=B+(charge.numerator+charge.denominator-1)//charge.denominator
    # k=0 would force B<=A-1-t, false here; hence delta(C)>=1,
    # e(C)>=ceil(A/2), and r<=C(A,2)-t-ceil(A/2).
    assert B>A-1-t
    hi=min(sum(s)-2*t,comb(A,2)-t-ceil(A/2))
    return lo,hi

def threshold_min_r(s):
    """Exact lower bound on r forced by all threshold capacities."""
    best=B
    for h in range(2,A):
        high=[x for x in s if x>=h]
        if not high:continue
        W=sum(high);z=max(high)  # maximum demand needs this many h-heavy sources
        while z<=B and 2*W>z*z-z+h*(h+1):z+=1
        if z>B:return None
        best=max(best,B+z*(h-1))
    return best

def dual_bound(s):
    """Return an exact certified lower bound on r-b from Hall dual weights."""
    ss=sorted(s,reverse=True)
    D=[sum(ss[:k]) for k in range(1,A+1)]
    M=[[min(A-j,sum(x<=j for x in ss[:k])) for j in range(1,A+1)] for k in range(1,A+1)]
    # Variables y_k>=0 and free mu; maximize sum yD+B*mu subject
    # mu+sum y A_{k,j} <= j-1.  linprog minimizes the negative objective.
    res=linprog([-x for x in D+[B]],
        A_ub=[[M[k][j] for k in range(A)]+[1] for j in range(A)],
        b_ub=list(range(A)),bounds=[(0,None)]*A+[(None,None)],method='highs')
    if not res.success:return Fraction(0)
    y=[max(Fraction(),Fraction(float(x)).limit_denominator(10000)) for x in res.x[:A]]
    mu=min(Fraction(j)-sum(y[k]*M[k][j] for k in range(A)) for j in range(A))
    assert all(mu+sum(y[k]*M[k][j] for k in range(A))<=j for j in range(A))
    return sum(y[k]*D[k] for k in range(A))+B*mu

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',type=int,choices=[225,226],required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    t=z.m-16*14;z.output.mkdir(parents=True,exist_ok=True)
    counts={'domain':0,'basic_empty':0,'threshold_empty':0,'dual_empty':0,'retained':0}
    kept=[]
    for s in demands(t):
        counts['domain']+=1;lo,hi=basic_bounds(s,t)
        if lo>hi:counts['basic_empty']+=1;continue
        tl=threshold_min_r(s)
        if tl is None or tl>hi:counts['threshold_empty']+=1;continue
        score=dual_bound(s)
        dlo=B+(score.numerator+score.denominator-1)//score.denominator
        lo=max(lo,tl,dlo)
        if lo>hi:counts['dual_empty']+=1;continue
        kept.append((s,lo,hi));counts['retained']+=1
    with open(z.output/'demands.txt','w') as f:
        f.write(str(len(kept))+'\n')
        for s,lo,hi in kept:f.write(' '.join(map(str,(*s,lo,hi)))+'\n')
    rep={'schema':'n30-d16-strong-prepare-v1','status':'PASS','scope':{'n':30,'Delta':16,'m':z.m,'a':A,'b':B,'t':t},'counts':counts,'retained':len(kept),'uses_deltaC_positive':True,'dual_lower_bounds_exactly_checked':True}
    (z.output/'PREPARE_REPORT.json').write_text(json.dumps(rep,indent=2)+'\n')
    print(json.dumps(rep,sort_keys=True))
if __name__=='__main__':main()
