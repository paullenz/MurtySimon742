#!/usr/bin/env python3
"""Exact envelope anatomy of the seven t=3 regime minima.

This replay is deliberately post-classification: the non-circular (h,J) regime
rules are already fixed and independently audited.  Here we expose which finite
label/source envelope states attain the exact minimum gap in each occupied cell.
No LP/MIP solver or floating point is used.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter,defaultdict
from fractions import Fraction as Q
from pathlib import Path
import importlib.util,json

A=12; B=16; DMAX=10
EXPECTED={
 (4,13):(0,'A0',Q(1)),
 (4,14):(1,'A1',Q(1)),
 (4,16):(5,'A530',Q(1)),
 (4,18):(30,'A530',Q(1)),
 (5,16):(6,'A38',Q(7421,385)),
 (5,18):(38,'A38',Q(1)),
 (5,20):(88,'A38',Q(484,21)),
}

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
 z2=sum(x>=2 for x in p['rho']);d1=p['s'].count(1)
 return h_res(p['rho']),2*z2-d1

def choose(h,J):
 if h==5:return 'A38'
 if (h,J)==(4,13):return 'A0'
 if (h,J)==(4,14):return 'A1'
 return 'A530'

def qmax(p,r):return min(A-r,sum(s<=r for s in p['s']))

def anatomy(mod,p,th):
 lam=th.get('lambda',Q(0));c=th.get('c',Q(0));mp=th.get('mu+',Q(0));mm=th.get('mu-',Q(0))
 taus={j:th.get(f'tau{j}',Q(0)) for j in range(1,A+1)}
 sc=Counter(p['s']);rc=Counter(p['rho']);ells={};sigs={}
 for s in sorted(sc):
  vals=[]
  for R in range(DMAX-s+1):
   for x in range(s,B-R+1):
    d=R+s;v=B-R-x;phi=mod.F(d,v)
    vals.append((lam*R+c*x+x*phi,R,x,d,v,phi))
  mn=min(z[0] for z in vals)
  ells[s]={'multiplicity':sc[s],'value':mn,'minimizers':[z for z in vals if z[0]==mn]}
 for r in sorted(rc):
  qm=qmax(p,r);vals=[]
  for q in range(qm+1):
   for pp in range(min(r+3,B-1-q)+1):
    alpha=r+q-1;w=B-q-pp;phi=mod.F(alpha,w)
    tt={j:mod.tterm(r,q,pp,j) for j in range(1,A+1)}
    val=mp*(q-pp)-mm*(q-pp)-c*q+sum(taus[j]*tt[j] for j in range(1,A+1))-q*phi
    vals.append((val,q,pp,alpha,w,phi,{j:v for j,v in tt.items() if v}))
  mn=min(z[0] for z in vals)
  sigs[r]={'multiplicity':rc[r],'qmax':qm,'value':mn,'minimizers':[z for z in vals if z[0]==mn]}
 label=sum(v['multiplicity']*v['value'] for v in ells.values())
 source=sum(v['multiplicity']*v['value'] for v in sigs.values())
 mass=lam*sum(p['rho']);gap=label+source-mass
 return {'label':label,'source':source,'lambda_r':mass,'gap':gap,'ell':ells,'sigma':sigs}

def encode_min(z):
 out=[]
 for x in z:
  if isinstance(x,Q):out.append(rat(x))
  elif isinstance(x,dict):out.append({str(k):v for k,v in x.items()})
  else:out.append(x)
 return out

def main():
 ap=ArgumentParser();ap.add_argument('--cover-script',type=Path,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 mod=load_module(z.cover_script);P=mod.load(z.demands_json,z.rows)
 if len(P)!=94:raise AssertionError(len(P))
 gaps={name:mod.gaps_for(P,th) for name,th in mod.TEMPLATES.items()}
 cells=defaultdict(list)
 for i,p in enumerate(P):
  h,J=features(p);name=choose(h,J);g=gaps[name][i]
  if g<=0:raise AssertionError((i,h,J,name,g))
  cells[(h,J)].append((i,name,g))
 if set(cells)!=set(EXPECTED):raise AssertionError(sorted(cells))
 results=[];signature_counts=Counter()
 for key in sorted(cells):
  idx,name,eg=EXPECTED[key];rows=cells[key];mn=min(g for _,_,g in rows)
  if mn!=eg or [i for i,n,g in rows if g==mn]!=[idx]:raise AssertionError((key,mn,rows))
  p=P[idx];a=anatomy(mod,p,mod.TEMPLATES[name])
  if a['gap']!=eg or a['gap']!=gaps[name][idx]:raise AssertionError((key,a['gap'],eg))
  ell={str(s):{'multiplicity':v['multiplicity'],'value':rat(v['value']),'minimizers':[encode_min(x) for x in v['minimizers']]} for s,v in a['ell'].items()}
  sig={str(r):{'multiplicity':v['multiplicity'],'qmax':v['qmax'],'value':rat(v['value']),'minimizers':[encode_min(x) for x in v['minimizers']]} for r,v in a['sigma'].items()}
  for s,v in a['ell'].items():
   for m in v['minimizers']:signature_counts[('L',s,m[1],m[2],m[3],m[4],str(m[5]))]+=1
  for r,v in a['sigma'].items():
   for m in v['minimizers']:signature_counts[('S',r,m[1],m[2],m[3],m[4],str(m[5]))]+=1
  results.append({'cell':list(key),'profile_index':idx,'template':name,'profiles_in_cell':len(rows),'gap':rat(eg),'s':p['s'],'rho':p['rho'],'s_hist':sorted(Counter(p['s']).items()),'rho_hist':sorted(Counter(p['rho']).items()),'label_contribution':rat(a['label']),'source_contribution':rat(a['source']),'lambda_r':rat(a['lambda_r']),'ell':ell,'sigma':sig})
 recurring=[{'signature':list(k),'occurrences':v} for k,v in signature_counts.most_common() if v>=2]
 out={'schema':'n29-t3-boundary-envelope-exact-v1','status':'PASS','profiles':94,'cell_minima':results,'recurring_minimizer_signatures':recurring,'arithmetic':'fractions.Fraction exact rational','solver_used':False,'floating_point_used':False,'interpretation':'Exact anatomy of the unique assigned-gap minimizer in every occupied (h,J) t=3 regime cell. These local envelope states are the finite targets for symbolic gap lower bounds.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','cell_minima':[(r['cell'],r['profile_index'],r['template'],r['gap']) for r in results],'recurring_signatures':len(recurring)},indent=2))
if __name__=='__main__':main()
