#!/usr/bin/env python3
"""Search analytic monotone hinge alternatives to discrete staircase potentials.

Coordinates are u=d/alpha for BC or u=s/rho for SH, and v=b-h/b-beta.
Each candidate feature is coordinatewise nondecreasing and therefore valid under
the corresponding product-order coupling:
  prod(D,V) = (u-D)_+ (v-V)_+;
  min(D,V)  = min((u-D)_+,(v-V)_+);
  diag(C)   = (u+v-C)_+.
All coefficients are constrained nonnegative. Profile-specific scalar identity
multipliers are allowed. Floating reconnaissance only.
"""
from pathlib import Path
from collections import Counter
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
def feat(kind,param,u,v):
    if kind=='prod':D,V=param;return max(0,u-D)*max(0,v-V)
    if kind=='min':D,V=param;return min(max(0,u-D),max(0,v-V))
    if kind=='diag':C=param[0];return max(0,u+v-C)
    raise ValueError(kind)
def feature_list(kind,umax=12,vmax=16):
    if kind in ('prod','min'):return [(kind,(D,V)) for D in range(0,umax) for V in range(0,vmax)]
    if kind=='diag':return [(kind,(C,)) for C in range(0,umax+vmax)]
    raise ValueError(kind)
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
    M=LP();spec=[]
    for kind in kinds:spec.extend(feature_list(kind))
    # dedup exact feature names by kind/param; F and G have independent weights
    A=[M.var(('F',kind)+param,(0,None),1) for kind,param in spec];B=[M.var(('G',kind)+param,(0,None),1) for kind,param in spec]
    def addpot(row,vars,u,v,factor,sign):
        for w,(kind,param) in zip(vars,spec):
            val=feat(kind,param,u,v)
            if val:row[w]=row.get(w,0)+sign*factor*val
    for pi,pf in enumerate(P):
        a,b,dmax=pf['a'],pf['b'],pf['dmax'];lam=M.var(('lambda',pi),(0,None),0.01);cc=M.var(('c',pi),(0,None),0.01);mp=M.var(('mu+',pi),(0,None),0.01);mm=M.var(('mu-',pi),(0,None),0.01);taus={j:M.var(('tau',pi,j),(0,None),0.01) for j in range(1,a+1)};sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(dmax-s+1):
                for x in range(s,b-R+1):
                    d=R+s;v=b-(R+x);row={e:1,lam:-R,cc:-x};addpot(row,A,d,v,x,-1);addpot(row,B,s,v,x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+b-a-1,b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;v=b-(q+pp);row={sg:1,mp:-(q-pp),mm:(q-pp),cc:q}
                    for jj in range(1,a+1):
                        tv=tterm(rho,q,pp,jj)
                        if tv:row[taus[jj]]=row.get(taus[jj],0)-tv
                    addpot(row,A,alpha,v,q,1);addpot(row,B,rho,v,q,1);M.le(row,0)
        r=sum(pf['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
    return M,spec
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n30-json',type=Path,required=True);ap.add_argument('--n29-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();N30=json.loads(z.n30_json.read_text());N29=json.loads(z.n29_json.read_text());p30=[{'s':r['s'],'rho':r['rho'],'a':13,'b':16,'dmax':11} for r in N30['records']];p29=[{'s':r['s'],'rho':r['rho'],'a':12,'b':16,'dmax':10} for r in N29['trimmed_survivor_records']];scopes={'n30':p30,'n29':p29,'both':p30+p29};families=[('diag',),('min',),('prod',),('diag','min'),('diag','prod'),('min','prod'),('diag','min','prod')];results={}
    for scope,P in scopes.items():
        rr=[]
        for kinds in families:
            M,spec=build(P,kinds);res=M.solve();q={'families':list(kinds),'features_per_FG':len(spec),'success':bool(res.success),'objective':float(res.fun) if res.success else None}
            if res.success:
                q['active_F']=sum(res.x[M.idx[('F',kind)+param]]>1e-8 for kind,param in spec);q['active_G']=sum(res.x[M.idx[('G',kind)+param]]>1e-8 for kind,param in spec);q['active_threshold_union']=sorted({j for pi,p in enumerate(P) for j in range(1,p['a']+1) if res.x[M.idx[('tau',pi,j)]]>1e-8})
            rr.append(q)
            if res.success:break
        results[scope]=rr
    out={'schema':'pairwise-monotone-hinge-potential-scan-v1','floating_point_reconnaissance_only':True,'results':results,'interpretation':'All hinge features are coordinatewise nondecreasing in the relevant pairwise product-order coordinates. Success is a valid-form numerical proposal; failure only falsifies the listed hinge cones.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
