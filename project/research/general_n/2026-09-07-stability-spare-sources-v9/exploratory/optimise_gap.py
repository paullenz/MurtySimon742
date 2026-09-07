import math
from scipy.optimize import minimize_scalar,brentq
lam=1-1/math.sqrt(2);alpha=3-2*math.sqrt(2);c=alpha/2

def gap(eta, eps, a=float('inf')):
 B=eta/eps**2; L=lam-eps; R=lam+math.sqrt(eta)-alpha+2*eta; Z=R/L
 return L*(1-B)-Z*(L+B+1/(2*a))-Z*Z/2
for a in [20,50,100,1000,float('inf')]:
 def best(e):
  r=minimize_scalar(lambda ep: -gap(e,ep,a),bounds=(.0001,.20),method='bounded')
  return -r.fun,r.x
 r=brentq(lambda e:best(e)[0],1e-10,.001)
 print(a,r,best(r))
for eta in [1e-5,2e-5,3e-5,5e-5,1e-4]:
 r=minimize_scalar(lambda ep:-gap(eta,ep),bounds=(.001,.20),method='bounded')
 print('sample',eta,r.x,-r.fun)
def gap2(eta, eps, a=float('inf')):
 B=eta/eps**2; L=lam-eps; R=lam+math.sqrt(eta)-alpha+2*eta; Z=R/L
 T=L+B+1/a
 return L*(1-B)-Z*T-max(0,Z-T-1/(2*a))**2/2
for a in [20,50,100,1000,float('inf')]:
 def best(e):
  r=minimize_scalar(lambda ep: -gap2(e,ep,a),bounds=(.0001,.24),method='bounded')
  return -r.fun,r.x
 r=brentq(lambda e:best(e)[0],1e-10,.003)
 print('better',a,r,best(r))
