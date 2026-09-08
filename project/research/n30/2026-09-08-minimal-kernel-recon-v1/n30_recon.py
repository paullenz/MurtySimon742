#!/usr/bin/env python3
"""Parameterized early-kernel reconnaissance for Murty-Simon at n=30.

Uses only audited generic ingredients from the n=29 minimal route:
charging-domain enumeration, residual-activity r bounds, threshold capacity,
and the exact source-capacity Hall dual.  It deliberately stops before residual
row enumeration and the corrected-v2 LP.
"""
from fractions import Fraction
from math import comb,lcm
import json
from scipy.optimize import linprog

N=30

def demands(a,b,t):
    need=Fraction(b+2*t)
    vals=[Fraction(x*(a+1-2*x),a-x) for x in range(a)]
    tail=[max(vals[i:]) for i in range(a)]
    cur=[]
    def rec(left,lo,score):
        if left==0:
            if score>=need:yield tuple(cur)
            return
        if score+left*tail[lo]<need:return
        for x in range(lo,a):
            if score+vals[x]+(left-1)*tail[x]<need:continue
            cur.append(x);yield from rec(left-1,x,score+vals[x]);cur.pop()
    yield from rec(a,0,Fraction())

def bounds(s,b,t):
    a=len(s)
    charge=sum((Fraction(x*(x-1),a-x) for x in s),Fraction())
    lo=b+(charge.numerator+charge.denominator-1)//charge.denominator
    hi=min(sum(s)-2*t,comb(a,2)-t)
    return lo,hi

def threshold_certificate(s,b,rmax):
    a=len(s)
    for h in range(2,a):
        high=[x for x in s if x>=h]
        if not high:continue
        zmax=min(b,(rmax-b)//(h-1))
        H=max(high);W=sum(high)
        if H>zmax:return {'kind':'source_count','h':h}
        rhs=zmax*zmax-zmax+h*(h+1)
        if 2*W>rhs:return {'kind':'threshold','h':h}
    return None

def dual_certificate(s,b,rmax):
    a=len(s);ss=sorted(s,reverse=True)
    D=[sum(ss[:k]) for k in range(1,a+1)]
    A=[[min(a-j,sum(x<=j for x in ss[:k])) for j in range(1,a+1)] for k in range(1,a+1)]
    res=linprog([-x for x in D+[b]],
        A_ub=[[A[k][j] for k in range(a)]+[1] for j in range(a)],
        b_ub=list(range(a)),bounds=[(0,None)]*a+[(None,None)],method='highs')
    if not res.success:return None
    y=[max(Fraction(),Fraction(float(x)).limit_denominator(10000)) for x in res.x[:a]]
    mu=min(Fraction(j)-sum(y[k]*A[k][j] for k in range(a)) for j in range(a))
    score=sum(y[k]*D[k] for k in range(a))+b*mu
    if score<=rmax-b:return None
    scale=lcm(mu.denominator,*(x.denominator for x in y))
    yi=[int(x*scale) for x in y];mui=int(mu*scale)
    assert all(mui+sum(yi[k]*A[k][j] for k in range(a))<=scale*j for j in range(a))
    assert sum(yi[k]*D[k] for k in range(a))+b*mui>scale*(rmax-b)
    return {'kind':'dual','scale':scale,'weights':yi,'mu':mui}

def scope(b,m,use_dual=True):
    a=N-1-b;t=m-b*(N-b)
    if a<=0:return {'n':N,'Delta':b,'m':m,'a':a,'b':b,'t':t,'kind':'universal-vertex'}
    counts={'bounds':0,'threshold':0,'source_count':0,'dual':0,'open':0};domain=0
    for s in demands(a,b,t):
        domain+=1;lo,hi=bounds(s,b,t)
        if lo>hi:counts['bounds']+=1;continue
        c=threshold_certificate(s,b,hi)
        if c:counts[c['kind']]+=1;continue
        if use_dual and dual_certificate(s,b,hi):counts['dual']+=1
        else:counts['open']+=1
    return {'n':N,'Delta':b,'m':m,'a':a,'b':b,'t':t,'demand_domain':domain,'counts':counts,'early_survivors':counts['open']}

def main():
    out={'schema':'n30-minimal-early-recon-v1','status':'PASS','scopes':[]}
    # Principal hard scopes.
    for m in (225,226):
        out['scopes'].append(scope(16,m,True))
        out['scopes'].append(scope(17,m,True))
        # For b>=18 the charging domain itself is empty; no LP proposal is needed.
        for b in range(18,29):out['scopes'].append(scope(b,m,False))
    by={(x['Delta'],x['m']):x for x in out['scopes']}
    assert by[17,226]['demand_domain']==250 and by[17,226]['early_survivors']==0
    assert by[17,225]['demand_domain']==1155 and by[17,225]['counts']['dual']==18 and by[17,225]['early_survivors']==0
    assert by[16,226]['demand_domain']==48046 and by[16,226]['early_survivors']==2596
    assert by[16,225]['demand_domain']==67050 and by[16,225]['early_survivors']==5386
    assert all(by[b,m]['demand_domain']==0 for b in range(18,29) for m in (225,226))
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
