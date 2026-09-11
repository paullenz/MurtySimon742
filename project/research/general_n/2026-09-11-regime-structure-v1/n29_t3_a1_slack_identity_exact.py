#!/usr/bin/env python3
"""Exact symbolic-on-support compression of the n=29,t=3 A1 regime.

Scope: the (h_res,J)=(4,14) regime under the support class actually present in
the audited frontier:
  s in {2,3,4}, rho in {1,3,4,5,6}, D1=0, rho1=9,
  12 labels, 16 sources, sum(s)=sum(rho)+6, h_res=4.

The logical order is important:
1. the scalar supplement-cutoff plus total selected-incidence capacity rejects
   every abstract histogram with D4>=7;
2. on the surviving D4<=6 class the A1 source envelope has its stable form;
3. there the exact certificate gap equals
     1 + 1454/135 (U-36) + 125/54 (24-V) + 23/9 (Z-16),
   where U=sum_{s_i>=3}s_i, V=sum_{s_i>=4}s_i,
   Z=sum_{rho_u>=4}rho_u;
4. h=4 and zero slack imply U>=36 and Z>=16, while D4<=6 gives V<=24.

No optimizer and no floating point are used. This is not a general-N theorem;
the remaining universal task is to derive/replace the stated support reduction
without relying on the finite n=29 frontier preparation.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import importlib.util,json

A=12;B=16
COEF_U=Q(1454,135);COEF_V=Q(125,54);COEF_Z=Q(23,9)
EXPECTED_ELL={2:Q(32,3),3:Q(55),4:Q(1028,15)}
EXPECTED_SIG={1:Q(0),3:-Q(253,3),4:-Q(253,3),5:-Q(92),6:-Q(299,3)}

def load_module(path:Path):
 spec=importlib.util.spec_from_file_location('cover',path)
 m=importlib.util.module_from_spec(spec);assert spec.loader is not None
 spec.loader.exec_module(m);return m

def rat(x:Q):return [x.numerator,x.denominator]
def h_res(rho):
 h=0
 for k,x in enumerate(sorted(rho,reverse=True),1):
  if x>=k:h=k
  else:break
 return h

def features(p):
 z2=sum(x>=2 for x in p['rho']);D1=p['s'].count(1)
 return h_res(p['rho']),2*z2-D1

def check_fixed_envelopes(mod):
 th=mod.TEMPLATES['A1'];lam=th.get('lambda',Q(0));c=th.get('c',Q(0));mp=th.get('mu+',Q(0));mm=th.get('mu-',Q(0));taus={j:th.get(f'tau{j}',Q(0)) for j in range(1,A+1)}
 ell={}
 for s in EXPECTED_ELL:
  ell[s]=min(lam*R+c*x+x*mod.F(R+s,B-R-x) for R in range(10-s+1) for x in range(s,B-R+1))
 if ell!=EXPECTED_ELL:raise AssertionError(('ell',ell))
 # r=1 has qmax=0; r>=4 sees all 12 labels and therefore qmax=A-r.
 for r,qm in ((1,0),(4,8),(5,7),(6,6)):
  vals=[mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*mod.tterm(r,q,p,j) for j in range(1,A+1))-q*mod.F(r+q-1,B-q-p)
        for q in range(qm+1) for p in range(min(r+3,B-1-q)+1)]
  if min(vals)!=EXPECTED_SIG[r]:raise AssertionError(('sigma',r,min(vals)))
 return th

def enumerate_domain():
 out=[]
 for d2 in range(13):
  for d3 in range(13-d2):
   d4=12-d2-d3;S=2*d2+3*d3+4*d4
   for r3 in range(8):
    for r4 in range(8-r3):
     for r5 in range(8-r3-r4):
      r6=7-r3-r4-r5
      R=9+3*r3+4*r4+5*r5+6*r6
      if S!=R+6:continue
      rho=[1]*9+[3]*r3+[4]*r4+[5]*r5+[6]*r6
      if h_res(rho)!=4:continue
      out.append({'d':(d2,d3,d4),'r':(r3,r4,r5,r6),'S':S,'R':R,
                  's':[2]*d2+[3]*d3+[4]*d4,'rho':rho})
 return out

def initial_caps(p):
 return [min(A-r,sum(s<=r for s in p['s'])) for r in p['rho']]
def scalar_cutoff(p):
 C=initial_caps(p);K=max(C,default=0);scores=[r+c for r,c in zip(p['rho'],C)]
 good=[k for k in range(1,K+1) if sum(z>=k-1 for z in scores)>=k+1]
 L=max(good) if good else 0
 return C,L,[min(c,L) for c in C]
def gap_direct(mod,p):return mod.gaps_for([p],mod.TEMPLATES['A1'])[0]
def tails(p):
 U=sum(s for s in p['s'] if s>=3);V=sum(s for s in p['s'] if s>=4);Z=sum(r for r in p['rho'] if r>=4)
 return U,V,Z
def gap_formula(p):
 U,V,Z=tails(p)
 return Q(1)+COEF_U*(U-36)+COEF_V*(24-V)+COEF_Z*(Z-16)

def main():
 ap=ArgumentParser();ap.add_argument('--cover-script',type=Path,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 mod=load_module(z.cover_script);th=check_fixed_envelopes(mod)
 D=enumerate_domain()
 if len(D)!=121:raise AssertionError(('abstract_domain',len(D)))
 survivors=[];rejected=[];qmax3_values=set()
 for p in D:
  C,L,qstar=scalar_cutoff(p);Qcap=sum(qstar);feasible_total=p['S']<=Qcap
  U,V,Z=tails(p)
  rec={'d':list(p['d']),'r':list(p['r']),'S':p['S'],'R':p['R'],'L':L,'total_cap':Qcap,'U':U,'V':V,'Z':Z}
  if not feasible_total:
   rejected.append(rec);continue
  # Only after structural survival do we invoke the stable A1 envelope.
  q3=min(9,sum(s<=3 for s in p['s']));qmax3_values.add(q3)
  vals=[-th.get('c',Q(0))*q+sum(th.get(f'tau{j}',Q(0))*mod.tterm(3,q,pp,j) for j in range(1,A+1))-q*mod.F(3+q-1,B-q-pp)
        for q in range(q3+1) for pp in range(min(6,B-1-q)+1)]
  if min(vals)!=EXPECTED_SIG[3]:raise AssertionError(('sigma3',q3,min(vals)))
  gd=gap_direct(mod,p);gf=gap_formula(p)
  if gd!=gf:raise AssertionError(('identity',p,gd,gf))
  rec['gap']=rat(gd);survivors.append(rec)
 if len(survivors)!=11 or len(rejected)!=110:raise AssertionError((len(survivors),len(rejected)))
 if any(x['d'][2]>6 for x in survivors):raise AssertionError('D4>6 survived')
 if any(x['d'][2]<=6 for x in rejected):raise AssertionError('D4<=6 rejected')
 if any(x['U']<36 or x['V']>24 or x['Z']<16 for x in survivors):raise AssertionError('tail slack')
 if any(Q(*x['gap'])<1 for x in survivors):raise AssertionError('gap<1')
 eq=[x for x in survivors if Q(*x['gap'])==1]
 if len(eq)!=1 or eq[0]['d']!=[2,4,6] or eq[0]['r']!=[3,4,0,0]:raise AssertionError(('equality',eq))
 # Cross-check against the complete regenerated t=3 frontier cell.
 P=mod.load(z.demands_json,z.rows);cell=[]
 for i,p in enumerate(P):
  if features(p)==(4,14):cell.append((i,Counter(p['s']),Counter(p['rho']),mod.gaps_for([p],mod.TEMPLATES['A1'])[0]))
 if len(cell)!=11:raise AssertionError(('frontier_cell',len(cell)))
 abstract={(tuple(x['d']),tuple(x['r'])) for x in survivors};actual=set()
 for i,sc,rc,g in cell:actual.add(((sc[2],sc[3],sc[4]),(rc[3],rc[4],rc[5],rc[6])))
 if actual!=abstract:raise AssertionError(('frontier_mismatch',abstract-actual,actual-abstract))
 if [i for i,sc,rc,g in cell if g==1]!=[1]:raise AssertionError(('frontier_equality',cell))
 out={'schema':'n29-t3-a1-slack-identity-exact-v2','status':'PASS','scope':{'n':29,'Delta':16,'t':3,'h':4,'J':14,'support_s':[2,3,4],'support_rho':[1,3,4,5,6],'rho1':9},'abstract_histogram_domain':121,'total_capacity_survivors':11,'total_capacity_rejections':110,'survivors_exactly_D4_le_6':True,'frontier_cell_profiles':11,'frontier_cell_equals_abstract_survivors':True,'a1_envelopes_on_survivors':{'ell':{str(k):rat(v) for k,v in EXPECTED_ELL.items()},'sigma':{str(k):rat(v) for k,v in EXPECTED_SIG.items()},'lambda':rat(th['lambda'])},'gap_identity':'gap = 1 + (1454/135)(U-36) + (125/54)(24-V) + (23/9)(Z-16)','tails':{'U':'sum s_i over s_i>=3','V':'sum s_i over s_i>=4','Z':'sum rho_u over rho_u>=4'},'survivor_slacks':{'U_min':min(x['U'] for x in survivors),'V_max':max(x['V'] for x in survivors),'Z_min':min(x['Z'] for x in survivors)},'minimum_gap':[1,1],'unique_equality_histogram':eq[0],'frontier_unique_equality_profile':1,'scalar_cutoff_argument':{'terminal_cap':'q*_u=min(C_u,L)','C_u':'min(12-rho_u, #{i:s_i<=rho_u})','necessary_total_incidence':'sum_i s_i <= sum_u q*_u','structural_order':'apply total-capacity rejection before stable A1 envelope identity'},'qmax3_values_checked_on_survivors':sorted(qmax3_values),'arithmetic':'fractions.Fraction exact rational','solver_used':False,'floating_point_used':False,'interpretation':'Within the audited A1 support class, the supplement scalar cutoff plus total selected-incidence capacity alone forces D4<=6. Only then is the stable A1 envelope invoked. h=4 and zero slack force U>=36 and Z>=16, so the exact A1 gap identity gives gap>=1 with unique equality at frontier profile 1. Universal progress now reduces to deriving the support class (or an equivalent inequality) without finite frontier preparation.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
