#!/usr/bin/env python3
"""Exact lower bound of three scalar templates for the fixed n=29,t=2 C11 3-D potential.

Profiles 0, 3 and 77 form an incompatibility triangle. For each pair this
script rebuilds the common-scalar linear system with required certificate gap
>= 0 (not gap >= 1), then checks a fixed sparse rational Farkas certificate.

For A x <= b with the 16 scalar variables constrained x>=0 and all envelope
variables free, a checked certificate y>=0 satisfies:
  * y^T A_j >= 0 for every nonnegative scalar column;
  * y^T A_j = 0 for every free envelope column;
  * y^T b = -1 < 0.
Hence the pair system is infeasible. Because the three pairs (0,3), (0,77),
(3,77) are all infeasible even at nonnegative gap, no two scalar templates can
cover all three profiles. Together with a separate exact three-template cover,
this proves template-count minimum 3 within this fixed-potential architecture.

Standard-library exact arithmetic only; no LP solver participates in acceptance.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json

BC={(3,6):3,(3,7):3,(3,8):3,(3,9):3,(3,10):4,(3,11):4,(3,12):4,(3,13):4}
J={14:8,16:7};SH3=29
COMP=['lambda','c','mu+','mu-']+[f'tau{j}' for j in range(1,13)]
CERTS={
 (0,3):[(3,59,1422),(115,127,2133),(154,50,2133),(254,59,474),(283,59,316),(314,59,948),(368,13,158),(397,1,1422),(405,59,2844),(409,10,711),(524,20,711),(647,10,237),(753,11,711),(759,49,711),(778,13,158),(781,7,158),(814,10,237),(897,40,711),(905,10,711)],
 (0,77):[(0,151,20525),(3,12,4105),(142,14,4105),(165,352,20525),(235,633,20525),(283,1899,41050),(314,633,41050),(368,173,20525),(397,249,20525),(405,211,41050),(409,84,4105),(544,14,4105),(652,14,821),(661,621,41050),(663,639,41050),(689,42,4105),(741,10,821),(765,6,4105),(778,14,4105)],
 (3,77):[(0,5,304),(115,5,152),(241,15,304),(353,1,76),(361,13,152),(375,157,1216),(377,23,1216),(422,15,304),(458,5,96),(494,25,1824),(499,5,304),(500,277,5472),(503,371,5472),(599,3,152),(738,15,152),(753,63,608),(755,45,608),(781,9,152),(867,3,38),(872,3,152)],
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

def system(P,inds):
 names=list(COMP);rows=[];rhs=[]
 def add(name):names.append(name);return len(names)-1
 for i in inds:
  pf=P[i];sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={s:add(('ell',i,s)) for s in sorted(sc)};sigs={r:add(('sig',i,r)) for r in sorted(rc)}
  for s in sorted(sc):
   e=ells[s]
   for R in range(10-s+1):
    for x in range(s,16-R+1):rows.append({e:1,0:-R,1:-x});rhs.append(x*phi(R+s,R+x,s))
  for r in sorted(rc):
   sg=sigs[r];qm=min(12-r,sum(si<=r for si in pf['s']))
   for q in range(qm+1):
    for p in range(min(r+3,15-q)+1):
     row={sg:1,2:-(q-p),3:(q-p),1:q}
     for j in range(1,13):
      tt=tterm(r,q,p,j)
      if tt:row[3+j]=row.get(3+j,0)-tt
     rows.append(row);rhs.append(-q*phi(r+q-1,q+p,r))
  # gap >= 0: lambda*sumrho - sum ell - sum sig <= 0
  row={0:sum(pf['rho'])}
  for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
  for r,n in rc.items():row[sigs[r]]=row.get(sigs[r],0)-n
  rows.append(row);rhs.append(0)
 return names,rows,rhs

def check_pair(P,pair,cert):
 names,rows,rhs=system(P,pair);coeff=[Q(0) for _ in names];br=Q(0);support=[]
 for ri,num,den in cert:
  if not 0<=ri<len(rows):raise AssertionError((pair,'row index',ri,len(rows)))
  y=Q(num,den)
  if y<=0:raise AssertionError((pair,'nonpositive multiplier',ri,y))
  support.append(ri);br+=y*rhs[ri]
  for j,a in rows[ri].items():coeff[j]+=y*a
 free_bad=[(j,names[j],coeff[j]) for j in range(16,len(names)) if coeff[j]!=0]
 theta_bad=[(j,names[j],coeff[j]) for j in range(16) if coeff[j]<0]
 if free_bad or theta_bad or br>=0:raise AssertionError((pair,free_bad[:5],theta_bad,br))
 return {'pair':list(pair),'rows':len(rows),'variables':len(names),'certificate_support':len(cert),'combined_rhs':[br.numerator,br.denominator],'nonzero_scalar_coefficients':{str(names[j]):[coeff[j].numerator,coeff[j].denominator] for j in range(16) if coeff[j]!=0},'free_column_nonzero_count':len(free_bad),'negative_scalar_coefficient_count':len(theta_bad),'status':'PASS'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=load(z.demands_json,z.rows)
 if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
 results=[check_pair(P,p,CERTS[p]) for p in [(0,3),(0,77),(3,77)]]
 out={'schema':'n29-t2-sh3-c11-three-template-lower-bound-exact-v1','status':'PASS','profiles':902,'triangle_profiles':[0,3,77],'required_common_gap':'nonnegative (>=0)','pair_certificates':results,'certificate_arithmetic':'fractions.Fraction exact rational','uses_lp_solver':False,'floating_point_used':False,'conclusion':'Profiles 0,3,77 are pairwise incompatible under a single nonnegative scalar template with the fixed C11 potential; therefore at least three scalar templates are necessary within this fixed-potential architecture.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
