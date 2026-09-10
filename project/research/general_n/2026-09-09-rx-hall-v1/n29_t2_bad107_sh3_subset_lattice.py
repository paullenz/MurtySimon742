#!/usr/bin/env python3
"""Enumerate the 16 D3+SH3 family subsets on the 107 n29,t2 obstruction profiles.

Previous run 34500939994 showed D3 remains necessary when one natural SH3
threshold is restored, while D2,D4,J0,J2 can each be deleted individually.
This scan fixes D3 and SH3 present, then enumerates every subset of the four
optional families {D2,D4,J0,J2}.  Floating reconnaissance only.

The output records all feasible subsets and the inclusion-minimal feasible
subsets.  Any minimal survivor must be promoted to the full 902-profile set and
then exactified before proof use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import Counter
from itertools import combinations
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
BAD=[0,1,2,3,4,5,6,7,8,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,38,39,40,77,78,79,82,84,87,91,92,93,94,107,112,113,121,126,127,128,129,134,135,136,145,173,178,180,181,192,193,194,195,196,197,208,209,210,211,212,231,232,256,257,258,259,260,368,381,382,385,403,404,410,411,412,415,435,436,437,438,439,440,441,442,483,498,499,501,502,503,505,566,567,570,681,683]
S=3; OPTIONAL=('D2','D4','J0','J2')

def build(P,opt,a=12,b=16,dmax=10):
 layers=[3]+([2] if 'D2' in opt else [])+([4] if 'D4' in opt else []);layers=tuple(sorted(layers))
 steps=tuple(sorted(([16] if 'J0' in opt else [])+([14] if 'J2' in opt else [])))
 M=rd.LP();rect=[]
 for D in layers:
  for V in range(b+1):rect.append((D,V,M.var(('BCrect',D,V),(0,None),1.0)))
 diag=[(K,M.var(('J',K),(0,None),1.0)) for K in steps];sh=M.var(('SH',S),(0,None),1.0)
 def add2d(row,d,h,factor,sign):
  v=b-h
  for D,V,w in rect:
   if d>=D and v>=V:row[w]=row.get(w,0)+sign*factor
  for K,w in diag:
   if d+v>=K:row[w]=row.get(w,0)+sign*factor
 for pi,pf in enumerate(P):
  lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01)
  taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)};sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
  for s,n in sorted(sc.items()):
   e=M.var(('ell',pi,s),(None,None));ells[s]=e
   for R in range(dmax-s+1):
    for x in range(s,b-R+1):
     row={e:1,lam:-R,cc:-x};add2d(row,R+s,R+x,x,-1)
     if s>=S:row[sh]=row.get(sh,0)-x
     M.le(row,0)
  for rho,n in sorted(rc.items()):
   sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
   for q in range(qmax+1):
    for pp in range(min(rho+b-a-1,b-1-q)+1):
     row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
     for j in range(1,a+1):
      tv=rd.tterm(rho,q,pp,j)
      if tv:row[taus[j]]=row.get(taus[j],0)-tv
     add2d(row,rho+q-1,q+pp,q,1)
     if rho>=S:row[sh]=row.get(sh,0)+q
     M.le(row,0)
  row={lam:sum(pf['rho'])}
  for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
  for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
  M.le(row,-1)
 return M,rect,diag,sh,layers,steps

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P0=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P0)!=902:raise SystemExit(f'expected 902 got {len(P0)}')
 P=[P0[i] for i in BAD];results=[]
 subsets=[]
 for r in range(5):
  subsets.extend(combinations(OPTIONAL,r))
 for opt in subsets:
  st=time.time();M,rect,diag,sh,layers,steps=build(P,set(opt));res=M.solve();rec={'optional_families':list(opt),'family_count_including_D3_SH3':2+len(opt),'layers':list(layers),'diagonal_K':list(steps),'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st}
  if res.success:
   rec['SH3_weight']=float(res.x[sh]);rec['objective']=float(res.fun);rec['active_generator_count']=sum(res.x[w]>1e-8 for _,_,w in rect)+sum(res.x[w]>1e-8 for _,w in diag)+(1 if res.x[sh]>1e-8 else 0)
  results.append(rec);print(json.dumps(rec,sort_keys=True),flush=True)
 feasible=[frozenset(r['optional_families']) for r in results if r['success']]
 minimal=[]
 for s in feasible:
  if not any(t < s for t in feasible):minimal.append(sorted(s))
 out={'schema':'n29-t2-bad107-sh3-subset-lattice-v1','bad_profile_count':107,'mandatory_families':['D3','SH3'],'optional_families':list(OPTIONAL),'floating_point_reconnaissance_only':True,'results':results,'minimal_feasible_optional_sets':sorted(minimal,key=lambda x:(len(x),x)),'interpretation':'Inclusion-minimal feasible sets are minimal only within the family lattice D3+SH3+subset{D2,D4,J0,J2} on bad107. Promote survivors to all 902 profiles before exactification.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
