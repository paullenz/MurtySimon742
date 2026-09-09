#!/usr/bin/env python3
"""Test supermodular BC + arbitrary monotone function of d+v.

The capped-sum family was too restrictive. This scan uses diagonal threshold
steps

    J_K(d,v) = 1[d+v >= K]

with nonnegative weights. Thus sum_K gamma_K J_K is an arbitrary nonnegative
nondecreasing function phi(d+v). The total potential is

    F(d,v) = G(d,v) + phi(d+v),

where G is nonnegative, coordinatewise nondecreasing and supermodular.

Each J_K is coordinatewise nondecreasing, hence every tested F gives a valid BC
transport inequality. Floating reconnaissance only; positive finite results must
be exactified before proof use.
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
def jval(K,d,v): return 1 if d+v>=K else 0

class LP:
    def __init__(self): self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs): self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items(): A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def levels(mode,b,maxsum):
    if mode=='b': return [b]
    if mode=='near': return [k for k in range(b-2,b+3) if 1<=k<=maxsum]
    if mode=='all': return list(range(1,maxsum+1))
    raise ValueError(mode)

def build(P,a,b,dmax,shapes,stepmode):
    M=LP();dtop=max(dmax,a-1);maxsum=dtop+b
    gv={(d,v):M.var(('G',d,v),(0,None),1.0) for d in range(dtop+1) for v in range(b+1)}
    Ks=levels(stepmode,b,maxsum);gam={K:M.var(('gamma',K),(0,None),1.0) for K in Ks}
    sw=[M.var(('SH',i),(0,None),1.0) for i in range(len(shapes))]
    for d in range(dtop):
        for v in range(b+1): M.le({gv[d,v]:1,gv[d+1,v]:-1},0)
    for d in range(dtop+1):
        for v in range(b): M.le({gv[d,v]:1,gv[d,v+1]:-1},0)
    for d in range(dtop):
        for v in range(b): M.le({gv[d+1,v+1]:-1,gv[d+1,v]:1,gv[d,v+1]:1,gv[d,v]:-1},0)
    def addpot(row,d,h,shpt,factor,sign):
        v=b-h;row[gv[d,v]]=row.get(gv[d,v],0)+sign*factor
        for K,w in gam.items():
            if d+v>=K: row[w]=row.get(w,0)+sign*factor
        for i,g in enumerate(shapes):
            if inside(shpt,g): row[sw[i]]=row.get(sw[i],0)+sign*factor
    for pi,pf in enumerate(P):
        lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01)
        taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;h=R+x;row={e:1,lam:-R,cc:-x};addpot(row,d,h,(s,-h),x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    d=rho+q-1;h=q+pp;row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for j in range(1,a+1):
                        tv=tterm(rho,q,pp,j)
                        if tv: row[taus[j]]=row.get(taus[j],0)-tv
                    addpot(row,d,h,(rho,-h),q,1);M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items(): row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items(): row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,gv,gam,Ks

def load_profiles(z):
    if z.mode in ('hard38','demand45'):
        B=json.loads(z.boundary_json.read_text());R=B['trimmed_survivor_records']
        if z.mode=='demand45':R=[r for r in R if r['demand_id']==45][:1]
        return [{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in R]
    P=allx.load29(z.demands_json,z.rows,2);return [{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['demand45','hard38','t2'],required=True);ap.add_argument('--step-mode',choices=['b','near','all'],required=True);ap.add_argument('--sh-mode',choices=['none','full'],default='none')
    ap.add_argument('--a',type=int,default=12);ap.add_argument('--b',type=int,default=16);ap.add_argument('--dmax',type=int,default=10);ap.add_argument('--boundary-json',type=Path);ap.add_argument('--demands-json',type=Path);ap.add_argument('--rows',type=Path);ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    if z.mode in ('hard38','demand45') and not z.boundary_json:raise SystemExit('--boundary-json required')
    if z.mode=='t2' and (not z.demands_json or not z.rows):raise SystemExit('--demands-json/--rows required')
    D=json.loads(z.dictionary_json.read_text());sh=[] if z.sh_mode=='none' else [tup(x['generators']) for x in D['SH']];P=load_profiles(z)
    st=time.time();M,gv,gam,Ks=build(P,z.a,z.b,z.dmax,sh,z.step_mode);res=M.solve();out={'schema':'n29-t2-bc-diagonal-step-v1','mode':z.mode,'step_mode':z.step_mode,'step_levels':Ks,'SH_mode':z.sh_mode,'SH_count':len(sh),'profiles':len(P),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if res.success:
        out['active_steps']=[{'K':K,'weight':float(res.x[w])} for K,w in gam.items() if res.x[w]>1e-8];out['active_step_count']=len(out['active_steps'])
        ash=[]
        for i in range(len(sh)):
            w=float(res.x[M.idx[('SH',i)]])
            if w>1e-8:ash.append({'index':i,'weight':w,'generators':[list(p) for p in sh[i]]})
        out['active_SH']=ash;out['active_SH_count']=len(ash)
    out['interpretation']='Tests G(d,v)+phi(d+v), where G is monotone supermodular and phi is nonnegative nondecreasing via diagonal threshold steps. Positive results are floating proposals until exactified.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='active_SH'},indent=2,sort_keys=True))
if __name__=='__main__':main()
