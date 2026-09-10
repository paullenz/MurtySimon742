#!/usr/bin/env python3
"""Exact lower bound of two scalar templates for the fixed n=30,t=1 3-D potential.

Profiles 0 and 2 from the seven preserved hard states cannot share a single
nonnegative scalar template even if the required common certificate gap is only
>=0.  This script rebuilds that two-profile system and checks one fixed sparse
rational Farkas certificate.  Combined with n30_t1_two_rational_templates_exact.py,
which gives an exact two-template cover, this proves template-count minimum 2
within this fixed-potential model.

Standard-library exact rational arithmetic only; no LP/MIP solver participates
in acceptance.
"""
from fractions import Fraction as Q
from collections import Counter
import json
A=13;B=16;DMAX=11
PROFILES=[
 {'s':[1,1,2,2,3,3,3,3,3,3,3,3,3],'rho':[1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3]},
 {'s':[1,2,2,2,2,2,3,3,3,3,3,3,3],'rho':[1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,3]},
]
BC={(1,7):7,(1,10):11,(1,12):5,(1,13):21,(1,14):29,(1,15):39,(2,12):6,(3,8):5,(3,9):8,(3,11):11}
J={15:17,16:8};SH3=39
COMP=['lambda','c','mu+','mu-']+[f'tau{j}' for j in range(1,14)]
CERT=[(9,2818,56969),(121,2818,56969),(276,12681,56969),(324,11272,56969),(349,1409,56969),(370,7277,56969),(397,777,56969),(415,1809,56969),(419,1409,56969),(429,10,56969),(436,2005,56969),(541,10075,56969),(660,5020,170907),(696,37295,170907),(739,16120,56969),(770,4030,56969),(796,5631,56969),(817,6459,56969),(845,2015,56969)]
def phi(d,h,s):
 v=B-h;ans=sum(w for (D,V),w in BC.items() if d>=D and v>=V)+sum(w for K,w in J.items() if d+v>=K)
 if s>=2:ans+=SH3
 return ans
def tterm(r,q,p,j):return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def system():
 names=list(COMP);rows=[];rhs=[]
 def add(n):names.append(n);return len(names)-1
 for ii,pf in enumerate(PROFILES):
  sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={s:add(('ell',ii,s)) for s in sorted(sc)};sigs={r:add(('sig',ii,r)) for r in sorted(rc)}
  for s,e in ells.items():
   for R in range(DMAX-s+1):
    for x in range(s,B-R+1):rows.append({e:1,0:-R,1:-x});rhs.append(x*phi(R+s,R+x,s))
  for r,sg in sigs.items():
   qm=min(A-r,sum(si<=r for si in pf['s']))
   for q in range(qm+1):
    for p in range(min(r+B-A-1,B-1-q)+1):
     row={sg:1,2:-(q-p),3:(q-p),1:q}
     for j in range(1,14):
      tt=tterm(r,q,p,j)
      if tt:row[3+j]=row.get(3+j,0)-tt
     rows.append(row);rhs.append(-q*phi(r+q-1,q+p,r))
  row={0:sum(pf['rho'])}
  for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
  for r,n in rc.items():row[sigs[r]]=row.get(sigs[r],0)-n
  rows.append(row);rhs.append(0)
 return names,rows,rhs
def main():
 names,rows,rhs=system();coeff=[Q(0) for _ in names];br=Q(0)
 for ri,num,den in CERT:
  assert 0<=ri<len(rows);y=Q(num,den);assert y>0;br+=y*rhs[ri]
  for j,a in rows[ri].items():coeff[j]+=y*a
 scalar_count=len(COMP);freebad=[(j,names[j],str(coeff[j])) for j in range(scalar_count,len(names)) if coeff[j]!=0];scalarbad=[(j,names[j],str(coeff[j])) for j in range(scalar_count) if coeff[j]<0]
 assert br==Q(-1);assert not freebad;assert not scalarbad
 out={'schema':'n30-t1-two-template-lower-bound-exact-v1','status':'PASS','profiles':[0,2],'required_common_gap':'nonnegative (>=0)','rows':len(rows),'variables':len(names),'certificate_support':len(CERT),'combined_rhs':[br.numerator,br.denominator],'free_column_nonzero_count':0,'negative_scalar_coefficient_count':0,'nonzero_scalar_coefficients':{str(names[j]):[coeff[j].numerator,coeff[j].denominator] for j in range(scalar_count) if coeff[j]!=0},'certificate_arithmetic':'fractions.Fraction exact rational','uses_lp_solver':False,'floating_point_used':False,'conclusion':'Hard profiles 0 and 2 cannot share one scalar template under the fixed n30,t1 13-term potential; together with the exact two-template cover this gives minimum template count 2 within the fixed-potential model.'}
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
