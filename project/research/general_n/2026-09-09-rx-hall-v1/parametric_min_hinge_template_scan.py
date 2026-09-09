#!/usr/bin/env python3
"""Falsify BC min-hinge families on n29 t=2/t=3 frontiers.

BC coordinates:
  label  : d=R+s,         v=b-(R+x)
  source : d=rho+q-1,     v=b-(q+p)

Two hinge modes are supported:
  template : parameter-only candidate
             (0,0), (0,t-1),
             (max(0,t-2),V) for V=max(0,a-t-2),...,a-1,
             (max(0,t-1),0), (t+1,0), duplicates removed.
  full     : every H_{D,V} on 0<=D<=dmax, 0<=V<=b.

Each BC feature is H_{D,V}(d,v)=min((d-D)_+,(v-V)_+).
Optional SH correction uses the canonical staircase dictionary in coordinates
(s,-h), exactly as the pairwise-staircase model.

Floating reconnaissance only. Any positive finite result must be exactified.
"""
from pathlib import Path
from collections import Counter
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py')
allx=module_from_spec(sp);sp.loader.exec_module(allx)

def leq(a,b): return all(x<=y for x,y in zip(a,b))
def inside(pt,g): return any(leq(q,pt) for q in g)
def tup(g): return tuple(tuple(p) for p in g)
def tterm(rho,q,p,j): return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
def hinge(D,V,d,v): return min(max(0,d-D),max(0,v-V))

def template(a,t):
    pts={(0,0),(0,max(0,t-1)),(max(0,t-1),0),(t+1,0)}
    D=max(0,t-2)
    for V in range(max(0,a-t-2),a): pts.add((D,V))
    return sorted(pts)

def hinge_family(a,b,dmax,t,mode):
    if mode=='template': return template(a,t)
    if mode=='full': return [(D,V) for D in range(dmax+1) for V in range(b+1)]
    raise ValueError(mode)

class LP:
    def __init__(self):
        self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items(): A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def build(P,a,b,dmax,t,shapes,features=None):
    H=list(features if features is not None else template(a,t))
    M=LP()
    hw=[M.var(('H',D,V),(0,None),1.0) for D,V in H]
    sw=[M.var(('SH',i),(0,None),1.0) for i in range(len(shapes))]
    def add_h(row,d,v,factor,sign):
        for w,(D,V) in zip(hw,H):
            z=hinge(D,V,d,v)
            if z: row[w]=row.get(w,0)+sign*factor*z
    def add_sh(row,pt,factor,sign):
        for i,g in enumerate(shapes):
            if inside(pt,g): row[sw[i]]=row.get(sw[i],0)+sign*factor
    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01)
        cc=M.var(('c',pi),(0,None),0.01)
        mp=M.var(('mu+',pi),(0,None),0.01)
        mm=M.var(('mu-',pi),(0,None),0.01)
        taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;v=b-(R+x);h=R+x
                    row={e:1,lam:-R,cc:-x}
                    add_h(row,d,v,x,-1)
                    add_sh(row,(s,-h),x,-1)
                    M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg
            qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    d=rho+q-1;v=b-(q+pp);h=q+pp
                    row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for j in range(1,a+1):
                        tv=tterm(rho,q,pp,j)
                        if tv: row[taus[j]]=row.get(taus[j],0)-tv
                    add_h(row,d,v,q,1)
                    add_sh(row,(rho,-h),q,1)
                    M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,H

def load_profiles(z):
    if z.mode in ('hard38','demand45'):
        B=json.loads(z.boundary_json.read_text())
        R=B['trimmed_survivor_records']
        if z.mode=='demand45': R=[r for r in R if r['demand_id']==45][:1]
        return [{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in R]
    P=allx.load29(z.demands_json,z.rows,z.t)
    return [{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['hard38','demand45','t2','t3'],required=True)
    ap.add_argument('--t',type=int,required=True);ap.add_argument('--a',type=int,default=12);ap.add_argument('--b',type=int,default=16);ap.add_argument('--dmax',type=int,default=10)
    ap.add_argument('--hinge-mode',choices=['template','full'],default='template')
    ap.add_argument('--sh-mode',choices=['none','full'],default='none')
    ap.add_argument('--dictionary-json',type=Path,required=True)
    ap.add_argument('--boundary-json',type=Path);ap.add_argument('--demands-json',type=Path);ap.add_argument('--rows',type=Path)
    ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    if z.mode in ('hard38','demand45') and not z.boundary_json:raise SystemExit('--boundary-json required')
    if z.mode in ('t2','t3') and (not z.demands_json or not z.rows):raise SystemExit('--demands-json/--rows required')
    D=json.loads(z.dictionary_json.read_text());sh=[] if z.sh_mode=='none' else [tup(x['generators']) for x in D['SH']]
    P=load_profiles(z);H=hinge_family(z.a,z.b,z.dmax,z.t,z.hinge_mode)
    known=[(0,0),(0,2),(1,7),(1,8),(1,9),(1,10),(1,11),(2,0),(4,0)]
    identity_ok=(H==known) if (z.a,z.t,z.hinge_mode)==(12,3,'template') else None
    st=time.time();M,H=build(P,z.a,z.b,z.dmax,z.t,sh,H);res=M.solve()
    out={'schema':'min-hinge-family-scan-v2','mode':z.mode,'a':z.a,'b':z.b,'t':z.t,'dmax':z.dmax,'profiles':len(P),'hinge_mode':z.hinge_mode,'hinges':H,'hinge_count':len(H),'known_t3_identity_ok':identity_ok,'SH_mode':z.sh_mode,'SH_count':len(sh),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if res.success:
        ah=[]
        for D,V in H:
            w=res.x[M.idx[('H',D,V)]]
            if w>1e-8:ah.append({'param':[D,V],'weight':float(w)})
        ash=[]
        for i in range(len(sh)):
            w=res.x[M.idx[('SH',i)]]
            if w>1e-8:ash.append({'index':i,'weight':float(w),'generators':[list(p) for p in sh[i]]})
        out.update({'active_hinges':ah,'active_hinge_count':len(ah),'active_SH':ash,'active_SH_count':len(ash)})
    out['interpretation']='Tests an analytic BC min-hinge family with optional canonical SH staircases. Positive results are floating proposals until exactified; negative results falsify only the stated family.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('hinges','active_hinges','active_SH')},indent=2,sort_keys=True))
if __name__=='__main__':main()
