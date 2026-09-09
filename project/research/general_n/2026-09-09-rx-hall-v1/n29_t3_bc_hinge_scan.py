#!/usr/bin/env python3
"""Targeted analytic hinge compression for the exact pure-BC n29 t=3 frontier.

Unlike the earlier cancelled broad hinge reconnaissance, this scan uses only the
BC potential F and all 94 regenerated n29 t=3 profiles, now known to need no SH
correction. Coordinates are d=R+s (label) / alpha=rho+q-1 (source) and
v=b-h = b-(R+x) / b-(q+p). Each feature is coordinatewise nondecreasing:
  diag(C)   = (d+v-C)_+
  min(D,V)  = min((d-D)_+,(v-V)_+)
  prod(D,V) = (d-D)_+(v-V)_+.
All feature weights are nonnegative. Profile-specific scalar dual multipliers and
envelopes remain allowed. Floating reconnaissance only; success needs exactification.
"""
from pathlib import Path
from collections import Counter
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('ex',HERE/'n29_all_t23_exactify.py');ex=module_from_spec(sp);sp.loader.exec_module(ex)

def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
def feat(kind,param,u,v):
    if kind=='prod':D,V=param;return max(0,u-D)*max(0,v-V)
    if kind=='min':D,V=param;return min(max(0,u-D),max(0,v-V))
    if kind=='diag':return max(0,u+v-param[0])
    raise ValueError(kind)
def feature_list(kinds,umax=12,vmax=16):
    out=[]
    for kind in kinds:
        if kind in ('prod','min'):out += [(kind,(D,V)) for D in range(0,umax) for V in range(0,vmax)]
        elif kind=='diag':out += [(kind,(C,)) for C in range(0,umax+vmax)]
    return out
class LP:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0):i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items():A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')
def build(P,kinds):
    M=LP();spec=feature_list(kinds);W=[M.var(('F',kind)+param,(0,None),1) for kind,param in spec]
    def addpot(row,u,v,factor,sign):
        for w,(kind,param) in zip(W,spec):
            z=feat(kind,param,u,v)
            if z:row[w]=row.get(w,0)+sign*factor*z
    for pi,pf in enumerate(P):
        a,b,dmax=12,16,10;lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01);taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)};sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;v=b-(R+x);row={e:1,lam:-R,cc:-x};addpot(row,d,v,x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;v=b-(q+pp);row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for jj in range(1,a+1):
                        tv=tterm(rho,q,pp,jj)
                        if tv:row[taus[jj]]=row.get(taus[jj],0)-tv
                    addpot(row,alpha,v,q,1);M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,spec
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=ex.load(z.demands,z.rows,3)
    families=[('diag',),('min',),('prod',),('diag','min'),('diag','prod'),('min','prod'),('diag','min','prod')];rr=[]
    for kinds in families:
        st=time.time();M,spec=build(P,kinds);res=M.solve();q={'families':list(kinds),'features':len(spec),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st}
        if res.success:
            active=[]
            for kind,param in spec:
                w=M.idx[('F',kind)+param]
                if res.x[w]>1e-8:active.append({'kind':kind,'param':list(param),'weight':float(res.x[w])})
            q['active_features']=active;q['active_count']=len(active)
        rr.append(q);print(json.dumps({k:v for k,v in q.items() if k!='active_features'},sort_keys=True),flush=True)
        if res.success:break
    out={'schema':'n29-t3-bc-hinge-scan-v1','profiles':len(P),'floating_point_reconnaissance_only':True,'results':rr,'interpretation':'BC-only analytic monotone hinge cones on the exact pure-BC n29 t=3 frontier. Failure falsifies only the tested cone; success is proposal-only until integer/rational exactification.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
