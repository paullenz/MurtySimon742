#!/usr/bin/env python3
from fractions import Fraction as F
import json

def require(x,msg):
    if not x: raise AssertionError(msg)

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def deriv(p):
    return trim([F(i)*p[i] for i in range(1,len(p))] or [F(0)])

def divrem(a,b):
    a=trim(a); b=trim(b)
    if b==[0]: raise ZeroDivisionError
    q=[F(0)]*max(1,len(a)-len(b)+1); r=a[:]
    while len(r)>=len(b) and r!=[0]:
        k=len(r)-len(b); c=r[-1]/b[-1]; q[k]+=c
        for i in range(len(b)): r[i+k]-=c*b[i]
        r=trim(r)
    return trim(q),trim(r)

def sturm(p):
    s=[trim(p),deriv(p)]
    while True:
        _,r=divrem(s[-2],s[-1])
        if r==[0]: return s
        s.append([-x for x in r])

def peval(p,x):
    z=F(0)
    for c in reversed(p): z=z*x+c
    return z

def variations(seq,x):
    signs=[]
    for p in seq:
        v=peval(p,x)
        if v>0: signs.append(1)
        elif v<0: signs.append(-1)
    return sum(a!=b for a,b in zip(signs,signs[1:]))

sqrt_lo,sqrt_hi=F(141421,100000),F(70711,50000)
require(sqrt_lo**2<2<sqrt_hi**2,'sqrt brackets')
alpha_lo,alpha_hi=F(183,625),F(2929,10000)
eps=F(1,300); L=F(121,500); U=F(341,1000)
require((alpha_lo-L)**2-eps*(1-L)==F(253,4687500),'lower y margin')
require((U-alpha_hi)**2-eps*(1-U)==F(35083,300000000),'upper y margin')
require(3-2*sqrt_hi>F(343,2000),'2c lower')

# P coefficients in ascending order.
P=list(map(F,[
 -723532716,
 20854785690,
 -290644878645,
 2234773372000,
 -9119933700000,
 18813120000000,
 -17654500000000,
 6000000000000,
]))
S=sturm(P)
vL,vU=variations(S,L),variations(S,U)
require(vL==4 and vU==4 and vL-vU==0,'Sturm root count')
require(peval(P,F(3,10))==F(4661739,20),'positive sample value')

beta=F(1529,2500)
q=((beta-F(1,2))/(1-beta))**2
q0=F(516,6250)
require(q==F(77841,942841) and q>q0,'degree ratio')
require(F(3,2)-sqrt_lo-eps<q0,'improved coefficient')
cup=F(8579,100000)
require(F(3,2)-sqrt_lo<cup,'original c upper')
small=[]
for a in range(2,50):
    d=q0*(a+1)**2-F(1,4)-cup*a*a
    require(d>0,'small-a %d'%a)
    small.append(d)
require(small[0]==F(3747,25000),'a=2 margin')
require(small[-1]==F(16821,100000),'a=49 margin')

print(json.dumps({
  'status':'PASS',
  'scope':'exact algebra only; universal graph-theoretic lemmas remain hand proofs',
  'epsilon':str(eps),
  'y_interval':[str(L),str(U)],
  'sturm_sequence_length':len(S),
  'sturm_variations':[vL,vU],
  'roots_in_interval':vL-vU,
  'P_at_3_over_10':str(peval(P,F(3,10))),
  'degree_ratio_squared':str(q),
  'small_a_cases':48,
  'small_a_min_margin':str(min(small))
},indent=2))
