#!/usr/bin/env python3
"""Small sound relaxation for the eight nontrivial n=30,m=226,Delta=16 rows.

The historical grouped LP is reduced to two coupled transportation systems.
Variables:
  W[rho-group,q,p]   fraction of a residual-degree group having source type(q,p)
  P[type,type]       source->supplement flow (per source in first group)
  L[demand-group,e]  fraction of equal-demand labels having excess e=x-s
  Z[type,labeltype]  selected source->label incidence density

Necessary local conditions retained:
  q <= a-rho, p <= rho+2, q+p <= 15;
  source->supplement arc only if rho_w+q_w >= q_u-1;
  selected incidence only if s<=rho and e>=p-rho+1.

Balances retained:
  source type normalisation;
  outgoing q and incoming p supplement flow;
  label excess-type normalisation;
  source selected degree q and label selected degree x=s+e.

Everything else from the historical grouped LP is discarded.  Thus infeasibility
of this system is a valid necessary-condition contradiction, but feasibility
would prove nothing.
"""
from __future__ import annotations
from collections import Counter,defaultdict
from functools import reduce
from math import gcd
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,hstack,vstack,csr_matrix

A=13;B=16
ROWS=[
 ('2233',[2,2]+[3]*11,[1]*7+[2]+[3]*8),
 ('2331',[2]+[3]*12,[1]*7+[3]*9),
 ('3^13-r35a',[3]*13,[1]*7+[3]*8+[4]),
 ('3^13-r35b',[3]*13,[1]*6+[2]+[3]*9),
 ('3344',[3]*4+[4]*9,[1]*6+[3]*2+[4]*8),
 ('3344b',[3]*2+[4]*11,[1]*5+[2]+[3]+[4]*9),
 ('3444',[3]+[4]*12,[1]*5+[2]+[4]*10),
 ('4^13',[4]*13,[1]*5+[3]+[4]*10),
]

class M:
 def __init__(self):self.names=[];self.eq=[];self.ub=[]
 def var(self,n):self.names.append(n);return len(self.names)-1
 def equal(self,d,b=0):self.eq.append(({j:c for j,c in d.items() if c},b))
 def le(self,d,b):self.ub.append(({j:c for j,c in d.items() if c},b))
 def arrays(self):
  def mat(rows):
   rr=[];cc=[];vv=[];bb=[]
   for i,(d,b) in enumerate(rows):
    bb.append(b)
    for j,c in d.items():rr.append(i);cc.append(j);vv.append(c)
   return coo_matrix((vv,(rr,cc)),shape=(len(rows),len(self.names))).tocsr(),np.array(bb,float)
  X,b=mat(self.ub);E,f=mat(self.eq);return X,b,E,f
 def solve(self,obj=None):
  X,b,E,f=self.arrays();c=np.zeros(len(self.names)) if obj is None else obj
  return linprog(c,A_ub=X,b_ub=b,A_eq=E,b_eq=f,bounds=(0,None),method='highs')

def add(d,j,c=1):d[j]=d.get(j,0)+c

