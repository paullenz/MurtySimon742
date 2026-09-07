#!/usr/bin/env python3
"""Exact finite checks supporting, NOT replacing, the symbolic v9 proofs."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product, combinations
from dataclasses import dataclass
import argparse, json, math

@dataclass(frozen=True)
class Q2:
    """Exact a+b sqrt(2); comparison uses rational squares, not floats."""
    a:F=F(0)
    b:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
    def __add__(self,y):
        y=cast(y);return Q2(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return Q2(-self.a,-self.b)
    def __sub__(self,y):return self+-cast(y)
    def __rsub__(self,y):return cast(y)+-self
    def __mul__(self,y):
        y=cast(y);return Q2(self.a*y.a+2*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,y):
        y=cast(y);d=y.a*y.a-2*y.b*y.b
        if d==0:raise ZeroDivisionError
        z=self*Q2(y.a,-y.b);return Q2(z.a/d,z.b/d)
    def __pow__(self,n):
        if n<0: return (1/self)**(-n)
        r=Q2(1)
        for _ in range(n):r=r*self
        return r
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if (a>0)==(b>0):return 1 if a>0 else -1
        q=a*a-2*b*b
        return ((q>0)-(q<0))*(1 if a>0 else -1)
    def __lt__(self,y):return (self-cast(y)).sign()<0
    def __le__(self,y):return (self-cast(y)).sign()<=0
    def __gt__(self,y):return (self-cast(y)).sign()>0
    def __ge__(self,y):return (self-cast(y)).sign()>=0
    def __rtruediv__(self,y):return cast(y)/self
    def __float__(self):return float(self.a)+float(self.b)*math.sqrt(2)
    def serial(self):return {'rational':str(self.a),'sqrt2_coefficient':str(self.b)}
def cast(y):return y if isinstance(y,Q2) else Q2(y)
def require(p,msg):
    if not p:raise ValueError(msg)

def constants():
    rt=Q2(0,1);c=Q2(F(3,2),-1);eta=F(1,5000);cp=c-eta
    lam=1-rt/2;L=F(6,25);B=F(9,125);Z=F(17,30);T=F(44,125)
    require(rt**2==Q2(2),'quadratic field')
    require(rt<F(70711,50000),'sqrt2 upper enclosure')
    require(0<lam-L,'positive demand threshold gap')
    require(F(1,360)<(lam-L)**2,'bad label fraction bound')
    # sqrt(eta)=sqrt(2)/100 exactly.
    R=lam+rt/100-2*cp
    require(R<F(17,125),'residual budget bound')
    require(F(17,125)/L==Z,'source count bound')
    require(L+B+F(1,25)==T,'threshold bound at a>=25')
    gap=L*(1-B)-(Z*Z+T*T)/2
    require(gap==F(239,1125000) and gap>0,'positive final gap')
    blo=F(613168,1000000);bhi=F(613169,1000000)
    # monotone x -> ((x-1/2)/(1-x))^2 on [1/2,1)
    require(((blo-F(1,2))/(1-blo))**2<cp,'new beta lower')
    require(cp<((bhi-F(1,2))/(1-bhi))**2,'new beta upper')
    require(cp>F(1,12),'rounding margin')
    small=[]
    for a in range(1,25):
        b=math.ceil(blo*(a+1)/(1-blo));d=b-a-1;t=d*d//4
        require(d>0 and c*a*a<t,'small-a old charging contradiction')
        small.append(dict(a=a,b_min=b,n_min=a+b+1,t_min=t,gap=(t-c*a*a).serial()))
    pairs=0
    for z in range(101):
        for k in range(z+1):
            for t in (F(0),F(z,3),F(z,2),F(z),F(z+3,2)):
                f=(z-k)*t+k*z-F(k*(k+1),2)
                rhs=(z*z+t*t)/2-(z-t-k)**2/2-F(k,2)
                require(f==rhs and f<=(z*z+t*t)/2,'pair square identity');pairs+=1
    # Exact deficit identity at integer demand values; symbolic proof is in the paper.
    n=0
    for a in range(1,101):
        for s in range(a):
            loss=2*(s-lam*a)**2/(a-s)
            f=F(s*(a-2*s),a-s)
            require(2*c*a-f==loss and 0<=loss,'deficit identity');n+=1
    # A scalar-only near-saturation witness; deliberately NOT a graph.
    M=200;a=35*M;b=56*M;h=10*M;z=14*M;r=z*h+(b-z);S=a*h;t=F(S-r,2)
    require(r>=F(a*h*h,a-h) and r-b==F(a*h*(h-1),a-h),'old scalar witness')
    require(cp*a*a<t and t<c*a*a,'strict improvement scalar witness')
    return dict(all_checks_pass=True,eta=str(eta),c=c.serial(),new_c=cp.serial(),
      beta_interval=[str(blo),str(bhi)],final_rational_gap=str(gap),small_a_cases=small,
      pair_capacity_identity_checks=pairs,deficit_identity_checks=n,
      scalar_witness=dict(a=a,b=b,h=h,z=z,r=r,S=S,t=str(t),is_graph=False,
      satisfies_basic_and_active_scalar_charging=True,satisfies_all_old_graph_constraints=False))

def spare_checks():
    coeffs=0
    for h in range(1,101):
        for j in range(h*h):
            A=F((h-1)*(j+1),h+j+1)
            P=F(h,h+j+1)-F(1,h+1)
            E=F(1,h+1)-F(h,(h+j)*(h+j+1))
            require(min(A,P,E)>=0,'spare coefficients');coeffs+=1
    # Reduced incidence witnesses show the bound is sharp for the reduced premises,
    # not existence of a critical graph or full residual system.
    witnesses=[]
    for h in range(1,11):
        for z in range(h,h*h+h+1):
            ell=(2*h-1)*z//h
            rows=[0]*z
            cols=[]
            for i in range(ell):
                sources=[(i*h+j)%z for j in range(h)]
                require(len(set(sources))==h,'distinct sources')
                for u in sources:rows[u]+=1
                cols.append(sources)
            require(max(rows)<=(2*h-1),'ordinary endpoint bound')
            require(h*ell<=(2*h-1)*z,'spare conclusion')
            witnesses.append(dict(h=h,z=z,labels=ell,max_out=max(rows),exceptional_arcs=0))
    for h in range(2,1001):
        require((2*h-1)*(h+2)//h==2*h+2,'two spare corollary')
    # h+1 formula has the h=1 special case but gives 2h for every h>=1.
    for h in range(1,1001):require((2*h-1)*(h+1)//h==2*h,'one spare corollary')
    return dict(all_checks_pass=True,nonnegative_coefficient_triples=coeffs,
        sharp_reduced_incidence_witnesses=len(witnesses),witnesses=witnesses,
        two_spare_integer_cases=999,one_spare_integer_cases=1000,
        sharpness_for_actual_critical_graphs_claimed=False)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    report={'constants':constants(),'spare_sources':spare_checks(),
      'status':'finite algebra/regression checks; symbolic proofs and graph lifting require mathematical review'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:{a:b for a,b in v.items() if a not in ['small_a_cases','witnesses']} if isinstance(v,dict) else v for k,v in report.items()},indent=2))
if __name__=='__main__':main()
