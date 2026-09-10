#!/usr/bin/env python3
"""Can an arbitrary first-coordinate monotone potential replace the D=3 BC layer?

Scope: 107 n=29,t=2 obstruction profiles.  Keep complete D2,D4 rectangle layers
and J0,J2, delete D3, and add all first-coordinate thresholds
S=2,...,12 with free common nonnegative weights. Since incidence coupling gives
s<=rho, every threshold transports:
  sum_i x_i 1[s_i>=S] <= sum_u q_u 1[rho_u>=S].
Their nonnegative combination is an arbitrary nondecreasing step potential of
the first coordinate over the relevant domain (up to an irrelevant constant).

Floating reconnaissance only.  Infeasibility would show D3 cannot be replaced
by any separable monotone s/rho potential within this tested basis on bad107.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import Counter
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
BAD=[0,1,2,3,4,5,6,7,8,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,38,39,40,77,78,79,82,84,87,91,92,93,94,107,112,113,121,126,127,128,129,134,135,136,145,173,178,180,181,192,193,194,195,196,197,208,209,210,211,212,231,232,256,257,258,259,260,368,381,382,385,403,404,410,411,412,415,435,436,437,438,439,440,441,442,483,498,499,501,502,503,505,566,567,570,681,683]
SHS=tuple(range(2,13))

def build(P,a=12,b=16,dmax=10):
 M=rd.LP();rect=[]
 for D in (2,4):
  for V in range(b+1):rect.append((D,V,M.var(('BCrect',D,V),(0,None),1.0)))
 diag=[(K,M.var(('J',K),(0,None),1.0)) for K in (14,16)]
 sh={S:M.var(('SH',S),(0,None),1.0) for S in SHS}
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
     for S,w in sh.items():
      if s>=S:row[w]=row.get(w,0)-x
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
     for S,w in sh.items():
      if rho>=S:row[w]=row.get(w,0)+q
     M.le(row,0)
  row={lam:sum(pf['rho'])}
  for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
  for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
  M.le(row,-1)
 return M,rect,diag,sh

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P0=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P0)!=902:raise SystemExit(f'expected 902 got {len(P0)}')
 P=[P0[i] for i in BAD];st=time.time();M,rect,diag,sh=build(P);res=M.solve()
 out={'schema':'n29-t2-bad107-dropD3-allSH-v1','bad_profile_count':107,'deleted_family':'D3','kept_layers':[2,4],'diagonal_K':[14,16],'SH_thresholds':list(SHS),'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
 if res.success:
  out['active_SH']={str(S):float(res.x[w]) for S,w in sh.items() if res.x[w]>1e-8};out['active_rectangles']=[{'D':D,'V':V,'weight':float(res.x[w])} for D,V,w in rect if res.x[w]>1e-8];out['active_diagonals']=[{'K':K,'c':16-K,'weight':float(res.x[w])} for K,w in diag if res.x[w]>1e-8];out['objective']=float(res.fun)
 out['interpretation']='If infeasible, no nonnegative combination of first-coordinate thresholds S=2..12 can replace D3 while D2,D4,J0,J2 remain available on bad107. If feasible, inspect active SH thresholds and promote to full902.'
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