def build(s,rho):
 m=M(); SG=sorted(Counter(rho).items()); LG=sorted(Counter(s).items())
 # Source type distributions.
 W={};types=defaultdict(list)
 for k,(rh,nk) in enumerate(SG):
  norm={}
  for q in range(A-rh+1):
   for p in range(min(rh+2,B-1-q)+1):
    w=m.var(('W',k,rh,q,p));W[k,q,p]=w;types[k].append((q,p,w));norm[w]=1
  m.equal(norm,1)
 # Supplement transport. P is a density per source in group k to individual
 # destinations in group l, exactly as in the historical grouped model.
 Pout=defaultdict(list);Pin=defaultdict(list)
 for k,(rh,nk) in enumerate(SG):
  for q,p,w in types[k]:
   if q==0:continue
   for l,(rh2,nl) in enumerate(SG):
    for q2,p2,w2 in types[l]:
     if k==l and nk<2:continue
     if rh2+q2<q-1:continue
     z=m.var(('P',k,q,p,l,q2,p2));Pout[k,q,p].append((l,z));Pin[l,q2,p2].append((k,z))
 for k,(rh,nk) in enumerate(SG):
  for q,p,w in types[k]:
   e={w:-q}
   for l,z in Pout[k,q,p]:add(e,z,SG[l][1]-(k==l))
   m.equal(e,0)
 for l,(rh,nl) in enumerate(SG):
  for q2,p2,w2 in types[l]:
   e={w2:-p2}
   for k,z in Pin[l,q2,p2]:add(e,z,SG[k][1]-(k==l))
   m.equal(e,0)
 # Label excess distributions. A label has x=s+e selected incidences, and
 # x<=B safely bounds e<=B-s.
 L={};ltypes=defaultdict(list)
 for g,(sg,ng) in enumerate(LG):
  norm={}
  for ex in range(B-sg+1):
   z=m.var(('L',g,sg,ex));L[g,ex]=z;ltypes[g].append((ex,z));norm[z]=1
  m.equal(norm,1)
 # Selected incidence transport.
 Zout=defaultdict(list);Zin=defaultdict(list)
 for k,(rh,nk) in enumerate(SG):
  for q,p,w in types[k]:
   if q==0:continue
   need=max(0,p-rh+1)
   for g,(sg,ng) in enumerate(LG):
    if sg>rh:continue
    for ex,lz in ltypes[g]:
     if ex<need:continue
     z=m.var(('Z',k,q,p,g,ex));Zout[k,q,p].append((g,z));Zin[g,ex].append((k,z))
 for k,(rh,nk) in enumerate(SG):
  for q,p,w in types[k]:
   e={w:-q}
   for g,z in Zout[k,q,p]:add(e,z,LG[g][1])
   m.equal(e,0)
 for g,(sg,ng) in enumerate(LG):
  for ex,lz in ltypes[g]:
   e={lz:-(sg+ex)}
   for k,z in Zin[g,ex]:add(e,z,SG[k][1])
   m.equal(e,0)
 return m

def exact_certificate(m):
 # Nonnegative variables, equalities only. A Farkas ray mu with A^T mu>=0,
 # b^T mu<0 suffices. Split free equality multipliers into +/- parts.
 _,_,E,f=m.arrays();N=len(m.names);ne=len(m.eq)
 D=hstack([-E.T,E.T],format='csr')
 D=vstack([D,csr_matrix(np.r_[f,-f].reshape(1,-1))],format='csr')
 rhs=np.r_[np.zeros(N),-1.0]
 res=linprog(np.ones(2*ne),A_ub=D,b_ub=rhs,bounds=(0,None),method='highs')
 if not res.success:return None
 for scale in (1000,1000000,1000000000):
  mu=[round(float(x-y)*scale) for x,y in zip(res.x[:ne],res.x[ne:])]
  coef=[0]*N;rv=0
  for (row,b),w in zip(m.eq,mu):
   if not w:continue
   rv+=w*b
   for j,c in row.items():coef[j]+=w*c
  if min(coef)>=0 and rv<0:
   factor=reduce(gcd,[abs(x) for x in mu] or [1]) or 1
   c={'eq':[(i,w//factor) for i,w in enumerate(mu) if w],
      'rhs':rv//factor,'variables':N,'equalities':ne}
   verify(m,c);return c
 return None

def verify(m,c):
 assert c['variables']==len(m.names) and c['equalities']==len(m.eq)
 coef=[0]*len(m.names);rhs=0
 for i,w in c['eq']:
  row,b=m.eq[i];rhs+=w*b
  for j,a in row.items():coef[j]+=w*a
 assert min(coef)>=0 and rhs==c['rhs'] and rhs<0

def eqkind(m,i):
 ts={m.names[j][0] for j in m.eq[i][0]}
 if ts=={'W'}:return 'source_norm'
 if ts<= {'W','P'}:return 'supplement_flow'
 if ts=={'L'}:return 'label_norm'
 if ts<= {'W','Z'}:return 'source_incidence'
 if ts<= {'L','Z'}:return 'label_incidence'
 return 'other'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output');z=ap.parse_args()
 out={'schema':'n30-m226-simplified-two-transport-v1','rows':[]}
 for tag,s,rho in ROWS:
  m=build(s,rho);sol=m.solve();row={'tag':tag,'status':int(sol.status),'variables':len(m.names),'equalities':len(m.eq)}
  if sol.status==2:
   c=exact_certificate(m);assert c is not None,tag
   from collections import Counter
   kinds=Counter(eqkind(m,i) for i,w in c['eq'])
   row['certificate']={'rhs':c['rhs'],'support_counts':dict(kinds),'terms':len(c['eq'])}
  out['rows'].append(row)
 assert all(x['status']==2 for x in out['rows'])
 text=json.dumps(out,indent=2,sort_keys=True)+'\n'
 if z.output:open(z.output,'w').write(text)
 print(text,end='')
if __name__=='__main__':main()
