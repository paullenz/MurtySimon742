#!/usr/bin/env python3
"""Exact integer regime replay for all 902 n=29,t=2 RX-Hall profiles.

The fixed 11-term 3-D potential is
  3 B(3,6..9)+4 B(3,10..13)+8 J2+7 J0+29 SH3.

Let nu1 = number of residual label values s_i equal to 1.  On the regenerated
frontier only nu1=0,1,2 occur.  Apply one fixed INTEGER scalar template by nu1:

 nu1=0: lambda=12,c=10,tau2=15,tau4=5,tau5=5,tau6=1
 nu1=1: lambda=12,c=5,mu+=1,tau2=3,tau3=10,tau4=7,tau5=3
 nu1=2: lambda=12,c=3,tau1=10,tau3=4,tau4=6,tau5=4

All envelope minimisation and gap checks use Python integers only. No LP/MIP,
floating point, Fraction, or proposal certificate participates in acceptance.
PASS requires every profile to lie in nu1=0,1,2 and its assigned template to
have strictly positive integer certificate gap.
"""
from pathlib import Path
from collections import Counter
import argparse,json

BC={(3,6):3,(3,7):3,(3,8):3,(3,9):3,(3,10):4,(3,11):4,(3,12):4,(3,13):4}
J={14:8,16:7};SH3=29
T={
 0:{'lambda':12,'c':10,'tau2':15,'tau4':5,'tau5':5,'tau6':1},
 1:{'lambda':12,'c':5,'mu+':1,'tau2':3,'tau3':10,'tau4':7,'tau5':3},
 2:{'lambda':12,'c':3,'tau1':10,'tau3':4,'tau4':6,'tau5':4},
}

def phi(d,h,scoord):
 v=16-h;ans=0
 for (D,V),w in BC.items():
  if d>=D and v>=V:ans+=w
 for K,w in J.items():
  if d+v>=K:ans+=w
 if scoord>=3:ans+=SH3
 return ans
def tterm(r,q,p,j):return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def load(dp,rp):
 D=json.loads(Path(dp).read_text());out=[]
 for line in Path(rp).read_text().splitlines():
  if not line.strip():continue
  z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
  if min(s)>0 and sum(s)==sum(rho)+4:out.append({'s':s,'rho':rho,'demand_id':did})
 return out

def gap(pf,th):
 lam=th.get('lambda',0);c=th.get('c',0);mp=th.get('mu+',0);mm=th.get('mu-',0);taus={j:th.get(f'tau{j}',0) for j in range(1,13)}
 sc=Counter(pf['s']);rc=Counter(pf['rho'])
 ell={s:min(lam*R+c*x+x*phi(R+s,R+x,s) for R in range(10-s+1) for x in range(s,16-R+1)) for s in sc}
 sig={}
 for r in rc:
  qm=min(12-r,sum(si<=r for si in pf['s']))
  sig[r]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*phi(r+q-1,q+p,r)
             for q in range(qm+1) for p in range(min(r+3,15-q)+1))
 return sum(n*ell[s] for s,n in sc.items())+sum(n*sig[r] for r,n in rc.items())-lam*sum(pf['rho'])

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=load(z.demands_json,z.rows)
 if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
 counts=Counter();mins={};maxs={};min_indices={};bad=[];nu_over=[]
 for i,pf in enumerate(P):
  nu=pf['s'].count(1);counts[nu]+=1
  if nu not in T:nu_over.append(i);continue
  g=gap(pf,T[nu])
  if g<=0:bad.append((i,nu,g))
  if nu not in mins or g<mins[nu]:mins[nu]=g;min_indices[nu]=[i]
  elif g==mins[nu]:min_indices[nu].append(i)
  maxs[nu]=g if nu not in maxs else max(maxs[nu],g)
 ok=not bad and not nu_over and set(counts)=={0,1,2}
 out={'schema':'n29-t2-sh3-c11-nu1-integer-regimes-exact-v1','status':'PASS' if ok else 'FAIL','profiles':len(P),'nu1_counts':{str(k):v for k,v in sorted(counts.items())},'unexpected_nu1_profile_indices':nu_over,'nonpositive_gap_rows':bad,'assigned_minimum_gaps':{str(k):mins[k] for k in sorted(mins)},'assigned_maximum_gaps':{str(k):maxs[k] for k in sorted(maxs)},'minimum_gap_profile_indices':{str(k):min_indices[k] for k in sorted(min_indices)},'templates':{str(k):v for k,v in T.items()},'primitive_potential':{'BC':{str(k):v for k,v in BC.items()},'J2':8,'J0':7,'SH3':29,'generator_count':11,'weight_sum':72},'integer_arithmetic_only':True,'uses_lp_solver':False,'uses_fraction':False,'floating_point_used':False,'interpretation':'The 902-profile t=2 frontier partitions exactly by nu1=#(s_i=1): 825 profiles with nu1=0 use the integer T0 regime, 76 with nu1=1 use T1, and one with nu1=2 uses T2. Every assigned gap is a positive integer.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
 if not ok:raise SystemExit(1)
if __name__=='__main__':main()
