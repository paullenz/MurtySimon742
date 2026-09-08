#!/usr/bin/env python3
"""Fresh N29 Delta16 demand generation and exact early pruning. No project imports."""
from fractions import Fraction
from math import comb,lcm
import json,argparse
from pathlib import Path
from scipy.optimize import linprog

def bounds(s,b,t):
    a=len(s);g=sum((Fraction(x*(x-1),a-x) for x in s),Fraction())
    lo=b+(g.numerator+g.denominator-1)//g.denominator
    return lo,min(sum(s)-2*t,comb(a,2)-t)

def demands(a,b,t):
    need=Fraction(b+2*t);vals=[Fraction(x*(a+1-2*x),a-x) for x in range(a)];tail=[max(vals[i:]) for i in range(a)];cur=[]
    def rec(left,lo,score):
        if not left:
            if score>=need:yield cur.copy()
            return
        if score+left*tail[lo]<need:return
        for x in range(lo,a):
            if score+vals[x]+(left-1)*tail[x]<need:continue
            cur.append(x);yield from rec(left-1,x,score+vals[x]);cur.pop()
    yield from rec(a,0,Fraction())

def pair_capacity(a,k,h,z):
    K=a-k+h;low=min(k,K,a-h);high=min(k,a-h);best=0
    for p in range(z+1):
        P=p*z-p*(p+1)//2
        if p and not(a-h>=K+1 and p*(K+1)<=P):continue
        best=max(best,(z-p)*low+min(p*high,P))
    return best

def support_cut(s,b,rmax):
    a=len(s)
    for h in range(2,a):
        high=[x for x in s if x>=h]
        if not high:continue
        zmax=min(b,(rmax-b)//(h-1))
        if max(high)>zmax:return {'kind':'source_count','h':h,'zmax':zmax}
        cap=max(pair_capacity(a,len(high),h,z) for z in range(zmax+1))
        if sum(high)>cap:return {'kind':'support','h':h,'zmax':zmax,'demand':sum(high),'capacity':cap}
    return None

def dual_cut(s,b,rmax):
    a=len(s);ss=sorted(s,reverse=True);D=[sum(ss[:k]) for k in range(1,a+1)]
    A=[[min(a-j,sum(x<=j for x in ss[:k])) for j in range(1,a+1)] for k in range(1,a+1)]
    res=linprog([-x for x in D+[b]],A_ub=[[A[k][j] for k in range(a)]+[1] for j in range(a)],b_ub=list(range(a)),bounds=[(0,None)]*a+[(None,None)],method='highs')
    if not res.success:return None
    y=[max(Fraction(),Fraction(float(x)).limit_denominator(10000)) for x in res.x[:a]]
    mu=min(Fraction(j)-sum(y[k]*A[k][j] for k in range(a)) for j in range(a));score=sum(y[k]*D[k] for k in range(a))+b*mu
    if score<=rmax-b:return None
    scale=lcm(mu.denominator,*(x.denominator for x in y));yi=[int(x*scale) for x in y];mui=int(mu*scale)
    assert all(mui+sum(yi[k]*A[k][j] for k in range(a))<=scale*j for j in range(a))
    assert sum(yi[k]*D[k] for k in range(a))+b*mui>scale*(rmax-b)
    return {'kind':'dual','scale':scale,'weights':yi,'mu':mui}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--t',type=int,choices=[2,3],required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();a=12;b=16;t=z.t;z.output.mkdir(parents=True,exist_ok=True)
    counts={};kept=[];domain=0
    for s in demands(a,b,t):
        domain+=1;lo,hi=bounds(s,b,t);rec={'s':s,'rmin':lo,'rmax':hi}
        if lo>hi:cert={'kind':'bounds'}
        else:cert=support_cut(s,b,hi) or dual_cut(s,b,hi) or {'kind':'OPEN'}
        counts[cert['kind']]=counts.get(cert['kind'],0)+1
        if cert['kind']=='OPEN':kept.append(rec)
    (z.output/'demands.json').write_text(json.dumps(kept,separators=(',',':'))+'\n')
    (z.output/'demands.txt').write_text(str(len(kept))+'\n'+''.join(' '.join(map(str,r['s']+[r['rmin'],r['rmax']]))+'\n' for r in kept))
    rep={'scope':{'n':29,'Delta':16,'m':208+t,'a':a,'b':b,'t':t},'demand_domain':domain,'counts':counts,'retained_demands':len(kept)}
    (z.output/'FRESH_PREPARE_REPORT.json').write_text(json.dumps(rep,indent=2)+'\n');print(json.dumps(rep))
if __name__=='__main__':main()
