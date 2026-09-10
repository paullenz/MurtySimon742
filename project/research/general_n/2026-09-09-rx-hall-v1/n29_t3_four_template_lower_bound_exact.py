#!/usr/bin/env python3
"""Exact lower bound of four scalar templates for the fixed n=29,t=3 potential.

Fixed global potential:
    F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9).

Profiles 0, 1, 38 and 30 form a four-vertex incompatibility clique.  For every
pair this script rebuilds the common-scalar system with required certificate
gap >= 0 and checks a fixed sparse rational Farkas certificate.

For A x <= b, the 16 scalar columns are constrained x>=0 and the envelope
columns are free.  Each checked y>=0 satisfies y^T A >=0 on scalar columns,
y^T A=0 on free columns, and y^T b=-1. Thus every pair is infeasible. No
three scalar templates can cover four pairwise-incompatible profiles. Together
with the separate exact four-template cover, the template count is exactly 4
within this fixed-potential model.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json
W={(3,0):6,(3,5):4,(3,9):3}
COMP=['lambda','c','mu+','mu-']+[f'tau{j}' for j in range(1,13)]
CERTS={
 (0,1):[(0,43,5472),(175,215,5472),(245,43,912),(278,43,608),(326,43,1824),(384,43,1368),(400,43,5472),(401,203,2736),(500,535,5472),(560,277,5472),(630,203,912),(654,5,19),(655,43,608),(706,203,1824),(739,43,456),(764,5,288),(775,67,1824),(780,203,5472)],
 (0,38):[(0,245,21866),(115,1121,21866),(175,4,841),(245,735,10933),(276,855,21866),(278,675,10933),(326,735,21866),(395,490,10933),(400,245,21866),(461,4825,21866),(518,6755,21866),(542,11305,43732),(544,2205,43732),(588,1930,10933),(624,1185,10933),(652,2455,21866),(661,965,21866)],
 (0,30):[(0,190,1459),(115,950,1459),(245,1140,1459),(278,1710,1459),(326,570,1459),(359,3675,11672),(395,2405,11672),(400,190,1459),(401,1994,1459),(461,13723,11672),(531,41545,11672),(555,27865,11672),(556,1710,1459),(562,1075,17508),(565,15655,35016),(593,5935,2918),(664,2055,1459),(675,1825,2918),(680,5935,11672)],
 (1,38):[(0,80,519),(99,89,519),(159,71,519),(229,80,173),(253,155,519),(254,205,519),(305,40,173),(374,160,519),(379,40,519),(440,75,346),(497,105,346),(521,105,346),(567,30,173),(594,205,1038),(639,10,519),(640,15,346)],
 (1,30):[(0,10,29),(99,19,29),(159,1,29),(229,30,29),(253,279,232),(254,81,232),(305,15,29),(330,81,464),(338,75,464),(367,41,116),(379,5,29),(440,225,464),(510,315,464),(534,315,464),(544,45,464),(586,45,116),(647,45,116),(659,45,464)],
 (38,30):[(60,75,466),(117,35,466),(136,35,233),(141,105,466),(187,30,233),(214,25,1864),(223,275,1864),(260,15,466),(261,83,233),(321,161,1864),(391,1155,1864),(415,1105,1864),(416,25,932),(425,165,1864),(467,165,466),(535,165,466),(540,165,1864)],
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
def system(P,pair):
 names=list(COMP);rows=[];rhs=[]
 def add(n):names.append(n);return len(names)-1
 for i in pair:
  pf=P[i];sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={s:add(('ell',i,s)) for s in sorted(sc)};sigs={r:add(('sig',i,r)) for r in sorted(rc)}
  for s,e in ells.items():
   for R in range(10-s+1):
    for x in range(s,16-R+1):rows.append({e:1,0:-R,1:-x});rhs.append(x*F(R+s,16-R-x))
  for r,sg in sigs.items():
   qm=min(12-r,sum(si<=r for si in pf['s']))
   for q in range(qm+1):
    for p in range(min(r+3,15-q)+1):
     row={sg:1,2:-(q-p),3:(q-p),1:q}
     for j in range(1,13):
      tt=tterm(r,q,p,j)
      if tt:row[3+j]=row.get(3+j,0)-tt
     rows.append(row);rhs.append(-q*F(r+q-1,16-q-p))
  row={0:sum(pf['rho'])}
  for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
  for r,n in rc.items():row[sigs[r]]=row.get(sigs[r],0)-n
  rows.append(row);rhs.append(0)
 return names,rows,rhs
def check(P,pair,cert):
 names,rows,rhs=system(P,pair);coeff=[Q(0) for _ in names];br=Q(0)
 for ri,num,den in cert:
  if not 0<=ri<len(rows):raise AssertionError((pair,ri,len(rows)))
  y=Q(num,den)
  if y<=0:raise AssertionError((pair,'nonpositive y',ri))
  br+=y*rhs[ri]
  for j,a in rows[ri].items():coeff[j]+=y*a
 freebad=[(j,names[j],coeff[j]) for j in range(16,len(names)) if coeff[j]!=0]
 scalarbad=[(j,names[j],coeff[j]) for j in range(16) if coeff[j]<0]
 if br>=0 or freebad or scalarbad:raise AssertionError((pair,br,freebad[:3],scalarbad[:3]))
 return {'pair':list(pair),'rows':len(rows),'variables':len(names),'certificate_support':len(cert),'combined_rhs':[br.numerator,br.denominator],'free_column_nonzero_count':len(freebad),'negative_scalar_coefficient_count':len(scalarbad),'nonzero_scalar_coefficients':{str(names[j]):[coeff[j].numerator,coeff[j].denominator] for j in range(16) if coeff[j]!=0},'status':'PASS'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=load(z.demands_json,z.rows)
 if len(P)!=94:raise SystemExit(f'expected 94 profiles, got {len(P)}')
 pairs=[(0,1),(0,38),(0,30),(1,38),(1,30),(38,30)];results=[check(P,p,CERTS[p]) for p in pairs]
 out={'schema':'n29-t3-four-template-lower-bound-exact-v1','status':'PASS','profiles':94,'clique_profiles':[0,1,38,30],'required_common_gap':'nonnegative (>=0)','pair_certificates':results,'certificate_arithmetic':'fractions.Fraction exact rational','uses_lp_solver':False,'floating_point_used':False,'conclusion':'Profiles 0,1,38,30 are pairwise incompatible under a single nonnegative scalar template with F=6B(3,0)+4B(3,5)+3B(3,9); therefore at least four scalar templates are necessary within this fixed-potential architecture.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
