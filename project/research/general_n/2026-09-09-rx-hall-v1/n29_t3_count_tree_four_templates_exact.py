#!/usr/bin/env python3
"""Exact deterministic count-tree replay for the n=29,t=3 RX-Hall frontier.

Global potential:
    F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9).

The 94 regenerated profiles are assigned by three elementary counts:
  r1 = number of rho_u equal to 1,
  s5 = number of s_i equal to 5,
  s1 = number of s_i equal to 1.

Decision tree:
  if r1 <= 8:
      if s5 == 0: use A530
      else:        use A38
  else:
      if s1 == 0: use A1
      else:        use A0

All envelope minimisation and gap checks use fractions.Fraction.  No LP/MIP or
floating point participates in acceptance. PASS requires every regenerated
profile to be assigned and its fixed rational template to have positive gap.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json

W={(3,0):6,(3,5):4,(3,9):3}
T={
 'A0': {'lambda':Q(140,81),'tau3':Q(29,12),'tau4':Q(23,12)},
 'A1': {'lambda':Q(9,5),'c':Q(16,3),'tau2':Q(23,3)},
 'A38':{'lambda':Q(9,5),'c':Q(141,70),'tau2':Q(841,210),'tau3':Q(1682,1155)},
 'A530':{'lambda':Q(9,5),'c':Q(103,144),'tau2':Q(1513,720),'tau3':Q(3101,1440),'tau4':Q(109,144)},
}
def F(d,v):return sum(w for (D,V),w in W.items() if d>=D and v>=V)
def tterm(r,q,p,j):return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def load(dp,rp):
 D=json.loads(Path(dp).read_text());out=[]
 for line in Path(rp).read_text().splitlines():
  if not line.strip():continue
  z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
  if min(s)>0 and sum(s)==sum(rho)+6:out.append({'s':s,'rho':rho,'demand_id':did})
 return out
def rat(x):return [x.numerator,x.denominator]
def choose(pf):
 r1=pf['rho'].count(1);s5=pf['s'].count(5);s1=pf['s'].count(1)
 if r1<=8:return 'A530' if s5==0 else 'A38'
 return 'A1' if s1==0 else 'A0'
def gap(pf,th):
 lam=th.get('lambda',Q(0));c=th.get('c',Q(0));mp=th.get('mu+',Q(0));mm=th.get('mu-',Q(0));taus={j:th.get(f'tau{j}',Q(0)) for j in range(1,13)}
 sc=Counter(pf['s']);rc=Counter(pf['rho'])
 ell={s:min(lam*R+c*x+x*F(R+s,16-R-x) for R in range(10-s+1) for x in range(s,16-R+1)) for s in sc}
 sig={}
 for r in rc:
  qm=min(12-r,sum(si<=r for si in pf['s']))
  sig[r]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*F(r+q-1,16-q-p)
             for q in range(qm+1) for p in range(min(r+3,15-q)+1))
 return sum(n*ell[s] for s,n in sc.items())+sum(n*sig[r] for r,n in rc.items())-lam*sum(pf['rho'])
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=load(z.demands_json,z.rows)
 if len(P)!=94:raise SystemExit(f'expected 94 profiles, got {len(P)}')
 counts=Counter();mins={};maxs={};minidx={};bad=[];details=Counter()
 for i,pf in enumerate(P):
  name=choose(pf);g=gap(pf,T[name]);counts[name]+=1;details[(pf['rho'].count(1)<=8,pf['s'].count(5)==0,pf['s'].count(1))]+=1
  if g<=0:bad.append((i,name,rat(g)))
  if name not in mins or g<mins[name]:mins[name]=g;minidx[name]=[i]
  elif g==mins[name]:minidx[name].append(i)
  maxs[name]=g if name not in maxs else max(maxs[name],g)
 ok=not bad and counts==Counter({'A38':73,'A1':11,'A530':9,'A0':1})
 out={'schema':'n29-t3-count-tree-four-templates-exact-v1','status':'PASS' if ok else 'FAIL','profiles':94,'global_potential':{'B(3,0)':6,'B(3,5)':4,'B(3,9)':3},'decision_tree':'if rho_ones<=8: A530 iff s_fives=0 else A38; otherwise A1 iff s_ones=0 else A0','leaf_counts':dict(counts),'assigned_minimum_gaps':{k:rat(v) for k,v in mins.items()},'assigned_maximum_gaps':{k:rat(v) for k,v in maxs.items()},'minimum_gap_profile_indices':minidx,'nonpositive_assigned_gaps':bad,'templates':{k:{x:rat(y) for x,y in v.items()} for k,v in T.items()},'exact_fraction_arithmetic':True,'uses_lp_solver':False,'floating_point_used':False,'interpretation':'All 94 t=3 frontier profiles are assigned to one exact rational template by a depth-2 tree using only count(rho=1), presence of s=5, and presence of s=1.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
 if not ok:raise SystemExit(1)
if __name__=='__main__':main()
