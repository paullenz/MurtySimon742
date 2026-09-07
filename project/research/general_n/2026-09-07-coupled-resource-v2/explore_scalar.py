from fractions import Fraction
from math import sqrt

def bound(a):
 vals=[Fraction(s*(a+1-2*s),a-s) for s in range(a)]
 p=max(vals)
 return a*p,[s for s,v in enumerate(vals) if v==p]
for n in range(25,41):
 target=n*n//4
 out=[]; eq=[]
 for b in range((n+1)//2+1,n-1):
  a=n-1-b;t=target-b*(n-b)
  M,ks=bound(a)
  if b+2*t<=M:out.append(b)
  if b+2*t==M:eq.append((b,a,t,ks))
 print(n,out,'equal',eq)
c=3-2*sqrt(2)
al=(.5+sqrt(c/2))/(1+sqrt(c/2))
print('cutoff',al)
def rgood(a,b,t,r):
 S=r+2*t;q,u=divmod(S,a)
 if q>=a or(q==a-1 and u):return False
 def g(s):return Fraction(s*(s-1),a-s)
 return r-b >= (a-u)*g(q)+(u*g(q+1) if u else 0)
for n in [27,28,29,30,31,32,33,40,50,100]:
 rows=[]
 for b in range((n+1)//2+1,n-1):
  a=n-1-b;t=n*n//4-b*(n-b);L=a*(a-1)//2-t
  kept=[]
  for k in range(a):
   if L < b+k+(a-k-1)*(a-k-2)//2:continue
   rs=[r for r in range(b,L-(a*k+1)//2+1) if rgood(a,b,t,r)]
   if rs:kept.append((k,min(rs),max(rs)))
  if kept:rows.append((b,kept))
 print('new',n,rows)
