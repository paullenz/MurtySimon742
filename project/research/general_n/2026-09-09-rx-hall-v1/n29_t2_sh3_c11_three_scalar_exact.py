#!/usr/bin/env python3
"""Exact three-template replay for all 902 n=29,t=2 RX-Hall frontier profiles.

Standard-library acceptance path: no LP/MIP solver and no floating point.
The global 3-D potential is the exact 11-term primitive potential

  3 B(3,6)+3 B(3,7)+3 B(3,8)+3 B(3,9)
 +4 B(3,10)+4 B(3,11)+4 B(3,12)+4 B(3,13)
 +8 J2 +7 J0 +29 SH3.

Three fixed small rational scalar templates are evaluated by exhaustive finite
minimisation using fractions.Fraction. PASS requires their union to give a
strictly positive potential-certificate gap for every regenerated profile.

Mathematical status: exact finite RX-Hall certificate conditional on the 3-D
potential-certificate lemma and the graph-to-profile bridge. It is not an
unrestricted Murty-Simon proof.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json

BC={(3,6):3,(3,7):3,(3,8):3,(3,9):3,(3,10):4,(3,11):4,(3,12):4,(3,13):4}
J={14:8,16:7};SH3=29
TEMPLATES={
 'T0':{'lambda':Q(12),'c':Q(3),'tau1':Q(48,5),'tau3':Q(4),'tau4':Q(6),'tau5':Q(22,5),'tau7':Q(1,4)},
 'T1':{'lambda':Q(12),'c':Q(13,2),'mu+':Q(1),'tau2':Q(13,5),'tau3':Q(43,4),'tau4':Q(13,2),'tau5':Q(7,2),'tau7':Q(2,3)},
 'T2':{'lambda':Q(12),'c':Q(10),'tau2':Q(46,3),'tau4':Q(19,4),'tau5':Q(14,3),'tau6':Q(5,4),'tau7':Q(1,5)},
}

def phi(d,h,scoord):
 v=16-h;ans=0
 for (D,V),w in BC.items():
  if d>=D and v>=V:ans+=w
 for K,w in J.items():
  if d+v>=K:ans+=w
 if scoord>=3:ans+=SH3
 return Q(ans)
def tterm(r,q,p,j):return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def load(dp,rp):
 D=json.loads(Path(dp).read_text());out=[]
 for line in Path(rp).read_text().splitlines():
  if not line.strip():continue
  z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
  if min(s)>0 and sum(s)==sum(rho)+4:out.append({'s':s,'rho':rho,'demand_id':did})
 return out
def rat(x):return [x.numerator,x.denominator]

def gaps(P,th):
 lam=th.get('lambda',Q(0));c=th.get('c',Q(0));mp=th.get('mu+',Q(0));mm=th.get('mu-',Q(0));taus={j:th.get(f'tau{j}',Q(0)) for j in range(1,13)}
 ell={s:min(lam*R+c*x+x*phi(R+s,R+x,s) for R in range(10-s+1) for x in range(s,16-R+1)) for s in range(1,11)}
 sig={}
 # qmax depends on each profile, so cache by (rho,qmax)
 for pf in P:
  for r in set(pf['rho']):
   qm=min(12-r,sum(si<=r for si in pf['s']));key=(r,qm)
   if key not in sig:
    sig[key]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*phi(r+q-1,q+p,r)
                 for q in range(qm+1) for p in range(min(r+3,15-q)+1))
 out=[]
 for pf in P:
  sc=Counter(pf['s']);rc=Counter(pf['rho'])
  g=sum(n*ell[s] for s,n in sc.items())
  for r,n in rc.items():
   qm=min(12-r,sum(si<=r for si in pf['s']));g+=n*sig[(r,qm)]
  g-=lam*sum(pf['rho']);out.append(g)
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=load(z.demands_json,z.rows)
 if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
 masks={};summary={}
 for name,th in TEMPLATES.items():
  gs=gaps(P,th);mask=[g>0 for g in gs];masks[name]=mask;pos=[g for g in gs if g>0]
  summary[name]={'coverage':sum(mask),'minimum_positive_gap':rat(min(pos)),'maximum_positive_gap':rat(max(pos)),'theta':{k:rat(v) for k,v in th.items()}}
 union=[any(masks[k][i] for k in masks) for i in range(902)];missing=[i for i,x in enumerate(union) if not x]
 mult=Counter(sum(masks[k][i] for k in masks) for i in range(902))
 unique={}
 for name in TEMPLATES:
  unique[name]=[i for i in range(902) if masks[name][i] and not any(masks[o][i] for o in TEMPLATES if o!=name)]
 out={'schema':'n29-t2-sh3-c11-three-scalar-exact-v1','status':'PASS' if not missing else 'FAIL','profiles':902,'template_count':3,'covered':sum(union),'missing_indices':missing,'coverage_multiplicity':{str(k):v for k,v in sorted(mult.items())},'unique_indices':unique,'templates':summary,'primitive_potential':{'BC':{str(k):v for k,v in BC.items()},'J2':8,'J0':7,'SH3':29,'generator_count':11,'weight_sum':72},'exact_fraction_arithmetic':True,'uses_lp_solver':False,'floating_point_used':False,'interpretation':'Three fixed small rational scalar templates plus one fixed 11-term primitive 3-D Hall potential give exact strict potential-certificate gaps for all 902 regenerated n29,t2 frontier profiles.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
 if missing:raise SystemExit(1)
if __name__=='__main__':main()
