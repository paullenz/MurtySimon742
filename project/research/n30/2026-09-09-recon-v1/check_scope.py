#!/usr/bin/env python3
from fractions import Fraction
from math import floor

n=30
fan=Fraction(n*n,4)+(Fraction(n*n,1)-Fraction(81,5)*n+56)/320
print('Fan strict upper expression =',fan,'=',float(fan))
print('integer m <=', (fan.numerator-1)//fan.denominator)

for m in (226,225):
    print('\nm =',m)
    for b in range(15,30):
        a=n-1-b
        t=m-b*(n-b)
        if t<=0:
            continue
        lhs=b+2*t
        rhs=((n-b)**2)//4
        print({'Delta':b,'a':a,'t':t,'hindex_lhs':lhs,'hindex_rhs':rhs,'hindex_excludes':lhs>rhs})

# Pointwise charging maxima for the borderline a values.
for a in (14,13,12,11):
    vals=[Fraction(s*(a+1-2*s),a-s) for s in range(a)]
    M=max(vals)
    print('a',a,'pointwise max',M,'sum max',a*M,'argmax',[s for s,v in enumerate(vals) if v==M])
