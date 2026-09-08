#!/usr/bin/env python3
from fractions import Fraction as F
import json

def require(x,msg):
    if not x: raise AssertionError(msg)

sqrt_lo,sqrt_hi=F(141421,100000),F(70711,50000)
require(sqrt_lo*sqrt_lo<2<sqrt_hi*sqrt_hi,'sqrt brackets')
alpha_lo,alpha_hi=F(183,625),F(2929,10000)
eps=F(1,750)
ylo,yhi=F(1307,5000),F(323,1000)
require((alpha_lo-ylo)**2>eps*(1-ylo),'lower y endpoint')
require((yhi-alpha_hi)**2>eps*(1-yhi),'upper y endpoint')
require(3-2*sqrt_hi>F(343,2000),'2c lower bound')
theta=F(227,1000)
flow=(alpha_lo-theta)**2/(1-theta)
require(flow>F(1,180),'low-label dispersion cost')
lowmass=F(6,25)
K=F(343,2000)-2*eps

def Q(y,A=25):
    hcap=theta+F(1,A)
    return y-theta*lowmass-((y-K)**2/theta**2+hcap**2)/2

require(Q(ylo)>0 and Q(yhi)>0,'concave endpoint margins')
beta=F(3063,5000)
q=((beta-F(1,2))/(1-beta))**2
q0=F(264,3125)
require(q>q0,'degree-ratio lower bound')
require(F(3,2)-sqrt_lo-eps<q0,'improved charging coefficient')
cup=F(43,500)
require(F(3,2)-sqrt_lo<cup,'original charging coefficient')
small=[]
for a in range(1,25):
    d=q0*(a+1)**2-F(1,4)-cup*a*a
    require(d>0,'small-a case %d'%a)
    small.append(d)
print(json.dumps({
  'status':'PASS',
  'scope':'exact arithmetic only; graph-theoretic lemmas remain hand proofs',
  'epsilon':str(eps),
  'theta':str(theta),
  'Q_lower_endpoint':str(Q(ylo)),
  'Q_upper_endpoint':str(Q(yhi)),
  'degree_ratio_squared':str(q),
  'small_a_cases':24,
  'small_a_min_margin':str(min(small))
},indent=2))
